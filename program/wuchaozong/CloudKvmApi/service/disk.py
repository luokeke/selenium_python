#! /usr/bin/python
# -*- coding: utf-8 -*-

import threading
import uuid
from subprocess import Popen, PIPE

import config
from common import utils

from TEST.LIBRARY.program.wuchaozong.CloudKvmApi import Instance

"""
disk
"""
scripts_dir = config.scripts_dir
log_path = "/var/log/disk.log"

def log(msg):
    if msg is not None and len(msg) > 0:
        f = open(log_path, "a")
        f.write("%s\n" % msg)
        f.close()

class Disk(object):
    def __init__(self):
        self.disk_dir = "%sdisk/" % scripts_dir

    """public method"""
    """disk"""
    def create_disk(self, **args):
        disk_type = ''
        disk = args["disk_name"]
        action = args["action"]
        if 'disk_type' in args:
            disk_type = args["disk_type"]
        if disk_type == 'accelerate':
            disk_size = int(args["disk_size"])
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, 'JS_create_disk')
            task = "/usr/bin/bash %s %s %d" % (script_file, disk, disk_size)
        elif disk_type == 'share':
            share_name = args["share_name"]
            script_file = "%s%s" % (self.disk_dir, 'share_attach')
            task = "/usr/bin/bash %s %s %s" % (script_file, share_name, disk)
        else:
            disk_size = int(args["disk_size"])
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, action)
            task = "/usr/bin/bash %s %s %s %d" % (script_file, instance, disk, disk_size)
        log(task)
        result = Popen(task, stdout=PIPE, shell=True).stdout.read()
        log(task)
        return {"code": 1 if "OK" in result else 0,"message":result}

    def attach_disk(self, **args):
        disk_type = ''
        if 'disk_type' in args:
            disk_type = args["disk_type"]
        if disk_type == 'accelerate':
            instance = args["instance_name"]
            disk = args["disk_name"]
            script_file = "%s%s" % (self.disk_dir, 'JS_attach_disk')
            task = "/usr/bin/bash %s %s %s" % (script_file, instance, disk)
        elif disk_type == 'share':
            share_name = args["share_name"]
            instance_int_IP = args["instance_int_IP"]
            script_file = "%s%s" % (self.disk_dir, 'share_setIP')
            task = "/usr/bin/bash %s '%s' '%s'" % (script_file, share_name, instance_int_IP)
        else:
            disk = args["disk_name"]
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, args["action"])
            task = "/usr/bin/bash %s %s %s" % (script_file, instance, disk)
        log(task)
        result = Popen(task, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {"code":1 if "OK" in result else 0,"message":result}

    def detach_disk(self, **args):
        disk_type = ''
        if 'disk_type' in args:
            disk_type = args["disk_type"]
        if disk_type == 'accelerate':
            disk = args["disk_name"]
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, 'JS_detach_disk')
            task = "/usr/bin/bash %s '%s' '%s'" % (script_file, instance, disk)
        elif disk_type == 'share':
            share_name = args["share_name"]
            instance_int_IP = args["instance_int_IP"]
            script_file = "%s%s" % (self.disk_dir, 'share_removeIP')
            task = "/usr/bin/bash %s %s %s" % (script_file, share_name, instance_int_IP)
        else:
            disk = args["disk_name"]
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, args["action"])
            task = "/usr/bin/bash %s %s %s" % (script_file, instance, disk)
        log(task)
        result = Popen(task, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {"code":1 if "OK" in result else 0,"message":result}

    def alloc_space(self, **args):
        capacityInGB = args["capacityInGB"]
        disk_name_or_uuid = args["disk_name_or_uuid"]
        tmp = {}
        tmp["disk_size"] = capacityInGB
        tmp["disk_name"] = disk_name_or_uuid
        tmp["action"] = "create_disk"
        tmp["instance_name"] = args["instance_name"]
        result = self.create_disk(**tmp)
        if result["code"] == 1 :
            tmp["action"] = "attach_disk"
            result = self.attach_disk(**tmp)
            if result["code"] == 1:
                disks = Instance().list_disks(**tmp)
                freshDisk = [disk  for disk in disks["data"] if tmp["disk_name"] in disk["fileName"]][0]
                result.update({"data":freshDisk})
                return result
            else:
                result.update({
                                        "data":{},
                                        "message":"Disk %s created for %s, but fails in attaching."%(tmp["disk_name"],tmp["instance_name"])})
                return result
        else:
            result.update({"data":{},"message":"Fails to create Disk %s for %s"%(tmp["disk_name"],tmp["instance_name"])})
            return result

    def resize_disk(self,**args):
	instance = args["instance_name"]
	disk = args["disk_name"]
	extraGB = args["extraGB"]
	r = {}
	invalid = not instance or not disk or not isinstance(extraGB,int) or extraGB <= 0
	if invalid:
		r.update({"message":"instance_name and disk should not be none.","code":0})
		return r
	""" get target that this disk attached to """
	getblks = "virsh domblklist %s" % instance
	result = Popen(getblks,shell=True,stdout=PIPE).stdout.read()
	target = None
	path = None
	for line in result.split("\n"):
			if disk in line:
				target = line.split()[0].strip()
				path   = line.split()[1].strip()
	if not target or not path:
		r.update({"message":"%s seems not to be one of %s's device" % (disk,instance),"code":0})
                return r
	""" detach disk from instance and resize disk with additional capacity in GB """
	dominfo = "virsh dominfo %s" % instance
	result = Popen(dominfo,shell=True,stdout=PIPE).stdout.read()
	live = "--live" if "running" in result else ""
	detach = "virsh detach-disk --domain %(domain)s --target %(target)s --config %(if_live)s" % {
		"domain":instance,
		"target":target,
		"if_live":live
	}
	result = Popen(detach,shell=True,stdout=PIPE).stdout.read()
	if "Disk detached successfully" not in result:
		r.update({
				"message":"System experiences a failure while trying to detach disk %s from  instance %s." % (disk,instance),
			      	"code":0
		})
                return r
	resize = "qemu-img resize -q %(path)s  +%(add)dG" % {
		"path":path,
		"add":extraGB
	}
	result = Popen(resize,shell=True,stderr=PIPE).stderr.read()
	if result:
		r.update({
                		"message":"System failure,details: %s" % result,
                                "code":0
                })
		self._restor_attach(instance,target,path,"live" in detach)
		return r
	else:
		try:
			self._restor_attach(instance,target,path,"live" in detach)
			r.update({
                        	"message":"Resize success!",
                                "code":1
                	})
			return r
        	except Exception as e:
			r.update({
                                "message":str(e),
                                "code":0
                	})
			return r

    def _restor_attach(self,instance,target,source,live):
	attach = "virsh attach-disk --domain %(domain)s --source %(source)s --target %(target)s --config %(hot)s" % {
		"domain":instance,
		"source":source,
		"target":target,
		"hot": "--live" if live else ""
	}
	result = Popen(attach,shell=True,stdout=PIPE).stdout.read()
	if "Disk attached successfully" not in result:
		raise Exception("System experiences a failure while attching disk %(source)s to instance %(instance)s" % {
						"source":source,
						"instance":instance
		})

    def remove_disk(self,**args):
        deleteDiskFile = args["deleteDiskFile"]
        """ step1 detach disk """
        args["action"] = "detach_disk"
        result = self.detach_disk(**args)
        log(str(deleteDiskFile))
        if "True" not in str(deleteDiskFile) and "true" not in str(deleteDiskFile):
            return result
        else:
            """ step2 delete disk """
            log("delete disk - detach disk: %s" % result)
            args["action"] = "delete_disk"
            result = self.delete_disk(**args)
            log("delete disk - delete disk: %s" % result)
            return result

    def delete_disk(self, **args):
        disk_type = ''
        disk = args["disk_name"]
        if 'disk_type' in args:
            disk_type = args["disk_type"]
        if disk_type == 'accelerate':
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, 'JS_delete_disk')
            task = "/usr/bin/bash %s %s" % (script_file, disk)
        elif disk_type == 'share':
            share_name = args["share_name"]
            script_file = "%s%s" % (self.disk_dir, 'share_detach')
            task = "/usr/bin/bash %s %s %s" % (script_file, share_name, disk)
        else:
            instance = args["instance_name"]
            script_file = "%s%s" % (self.disk_dir, args["action"])
            task = "/usr/bin/bash %s %s %s" % (script_file, instance, disk)
        log(task)
        result = Popen(task, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {"code": 1 if "OK" in result else 0, "message": result}
    def expansion_disk(self, **args):
        disk_type = ''
        instance = args["instance_name"]
        disk = args["disk_name"]
        if 'disk_type' in args:
            disk_type = args["disk_type"]
        if disk_type == 'accelerate':
            disk_add_size = args["disk_add_size"]
            script_file = "%s%s" % (self.disk_dir, 'JS_expansion_disk')
            task = "/usr/bin/bash %s %s %s %s" % (script_file, disk, disk_add_size, instance)
        elif disk_type == 'share':
            #共享盘扩容接口不在使用-20170524
            return {"code": 0, "message": "not support"}
            disk_total_size = args["disk_total_size"]
            script_file = "%s%s" % (self.disk_dir, 'share_Resize.bash')
            task = "/usr/bin/bash %s %s %d" % (script_file, disk, disk_total_size)
        else:
            script_file = "%s%s" % (self.disk_dir, args["action"])
            task = "/usr/bin/bash %s %s %s" % (script_file, instance, disk)
        log(task)
        result = Popen(task, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {"code": 1 if "OK" in result else 0, "message": result}
    def _run_backend(self,cmd,outlog):
        '''
        后台运行
        '''
        back_task = Popen(cmd,shell=True,stderr=open(outlog,"a"))
        while True:
            try:
                code = back_task.poll()
                if code is not None:
                    break
            except Exception:
                break
            time.sleep(10)
    def disk_migration(self,**args):
        arg_list = ['disk_type','disk_name']
        if utils.arg_exists(arg_list,**args):
            pass
        else:
            return {"code":0, "message":"arg missing"}
        disk_type = args["disk_type"]
        disk_name = args["disk_name"]
        if disk_type == 'accelerate':
            destHost = args["destHost"]
            script_path = "%s%s" % (self.disk_dir,"JS_migrate_disk")
            taskid = str(uuid.uuid4())
            logfile = "%s/JS_disk_migration-task-%s.log" %('/var/log',taskid)
            cmd = "/bin/bash %s %s %s" % (script_path, destHost, disk_name)
            task = threading.Thread(target=self._run_backend,args=(cmd,logfile,))
            task.start()
            return { "code":1,
                    "message":"%s migration started" %disk_name,
                    "taskid":taskid }
        else:
            return { "code":0,
                    "messauge":"Unknown disk type"}

    def disk_migration_progress(self,**args):
        arg_list = ['disk_type','disk_name']
        if utils.arg_exists(arg_list,**args):
            pass
        else:
            return {"code":0, "message":"arg missing"}
        disk_type = args["disk_type"]
        disk_name = args["disk_name"]
        if disk_type == 'accelerate':
            migration_outfile = "/var/log/Giant/disk/migrate_disk/%s" %(disk_name)
        if utils.file_exists(migration_outfile):
            reader = open(migration_outfile,"r")
            txt = reader.read()
            reader.close()
            if len(txt.strip()) == 0:
                return { "code":1,
                         "message":"preparing migration",
                         "progress":"30%" }

            if "error" in txt:
                return { "code":0,
                         "message":txt,
                         "progress":"-1" }
            if "OK" in txt:
                return { "code":1,
                         "message":"migration success",
                         "progress":"100%" }

        else:
            return { "code":1,
                     "message":"preparing migration",
                     "progress":"0%" }
