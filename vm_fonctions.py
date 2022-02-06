#! /usr/bin/python3
# -*utf-8* 
import requests
import subprocess
import os
import config

headers = {'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'}
url_liste = "http://127.0.0.1:8697/api/vms"

def start_vmrest():
    subprocess.Popen("start_vmrest.sh", shell=True)
    print("vmrest start")

def stop_vmrest():
    os.system('pkill vmrest')

def list_vms():
    all_vm = requests.get(url_liste,auth=(config.username,config.password))
    print(all_vm.json())
    return all_vm

def power_on(id):
    # before see if already start
    state = show_state(id)
    if state == "poweredOff":
        url_vm = f"http://127.0.0.1:8697/api/vms/{str(id)}/power"
        requete_start = requests.put(url_vm,auth=(config.username,config.password),data='on',headers=headers)
        print(f"VM start")
        vm = "start"
    else:
        vm = "start"
        print("VM déjà allumée")
    return vm

def power_off(id):
    state = show_state(id)
    if state == "poweredOn":
        url_vm = f"http://127.0.0.1:8697/api/vms/{str(id)}/power"
        requete_stop = requests.put(url_vm,auth=(config.username,config.password),data='off',headers=headers)
        print(f"VM Stop")
        vm = "stop"
    else:
        vm = "stop"
        print("VM déjà allumée")
    return vm

def show_ip(id):
    url_ip = f"http://127.0.0.1:8697/api/vms/{str(id)}/ip"
    request_ip = requests.get(url_ip,auth=(config.username,config.password))
    print(request_ip.json())

def show_components(id):
    url_vm = f"http://127.0.0.1:8697/api/vms/{id}"
    r_state = requests.get(url_vm,auth=(config.username,config.password))
    print(r_state.content)

def show_state(id):
    url_vm = f"http://127.0.0.1:8697/api/vms/{str(id)}/power"
    r_state = requests.get(url_vm,auth=(config.username,config.password))
    return r_state.json()['power_state']
