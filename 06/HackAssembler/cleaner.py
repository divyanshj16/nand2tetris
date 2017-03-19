import re

class Cleaner(object):
    def clean(self,line):
        line = re.sub(r'\s+', '', line)
        instruction = line.split('//')[0]
        return instruction

def main():
    cleaner = Cleaner()
    string = input("Enter the string to be cleared: ")
    print(cleaner.clean(string))

if __name__ == '__main__':
    main()    
