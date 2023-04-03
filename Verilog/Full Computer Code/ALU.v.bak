module ALU(
input clk, clr, stop,
input [31:0] regA, regB,
input [4:0] OPCode, 
output [31:0] regLO, regHI
);

	generate
		if (OPCode == 'b00001) left_shift SHL (clk, clr, regA regLO) ; else 						//SHL Module Name: 
		if (OPCode == 'b00010) right_shift_combined SHRL (clk, clr, 'b0, regA, regLO); else 				//SHR logical Module Name:
		if (OPCode == 'b00010) right_shift_combined SHRA (clk, clr, 'b1, regA regLO); else				//SHR arithmetic Module Name: 
		if (OPCode == 'b00011) left_rotate rotateL ( clk, clr, regA, regLO); else 					//Rotate L Module Name: 
		if (OPCode == 'b00100) right_rotate rotateR (clk, clr, regA, regLO); else 					//Rotate R Module Name: 
		if (OPCode == 'b00101) logical_and log_and (regA, regB regLO); else 						//AND Module Name: 
		if (OPCode == 'b00110) logical_or log_or (regA, regB, regLO); else 						//OR Module Name: 
		if (OPCode == 'b00111) NOT Not (regA, regLO); else 								//NOT Module Name: NOT
		if (OPCode == 'b01000) twoCompliment neg (regA, regLO); else 							//Neg Module Name: twoCompliment
		if (OPCode == 'b01001) Hierarchical_CLA add('b0, regA, regB, regHI, regLO); else 				//Add Module Name: 
		if (OPCode == 'b01010) Hierarchical_CLA subtract('b1, regA, regB, regHI, regLO) ; else 				//Subtract Module Name: 
		if (OPCode == 'b01011) boothMultiplier mul (regA, regB, regHI, regLO); else 					//Multiply Module Name: boothMultiplier
		if (OPCode == 'b01100) nonRestoringDivisionPosiNeg div (regA, regB, regLO, regHI);  				//Divide Module Name: nonRestoringDivisionPosiNeg
	endgenerate
	
endmodule
