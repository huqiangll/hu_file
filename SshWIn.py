import subprocess
import sys

ssh = subprocess.Popen([r"ssh",
                    "root@106.15.244.173",
                    "-pw", "Huqiang2018",
                    "-C", "uname -a"],
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
error = ssh.stderr.readlines()
if error:
    for err in error:
        sys.stderr.write("ERROR: {}\n".format(err,encoding='utf-8'))
if result:
    print(result)