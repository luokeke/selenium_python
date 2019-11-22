#! /usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import config

"""
monitor
"""
scripts_dir = config.scripts_dir

class Monitor(object):
    def __init__(self):
        self.monitor_dir = "%smonitor/" % scripts_dir

    def list(self, **args):
        action = args["action"]
        abs_path = "%s%s" % (self.monitor_dir, action)
        result = Popen("/usr/bin/bash %s" % abs_path, stdout=PIPE, shell=True).stdout.read()
        return result
