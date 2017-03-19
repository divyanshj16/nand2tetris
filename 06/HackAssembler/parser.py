class Parser(object):
	"""Parser for hack assembly language. It can decode the instruction into its different parts."""


	def __init__(self, instruction):
		self.instruction = instruction
		self.comp = ''
		self.dest = 'null'
		self.jmp = 'null'               #default dest and jmp = null
		self.parse();

	def	type(self):
		if (self.instruction.startswith('@')):          # If instruction startswith @ then its a A instruction otherwise C
			return "A"
		else:
			return "C"

	def parse(self):
		if not (self.type() == 'A'):
			part1 = self.instruction.split(';')         #jump is seperated by ; in a instruction
			try:
				self.jmp = part1[1].rstrip('\n')        #strips \n at the end of statement
			except:
				pass
				#print("No Jmp statement")
			finally:
				instructionPart = part1[0]
			part2 = instructionPart.split('=')          #splitting the destination and computation part
			if len(part2) > 1:
				#print("intruction with destination")
				self.dest = part2[0].rstrip('\n')       #storing in object parameters all the values
				self.comp = part2[1].rstrip('\n')
			else:
				self.comp= part2[0].rstrip('\n')

def main():
	instruction = input("Enter a Instruction: ")
	if len(instruction) < 1:
		instruction = "dest=comp;jmp"
	parser = Parser(instruction);
	print("comp = " + parser.comp)
	print("dest = " + parser.dest)
	print("jmp = " + parser.jmp)
	print("type = " + parser.type())

if __name__ == '__main__':
	main()
