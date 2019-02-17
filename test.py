import wexpect

child = wexpect.run("ssh root@106.15.224.173 'ls -l'", events={'(?i)password': 'Huqiang2018\\n'})
print child