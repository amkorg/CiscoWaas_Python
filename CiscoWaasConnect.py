def waas_connect(hostname):
  try:
#    hostname = 'AARTA211'
    username = 'user_name'
    password = 'user_password'
    command = 'sh run | i tacacs host'
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    data = stdout.read()
    print(hostname)
    print(data)
    datastr = str(data, 'utf-8')
    print(datastr)

if __name__ = '__main__':
  hostname = 'abcwaas101'
  waas_connect(hostname)