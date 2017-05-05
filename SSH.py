import paramiko

def SSH(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username='admin', password='admin',timeout=20)
        return ip
    except:
        pass
if __name__== "__main__":
    w = open('success.txt','w')
    ip = open('ip.txt','r').read()
    spl = ip.split()
    for i in spl:
        a = SSH(i)
        if (a != None):
            w.write(a + "\n")
    print "Finish!"
    w.close()
