import paramiko
paramiko.util.log_to_file('/tmp/paramiko.log')

# Open a transport

host = "137.195.183.53"
port = 22
transport = paramiko.Transport((host, port))

# Auth

password = "helmi"
username = "helmi"
transport.connect(username = username, password = password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download

filepath = '/media/disk2/helmi/hazard_clips/Clips/07012018Jace.wmv'
localpath = '/home/helmi/test.wmv'
sftp.get(filepath, localpath)

# Upload

# filepath = '/home/foo.jpg'
# localpath = '/home/pony.jpg'
# sftp.put(localpath, filepath)

# Close

sftp.close()
transport.close()
