MOV AL,5; AL holds 5
MOV [50],AL; Value of AL is at [0x50]
MOV BL,6; BL holds 6
MOV [60],BL; Value of BL is at [0x60]
MOV AL,[50]; Stores what is in [0x50] in AL
MOV BL,[60]; Stores what is in [0x60] in BL
ADD AL,BL; AL holds the output (z)
MOV [50],AL; z is stored in [0x50]
END