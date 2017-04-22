class CodeWriter(object):
    '''Converts VM commands to hack assembly commands'''

    eq = 'EQ_'
    eq_ctr = 1
    default = 'DEFAULT_'
    default_ctr = 1

    inc_SP = '\n@SP\nM = M + 1\n'
    pop2 = '\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n'
    in_pop1 = '\n@SP\nA = M\nA = A - 1\n'
    pop1 = '\n@SP\nA = M\n'
    u_jmp = '\n0;JMP'



    def __init__(self):
        self.current_command = ''
        self.current_command_translation = ''

    def write_arithmetic(self,command):
        self.current_command = command
        if command == 'add':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M + D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation
        if command == 'sub':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M - D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation
        if command == 'neg':
            self.current_command_translation = '//' + self.current_command + CodeWriter.in_pop1 + 'M = -M' + CodeWriter.inc_SP
            return self.current_command_translation
        if command == 'eq':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + '@' + CodeWriter.eq + \
            str(CodeWriter.eq_ctr) + '\nD = M - D;JEQ' + CodeWriter.pop1 + 'M = 0\n@' + CodeWriter.default + \
            str(CodeWriter.default_ctr) + CodeWriter.u_jmp + '\n(' + CodeWriter.eq + str(CodeWriter.eq_ctr) + ')\nM = -1\n(' + \
            CodeWriter.default + str(CodeWriter.default_ctr) + ')' + CodeWriter.inc_SP
            CodeWriter.eq_ctr += 1
            CodeWriter.default_ctr += 1
            return self.current_command_translation
