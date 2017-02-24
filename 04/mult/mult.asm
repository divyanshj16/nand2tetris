// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@mult
M = 0

@i
M = 1

(LOOP)
@R1
D = M
@i
D = M - D
@END
D;JGT      //jUMP if greater than 0

@R0
D = M
@mult
M = M + D
@i
M = M + 1

@mult
D = M
@R2
M = D

@LOOP
0;JMP



(END)
@END

0;JMP