print 'h'
import os
import sys
import traceback

#import winpexpect

import pexpect
#import winpexpect
from pexpect import popen_spawn
from pexpect.popen_spawn import PopenSpawn
#child = winpexpect.winspawn('ssh -tt root@192.168.100.99')


def something():
    child = PopenSpawn('ssh root@106.15.224.173')  # powershell
    print child.before, child.after
    i = child.expect('password')
    if i == 0:  # Timeout
        print 'ERROR!'
        print 'SSH could not login. Here is what SSH said:'
        print child.before, child.after
        return None
    if i == 1:
        child.sendline('Huqiang2018')
        print child.before.decode('gbk')
    return child

if __name__ == '__main__':
    try:
       something()
    except Exception,e:
        print (e)
        traceback.print_exc()
        os._exit(1)




