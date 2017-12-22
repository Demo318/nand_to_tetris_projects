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

//initialize to white
    @color
    M=0

//start loop to check keyboard situation
(CHECK)

//check if key pressed. If so, jump to BLACK
    @KBD
    D=M
    @BLACK
    D;JGT
    @color
    M=0
    @FILL
    0;JMP


(BLACK) //assign -1 to color 
    @color
    M=-1
    @FILL
    0;JMP

(FILL)
    @i
    M=-1

(FLOOP)

    @i //i++
    M=M+1

    @KBD
    D=A
    @SCREEN
    D=D-A
    @i
    D=D-M
    @CHECK //jump to check on keyboard again if all pixes have been written
    D;JEQ

    @SCREEN //select the next word of SCREEN based on i value
    D=A
    @i
    D=D+M
    @R0
    M=D //store RAM address of next word of SCREEN in R0

    @color //retreive color and write it to new SCREEN word
    D=M
    @R0
    A=M
    M=D

    @FLOOP
    0;JMP // go to FLOOP to fill in the next word of the screen

