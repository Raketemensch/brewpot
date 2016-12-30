#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE

devicePath = '/sys/bus/w1/devices/'
powerSwitchBin = '/usr/local/bin/codesend'
#onCode = '21811'
#offCode = '21820'

def turnOutletOn(onCode):
    print 'turning outlet on....'
    proc = Popen(powerSwitchBin + ' ' + onCode, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    print out, err, proc.returncode

def turnOutletOff(offCode):
    print 'turning outlet off....'
    proc = Popen(powerSwitchBin + ' ' + offCode, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    print out, err, proc.returncode

#turnOutletOn(onCode)
#turnOutletOff(offCode)