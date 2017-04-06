import unittest
from parser import Parser
from unittest.mock import Mock

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

    # def test_command_type_arithmetic(self):
    #     types_of_commands = ['add','sub','neg','eq','gt','lt','and','or','not']
    #     assertEquals(parser.command_type(" add "),0,"Arithmetic type command")



if __name__ == '__main__':
    unittest.main()
