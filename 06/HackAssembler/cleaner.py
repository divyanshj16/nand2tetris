import re

class Cleaner(object):
    """Cleans the instruction from whitespaces and comments"""

    addressCounter = 15

    labels = {                  #dictionary fro predefined labels
    'R0' : '0',
    'R1' : '1',
    'R2' : '2',
    'R3' : '3',
    'R4' : '4',
    'R5' : '5',
    'R6' : '6',
    'R7' : '7',
    'R8' : '8',
    'R9' : '9',
    'R10' : '10',
    'R11' : '11',
    'R12' : '12',
    'R13' : '13',
    'R14' : '14',
    'R15' : '15',
    'SCREEN' : '16384',
    'KBD' : '24576',
    'SP' : '0',
    'LCL' : '1',
    'ARG' : '2',
    'THIS' : '3',
    'THAT' : '4'
    }

    def clean(self,line):
        if line.startswith('('):
            return None
        line = re.sub(r'\s+', '', line)         #removes whitespaces
        instruction = line.split('//')[0]       #removes comments
        return instruction

    def addLabel(self,label,ctr):
        Cleaner.labels[label] = ctr
        print(Cleaner.labels[label])

    def getVariableAddress(self,string):
        try:
            value = Cleaner.labels[string]
            return value
        except KeyError:
            Cleaner.addressCounter += 1             #variables can be allocated from adddress 16
            Cleaner.labels[string] = Cleaner.addressCounter
            print(Cleaner.addressCounter)
            return Cleaner.addressCounter


def main():
    cleaner = Cleaner()
    string = input("Enter the string to be cleared: ")
    print(cleaner.clean(string))

if __name__ == '__main__':
    main()
