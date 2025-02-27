	JMP Start	;Jump to main program
	DB 50		;Initialize vector table
	DB 60
	DB 70
	DB 80
Start:
	IN 00		;Get first number
	SUB AL,30	;Convert first number from ASCII
	MOV [90],AL	;Move first number to [90]
	MOV BL,[90]	;Move first number into BL
	IN 00		;Get second number
	SUB AL,30	;Convert second number from ASCII
	MOV [90],AL	;Move second number into [90]
	MOV CL,[90]	;Move second number into CL
	IN 00		;Get operation
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
	JMP end
subtract:
	INT 03		;Call Subtraction interrupt
	JMP end
multiply:
	INT 04		;Call multiplication
	JMP end
divide:
	INT 05		;Call division interrupt
end:
	HALT

	ORG 50		;Organize addition interrupt
	ADD BL,CL	;Add user input and store the result in BL
	IRET		;Return to main function

	ORG 60		;Organize subtraction interrupt
	SUB BL,CL	;Subtract second number from the first and store the result in BL
	IRET		;Return to main program

	ORG 70		;Organize multiplication interrupt
	MUL BL,CL	;Multiply user input and store the result in BL
	IRET		;Return to main program

	ORG 80		;Organize division interrupt
	DIV BL,CL	;Divide second number by the first and store the result in BL
	IRET		;Return to the main program
	END