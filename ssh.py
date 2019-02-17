import traceback



import pexpect
from pexpect.popen_spawn import PopenSpawn

try:
    child = PopenSpawn('cmd')
    child.sendline('ping')
    child.sendline('exit')
    child.expect(pexpect.EOF)
    out = child.before.decode('gbk')
    print out

except pexpect.EOF:
    traceback.print_exc()