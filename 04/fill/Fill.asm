// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
@i
M = 0

@KBD
D = M

@WHITE
D;JEQ

@BLACK
D;JNE

(WHITE)
@SCREEN
D = A

@i
A = D + M
M = 0

@SCREEN
D = A

@i
D = M + D


@KBD
D = D - A

@i
M = M + 1

@END
D;JEQ

@KBD
D = M

@END
D;JNE

@WHITE
0;JMP


(BLACK)
@SCREEN
D = A

@i
A = D + M
M = -1

@SCREEN
D = A

@i
D = M + D

@KBD
D = D - A

@i
M = M + 1

@END
D;JEQ

@KBD
D = M

@END
D;JEQ

@BLACK
0;JMP


(END)
@LOOP
0;JMP

