import paramiko
p=paramiko.SSHClient()
with open("config.txt") as f:
    line=f.readline()
    ls=line.split(",")
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect("%s"%ls[0],port =22, username = "%s"%ls[1], password="%s"%ls[2])
    stdin, stdout, stderr = p.exec_command("uname -a")
    opt = stdout.readlines()
    opt ="".join(opt)
    print(opt)
    temp=open("%s.txt"%ls[0],"w")
    temp.write(opt)
    temp.close()


