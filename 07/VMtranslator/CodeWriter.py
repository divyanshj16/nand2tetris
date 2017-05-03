from constants import types_of_arithmetic_commands, types_of_segments,type_of_commands,seg_name,pointer_name

class CodeWriter(object):
    '''Converts VM commands to hack assembly commands'''

    eq = 'EQ_'
    default = 'DEFAULT_'
    gt = 'GT_'
    lt = 'LT_'
    static_ = 'static'
    temp_ = 5

    inc_SP = '\n@SP\nM = M + 1\n'
    pop2 = '\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n'
    in_pop1 = '\n@SP\nA = M\nA = A - 1\n'
    pop1 = '\n@SP\nA = M\n'
    u_jmp = '\n0;JMP'
    dec_SP = '@SP\nM = M - 1\n'





    def __init__(self):
        self.current_command = ''
        self.current_command_translation = ''
        self.eq_ctr = 1
        self.gt_ctr = 1
        self.default_ctr = 1
        self.lt_ctr = 1

    def write_arithmetic(self,command):
        self.current_command = command

        if command == 'add':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M + D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation

        if command == 'sub':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M - D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation

        if command == 'neg':
            self.current_command_translation = '//' + self.current_command + CodeWriter.in_pop1 + 'M = -M\n'
            return self.current_command_translation

        if command == 'eq':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + '@' + CodeWriter.eq + \
            str(self.eq_ctr) + '\nD = M - D;JEQ' + CodeWriter.pop1 + 'M = 0\n@' + CodeWriter.default + \
            str(self.default_ctr) + CodeWriter.u_jmp + '\n(' + CodeWriter.eq + str(self.eq_ctr) + ')\nM = -1\n(' + \
            CodeWriter.default + str(self.default_ctr) + ')' + CodeWriter.inc_SP
            self.eq_ctr += 1
            self.default_ctr += 1
            return self.current_command_translation

        if command == 'gt':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + '@' + CodeWriter.gt + \
            str(self.gt_ctr) + '\nD = M - D;JGT' + CodeWriter.pop1 + 'M = 0\n@' + CodeWriter.default + \
            str(self.default_ctr) + CodeWriter.u_jmp + '\n(' + CodeWriter.gt + str(self.gt_ctr) + ')\nM = -1\n(' + \
            CodeWriter.default + str(self.default_ctr) + ')' + CodeWriter.inc_SP
            self.gt_ctr += 1
            self.default_ctr += 1
            return self.current_command_translation


        if command == 'lt':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + '@' + CodeWriter.lt + \
            str(self.lt_ctr) + '\nD = M - D;JLT' + CodeWriter.pop1 + 'M = 0\n@' + CodeWriter.default + \
            str(self.default_ctr) + CodeWriter.u_jmp + '\n(' + CodeWriter.lt + str(self.lt_ctr) + ')\nM = -1\n(' + \
            CodeWriter.default + str(self.default_ctr) + ')' + CodeWriter.inc_SP
            self.lt_ctr += 1
            self.default_ctr += 1
            return self.current_command_translation

        if command == 'and':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M & D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation

        if command == 'or':
            self.current_command_translation = '//' + self.current_command + CodeWriter.pop2 + 'D = M | D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n'
            return self.current_command_translation

        if command == 'not':
            self.current_command_translation = '//' + self.current_command + CodeWriter.in_pop1 + 'M = !M\n'
            return self.current_command_translation

    def write_push_pop(self, c_type, segment, index):
        comment = '//' + type_of_commands[c_type] + ' ' + types_of_segments[segment] + ' ' + str(index) + '\n'

        if segment == 3:      #constant
             self.current_command_translation = comment + '@' + str(index) + '\nD = A\n@SP\nA = M\nM = D' + CodeWriter.inc_SP
             return self.current_command_translation

        if c_type == 1:   #push

            if segment in [0,1,4,5]:   #ARG,LCL,THIS,THAT
                self.current_command_translation = comment + '@' + str(index) + '\nD = A\n@' + seg_name[segment] + \
                 '\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n'

            if segment == 2:  #static
                self.current_command_translation = comment + '@' + CodeWriter.static_ + '.' + str(index) + \
                 '\nD = M\n@SP\nA = M\nM = D' + CodeWriter.inc_SP

            if segment == 7:  #temp
                self.current_command_translation = comment + '@' + str(CodeWriter.temp_ + index) + \
                '\nD = M\n@SP\nA = M\nM = D\nM = M + 1\n'\

            if segment == 6: #pointer
                self.current_command_translation = comment + '@' + pointer_name[index] + \
                 '\nD = A\n@SP\nA = M\nM = D\nM = M + 1\n'


        if c_type == 2:  #pop

            if segment in [0,1,4,5]:   #ARG,LCL,THIS,THAT
                self.current_command_translation = comment + CodeWriter.dec_SP + '@' + str(index) + \
                 '\nD = A\n@' + seg_name[segment] + '\nA = M\nD = A + D\n@R13\nM = D\n@SP\nA = M\nD = M\n@R13\nA = M\nM = D\n'

            if segment == 2:  #static
                self.current_command_translation = comment + CodeWriter.dec_SP + 'A = M\nD = M\n@' + \
                CodeWriter.static_ + '.' + str(index) + '\nM = D\n'

            if segment == 7: #temp
                self.current_command_translation = comment + CodeWriter.dec_SP + 'A = M\nD = M\n@' + \
                 str(CodeWriter.temp_ + index) + '\nM = D\n'

            if segment == 6: #pointer
                self.current_command_translation = comment + CodeWriter.dec_SP + 'A = M\nD = M\n@' + pointer_name[index] + '\nM = D\n'

        return self.current_command_translation


        # comment = '//' + type_of_commands[c_type] + ' ' + types_of_segments[segment] + ' ' + str(index) + '\n'
        # if segment == 0:
        #     if c_type == 1:   #ARG
        #         self.current_command_translation = comment + '@' + str(index) + '\nD = A\n@ARG\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n'
        #         return self.current_command_translation
        # if segment == 3:      #constant
        #     self.current_command_translation = comment + '@' + str(index) + '\nD = A\n@SP\nA = M\nM = D' + CodeWriter.inc_SP
        #     return self.current_command_translation
