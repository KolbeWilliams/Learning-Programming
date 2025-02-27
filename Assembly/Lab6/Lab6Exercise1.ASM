	JMP Start
	DB 00
	DB 00
	DB 00
Start:
	MOV AL,4	;Move the base (2) into AL
	MOV [02],AL	;Move Al into [02]
	MOV BL,3	;Move the power (3) into BL
	MOV [03],BL	;Move BL into [3]
	CALL 30		;Call the function
	HALT

	ORG 30		;Create the function
	MOV AL,[02]	;Move the base into AL
	MOV BL,[03]	;Move the power into BL
	MOV DL,[02]	;Move the base into DL for multiplication with AL
loop:
	MUL AL,DL	;Perform multiplication
	SUB BL,1	;Decrement counter (CL)
	CMP BL,1	;Compare the counter (CL) with 1
	JNZ loop	;If the counter is not 1, repeat the loop
	MOV [04],AL	;Store the answer in [04]
	RET
	END