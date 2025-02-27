	JMP Start	;Jump to main program
	DB 50		;Initialize vector table
	DB 60
	DB 70
	DB 80
Start:
	IN 00		;Get first number
	CMP AL,0D	;Check if user input was enter
	JZ end		;End the program if the user input was enter
	SUB AL,30	;Convert first number from ASCII
	PUSH AL		;Push the first number onto the stack
	IN 00		;Get second number
	CMP AL,0D	;Check if user input was enter
	JZ end		;End the program if the user input was enter
	SUB AL,30	;Convert second number from ASCII
	PUSH AL		;Push the second number onto the stack
	IN 00		;Get operation
	CMP AL,0D	;Check if user input was enter
	JZ end		;End the program if the user input was enter
	CMP AL,2B	;Check if user entered +
	JZ add		;Jumpt to add if user entered +
	CMP AL,2D	;Check if user entered -
	JZ subtract	;Jump to subtract if user entered -
	CMP AL,2A	;Check if user entered *
	JZ multiply	;Jump to multiply if user entered *
	CMP AL,2F	;Check if user entered /
	JZ divide	;Jump to divide if user entered /
add:
	INT 02		;Call addition interrupt
	JMP loop
subtract:
	INT 03		;Call Subtraction interrupt
	JMP loop
multiply:
	INT 04		;Call multiplication
	JMP loop
divide:
	INT 05		;Call division interrupt
loop:
	JMP Start	;Jump to the start until user presses enter
end:
	HALT

	ORG 50		;Organize addition interrupt
	POP AL		;Pop return address into AL
	POP CL		;Pop the second number into CL
	POP BL		;Pop the first number into BL
	ADD BL,CL	;Add user input and store the result in BL
	PUSH BL		;Push the reult onto the stack
	PUSH AL		;Push the return address back onto the stack
	IRET		;Return to main function

	ORG 60		;Organize subtraction interrupt
	POP AL		;Pop return address into AL
	POP CL		;Pop the second number into CL
	POP BL		;Pop the first number into BL
	SUB BL,CL	;Subtract second number from the first and store the result in BL
	PUSH BL		;Push the reult onto the stack
	PUSH AL		;Push the return address back onto the stack
	IRET		;Return to main program

	ORG 70		;Organize multiplication interrupt
	POP AL		;Pop return address into AL
	POP CL		;Pop the second number into CL
	POP BL		;Pop the first number into BL
	MUL BL,CL	;Multiply user input and store the result in BL
	PUSH BL		;Push the reult onto the stack
	PUSH AL		;Push the return address back onto the stack
	IRET		;Return to main program

	ORG 80		;Organize division interrupt
	POP AL		;Pop return address into AL
	POP CL		;Pop the second number into CL
	POP BL		;Pop the first number into BL
	DIV BL,CL	;Divide second number by the first and store the result in BL
	PUSH BL		;Push the reult onto the stack
	PUSH AL		;Push the return address back onto the stack
	IRET		;Return to the main program
	END