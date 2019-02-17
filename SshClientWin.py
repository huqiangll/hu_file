import traceback

import pexpect
from pexpect.popen_spawn import PopenSpawn




try:
    child = PopenSpawn('ssh  root@106.15.224.173')  # powershellz
    child.sendline('Huqiang2018')
    print child.before, child.after

    i = child.expect([pexpect.TIMEOUT,'password: '])
    if i == 0:  # Timeout
        print 'ERROR!'
        print 'SSH could not login. Here is what SSH said:'
        print child.before, child.after
    if i == 1:
        child.sendline('Huqiang2018')
        child.sendline('ls -l')
        print child.before, child.after
except pexpect.EOF:
    traceback.print_exec()
