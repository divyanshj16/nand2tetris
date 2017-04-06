class Parser(object):
    types_of_commands = ['add','sub','neg','eq','gt','lt','and','or','not']

    def cleaner(self,command):
        command =  command.strip()
        if len(command) < 1:
            return ""                           #for empty line
        elif command.startswith("//"):
            return ""                           #for empty line
        else:
            return command.split('//')[0].strip()


    def command_type(self,command):
        pass
