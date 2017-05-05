from constants import types_of_arithmetic_commands, types_of_segments


class Parser(object):



    def __init__(self):
        self.arg1 = ''
        self.arg2 = ''
        self.command = ''
        self.command_id = -1
        self.type = 100

    def clean(self,command):
        stripped_command =  command.strip()
        if len(stripped_command) < 1:
            return ""                           #for empty line
        elif stripped_command.startswith("//"):
            return ""                           #for comment
        else:
            self.command = stripped_command.split('//')[0].strip()
            return self.command                   #for inline comments and normal commands


    def command_type(self,command):
        com_type = command.split()[0]
        if com_type in types_of_arithmetic_commands:
            self.type = 0
            return 0                                # 0 is For arithmetic commands i.e c_arithmetic
        if com_type == 'push':
            self.type = 1
            return 1                                # 1 is For c_push or push commands
        if com_type == 'pop':
            self.type = 2
            return 2                                # 2 is For c_pop commands

        #for c_return split method is not called

    def split_command(self,command):
        parts = command.split()
        if self.type == 0:
            self.arg1 = command
            self.arg2 = ''
        if self.type == 1 or self.type == 2:
            self.arg1 = parts[1]
            self.arg2 = parts[2]
            self.command_id = Parser.set_command_id(self.arg1)

    def set_command_id(segment):
        return types_of_segments.index(segment)
