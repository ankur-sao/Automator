from os import listdir
from os.path import isfile, join

mypath = '/Users/ansao/Desktop/pythonPlayGround/files'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for files in onlyfiles:
    print 'file: {0}'.format(files)

replacements = {'girlfriend': 'Hope', '<manager>' : 'madhavi', '<boss>': 'ramesh'}

for files in onlyfiles:
    fileInMemory = []
    with open(join(mypath, files)) as infile:
        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            fileInMemory.append(line)
    with open(join(mypath,files), 'w') as outfile:
        for line in fileInMemory:
            outfile.write(line)




