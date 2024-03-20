import paramiko

def run_src(**kwargs)
  client = paramiko.Transport((url, port))
  if client:
    privKeyPath = join(dirname(abspath(file), 'example.key')
    privKey = paramiko.Ed25519Key.from_private_key_file(filename = privKeyPath)  
    client.connect(username, pkey)
    session = client.open_channel(kind='session')
