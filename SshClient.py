
#linux
import sys

from pexpect import pxssh

ssh = pxssh.pxssh()


class SshClient(object):

    def conn(self, hostname, username, password):
        return ssh.login(hostname, username,password, original_prompt='[$#>]')


    def close_conn(self):
        ssh.logout()

    def exec_cmd(self, cmd):
        ssh.sendline(cmd)
        ssh.prompt()
        print (ssh.before)

if __name__ == '__main__':
    print (sys.platform)
    a = SshClient()
    a.conn('106.15.224.173','root','Huqiang2018')

    a.exec_cmd('ls -l')
    a.close_conn()