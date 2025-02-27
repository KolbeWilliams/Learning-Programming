MOV AL,5; The register AL is storing 5(x)
MOV BL,6; The register AL is storing 6(y)
MOV CL,0; The register CL is now storing 0
ADD CL,AL; The register CL is storing the value of AL (5)
ADD CL,BL; The register CL is storing the value of x+y (11)
ADD CL,AL; The register AL is now holding the output(z)
END