MOV AL,4; AL stores the value of x
MOV BL,1; BL stores 1 for AND operation in function
CALL 50; Calls the function
ADD AL,1; Adds 1 to x
CALL 50; Calls the function
HALT; Halts the program

ORG 50; Stores function instructions in 50
PUSH AL; Pushes value of x onto stack
POP CL; Pops value of x into CL register
AND CL,BL; Bitwise AND operation
CMP CL,0; Compares result of bitwise AND and 0
JNZ skip; Jumps to skip if result is not 0
MUL Al,2; Multiplies value of x by 2
skip:
RET; Returns to main program
END