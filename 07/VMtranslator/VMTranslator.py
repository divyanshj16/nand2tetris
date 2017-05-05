import CodeWriter
import parser
import constants
import sys

in_file = sys.argv[1]
out_file = in_file.split('.')[0] + '.asm'

with open(in_file,'r') as fin:
    with open(out_file,'w') as fout:
        for line in fin:
            ps = parser.Parser()
            cw = CodeWriter.CodeWriter()
            cleaned = ps.clean(line)
            if cleaned != '':
                c_type = ps.command_type(cleaned)
                ps.split_command(cleaned)
                arg2 = ps.arg2
                segment = ps.command_id
                if c_type == 0:
                    translation = cw.write_arithmetic(cleaned)
                if c_type == 1 or c_type == 2:
                    translation = cw.write_push_pop(c_type,segment,int(arg2))
                fout.write(translation)
