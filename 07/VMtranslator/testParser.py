import unittest
from parser import Parser

class testParser(unittest.TestCase):
    """Test class for Parser class."""

    def setUp(self):
        self.parser = Parser()

    def test_cleaner_comments(self):
        cleaned = self.parser.cleaner('//This is a comment')
        self.assertEqual(cleaned,"","The line is a Comment")

    def test_cleaner_whitespaces(self):
        cleaned = self.parser.cleaner('  add   ',)
        self.assertEqual(cleaned,"add","command stripped")

    def test_cleaner_inlineComments(self):
        self.assertEqual(self.parser.cleaner('add   //this adds 2 stack'),'add',"comment removed")

    def test_cleaner_emptyline(self):
        self.assertEqual(self.parser.cleaner('               \n'),'','empty line')

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




if __name__ == '__main__':
    unittest.main()
