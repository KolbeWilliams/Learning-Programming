	MOV BL,50
loop:
	MOV CL,[BL]
	CMP CL,FF	;Compare with end of array
	JZ end
	IN 00		;User input in AL
	PUSH AL		;Push user input onto the stack
	CALL 40		;Call function
	POP AL		;Pop converted number into AL
	MOV[BL],AL	;Converted values stored in array
	ADD AL,30	;Add 48 (30 in hex) back to AL for comparison
	INC BL		;Increment BL to go to next location in the array
	CMP AL,0D	;Compare AL with enter
	JNZ loop
end:
	HALT

	ORG 40		;Create function to conver from ASCII
	POP DL		;Pop the return address into DL
	POP AL		;Get user input from the stack
	SUB AL,30	;Convert from ASCII by subtracting 48 (30 in hex)
	PUSH AL		;Push Converted value onto the stack
	PUSH DL		;Push the return address back onto the stack
	RET
	
	ORG 50		;Declare Array
	DB 00
	DB 00
	DB 00
	DB 00
	DB FF		;Set end of the array
	END