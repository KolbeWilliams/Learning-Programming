MOV AL,4
MOV BL,1; BL is the register storing y
Loop:
	MUL BL,2; BL is the register storing y
	SUB AL,1
	JZ loopend
	JMP Loop
loopend:
	END
