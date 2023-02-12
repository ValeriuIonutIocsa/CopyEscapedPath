import sys
import time
import os

import pyperclip

start_time = time.time()
sys.stdout.write('\nstarting copy escaped path script\n')

if sys.argv.__len__() < 2:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

sys.stderr.write('\n')

file_path = sys.argv[1]
sys.stderr.write('file path:\n' + file_path + '\n')

abs_file_path = os.path.abspath(file_path)
escaped_file_Path = abs_file_path.replace('\\', '\\\\')
sys.stderr.write('escaped file path:\n' + escaped_file_Path + '\n')

pyperclip.copy(escaped_file_Path)
pyperclip.paste()

exec_time = str(round(time.time() - start_time, 2))
sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n\n')
