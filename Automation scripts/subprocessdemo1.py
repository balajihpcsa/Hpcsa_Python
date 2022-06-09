import subprocess

cmd = "dir"
#return
returned_output = subprocess.check_output(cmd, shell=True)
#decode will convert output from bytes to string
print("current directory : ", returned_output.decode("utf-8"))
