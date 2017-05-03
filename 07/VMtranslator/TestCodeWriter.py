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
        converted_string = self.cdw.write_arithmetic('eq')
        self.assertEqual(converted_string,'//eq\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@EQ_1\nD = M - D;JEQ\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(EQ_1)\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        converted_string = self.cdw.write_arithmetic('eq')
        self.assertEqual(converted_string,'//eq\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@EQ_2\nD = M - D;JEQ\n@SP\nA = M\nM = 0\n@DEFAULT_2\n0;JMP\n(EQ_2)\nM = -1\n(DEFAULT_2)\n@SP\nM = M + 1\n')

    def test_write_arithmetic_gt(self):
        converted_string = self.cdw.write_arithmetic('gt')
        self.assertEqual(converted_string,'//gt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@GT_1\nD = M - D;JGT\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(GT_1)\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        self.cdw.write_arithmetic('gt')
        self.cdw.write_arithmetic('eq')
        converted_string = self.cdw.write_arithmetic('gt')
        self.assertEqual(converted_string,'//gt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@GT_3\nD = M - D;JGT\n@SP\nA = M\nM = 0\n@DEFAULT_4\n0;JMP\n(GT_3)\nM = -1\n(DEFAULT_4)\n@SP\nM = M + 1\n')

    def test_write_arithmetic_lt(self):
        converted_string = self.cdw.write_arithmetic('lt')
        self.assertEqual(converted_string,'//lt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@LT_1\nD = M - D;JLT\n@SP\nA = M\nM = 0\n@DEFAULT_1\n0;JMP\n(LT_1)\nM = -1\n(DEFAULT_1)\n@SP\nM = M + 1\n')
        self.cdw.write_arithmetic('lt')
        self.cdw.write_arithmetic('eq')
        self.cdw.write_arithmetic('gt')
        converted_string = self.cdw.write_arithmetic('lt')
        self.assertEqual(converted_string,'//lt\n@SP\nAM = M - 1\nD = M\n@SP\nAM = M - 1\n@LT_3\nD = M - D;JLT\n@SP\nA = M\nM = 0\n@DEFAULT_5\n0;JMP\n(LT_3)\nM = -1\n(DEFAULT_5)\n@SP\nM = M + 1\n')

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

    # def test_write_push_pop_argument(self):
    #     converted_string = self.cdw.write_push_pop(1,0,3)
    #     self.assertEqual(converted_string,'//push argument 3\n@3\nD = A\n@ARG\nA = M\nA = A + D\nD = M\n@SP\nA = M\nM = D\n@SP\nM = M + 1\n')
    #
    #





if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCodeWriter)
    # unittest.TextTestRunner(verbosity=2).run(suite)
