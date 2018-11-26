import os
import shutil
source = 'Source'
result = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))
my_dir = os.path.join(current_dir, source)
work_dir = os.path.join(current_dir, result)

os.chdir(my_dir)

if result not in os.listdir(current_dir):
    os.makedirs(work_dir)
for files in os.listdir(my_dir):
    shutil.copy(files, work_dir, follow_symlinks=True)

os.chdir(work_dir)

for files in os.listdir(work_dir):
    print(files)
    args = 'sips --resampleWidth 200 ' + files
    print(args)
    os.system(args)
