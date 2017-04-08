import unittest
from parser import Parser

class testParser(unittest.TestCase):
    """Test class for Parser class."""

    def setUp(self):
        self.parser = Parser()

    def test_cleaner_comments(self):
        cleaned = self.parser.cleaner('//This is a comment')
        self.assertEqual(cleaned,"","The line is a Comment")
        self.assertEqual(self.parser.command,'')

    def test_cleaner_whitespaces(self):
        cleaned = self.parser.cleaner('  add   ',)
        self.assertEqual(cleaned,"add","command stripped")
        self.assertEqual(self.parser.command,'add')

    def test_cleaner_inlineComments(self):
        self.assertEqual(self.parser.cleaner('add   //this adds 2 stack'),'add',"comment removed")
        self.assertEqual(self.parser.command,'add')

    def test_cleaner_emptyline(self):
        self.assertEqual(self.parser.cleaner('               \n'),'','empty line')
        self.assertEqual(self.parser.command,'')

    def test_cleaner_dataMember(self):
        self.parser.cleaner("   push         local    17       //this is a test")
        self.assertEqual(self.parser.command,'push         local    17')


    def test_command_type_arithmetic(self):
        types_of_commands = ['add','sub','neg','eq','gt','lt','and','or','not']
        self.assertEqual(self.parser.command_type("add"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("sub"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("neg"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("eq"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("gt"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("lt"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("and"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("or"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("or"),0,"Arithmetic type command")
        self.assertEqual(self.parser.command_type("not"),0,"Arithmetic type command")

    def test_command_type_push(self):
        self.assertEqual(self.parser.command_type('push segment index'),1,"push type command")

    def test_command_type_pop(self):
        self.assertEqual(self.parser.command_type('pop segment index'),2,"pop type command")

    def test_split_non_arithmetic(self):
        self.parser.command_type('push constant 14')
        self.parser.split_command("push constant 14")
        self.assertEqual(self.parser.arg1,'constant',"argument 1 is constant arg1")
        self.assertEqual(self.parser.arg2,'14',"argument 2  is 14 arg2")

    def test_split_arithmetic(self):
        self.parser.command_type('add')
        self.parser.split_command("add")
        self.assertEqual(self.parser.arg1,'add',"non arithmetic command itself is stored in arg1")
        self.assertEqual(self.parser.arg2,'',"empty string is arg2")


if __name__ == '__main__':
    unittest.main()
    # FOR VERBOSE TESTS
    # suite = unittest.TestLoader().loadTestsFromTestCase(testParser)
    # unittest.TextTestRunner(verbosity=3).run(suite)
