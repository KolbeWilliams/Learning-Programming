	JMP Start	;Skip to main program
	DB 50		;Initialize vector table

Start:
	MOV BL,A	;Move 10 (A in hex) into BL
	IN 00		;Get user input (Stored in AL)
	SUB AL,30	;Convert user input from ASCII
	CMP AL,0	;Check if user input was 0
	JZ interrupt	;Jump to interrupt if it was 0
	JNZ end		;Skip interrupt if it was not 0
interrupt:
	INT 02		;Call interrupt
end:
	DIV BL,AL	;Carry out division (Result is stored in BL)
	HALT

	ORG 50		;Organize interrupt at memory location 50
	IN 00		;Get user input again
	SUB AL,30	;Convert user input from ASCII
	IRET		;Return to main program
	END