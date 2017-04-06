class Parser(object):
    types_of_arithmetic_commands = ['add','sub','neg','eq','gt','lt','and','or','not']

    def __init__(self):
        self.arg1 = ''
        self.arg2 = ''
        self.command = ''
        self.type = 100

    def cleaner(self,command):
        stripped_command =  command.strip()
        if len(stripped_command) < 1:
            return ""                           #for empty line
        elif stripped_command.startswith("//"):
            return ""                           #for empty line
        else:
            self.command = stripped_command.split('//')[0].strip()
            return self.command                   #for inline comments and normal commands


    def command_type(self,command):
        com_type = command.split()[0]
        if com_type in Parser.types_of_arithmetic_commands:
            self.type = 0
            return 0                                # For arithmetic commands i.e c_arithmetic
        if com_type == 'push':
            self.type = 1
            return 1                                # For c_push or push commands
        if com_type == 'pop':
            self.type = 2
            return 2                                # For c_pop commands

        #for c_return split method is not called

    def split_command(self,command):
        parts = command.split()
        if self.type == 0:
            self.arg1 = command
            self.arg2 = ''
        if self.type == 1 or self.type == 2:
            self.arg1 = parts[1]
            self.arg2 = parts[2]
