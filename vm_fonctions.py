#! /usr/bin/python3
# -*utf-8* 
import requests
import subprocess
import os
import time

headers = {'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'}
url_liste = "http://127.0.0.1:8697/api/vms"

def start_vmrest():
    subprocess.call("vmrest")
    print("vmrest start")

def stop_vmrest():
    os.system('pkill vmrest')

def list_vms():
    all_vm = requests.get(url_liste,auth=('babidi','Pa$$w0rd'))
    print(all_vm.json())
    return all_vm

def power_on(id):
    url_vm = f"http://127.0.0.1:8697/api/vms/{str(id)}/power"
    requete_start = requests.put(url_vm,auth=('babidi','Pa$$w0rd'),data='on',headers=headers)
    print(f"VM start")
    vm = "start"
    return vm

def power_off(id):
    url_vm = f"http://127.0.0.1:8697/api/vms/{str(id)}/power"
    requete_start = requests.put(url_vm,auth=('babidi','Pa$$w0rd'),data='off',headers=headers)
    print(f"VM Stop")
    vm = "stop"
    return vm

def show_ip(id):
    url_ip = f"http://127.0.0.1:8697/api/vms/{str(id)}/ip"
    request_ip = requests.get(url_ip,auth=('babidi','Pa$$w0rd'))
    print(request_ip.json())

def show_state(id):
    url_vm = f"http://127.0.0.1:8697/api/vms/{id}"
    r_state = requests.get(url_vm,auth=('babidi','Pa$$w0rd'))
    print(r_state.content)

