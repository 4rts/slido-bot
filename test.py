import os


sudoPassword = 'Err0r:Success!'
command = 'protonvpn c -r'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))