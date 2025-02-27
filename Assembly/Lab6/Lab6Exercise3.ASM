	MOV BL,30	;Move the starting address of the array to BL
	PUSH BL		;Push starting address of the array onto the stack
loop:
	MOV AL,[BL]	;Move the array element into AL
	CMP AL,FF	;Check if its the end of the array
	JZ end		;Break the loop if its the end of the array so that CL isn't incremented
	INC BL		;Go to next array element
	INC CL		;Increment CL to hold length of the array
	CMP AL,FF	;Check if its the end of the array
	JNZ loop	;Repeat the loop if its not the end of the array
end:
	PUSH CL		;Push the size of the array onto the stack
	CALL 40
	HALT

	ORG 30		;Declare the array
	DB 2
	DB 5
	DB A
	DB 0
	DB 6
	DB FF		;Set the end of the array as FF

	ORG 40		;Create the function
	POP DL		;Pop the return address into DL
	POP CL		;Pop the array size into CL to use as a counter
	POP BL		;Pop the starting address of the array into BL
	PUSH DL		;Push return address onto the stack
	PUSH CL		;Push size of the array onto the stack
	XOR DL,DL	;Reset DL
loop2:	
	MOV AL,[BL]	;Move the array element into AL
	ADD DL,AL	;Add the elements of the array
	SUB CL,1	;Decrement CL
	INC BL		;Increment BL to go to next element
	CMP CL,0	;Check if its the end of the array
	JNZ loop2	;Repeat the loop if its not the end of the array
	POP CL		;Get size of the array from the stack
	DIV DL,CL	;Divide the total of the elements by the length of the array
	POP AL		;Pop the return address into AL
	PUSH DL		;Push the result onto the stack
	PUSH AL 	;Push the return address back onto the stack
	RET
	END