#!/usr/bin/env python
# encoding: utf-8

import config
import os
from subprocess import PIPE, Popen

from common import utils


class ManageFlow(object):
    '''
    管理流表
    '''

    def __init__(self):
        self.scripts_dir = config.scripts_dir

    def _get_ovs_lan_port(self, domain):
        """
        获取虚机ovs内网端口
        """
        host_ofport_name = "lan%s" % domain
        find_ofport = "ovs-vsctl get Interface %s ofport" % host_ofport_name
        find_ofport_result = Popen(find_ofport, shell=True, stdout=PIPE).stdout.read()
        if "no row" in find_ofport_result.strip():
            return None
        else:
            return find_ofport_result.strip()

    def _get_host_vxlan_port(self, host):
        host_ofport_name = "vxlan%s" % host
        find_ofport = "ovs-vsctl get Interface %s ofport" % host_ofport_name
        find_ofport_result = Popen(find_ofport, shell=True, stdout=PIPE).stdout.read()
        if "no row" in find_ofport_result.strip():
            return None
        else:
            return find_ofport_result.strip()

    def qos_queue(self, **args):
        '''
        qos_queue带宽共享器
        '''
        arg_list = ['op_type', 'op_object']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        op_type = args["op_type"]
        op_object = args["op_object"]

        if op_type == 'create':
            # 创建队列
            result = self._create_queue(**args)
            return result
        elif op_type == 'add':
            # 将ip添加到队列
            result = self._add_ip2queue(**args)
            return result
        elif op_type == 'remove':
            # 将ip添加到队列
            result = self._rm_ip2queue(**args)
            return result
        else:
            return {"code": 0, "message": "unsupported opreation %s" % op_type}

    def _create_queue(self, **args):
        '''
        创建队列
        '''
        arg_list = ['bandwidth', 'queue_id', 'qos_id']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        bandwidth = args['bandwidth']
        queue_id = args["queue_id"]
        qos_id = args["qos_id"]
        cmd = '/bin/bash %s%s%s%s "%s" "%s" "%s"' % (self.scripts_dir, 'network', os.sep, 'create_queue-wan', bandwidth, qos_id, queue_id)
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return {"code": 0, "message": err}
        else:
            return {"code": 1, "message": "success", "queue_uuid": result.strip()}

    def _add_ip2queue(self, **args):
        '''
        ip添加到队列
        '''
        arg_list = ['vm_wan_mac', 'queue_id', 'sw_dev_mac', 'sw_gw_mac', 'uplink_port']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        vm_wan_mac = args["vm_wan_mac"]
        queue_id = args["queue_id"]
        sw_dev_mac = args["sw_dev_mac"]
        sw_gw_mac = args["sw_gw_mac"]
        uplink_port = args["uplink_port"]
        cmd = 'ovs-ofctl add-flow br-wan \
                "table=0,priority=101,dl_src=%(vm_wan_mac)s,dl_dst=%(sw_dev_mac)s \
                actions=enqueue:%(uplink_port)s:%(queue_id)s"; \
                ovs-ofctl add-flow br-wan \
                "table=0,priority=101,dl_src=%(vm_wan_mac)s,dl_dst=%(sw_gw_mac)s \
                actions=enqueue:%(uplink_port)s:%(queue_id)s"' % {
            "vm_wan_mac": vm_wan_mac,
            "sw_dev_mac": sw_dev_mac,
            "uplink_port": uplink_port,
            "queue_id": queue_id,
            "sw_gw_mac": sw_gw_mac
        }
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return {"code": 0, "message": err}
        else:
            return {"code": 1, "message": "success"}

    def _rm_ip2queue(self, **args):
        '''
        从队列中删除
        '''
        arg_list = ['vm_wan_mac', 'queue_id', 'sw_dev_mac', 'sw_gw_mac', 'uplink_port']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        vm_wan_mac = args["vm_wan_mac"]
        queue_id = args["queue_id"]
        sw_dev_mac = args["sw_dev_mac"]
        sw_gw_mac = args["sw_gw_mac"]
        uplink_port = args["uplink_port"]
        cmd = 'ovs-ofctl del-flows br-wan \
                "table=0,dl_src=%(vm_wan_mac)s,dl_dst=%(sw_dev_mac)s"; \
                ovs-ofctl del-flows br-wan \
                "table=0,dl_src=%(vm_wan_mac)s,dl_dst=%(sw_gw_mac)s"' % {
            "vm_wan_mac": vm_wan_mac,
            "sw_dev_mac": sw_dev_mac,
            "sw_gw_mac": sw_gw_mac
        }
        result, err = utils.util_exec(cmd)
        if len(err) > 0:
            return {"code": 0, "message": err}
        else:
            return {"code": 1, "message": "success"}

    def lvs_nat_netnode(self, **args):
        arg_list = ['mode', 'op_type', 'net_mode']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        mode = 1 if int(args["mode"]) == 1 else 0
        op_type = args["op_type"]
        net_mode = args["net_mode"]
        user_vni = args["user_vni"]
        if mode == 1:
                # lvsnat不在同一宿主
            if net_mode == "lvsnat":
                if "director_int_mac" not in args:
                    return {"code": 0, "message": "director_int_mac required !"}
                director_int_mac = args["director_int_mac"]

                if "realserver_int_ip" not in args:
                    return {"code": 0, "message": "realserver_int_ip required !"}
                realserver_int_ip = args["realserver_int_ip"]

                if "realserver_int_mac" not in args:
                    return {"code": 0, "message": "realserver_int_mac required !"}
                realserver_int_mac = args["realserver_int_mac"]

                if "director_host_int_ip" not in args:
                    return {"code": 0, "message": "director_host_int_ip required !"}

                if "user_vni" not in args:
                    return {"code": 0, "message": "user_vni required!"}

                director_host_int_ip = args["director_host_int_ip"]

                host_vxlan_port = self._get_host_vxlan_port(director_host_int_ip)
                if not host_vxlan_port:
                    return {"code": 0, "message": "Tunnel endpoint to host %s not found !" % director_host_int_ip}
                # 添加
                if op_type == 'add':
                    template = "ovs-ofctl add-flow br-lan \"table=0,priority=100,\
                                ip,tun_id=%(user_vni)s,dl_dst=%(director_int_mac)s,dl_src=%(realserver_int_mac)s,nw_src=%(realserver_int_ip)s,\
                                actions=output:%(host_vxlan_port)s\""
                    command = template % {
                        "user_vni": user_vni,
                        "director_int_mac": director_int_mac,
                        "realserver_int_mac": realserver_int_mac,
                        "realserver_int_ip": realserver_int_ip,
                        "host_vxlan_port": host_vxlan_port
                    }
                    os.system(command)
                    return {"code": 1, "message": "SUCCESS"}
                # 删除
                elif op_type == 'remove':
                    template = "ovs-ofctl del-flows br-lan \"table=0,\
                                ip,tun_id=%(user_vni)s,dl_dst=%(director_int_mac)s,dl_src=%(realserver_int_mac)s,nw_src=%(realserver_int_ip)s\""
                    command = template % {
                        "user_vni": user_vni,
                        "director_int_mac": director_int_mac,
                        "realserver_int_mac": realserver_int_mac,
                        "realserver_int_ip": realserver_int_ip,
                    }
                    os.system(command)
                    return {"code": 1, "message": "SUCCESS"}

    def lvs_nat_computer(self, **args):
        arg_list = ['mode', 'op_type', 'op_object', 'net_mode']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        mode = 0 if int(args["mode"]) == 0 else 1
        op_type = args["op_type"]
        op_object = args["op_object"]
        net_mode = args["net_mode"]
        if mode == 0:
                # lvsnat同一宿主
            if net_mode == "lvsnat":
                if "director_int_mac" not in args:
                    return {"code": 0, "message": "director_int_mac required !"}
                director_int_mac = args["director_int_mac"]

                if "realserver_int_ip" not in args:
                    return {"code": 0, "message": "realserver_int_ip required !"}
                realserver_int_ip = args["realserver_int_ip"]
                # director
                if op_object == 'director':

                    if "realserver" not in args:
                        return {"code": 0, "message": "realserver required !"}
                    realserver = args["realserver"]

                    domain_lan_ovs_port = self._get_ovs_lan_port(realserver)
                    # 添加
                    if op_type == 'add':

                        template = "ovs-ofctl add-flow br-lan \"table=0,priority=100,\
	                                ip,dl_src=%(director_int_mac)s,nw_dst=%(realserver_int_ip)s,\
	                                actions=output:%(domain_lan_ovs_port)s\""
                        command = template % {
                            "director_int_mac": director_int_mac,
                            "realserver_int_ip": realserver_int_ip,
                            "domain_lan_ovs_port": domain_lan_ovs_port
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}
                    # 删除
                    elif op_type == 'remove':

                        template = "ovs-ofctl del-flows br-lan \"table=0,\
	                                ip,dl_src=%(director_int_mac)s,nw_dst=%(realserver_int_ip)s,\""
                        command = template % {
                            "director_int_mac": director_int_mac,
                            "realserver_int_ip": realserver_int_ip,
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}
                # realserver
                if op_object == 'realserver':

                    if "realserver_int_mac" not in args:
                        return {"code": 0, "message": "realserver_int_mac required !"}
                    realserver_int_mac = args["realserver_int_mac"]
                    # 添加
                    if op_type == 'add':

                        if "director" not in args:
                            return {"code": 0, "message": "director required !"}
                        director = args["director"]

                        domain_lan_ovs_port = self._get_ovs_lan_port(director)

                        template = "ovs-ofctl add-flow br-lan \"table=0,priority=101,\
	                                ip,dl_dst=%(director_int_mac)s,dl_src=%(realserver_int_mac)s,nw_src=%(realserver_int_ip)s\
	                                actions=output:%(domain_lan_ovs_port)s\""
                        command = template % {
                            "director_int_mac": director_int_mac,
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                            "domain_lan_ovs_port": domain_lan_ovs_port
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}
                    # 添加
                    elif op_type == 'remove':

                        template = "ovs-ofctl del-flows br-lan \"table=0,\
	                                ip,dl_dst=%(director_int_mac)s,dl_src=%(realserver_int_mac)s,nw_src=%(realserver_int_ip)s\""
                        command = template % {
                            "director_int_mac": director_int_mac,
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}
        if mode == 1:
            # lvsnat
            if net_mode == "lvsnat":
                if "realserver_int_mac" not in args:
                    return {"code": 0, "message": "realserver_int_mac required !"}
                realserver_int_mac = args["realserver_int_mac"]

                if "realserver_int_ip" not in args:
                    return {"code": 0, "message": "realserver_int_ip required !"}
                realserver_int_ip = args["realserver_int_ip"]

                if "realserver_int_vlan" not in args:
                    return {"code": 0, "message": "realserver_int_vlan required !"}
                realserver_int_vlan = args["realserver_int_vlan"]

                if "director" not in args:
                    return {"code": 0, "message": "director required !"}

                if "user_vni" not in args:
                    return {"code": 0, "message": "user_vni required !"}
                director = args["director"]
                user_vni = args["user_vni"]

                default_vxlan_port = args.get("default_vxlan_port", 1)
                # director
                if op_object == 'director':
                    # 添加
                    if op_type == 'add':

                        domain_lan_ovs_port = self._get_ovs_lan_port(director)

                        template = "ovs-ofctl add-flow br-lan \"table=0,priority=101,\
                                    ip,tun_id=%(user_vni)s,nw_src=%(realserver_int_ip)s,dl_src=%(realserver_int_mac)s,\
                                    action=strip_vlan,output:%(domain_lan_ovs_port)s\""
                        command = template % {
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                            "user_vni": user_vni,
                            "domain_lan_ovs_port": domain_lan_ovs_port
                        }
                        os.system(command)

                        template = "ovs-ofctl add-flow br-lan \"table=0,priority=100,\
                                    ip,nw_dst=%(realserver_int_ip)s,dl_dst=%(realserver_int_mac)s,\
                                    action=mod_vlan_vid:%(realserver_int_vlan)s,set_field:%(user_vni)s->tun_id,output:%(default_vxlan_port)s\""
                        command = template % {
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                            "realserver_int_vlan": realserver_int_vlan,
                            "user_vni": user_vni,
                            "default_vxlan_port": default_vxlan_port
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}
                    # 删除
                    if op_type == 'remove':

                        template = "ovs-ofctl del-flows br-lan \"table=0,\
                                    ip,tun_id=%(user_vni)s,nw_src=%(realserver_int_ip)s,dl_src=%(realserver_int_mac)s,\""
                        command = template % {
                            "user_vni": user_vni,
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                        }
                        os.system(command)

                        template = "ovs-ofctl del-flows br-lan \"table=0,\
                                    ip,nw_dst=%(realserver_int_ip)s,dl_dst=%(realserver_int_mac)s,\""
                        command = template % {
                            "realserver_int_ip": realserver_int_ip,
                            "realserver_int_mac": realserver_int_mac,
                        }
                        os.system(command)
                        return {"code": 1, "message": "SUCCESS"}

    def ip_white_list(self, **args):
        '''
        ip白名单
        '''
        cmd = ''
        arg_list = ['ywip', 'ip', 'instance_name']
        if utils.arg_exists(arg_list, **args):
            pass
        else:
            return {"code": 0, "message": "arg missing %s" % arg_list}
        db_ip = args["ywip"]
        ip = args["ip"]
        instance_name = args["instance_name"]
        op_type = args['op_type']
        if op_type == 'add':
            port = self._get_ovs_lan_port(instance_name)
            if not port:
                return {"code": 0, "message": "get ovs lan port failed."}
            cmd = 'ovs-ofctl add-flow br-lan \
                "table=2,priority=100,tun_id=0,ip, \
                nw_src=%s,nw_dst=%s,actions=strip_vlan,output:%s"' % (db_ip, ip, port)
        if op_type == 'remove':
            cmd = 'ovs-ofctl del-flows br-lan \
                "tun_id=0,ip, \
                nw_src=%s,nw_dst=%s"' % (db_ip, ip)
        if cmd:
            result, err = utils.util_exec(cmd)
            if len(err) > 0:
                return {"code": 0, "message": err}
            else:
                return {"code": 1, "message": "success"}
