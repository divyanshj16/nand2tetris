class Translator(object):
    compDict = {                       #dictionary for computation from n2t book
    "0" : "0101010",
    "1" : "0111111",
    "-1" : "0111010",
    "D" : "0001100",
    "A" : "0110000",
    "!D" : "0001101",
    "!A" : "0110001",
    "-D" : "0001111",
    "-A" : "0110011",
    "D+1" : "0011111",
    "A+1" : "0110111",
    "D-1" : "0001110",
    "A-1" : "0110010",
    "D+A" : "0000010",
    "D-A" : "0010011",
    "A-D" : "0000111",
    "D&A" : "0000000",
    "D|A" : "0010101",
    "M" : "1110000",
    "!M" : "1110001",
    "-M" : "1110011",
    "M+1" : "1110111",
    "M-1" : "1110010",
    "D+M" : "1000010",
    "D-M" : "1010011",
    "M-D" : "1000111",
    "D&M" : "1000000",
    "D|M" : "1010101"
    }

    jmpDict = {             #dictionary for jump commands
    "null" : "000",
    "JGT" : "001",
    "JEQ" : "010",
    "JGE" : "011",
    "JLT" : "100",
    "JNE" : "101",
    "JLE" : "110",
    "JMP" : "111"
    }

    destDict = {            #dictionary for destination commands
    "null" : "000",
    "M" : "001",
    "D" : "010",
    "MD" : "011",
    "A" : "100",
    "AM" : "101",
    "AD" : "110",
    "AMD" : "111"
    }
    def __init__(self):
        pass

    def comp(self, comp):
        return Translator.compDict[comp]

    def dest(self, dest):
        return Translator.destDict[dest]

    def jmp(self, jmp):
        return Translator.jmpDict[jmp]

    def aInst(self, address):
        binaryAddress = bin(int(address))[2:]       #converting address to binary
        mult = 15 - len(binaryAddress);             #converting to 15 bit binary as required by the hardware
        actualAddress = "0" * mult + binaryAddress
        return actualAddress

def main():
    translator = Translator()
    cType = input("enter comp part: ")
    print (translator.comp(cType))
    jType = input("enter jmp part: ")
    print (translator.jmp(jType))
    dType = input("enter dest part: ")
    print (translator.dest(dType))
    aType = input("enter address: ")
    print (translator.aInst(aType))

if __name__ == '__main__':
    main()
