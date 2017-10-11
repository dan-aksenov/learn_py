import os, sys

'''
Change file's extension.
'''

work_dir = sys.argv[1]
old_ext = sys.argv[2]
new_ext = sys.argv[3]
old_ext = "." + old_ext
print old_ext
new_ext = "." + new_ext

files = os.listdir(work_dir)
for filename in files:
  file_ext = os.path.splitext(filename)[1]
  if old_ext == file_ext:
   # print old_ext
    newfile = filename.replace(old_ext,new_ext)
    os.rename(
      os.path.join(work_dir, filename),
        os.path.join(work_dir, newfile))
