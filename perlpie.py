'''A python replacement for perl -p -i -e 's/replaced/replacement/g' `find . -type f`
param1: directory
param2: string to replace
param3: replacement string

'''

import string
import sys
import getopt
import os

def listfiles(dir,replace,replacement):
    basedir = dir
    subdirlist = []
    for item in os.listdir(basedir):
        if os.path.isfile(os.path.join(basedir,item)):
            if not os.path.join(basedir,item) == 'perlpie.py':
                print os.path.join(basedir,item)
                s = ''
                try:
                    f = open(os.path.join(basedir,item), 'r+')
                    s = f.readlines()
                finally:
                    f.close()
                s = string.join(s, '')
                s = s.replace("tiny",replacement)
                if os.path.join(basedir,item) == 'urls.py':
                    print s
                try:
                    f = open(os.path.join(basedir,item), 'w+')
                    f.write(s)
                finally:
                    f.close()
        else:
            subdirlist.append(os.path.join(basedir, item))
    for subdir in subdirlist:
        listfiles(subdir,replace,replacement)

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    if len(args) < 3:
        print "Error: Mission params\nparam1: directory \nparam2: string to replace \nparam3: replacement string"
        return
    # process arguments
    listfiles(args[0], args[1], args[2]) # process() is defined elsewhere

if __name__ == '__main__':
    main()
