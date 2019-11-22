#! /usr/bin/python
# -*- coding: utf-8 -*-

import config
import copy
import json
import os
import re
import threading
import time
import urllib
import uuid
from subprocess import PIPE, Popen

from common import db, utils

scripts_dir = config.scripts_dir
log_path = "/var/log/instance.log"
vnc_server = "http://10.38.228.77:9000/"

# vnc_server="http://10.136.0.154:9000/"


def log(msg):
    if msg is not None and len(msg) > 0:
        f = open(log_path, "a")
        f.write("%s\n" % msg)
        f.close()


def get_host():
    """host"""
    f = open("/etc/hostname", "r")
    tmp = f.read()
    f.close()
    return tmp.strip()


def getLocalIP():
    addrs = "ip -o addr"
    result = Popen(addrs, shell=True, stdout=PIPE).stdout.read()
    result = [
        dev for dev in result.split("\n")
        if "global" in dev and "inet 10." in dev
    ]
    if len(result) > 0:
        return result[0].split()[3].split("/")[0]
    print result
    raise Exception("Local Address Unknown")


class Instance(object):
    def __init__(self):
        self.instance_dir = "%sinstance/" % scripts_dir
        self.instance_info = None
        self.instance_data = config.instance_data

    """public method"""
    """instance"""

    def create_instance(self, **args):
        action = args["action"]
        instance_name = args["instance_name"]
        instance_description = args["instance_description"]
        instance_mem = args["instance_mem"]
        instance_cpu = args["instance_cpu"]
        script_file = "%s%s" % (self.instance_dir, action)
        create_instance = "/usr/bin/bash %s %s %s %s %s" % (
            script_file, instance_name, instance_description, instance_mem,
            instance_cpu)
        log(create_instance)
        result = Popen(create_instance, stdout=PIPE, shell=True).stdout.read()
        log(result)
        if "succeed" not in result:
            return {"code": 0, "message": "Fails", "data": None}
        """ return the details of guest KVM """
        tmp = {"instance_name": instance_name, "action": "start_instance"}
        """ start guest KVM to get complete infos """
        self.start_instance(**tmp)
        dominfo = self.describe_instance(**tmp)
        return {"code": 1, "message": "SUCCESS", "data": dominfo["data"]}

    def openVNC(self, **args):
        host = getLocalIP()
        instance_name = args["instance_name"]
        getDomainUUID = "virsh domuuid %s" % instance_name
        result = Popen(getDomainUUID, shell=True, stdout=PIPE).stdout.read()
        log(result)
        if "error" in result:
            raise Exception("Guest %s doesnt exist." % instance_name)
        guest_uuid = result.strip()
        vnc_port = self.__get_vncport(instance_name)["vnc_port"]
        request = {
            "action": "gen_token",
            "guest_uuid": guest_uuid,
            "host": host,
            "port": vnc_port
        }
        log(request)
        fd = urllib.urlopen(vnc_server, json.dumps(request))
        result = fd.read()
        log(result)
        if "token" in result:
            result = json.loads(result)
            result.update({"code": 1, "message": "SUCCESS"})
            return result
        return {"code": 0, "message": "Fails"}

    def describe_instance(self, **args):
        instance_name = args["instance_name"]
        cmdline = "virsh dominfo %s" % instance_name
        result = Popen(cmdline, stdout=PIPE, shell=True).stdout.read()
        log("describe_instance: %s" % result)
        if "Domain not found" in result:
            return "Domain of %s not found" % instance_name
        self.instance_info = result
        dominfo = {}
        dominfo.update(self.__get_host(instance_name))
        log("desc:get_host:%s" % dominfo)
        dominfo.update(self.__get_interfaces(instance_name))
        log("desc:get_interfaces:%s" % dominfo)
        dominfo.update(self.__get_blks(instance_name))
        log("desc:get_blks:%s" % dominfo)
        dominfo.update(self.__get_running_state(instance_name))
        log("desc:get_state:%s" % dominfo)
        dominfo.update(self.__get_uuid(instance_name))
        log("desc:get_uuid:%s" % dominfo)
        dominfo.update(self.__get_memory(instance_name))
        log("desc:get_memory:%s" % dominfo)
        dominfo.update(self.__get_cpus(instance_name))
        log("desc:get_cpus:%s" % dominfo)
        dominfo.update(self.__get_vncport(instance_name))
        log("desc:get_vnc:%s" % dominfo)
        log("describe_instance: end with result %s" % dominfo)
        return {"Status": "Success", "data": dominfo}

    def start_instance(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        script_path = "%s%s" % (self.instance_dir, action)
        start = "/usr/bin/bash %s %s" % (script_path, instance_name)
        log(start)
        result = Popen(start, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {
            "message": "SUCCESS" if "OK" in result else "Error",
            "code": 1 if "OK" in result else 0
        }

    def reboot_instance(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        script_path = "%s%s" % (self.instance_dir, action)
        reboot = "/usr/bin/bash %s %s" % (script_path, instance_name)
        log(reboot)
        result = Popen(reboot, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {
            "message": "SUCCESS" if "OK" in result else "Error",
            "code": 1 if "OK" in result else 0
        }

    def resize_instance(self, **args):
        log(args)
        instance_name = args["instance_name"]
        action = args["action"]
        args["action"] = "describe_instance"
        old_config = self.describe_instance(**args)["data"]
        log(old_config)
        cpu_count = int(args["vcpu"]) if "vcpu" in args else old_config["cpu"]
        memory_KiB = int(args["memory"]) * 1000 if "memory" in args else int(
            old_config["memory"].split()[0].strip())
        script_path = "%s%s" % (self.instance_dir, action)
        resize = "/usr/bin/bash %s %s %s %s" % (script_path, instance_name,
                                                cpu_count, memory_KiB)
        log(resize)
        result = Popen(resize, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {
            "message": "SUCCESS" if "OK" in result else "Error",
            "code": 1 if "OK" in result else 0
        }

    def stop_instance(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        script_path = "%s%s" % (self.instance_dir, action)
        stop = "/usr/bin/bash %s %s" % (script_path, instance_name)
        log(stop)
        result = Popen(stop, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {
            "message": "SUCCESS" if "OK" in result else "Error",
            "code": 1 if "OK" in result else 0
        }

    def destroy_instance(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        destroy_instance = "/usr/bin/bash %s %s" % ("%s%s" %
                                                    (self.instance_dir,
                                                     action), instance_name)
        log(destroy_instance)
        result = Popen(destroy_instance, stdout=PIPE, shell=True).stdout.read()
        return {"message": "SUCCESS", "code": 1}

    """attach iso to cdrom device"""

    def attach_iso(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        iso_ftp = args["iso_ftp_url"]
        iso_name = iso_ftp.rsplit("/", 1)[1]
        attachScript = "/usr/bin/bash %s %s %s %s" % ("%s%s" %
                                                      (self.instance_dir,
                                                       action), instance_name,
                                                      iso_ftp, iso_name)
        log(attachScript)
        result_code = os.system(attachScript) / 256
        message = "SUCCESS" if result_code == 0 else "Fail"
        return {"message": message, "code": 1 if result_code == 0 else 0}

    """detach iso from guest"""

    def detach_iso(self, **args):
        instance_name = args["instance_name"]
        action = args["action"]
        detachScript = "/usr/bin/bash %s %s" % ("%s%s" % (self.instance_dir,
                                                          action),
                                                instance_name)
        log(detachScript)
        result_code = os.system(detachScript) / 256
        message = "SUCCESS" if result_code == 0 else "Fail"
        return {"message": message, "code": result_code}

    """set interface mac"""

    def set_interface_mac(self, **args):
        log(args)
        instance_name = args["instance_name"]
        macAddress = args["macAddress"]
        newMacAddress = args["newMacAddress"]
        """reconfig guestXml with new mac address"""
        guestXmlPath = "/data/instance/%s/%s.xml" % (instance_name,
                                                     instance_name)
        backupXml = "virsh dumpxml %s" % instance_name
        """ensure guest running to generate complete guestXml"""
        tmp = copy.copy(args)
        tmp["action"] = "start_instance"
        self.start_instance(**tmp)
        guestXml = Popen(backupXml, stdout=PIPE, shell=True).stdout.read()
        log(guestXml)
        log(guestXmlPath)
        writer = open(guestXmlPath, "w"
                      if os.path.exists(guestXmlPath) else "a")
        validMac = False
        for line in guestXml.split("\n"):
            if macAddress in line:
                log(line)
                validMac = True
                line = newMacAddress.join(line.split(macAddress))
            writer.write("%s%s" % (line, "\n"))
        writer.close()
        if not validMac:
            return {
                "code":
                0,
                "message":
                "Specified mac address %s not found in guest %s" %
                (macAddress, instance_name)
            }
        """redefine guest with fresh guestXml"""
        redefine_script = "%s%s" % (self.instance_dir, "redefine_instance")
        redefine = "/usr/bin/bash %(redefine_script)s %(instance_name)s %(guestXmlPath)s" % {
            "redefine_script": redefine_script,
            "guestXmlPath": guestXmlPath,
            "instance_name": instance_name
        }
        log(redefine)
        result = Popen(redefine, stdout=PIPE, shell=True).stdout.read()
        return {
            "code": 1 if "OK" in result else 0,
            "message": "SUCCESS" if "OK" in result else result
        }

    def get_instances(self, **args):
        get_instances = "virsh list --all"
        result = Popen(get_instances, stdout=PIPE, shell=True).stdout.read()
        lines = result.split("\n")[2:]
        log(lines)
        instances = []
        for line in lines:
            if len(line.strip()) > 0:
                instance_name = line.split()[1].strip()
                instances.append({"name": instance_name})
        return {"data": instances}

    """instance-ethernets"""

    def list_ethernets(self, **args):
        instance = args["instance_name"]
        ethernets = [
            eth for eth in self.__get_interfaces(instance)["nics"].values()
        ]
        return {"data": ethernets}

    """instance-disk"""

    def list_disks(self, **args):
        instance_name = args["instance_name"]
        return {
            "data":
            [blk for blk in self.__check_out_blks(instance_name).values()]
        }

    def kvm_conn_mgmt(self, **args):
        instance_name = args["instance_name"]
        # nics = self.__get_interfaces(instance_name)
        macAddress = args["macAddress"]
        # wan_device = [desc["label"] for nic, desc in nics["nics"].iteritems() if macAddress in desc["macAddress"]][0].split(":")[-1]
        nic_status = args["connected"]
        wan_device = "br0%s" % instance_name
        kvm_conn_mgmt = "ip link set %s %s" % (wan_device, "up"
                                               if nic_status else "down")
        log(kvm_conn_mgmt)
        result = Popen(kvm_conn_mgmt, shell=True, stdout=PIPE).stdout.read()
        log("Set wan insterface(%s) of %s to %s ,and get result %s" %
            (wan_device, instance_name, nic_status, result))
        return {"code": 1, "message": "SUCCESS"}

    """bandwidth"""

    def set_bandwidth(self, **args):
        dominfo = self.describe_instance(**args)["data"]
        log(dominfo)
        enable_live_operation = "running" in dominfo["state"]
        bandwidth_Mb = int(str(args["bandwidth"]))
        if bandwidth_Mb == 0:
            bandwidth_Mb = 0.008
        nic_type = "wan"
        if "nic" in args:
            nic_type = args["nic"]
        instance_name = args["instance_name"]
        interface = self.__get_interfaces(instance_name)
        nics = interface["nics"]
        interface = nics[nic_type]
        set_bandwidth = "virsh domiftune --domain %(domain)s \
                                         --interface %(mac)s \
                                         --outbound %(outbound)d,%(out_peak)d,%(out_burst)d \
                                         --config %(live)s" % {
            "domain": args["instance_name"],
            "mac": interface["macAddress"],
            "outbound": bandwidth_Mb * 125,
            "out_peak": bandwidth_Mb * 125,
            "out_burst": bandwidth_Mb * 125,
            "live": "" if not enable_live_operation else "--live"
        }
        log(set_bandwidth)
        result = Popen(set_bandwidth, stdout=PIPE, shell=True).stdout.read()
        log(result)
        return {"message": "Success", "code": 1}

    """inner method"""
    """host"""

    def __get_host(self, instance):
        vm_name = [
            line for line in self.instance_info.split("\n") if "Name" in line
        ][0].split(":")[1].strip()
        return {"host": get_host(), "name": vm_name}

    """instance"""

    def __get_running_state(self, instance):
        running_state = [
            line for line in self.instance_info.split("\n") if "State" in line
        ][0].split(":")[1].strip()
        return {"state": running_state}

    def __get_uuid(self, instance):
        uuid = [
            line for line in self.instance_info.split("\n") if "UUID" in line
        ][0].split()[1]
        return {"uuid": uuid}

    def __get_memory(self, instance):
        memory = [
            line for line in self.instance_info.split("\n")
            if "Max memory" in line
        ][0].split(":")[1]
        return {"memory": memory.strip()}

    def __get_cpus(self, instance):
        cpu = [
            line for line in self.instance_info.split("\n") if "CPU(s)" in line
        ][0].split()[1]
        return {"cpu": int(cpu.strip())}

    """instance-disk"""

    def __get_blks(self, instance):
        return {"disks": self.__check_out_blks(instance)}

    def __check_out_blks(self, instance):
        check_out_klbs = "virsh domblklist %s" % instance
        result = Popen(check_out_klbs, stdout=PIPE, shell=True).stdout.read()
        disks_map = {}
        for line in result.split("\n"):
            if len(line.strip()) > 0 and line.startswith("vd"):
                mount_point = line.split()[0].strip()
                disk_file = line.split()[1].strip()
                disk = {
                    "capacityInGB": 40 if "vda" in line else 0,
                    "isSystemPartition": "true" if "vda" in line else "false",
                    "UUID": disk_file.split("/")[-1],
                    "fileName": "%s:%s" % (get_host(), disk_file),
                    "label": mount_point
                }
                disks_map.update({mount_point: disk})
        return disks_map

    """Set Iops"""

    def set_disk_iops(self, **args):
        instance_name = args["instance_name"]
        disk = args["disk_uuid"]
        iops = int(args["iops"])
        dominfo = "virsh dominfo %s" % instance_name
        domdetails = Popen(dominfo, stdout=PIPE, shell=True).stdout.read()
        live = "running" in domdetails
        if "system" in disk:
            device = "vda"
        else:
            get_blks = "virsh domblklist %s" % instance_name
            blks = Popen(get_blks, stdout=PIPE, shell=True).stdout.read()
            for line in blks.split("\n"):
                if disk in line:
                    device = line.split()[0].strip()
                    break
        if device is None:
            return {"message": "Device %s not found " % disk, "code": 0}
        setblktune = "virsh blkdeviotune     \
                    --domain %(domain)s   \
                    --device %(device)s     \
                    --read-iops-sec %(riops)d \
                    --write-iops-sec %(wiops)d   \
                    %(live)s --config" % {
            "domain": instance_name,
            "device": device,
            "riops": iops,
            "wiops": iops,
            "live": "--live" if live else ""
        }
        log(setblktune)
        retv = Popen(setblktune, stdout=PIPE, shell=True).stdout.read()
        log(retv)
        success = len(retv.strip()) == 0
        return {
            "message": "SUCCESS" if success else retv,
            "code": 1 if success else 0
        }

    """Vnc Port"""

    def __get_vncport(self, instance):
        get_vnc = "virsh vncdisplay %s" % instance
        pipe = Popen(get_vnc, stdout=PIPE, stderr=PIPE,shell=True)
        result , errinfo = pipe.stdout.read(), pipe.stderr.read()
        if len(errinfo) > 0:
            return {"vnc_port": -1}
        if "error" in result:
            return {"vnc_port": -1}
        vnc_port = result.strip().split(":")[1]
        return {"vnc_port": int(vnc_port) + 5900}

    """interface"""

    def __get_interfaces(self, instance):
        get_interfaces = "virsh domiflist %s" % instance
        result = Popen(get_interfaces, stdout=PIPE, shell=True).stdout.read()
        nics = {}
        for line in result.split("\n"):
            if "br0" in line:
                device = line.split()[0]
                nics.update({
                    "wan": {
                        "macAddress":
                        line.split()[4],
                        "networkLabelName":
                        "br-wan",
                        "connected":
                        "true" if "up" in self.__get_interface_status(device)
                        else "false",
                        "startConnected":
                        "true",
                        "label":
                        "%s:%s:%s" % (get_host(), "br-wan", device),
                        "isInternet":
                        "true"
                    }
                })
            if "br1" in line:
                device = line.split()[0]
                nics.update({
                    "lan": {
                        "macAddress":
                        line.split()[4],
                        "networkLabelName":
                        "br-lan",
                        "connected":
                        "true" if "up" in self.__get_interface_status(device)
                        else "false",
                        "startConnected":
                        "true",
                        "label":
                        "%s:%s:%s" % (get_host(), "br-lan", device),
                        "isInternet":
                        "false"
                    }
                })
        log("===== IFs: %s" % nics)
        return {"nics": nics}

    def __get_interface_status(self, nic_device):
        if "-" in nic_device:
            return "down"
        get_interface_status = "ip -o link show %s" % nic_device
        log(get_interface_status)
        line = Popen(
            get_interface_status, shell=True, stdout=PIPE).stdout.read()
        log(line)
        if "UNKNOWN" in line:
            return "up"
        elif "DOWN" in line:
            return "down"
        else:
            pass

    def create_local_snapshot(self, **args):
        if "instance_name" not in args:
            return {"code": 0, "message": "domain not specified !"}
        if "disk_uuid" not in args:
            return {"code": 0, "message": "disk_uuid required !"}
        instance_name = args["instance_name"]
        disk_uuid = args["disk_uuid"]
        if '-system' in disk_uuid:
            disk_uuid = 'system'
        #blks = self.__check_out_blks(instance_name)
        # if (len(blks.keys())) > 1:
        #    return { "code": 0,
        #             "message": "please detach data disks before making snapshots !"
        #    }
        snap_name = "%s_%s" % (disk_uuid, uuid.uuid4())
        create_local_snapshot = "/bin/bash %s%s%s '%s' '%s' '%s'" % (
            self.instance_dir, os.sep, "create_local_disk_snapshot",
            instance_name, disk_uuid, snap_name)
        result = Popen(
            create_local_snapshot, stdout=PIPE, shell=True).stdout.read()
        if "OK" in result:
            date = time.strftime("%Y-%m-%d %H:%M:%S",
                                 time.localtime(time.time()))
            return {
                "code": 1,
                "message": "success",
                "snapshot": {
                    "name": "%s" % snap_name,
                    "create_time": "%s" % date
                }
            }

    def delete_local_snapshot(self, **args):
        if "instance_name" not in args or "snapshot" not in args:
            return {"code": 0, "message": "domain or snapshot not specified !"}
        domain = args["instance_name"]
        snapshot = args["snapshot"]
        delete_local_snapshot = "/bin/bash %s%s%s %s %s" % (
            self.instance_dir, os.sep, "delete_local_disk_snapshot", domain,
            snapshot)
        result = Popen(
            delete_local_snapshot, stdout=PIPE, shell=True).stdout.read()

        if "OK" in result:
            return {"code": 1, "message": "%s" % (result.strip())}
        else:
            return {"code": 0, "message": "fail with '%s'" % (result.strip())}

    def restore_from_local_snapshot(self, **args):
        if "instance_name" not in args or "snapshot" not in args:
            return {"code": 0, "message": "domain or snapshot not specified !"}
        domain = args["instance_name"]
        snapshot = args["snapshot"]

        restore_snapshot = "/bin/bash %s%s%s %s %s" % (
            self.instance_dir, os.sep, "restore_from_local_disk_snapshot",
            domain, snapshot)
        result = Popen(restore_snapshot, stdout=PIPE, shell=True).stdout.read()

        if "OK" in result:
            return {"code": 1, "message": "success"}
        else:
            return {"code": 0, "message": "fail with '%s'" % (result.strip())}

    def create_cloud_snapshot(self, **args):
        if "instance_name" not in args:
            return {"code": 0, "message": "domain not specified !"}
        domain = args["instance_name"]
        script_path = "%s%s" % (self.instance_dir, "create_cloud_snapshot")
        snap = "%s-cloudsnap-%s" % (domain, uuid.uuid4())
        create_snapshot = "/bin/bash %s %s %s" % (script_path, domain, snap)
        result = Popen(create_snapshot, shell=True, stdout=PIPE).stdout.read()
        if "OK" not in result:
            return {"code": 0, "message": "fail with %s" % (result.strip())}
        snapshot_uuid = snap.split("-cloudsnap-")[-1]
        return {
            "code": 1,
            "message": "success",
            "snapshot": "%s" % snapshot_uuid
        }

    def delete_cloud_snapshot(self, **args):
        if "instance_name" not in args or "snapshot" not in args:
            return {"code": 0, "message": "domain or snapshot not specified !"}
        domain = args["instance_name"]
        snapshot = args["snapshot"]
        script_path = "%s%s" % (self.instance_dir, "delete_cloud_snapshot")
        delete_snapshot = "/bin/bash %s %s %s" % (script_path, domain,
                                                  snapshot)
        result = Popen(delete_snapshot, shell=True, stdout=PIPE).stdout.read()
        if "OK" not in result:
            return {"code": 0, "message": "fail with %s" % (result.strip())}
        return {"code": 1, "message": "success"}

    def restore_from_cloud_snapshot(self, **args):
        if "instance_name" not in args or "snapshot" not in args:
            return {"code": 0, "message": "domain or snapshot not specified !"}
        domain = args["instance_name"]
        snapshot = args["snapshot"]
        script_path = "%s%s" % (self.instance_dir,
                                "restore_from_cloud_snapshot")
        restore_from_snapshot = "/bin/bash %s %s %s" % (script_path, domain,
                                                        snapshot)
        result = Popen(
            restore_from_snapshot, shell=True, stdout=PIPE).stdout.read()
        if "OK" not in result:
            return {"code": 0, "message": "fail with %s" % (result.strip())}
        return {"code": 1, "message": "success"}

    def read_console(self, **args):
        if "instance_name" not in args or not args["instance_name"]:
            return {"code": 0, "message": "Domain name not specified !"}
        domain = args["instance_name"]
        domain_folder = "%(instance_data)s%(domain)s%(sep)s" % {
            "instance_data": self.instance_data,
            "domain": domain,
            "sep": os.sep
        }
        domain_console_log = "%s%s" % (domain_folder, "console.log")
        console_last_read_pos = "%s%s" % (domain_folder, "last_read_pos")

        def read_pos(file):
            if not os.path.exists(file):
                fd = open(file, "a")
                pos = 0
                fd.write("%s" % pos)
            else:
                fd = open(file, "r")
                pos = int(fd.read().strip())
            fd.close()
            return pos

        def update_pos(file, pos):
            fd = open(file, "w")
            fd.write("%s" % pos)
            fd.close()

        if not os.path.exists(domain_console_log):
            return {
                "code": 0,
                "message": "ensure that kvm starts with '--serial' option"
            }
        fd = open(domain_console_log, "r")
        pos = read_pos(console_last_read_pos)
        try:
            fd.seek(pos)
        except Exception:
            fd.seek(0)
        lines = fd.readline()
        update_pos(console_last_read_pos, fd.tell())
        fd.close()
        return {"code": 1, "message": lines}

    def attach_tools(self, **args):
        if "instance_name" not in args or not args["instance_name"]:
            return {"code": 0, "message": "Instance name required !"}
        instance = str(args["instance_name"])
        if "iso_file" not in args or not args["iso_file"]:
            return {"code": 0, "message": "ISO file required !"}
        iso_file = str(args["iso_file"])
        if "iso_type" not in args:
            return {
                "code": 0,
                "message":
                "ISO type required ! 0 for PE and 1 for Oracle/MSSQL.."
            }
        iso_type = args["iso_type"]
        script_path = "%s%s" % (self.instance_dir, "attach_tools")
        command = "/bin/bash %s %s %s %d" % (script_path, instance, iso_file,
                                             iso_type)
        log(command)
        result = Popen(command, shell=True, stdout=PIPE).stdout.read()
        log(result)
        if "OK" in result:
            return {"code": 1, "message": "ISO Successfully Attached !"}
        else:
            return {"code": 0, "message": result}

    def detach_tools(self, **args):
        if "instance_name" not in args or not args["instance_name"]:
            return {"code": 0, "message": "Instance name required !"}
        instance = args["instance_name"]
        if "iso_type" not in args:
            return {
                "code": 0,
                "message":
                "ISO type required ! 0 for PE and 1 for Oracle/MSSQL.."
            }
        iso_type = args["iso_type"]
        script_path = "%s%s" % (self.instance_dir, "detach_tools")
        command = "/bin/bash %s %s %d" % (script_path, instance, iso_type)
        log(command)
        result = Popen(command, shell=True, stdout=PIPE).stdout.read()
        log(result)
        if "OK" in result:
            return {"code": 1, "message": "ISO Successfully detached !"}
        else:
            return {"code": 0, "message": result}

    def _run_backend(self, cmd, outlog):
        '''
        后台运行
        '''
        back_task = Popen(cmd, shell=True, stderr=open(outlog, "a"))
        while True:
            try:
                code = back_task.poll()
                if code is not None:
                    break
            except Exception:
                break
            time.sleep(10)

    def live_migration(self, **args):
        log("Start live migration with request: %s" % args)
        if "instance_name" not in args or "destHost" not in args:
            return {
                "code": 0,
                "message": "Instance name or destHost required !"
            }
        instance = args["instance_name"]
        destHost = args["destHost"]
        script_path = "%s%s" % (self.instance_dir, "migrate.sh")
        taskid = str(uuid.uuid4())
        logfile = "%s%s/migration-task-%s.log" % (config.instance_data,
                                                  instance, taskid)
        cmd = "/bin/bash %s %s %s" % (script_path, instance, destHost)
        task = threading.Thread(
            target=self._run_backend, args=(cmd, logfile, ))
        task.start()
        return {"code": 1, "message": "migration started", "taskid": taskid}

    def display_migration_progress(self, **args):
        instance_name = args["instance_name"]
        taskid = args["taskid"]
        destHost = args["destHost"]
        migration_outfile = "/var/log/Giant/instance/live_migrate/%s.log" % (
            instance_name)
        if utils.file_exists(migration_outfile):
            reader = open(migration_outfile, "r")
            txt = reader.read()
            reader.close()
            if len(txt.strip()) == 0:
                return {
                    "code": 1,
                    "message": "preparing migration",
                    "progress": "30%"
                }

            if "error" in txt:
                return {"code": 0, "message": txt, "progress": "-1"}
            if "ok" in txt:
                return {
                    "code": 1,
                    "message": "migration success",
                    "progress": "100%"
                }

        else:
            return {
                "code": 1,
                "message": "preparing migration",
                "progress": "5%"
            }

    def undefine_vm(self, **args):
        arg_list = ['instance_name']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing"}
        instance_name = args["instance_name"]
        script_file = "%s%s" % (self.instance_dir, 'undefine.sh')
        cmd = "/usr/bin/bash %s %s" % (script_file, instance_name)
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return {"code": 0, "message": err}
        return {"code": 1, "message": result}

    def redefine_clock(self, **args):
        arg_list = ['instance_name', 'os_type']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing"}
        instance_name = args["instance_name"]
        os_type = args["os_type"]
        script_file = "%s%s" % (self.instance_dir, 'redefine_clock.bash')
        cmd = "/usr/bin/bash %s %s %s" % (script_file, instance_name, os_type)
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return {"code": 0, "message": err}
        return {"code": 1, "message": result}
    def special_line(self, **args):
        arg_list = ['instance_name','vlan_id']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return { "code": 0,
                     "message": "arg missing"}
        instance_name = args["instance_name"]
        vlan_id = args["vlan_id"]
        script_file = "%s%s" % (self.instance_dir, 'special_line')
        cmd = "/usr/bin/bash %s %s %s" % (script_file, instance_name, vlan_id)
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return { "code": 0, "message": err}
        return { "code": 1, "message": result}
