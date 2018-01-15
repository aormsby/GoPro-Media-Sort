import sys
import os
import fnmatch

# TODO modify program so it can be run from any directory
TARGET_DIR = sys.argv[1]

# TODO clean up program based on pyLint criteria
dirsflagged = []

def flagdirs():
    extensions = ['*.[Jj][Pp][Gg]', '*.[Mm][Pp]4']
    # for root, dirs, files in os.walk('.'):
    for root, dirs, files in os.walk(TARGET_DIR):
        # print (root, dirs, files)
        if 'photo' in dirs or 'video' in dirs or root.endswith('photo') or root.endswith('video'):
            # print (root, dirs, files)
            # print(root)
            continue
        for ext in extensions:
            match = []
            for filename in fnmatch.filter(files, ext):
                # print(filename)
                match.append(filename)
            if match:
                dirsflagged.append([ext, root, match])
    # print(dirsflagged[0][1])

def arrangemedia ():
    for dirs in dirsflagged:
        newpath = ''
        if dirs[0] == '*.[Jj][Pp][Gg]':
            # print('J', dirs)
            newpath = dirs[1] + '/photo'
            if not os.path.exists(newpath):
                os.makedirs(newpath)
        elif dirs[0] == '*.[Mm][Pp]4':
            # print('M', dirs)
            newpath = dirs[1] + '/video'
            if not os.path.exists(newpath):
                os.makedirs(newpath)
        for files in dirs[2]:
            os.rename(dirs[1] + '/' + files, newpath + '/' + files)
            # print(newpath + '/' + files)

def displaycomplete ():
    print('\n* sort complete *\n')

flagdirs()
arrangemedia()
displaycomplete();
