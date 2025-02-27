
; ===== COUNT =================================================
	MOV	AL,3	; Move 0 into the AL register
	MOV	BL,5
REP:			; This label is used with jump commands
	ADD	AL,BL	; Add two to AL
	JMP	REP	; Jump back to the rep label
	
	END		; Program ends here
; =============================================================
