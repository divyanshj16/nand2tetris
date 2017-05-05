import unittest
from CodeWriter import CodeWriter

class TestCodeWriter(unittest.TestCase):
    '''Test class for CodeWriter Class'''

    def setUp(self):
        self.cdw = CodeWriter()

    def test_write_arithmetic_add(self):
        converted_string = self.cdw.write_arithmetic("add")
        self.assertEqual(converted_string,"//add\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M + D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n")

    def test_write_arithmetic_sub(self):
        converted_string = self.cdw.write_arithmetic('sub')
        self.assertEqual(converted_string,'//sub\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n')

    def test_write_arithmetic_neg(self):
        converted_string = self.cdw.write_arithmetic('neg')
        self.assertEqual(converted_string,'//neg\n@SP\nA = M\nA = A - 1\nM = -M\n')

    def test_write_arithmetic_eq(self):
        CodeWriter.default_ctr = 1
        CodeWriter.lt_ctr = 1
        CodeWriter.gt_ctr = 1
        converted_string = self.cdw.write_arithmetic('eq')
        self.assertEqual(converted_string,'//eq\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@EQ_1\nD;JEQ\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(EQ_1)\n@SP\nA = M\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_arithmetic('eq')
        self.assertEqual(converted_string,'//eq\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@EQ_2\nD;JEQ\n@SP\nA = M\nM = 0\n@DEFAULT_2\n0;JMP\n(EQ_2)\n@SP\nA = M\nM = -1\n(DEFAULT_2)\n@SP\nM = M + 1\n')

    def test_write_arithmetic_gt(self):
        CodeWriter.default_ctr = 1
        CodeWriter.lt_ctr = 1
        CodeWriter.gt_ctr = 1
        converted_string = self.cdw.write_arithmetic('gt')
        self.assertEqual(converted_string,'//gt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@GT_1\nD;JGT\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(GT_1)\n@SP\nA = M\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        self.cdw.write_arithmetic('gt')
        self.cdw.write_arithmetic('eq')
        converted_string = self.cdw.write_arithmetic('gt')
        self.assertEqual(converted_string,'//gt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@GT_3\nD;JGT\n@SP\nA = M\nM = 0\n@DEFAULT_4\n0;JMP\n(GT_3)\n@SP\nA = M\nM = -1\n(DEFAULT_4)\n@SP\nM = M + 1\n')

    def test_write_arithmetic_lt(self):
        CodeWriter.default_ctr = 1
        CodeWriter.lt_ctr = 1
        CodeWriter.gt_ctr = 1
        converted_string = self.cdw.write_arithmetic('lt')
        self.assertEqual(converted_string,'//lt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@LT_1\nD;JLT\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(LT_1)\n@SP\nA = M\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        self.cdw.write_arithmetic('lt')
        self.cdw.write_arithmetic('eq')
        self.cdw.write_arithmetic('gt')
        converted_string = self.cdw.write_arithmetic('lt')
        self.assertEqual(converted_string,'//lt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M - D\n@LT_3\nD;JLT\n@SP\nA = M\nM = 0\n@DEFAULT_5\n0;JMP\n(LT_3)\n@SP\nA = M\nM = -1\n(DEFAULT_5)\n@SP\nM = M + 1\n')

    def test_write_arithmetic_and(self):
        converted_string = self.cdw.write_arithmetic('and')
        self.assertEqual(converted_string,'//and\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M & D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n')

    def test_write_arithmetic_or(self):
        converted_string = self.cdw.write_arithmetic('or')
        self.assertEqual(converted_string,'//or\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\nD = M | D\n@SP\nAM = M + 1\nA = A - 1\nM = D\n')

    def test_write_arithmetic_not(self):
        converted_string = self.cdw.write_arithmetic('not')
        self.assertEqual(converted_string,'//not\n@SP\nA = M\nA = A - 1\nM = !M\n')

    def test_write_push_constant(self):
        converted_string = self.cdw.write_push_pop(1,3,17)
        self.assertEqual(converted_string,'//push constant 17\n@17\nD = A\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')

    def test_write_push_pop_argument(self):
        converted_string = self.cdw.write_push_pop(1,0,3)
        self.assertEqual(converted_string,'//push argument 3\n@3\nD = A\n@ARG\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,0,7)
        self.assertEqual(converted_string,'//pop argument 7\n@SP\nM = M - 1\n@7\nD = A\n@ARG\nA = M\nD = A + D\n@R13\nM = D\n@SP\nA = M\nD = M\n@R13\nA = M\nM = D\n')

    def test_write_push_pop_local(self):
        converted_string = self.cdw.write_push_pop(1,1,5)
        self.assertEqual(converted_string,'//push local 5\n@5\nD = A\n@LCL\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,1,10)
        self.assertEqual(converted_string,'//pop local 10\n@SP\nM = M - 1\n@10\nD = A\n@LCL\nA = M\nD = A + D\n@R13\nM = D\n@SP\nA = M\nD = M\n@R13\nA = M\nM = D\n')


    def test_write_push_pop_this(self):
        converted_string = self.cdw.write_push_pop(1,4,12)
        self.assertEqual(converted_string,'//push this 12\n@12\nD = A\n@THIS\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,4,2)
        self.assertEqual(converted_string,'//pop this 2\n@SP\nM = M - 1\n@2\nD = A\n@THIS\nA = M\nD = A + D\n@R13\nM = D\n@SP\nA = M\nD = M\n@R13\nA = M\nM = D\n')


    def test_write_push_pop_that(self):
        converted_string = self.cdw.write_push_pop(1,5,1)
        self.assertEqual(converted_string,'//push that 1\n@1\nD = A\n@THAT\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,5,6)
        self.assertEqual(converted_string,'//pop that 6\n@SP\nM = M - 1\n@6\nD = A\n@THAT\nA = M\nD = A + D\n@R13\nM = D\n@SP\nA = M\nD = M\n@R13\nA = M\nM = D\n')

    def test_write_push_pop_static(self):
        converted_string = self.cdw.write_push_pop(1,2,4)
        self.assertEqual(converted_string,'//push static 4\n@static.4\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,2,8)
        self.assertEqual(converted_string,'//pop static 8\n@SP\nM = M - 1\nA = M\nD = M\n@static.8\nM = D\n')

    def test_write_push_pop_temp(self):
        converted_string = self.cdw.write_push_pop(1,7,4)
        self.assertEqual(converted_string,'//push temp 4\n@9\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(2,7,5)
        self.assertEqual(converted_string,'//pop temp 5\n@SP\nM = M - 1\nA = M\nD = M\n@10\nM = D\n')

    def test_write_push_pop_pointer_push(self):
        converted_string = self.cdw.write_push_pop(1,6,0)
        self.assertEqual(converted_string,'//push pointer 0\n@THIS\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_push_pop(1,6,1)
        self.assertEqual(converted_string,'//push pointer 1\n@THAT\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')

    def test_write_push_pop_pointer_pop(self):
          converted_string = self.cdw.write_push_pop(2,6,0)
          self.assertEqual(converted_string,'//pop pointer 0\n@SP\nM = M - 1\nA = M\nD = M\n@THIS\nM = D\n')
          converted_string = self.cdw.write_push_pop(2,6,1)
          self.assertEqual(converted_string,'//pop pointer 1\n@SP\nM = M - 1\nA = M\nD = M\n@THAT\nM = D\n')










if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCodeWriter)
    # unittest.TextTestRunner(verbosity=2).run(suite)
