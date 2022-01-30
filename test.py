#! /usr/bin/python3
# -*utf-8* 

from django import conf
import requests
import subprocess
import os
import vm_fonctions
import config

vm_fonctions.start_vmrest()
vm_fonctions.list_vms()

vm_fonctions.power_on(config.id_tor)

vm_fonctions.power_off(config.vm_kali_id)