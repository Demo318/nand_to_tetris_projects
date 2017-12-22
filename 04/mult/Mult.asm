// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// initialize i = 0
// start loop, adding R0 to R2, R1 times
// loop jumps to END when i == R1



    //initialize i
    @i
    M=0

    //initialize R2
    @R2
    M=0

(LOOP)
    //check if loop condition met
    @i
    D=M
    @R1
    D=M-D
    @END
    D;JEQ

    //Add R0 to R2
    @R0
    D=M
    @R2
    M=D+M

    //i++
    @i
    M=M+1

    //jump back to joop
    @LOOP
    0;JMP

(END)
    @END
    0;JMP

