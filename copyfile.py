import os
import shutil

src = 'path of source folder'

des = 'path of destination folder'

for filename in os.listdir(src)
    if filename.endswith('.xlsx')
        shutil.copy(src + '/' +filename, des)
        print(filename)
