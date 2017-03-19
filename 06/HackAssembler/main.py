import parser
import translator
import cleaner
import sys
import os

inFile = sys.argv[1]                               #take input from command line
outFile = inFile.split('.')[0] + '.hack'            #outFile is a hack file with same name as input file

cleaner = cleaner.Cleaner()                        #making cleaner object
translator = translator.Translator()                #translator object creation

try:
    fin = open(inFile,'r')
    fout = open(outFile,'w')                       #write mode outfile
    for line in fin:              # PASS: 2
        if cleaner.clean(line):                     #cleaner returns empty string if find a full line comment or a empty line
            line = cleaner.clean(line)
            #print(line)
            parsed = parser.Parser(line)            #parses the line
            iType = parsed.type()                  #gets the type of instruction
            print (iType)

            if iType == 'A':
                hackCode = '0' + translator.aInst(line[1:])   #opcode for a instruction is 0 followed by the 15 bit address passed to translator

            if iType == 'C':
                hackCode = '111' + translator.comp(parsed.comp) + translator.dest(parsed.dest) + translator.jmp(parsed.jmp) #gathers destination computaion and jump parts in binary format and concatenates to 111 which op-code of c instruction

            print(hackCode)
            fout.write(hackCode + '\n')
        else:
            print("comment or emptyline\n")

    fin.close()
    fout.close()

except FileNotFoundError:
    print("pass Valid file name as argument")
