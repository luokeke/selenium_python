#! /usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import config
import threading
import re
import os
import shutil
from common import utils

"""
image:
image_id,image_name,image_os,image_size
"""
scripts_dir = config.scripts_dir
log_path = "/var/log/image.log"

def log(msg):
    if msg is not None and len(msg) > 0:
        f = open(log_path, "a")
        f.write("%s\n" % msg)
        f.close()


class Image(object):
    def __init__(self):
        self.image_dir = "%simage/" % scripts_dir

    """public method"""
    """image"""
    def list_image(self, **args):
        action = args["action"]
        script_file = "%s%s" % (self.image_dir, action)
        result = Popen("/usr/bin/bash %s" % script_file, stdout=PIPE, shell=True).stdout.read()
        if result == "":
            return "There has no available image."
        image_list = []
        for line in result.split("\n"):
            if len(line.strip()) != 0:
                image_dict = {"image_name": line}
                image_list.append(image_dict)
        return image_list

    def check_sync_progress(self, **args):
        if "image" not in args:
            return {"code":0, "message":"image name not specified !"}
        state_file = "%s%s.state" % (config.images, args["image"])
        if not os.path.exists(state_file):
            return {"code":0, "message":"image state file not found !"}

        def read_state(state):
            fd = open(state, "r")
            tmp = fd.read()
            fd.close()
            return int(tmp)

        state = read_state(state_file)
        if state < 0:
            return {"code":0, "message":"Image server error !"}
        elif state == 1:
            os.remove(state_file)
            return {"code":1, "message":"OK !", "progress":100.0}
        image_meta_file = "%s/meta/%s.size" % (config.images, args["image"])

        def read_meta_size(meta):
            fd = open(meta, "r")
            tmp = fd.read()
            fd.close()
            return int(tmp)

        total_size = read_meta_size(image_meta_file)

        def copied_image_capacity():
            disp_image = "ls -l  %s%s" % (config.images, args["image"])
            result = Popen(disp_image, stdout=PIPE, shell=True).stdout.read()
            return int(result.split()[4])

        capacity_copied = copied_image_capacity()
        rate = round(100 * 1.0 * capacity_copied / total_size, 1)
        return {"code":1, "message":"Downloading ...", "progress":rate}

    def sync_image(self, **args):
        if "image" not in args:
            return {"code":0, "message":"image name not specified !"}
        if "ftp_server" not in args:
            return {"code":0, "message":"ftp_server not specified !"}
        script = "%s%s" % (self.image_dir, args["action"])

        def update_progress(state_file,state):
            fd = open(state_file, "w" if os.path.exists(state_file) else "a")
            fd.write("%s" % state)
            fd.close()

        def aysnc_task(state_file):
            update_progress(state_file, 0)
            result = Popen("/bin/sh %s %s %s %s" % (script, args["ftp_server"], args["image"], config.images),
                        stdout=PIPE,
                        shell=True).stdout.read()
            if "OK" in result:
                update_progress(state_file, 1)
            elif "Fail" in result:
                update_progress(state_file, -1)
            elif "DuplicateTask" in result:
                return {"code":1, "message":"Duplicate task !"}

        progress_log = "%s%s.state" % (config.images, args["image"])
        th = threading.Thread(target=aysnc_task, args=(progress_log,))
        th.start()
        return {"code":1, "message":"Starting to async image %s ..." % args["image"]}


    def copy_image(self, **args):
        image_name = args["image_name"]
        instance_name = args["instance_name"]
        action = args["action"]
        script_file = "%s%s" % (self.image_dir, action)
        copy_image = "/usr/bin/bash %s %s %s" % (script_file, image_name, instance_name)
        log(copy_image)
        result = Popen(copy_image, stdout=PIPE, shell=True).stdout.read()
        log(result)
        if "succeed" not in result:
            raise Exception("Failed to copy image.")
        return {"code": 1, "message": result}


    def image_exists(self, **args):

        if "image" not in args or not args["image"]:
            return {"code":0, "message":"Image name not specified !"}
        image = args["image"]

        if image.count("/") > 0:
            image = image.rsplit("/")[-1]

        image_exists = "rbd ls --pool images"
        result = Popen(image_exists, shell=True, stdout=PIPE).stdout.read()

        image_exists = image in result
        return { "code": 1 if image_exists else 0,
                 "message":"Image %s %s exists !" % (image, "" if image_exists else "not")
        }

    def move_image(self, **args):

        if "source" not in args or not args["source"]:
            return {"code":0, "message":"Source file not specified !"}
        if "dest" not in args or not args["dest"]:
            return {"code":0, "message":"Dest file not specified !"}

        source = args["source"]
        dest = args["dest"]

        log("source: %s" % source)
        log("dest: %s" % dest)

        if source == dest:
            return {"code":1, "message":"WARN:Dest/Source files are the same one !"}

        def uuid_like(param):
            return re.search(r'[0-9a-z]{4}(-[0-9a-z]{4}){3}-[0-9a-z]{12}', param) is not None

        _, tmp1, source_file = source.rsplit('/', 2)
        _, tmp2, dest_file = dest.rsplit('/', 2)

        cut = 0  # Move 'system' to 'Pre'
        if uuid_like(source_file):
            cut, domain_name = 1, tmp2
        elif uuid_like(dest_file):
            cut, domain_name = 0, tmp1

        script = "/bin/bash %s%s%s%s %s %d %s %s" % (scripts_dir,
                                                     'image',
                                                     os.sep,
                                                     'move_image',
                                                     domain_name,
                                                     cut,
                                                     source_file,
                                                     dest_file)

        print script

        result = Popen(script, shell=True, stdout=PIPE).stdout.read()
        print "+++++++move image+++++"
        print result

        if "OK" in result:
            return {"code":1, "message":"Move file success !"}
        elif "error" in result:
            return {"code":0, "message":"Move file error !"}

    def rm_pre_image(self, **args):
        '''
        删除预创建好的系统盘
        '''
        arg_list = ['path']
        if utils.arg_exists(arg_list,**args):
            pass
        else:
            return {"code":0, "message":"arg missing %s" %arg_list}
        path = args["path"]
        image = path.rsplit("/")[-1]
        if utils.uuid_like(image):
            cmd = '/bin/bash %s%s%s%s "%s"' %(scripts_dir,
                                            'image',
                                            os.sep,
                                            'rm_pre_image',
                                            image)
            log(cmd)
            result,err = utils.util_exec(cmd)
            if len(err) > 0:
                return {"code":0, "message":err}
            else:
                return {"code":1, "message":result}
        else:
            return {"code":0, "message":"pre_image %s format error" %path}
    def copy_image_prev(self, **args):
        image_name = args["image_name"]
        dest = args["dest"]
        action = args["action"]
        script_file = "%s%s" % (self.image_dir, action)
        file_name = dest.rsplit("/")[-1]
        copy_image = "/usr/bin/bash %s %s %s" % (script_file, image_name, file_name)
        log(copy_image)
        result = Popen(copy_image, stdout=PIPE, shell=True).stdout.read()
        log(result)
        if "succeed" not in result:
            #raise Exception("Failed to copy image.")
            return {"code": 0, "message": "copy_image_prev error"}
        return {"code": 1, "message": result}


