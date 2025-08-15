import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x srk')
    os.system('./srk')
elif bit == '32bit':
    os.system('chmod +x srk32')
    os.system('./srk32')
else:
    print('device not supported')
