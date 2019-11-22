#!/usr/bin/env python
# encoding: utf-8
# author   guojy8993
# date     2017/02/22

import os
import shutil
import json
import re
from subprocess import PIPE,Popen

PROC_NETNS = "/proc/%(pid)s/ns/net"
NET_NS = "/var/run/netns/"


log_path = "/var/log/instance.log"
def log(msg):
    if msg is not None and len(msg) > 0:
            f = open(log_path, "a")
            f.write("%s\n" % msg)
            f.close()

def util_exec(command):
    if not command or len(command.strip()) == 0:
        return "", ""
    pipe = Popen(command,
                 shell=True,
                 stdout=PIPE,
                 stderr=PIPE)
    #err = pipe.stderr.read()
    #if len(err) > 0:
    #    log(command)

    return pipe.stdout.read(), pipe.stderr.read()

def getLocalIP():
    addrs = "ip -o addr"
    result = Popen(addrs,shell=True,stdout=PIPE).stdout.read()
    result = [dev for dev in result.split("\n") if "global" in dev and "inet 10." in dev]
    if len(result) > 0:
        return result[0].split()[3].split("/")[0]
    #raise Exception("Local Address Unknown")
    return False
def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port
def file_exists(filename):
    return os.path.exists(filename)
def arg_exists(arg_list,**args):
    for arg_name in arg_list:
        if arg_name not in args:
            return False
    return True
def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        return False
def uuid_like(param):
    return re.search(r'[0-9a-z]{4}(-[0-9a-z]{4}){3}-[0-9a-z]{12}', param) is not None

if __name__ == "__main__":
    port = get_open_port()
    print port
    ip = getLocalIP()
    print ip
    print file_exists('/tmp/1.html')
