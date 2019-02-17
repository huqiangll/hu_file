import winpexpect as winpexpect

winpexpect.run("ssh root@106.15.224.173 'mkdir hu'", events={'(?i)password': 'Huqiang2018\\n'})
print 'hhhhhhhhhhhhhh'
import sys, winpexpect
child = winpexpect.winspawn('nslookup')
child.logfile = sys.stdout
child.expect('\n>')
child.sendline('www.google.com')
child.expect('\n>')

result = winpexpect.winspawn('ssh %s@%s' % ('root','106.15.224.173'))
print result.before,child.after
result.sendline('Huqiang2018')
result.sendline('ls -l')
print result.before,result.after
result.interact()
print 'hu'


result = winpexpect.run ("ssh  root@106.15.224.173   'hostname hu'", events={'(?i)password':'Huqiang2018\\n'})

print 'hu'


def test_expect():
    ps = winpexpect.winspawn('ping')
    ps.sendline('exit')
    print ps.before.decode('gbk')
    ps.terminate()
test_expect()

a ='\xcf\xb5\xcd\xb3\xd5\xd2\xb2\xbb\xb5\xbd\xd6\xb8\xb6\xa8\xb5\xc4\xce\xc4\xbc\xfe\xa1\xa3'
print a.decode('gbk')

