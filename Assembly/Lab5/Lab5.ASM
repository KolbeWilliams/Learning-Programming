	MOV AL, 40; Initialize BL to starting address of the first array
	MOV BL, 54; Initialize CL to ending address of the second array
loop:
	MOV CL,[AL]
	MOV [BL], CL; Copy value in location of AL into end of BL
	INC AL; Increment AL to go to next location in the array
	SUB BL,1; Decrement BL to go to next location in the array
	CMP CL, FF; Compare index with end of array
	JNZ loop
	HALT

	ORG 40; Declare first array
	DB 05
	DB 04
	DB 03
	DB 02
	DB 01
	DB FF

	ORG 50; Declare Second array
	DB 00
	DB 00
	DB 00
	DB 00
	DB 00
	DB FF
	END