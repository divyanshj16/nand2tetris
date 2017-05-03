//push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
//eq
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@EQ_1
D;JEQ
@SP
A = M
M = 0
@DEFAULT_1
0;JMP
(EQ_1)
@SP
A = M
M = -1
(DEFAULT_1)
@SP
M = M + 1
//push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 16
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
//eq
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@EQ_2
D;JEQ
@SP
A = M
M = 0
@DEFAULT_2
0;JMP
(EQ_2)
@SP
A = M
M = -1
(DEFAULT_2)
@SP
M = M + 1
//push constant 16
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
//eq
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@EQ_3
D;JEQ
@SP
A = M
M = 0
@DEFAULT_3
0;JMP
(EQ_3)
@SP
A = M
M = -1
(DEFAULT_3)
@SP
M = M + 1
//push constant 892
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
//lt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@LT_1
D;JLT
@SP
A = M
M = 0
@DEFAULT_4
0;JMP
(LT_1)
@SP
A = M
M = -1
(DEFAULT_4)
@SP
M = M + 1
//push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 892
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
//lt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@LT_2
D;JLT
@SP
A = M
M = 0
@DEFAULT_5
0;JMP
(LT_2)
@SP
A = M
M = -1
(DEFAULT_5)
@SP
M = M + 1
//push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
//lt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@LT_3
D;JLT
@SP
A = M
M = 0
@DEFAULT_6
0;JMP
(LT_3)
@SP
A = M
M = -1
(DEFAULT_6)
@SP
M = M + 1
//push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
//gt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@GT_1
D;JGT
@SP
A = M
M = 0
@DEFAULT_7
0;JMP
(GT_1)
@SP
A = M
M = -1
(DEFAULT_7)
@SP
M = M + 1
//push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
//gt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@GT_2
D;JGT
@SP
A = M
M = 0
@DEFAULT_8
0;JMP
(GT_2)
@SP
A = M
M = -1
(DEFAULT_8)
@SP
M = M + 1
//push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
//gt
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@GT_3
D;JGT
@SP
A = M
M = 0
@DEFAULT_9
0;JMP
(GT_3)
@SP
A = M
M = -1
(DEFAULT_9)
@SP
M = M + 1
//push constant 57
@57
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 31
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1
//push constant 53
@53
D = A
@SP
A = M
M = D
@SP
M = M + 1
//add
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M + D
@SP
AM = M + 1
A = A - 1
M = D
//push constant 112
@112
D = A
@SP
A = M
M = D
@SP
M = M + 1
//sub
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M - D
@SP
AM = M + 1
A = A - 1
M = D
//neg
@SP
A = M
A = A - 1
M = -M
//and
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M & D
@SP
AM = M + 1
A = A - 1
M = D
//push constant 82
@82
D = A
@SP
A = M
M = D
@SP
M = M + 1
//or
@SP
AM = M - 1
D = M
@SP
AM = M - 1
D = M | D
@SP
AM = M + 1
A = A - 1
M = D
//not
@SP
A = M
A = A - 1
M = !M
