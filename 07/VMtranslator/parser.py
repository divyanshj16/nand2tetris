class Parser(object):
    types_of_arithmetic_commands = ['add','sub','neg','eq','gt','lt','and','or','not']


    def cleaner(self,command):
        command =  command.strip()
        if len(command) < 1:
            return ""                           #for empty line
        elif command.startswith("//"):
            return ""                           #for empty line
        else:
            return command.split('//')[0].strip()  #for inline comments and normal commands


    def command_type(self,command):
        com_type = command.split()[0]
        if com_type in Parser.types_of_arithmetic_commands:
            return 0                                # For arithmetic commands i.e c_arithmetic
        if com_type == 'push':
            return 1                                # For c_push or push commands
        if com_type == 'pop':
            return 2                                # For c_pop commands
