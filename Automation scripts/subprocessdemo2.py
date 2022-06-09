import subprocess, sys

cmd = "netstat -p tcp"

p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == "" and p.poll() != None:
        break
    if out != "":
        sys.stdout.write(out.decode())
        sys.stdout.flush()
