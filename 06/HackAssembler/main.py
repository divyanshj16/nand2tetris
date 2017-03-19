import parser
import translator
import cleaner
import sys
import os

inFile = sys.argv[1]
outFile = inFile.split('.')[0] + '.hack'

cleaner = cleaner.Cleaner()
translator = translator.Translator()

try:
    fin = open(inFile,'r')
    fout = open(outFile,'w')
    for line in fin:
        if cleaner.clean(line):
            parsed = parser.Parser(line)
            iType = parsed.type()
            print (iType + "\n" )

            if iType == 'A':
                hackCode = '0' + translator.aInst(line[1:])

            if iType == 'C':
                hackCode = '111' + translator.comp(parsed.comp) + translator.dest(parsed.dest) + translator.jmp(parsed.jmp)

            print(hackCode + '\n')
            fout.write(hackCode + '\n')
        else:
            print("comment or emptyline\n")

    fin.close()
    fout.close()

except FileNotFoundError:
    print("pass Valid file name as argument")
