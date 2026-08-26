import subprocess
ps_num = 1
num = 5
file_prefix = '_ps'+str(ps_num)+'_'
lastname = ''
filetowrite="_ps"+str(ps_num)+"_outputs.txt"
with open(filetowrite,"x"):
    pass
for i in range(1,num+1):
    filename = file_prefix + str(i) + lastname + '.py'
    print(filename)
    result = subprocess.run(['python',filename],capture_output=True,text=True)
    with open(filetowrite, "a") as f:
        f.write("-"*10 + filename + "-"*10 + '\n')
        f.write(result.stdout)
