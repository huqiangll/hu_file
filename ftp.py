import sys

import winpexpect
from pexpect import TIMEOUT
from pip._vendor.webencodings.tests import assert_raises

ps = winpexpect.winspawn('powershell.exe -command -')
assert_raises(TIMEOUT, ps.wait, timeout=2)
ps.terminate()

child = winpexpect.winspawn('ssh', ['-tty','root@106.15.224.173'])
child.logfile = sys.stdout

child.sendline('Huqiang2018')
child .sendline('ls -l /')
print('Now enter the FTP interactive mode')
child.interact()