module ALU(
input [31:0] regA, regB,
input [4:0] OPCode, 
output [63:0] regZ
);
integer i;

wire [31:0] regLOshl;
wire [31:0] regLOshrl;
wire [31:0] regLOshra;
wire [31:0] regLOrotatel;
wire [31:0] regLOrotater;
wire [31:0] regLOlog_and;
wire [31:0] regLOlog_or;
wire [31:0] regLOnot;
wire [31:0] regLOneg;
wire [31:0] regLOadd;
wire [31:0] regLOsub;
wire [31:0] regLOmul, regHImul;
wire [31:0] regLOdiv, regHIdiv;

wire regHIadd, regHIsub;

reg [31:0] regLO, regHI;

//Generate the computational hardware, this will perform all operations, and then we will then later choose the one we want
	generate
		left_shift SHL (1'b1, 1'b0, regA, regLOshl);  								//SHL Module Name: left_shift
		right_shift_combined SHRL (1'b1, 1'b0, 1'b0, regA, regLOshrl);  		//SHR logical Module Name: right_shift_combined
		right_shift_combined SHRA (1'b1, 1'b0, 1'b1, regA, regLOshra); 		//SHR arithmetic Module Name: right_shift_combined
		left_rotate rotateL ( 1'b1, 1'b0, regA, regLOrotatel);  				//Rotate L Module Name: left_rotate
		right_rotate rotateR (1'b1, 1'b0, regA, regLOrotater);  				//Rotate R Module Name: left_rotate
		logical_and log_and (regA, regB, regLOlog_and); 						//AND Module Name: logical_and
		logical_or log_or (regA, regB, regLOlog_or);  							//OR Module Name: logical_or
		NotOperation operationNot (regA, regLOnot);  							//NOT Module Name: NOT
		twoCompliment neg (regA, regLOneg); 										//Neg Module Name: twoCompliment
		Hierarchical_CLA add(1'b0, regA, regB, regHIadd, regLOadd);  		//Add Module Name: Hierarchical_CLA
		Hierarchical_CLA sub(1'b1, regA, regB, regHIsub, regLOsub);  		//Subtract Module Name: Hierarchical_CLA
		boothMultiplier mul (regA, regB, regHImul, regLOmul); 				//Multiply Module Name: boothMultiplier
		nonRestoringDivisionPosiNeg div (regA, regB, regLOdiv, regHIdiv); //Divide Module Name: nonRestoringDivisionPosiNeg
	endgenerate

	always @ (*) begin
		if (OPCode == 5'b00001) regLO = regLOshl;	else							//SHL Module Name: left_shift
		if (OPCode == 5'b00010) regLO = regLOshrl; else							//SHR logical Module Name: right_shift_combined
		if (OPCode == 5'b00011) regLO = regLOshra; else							//SHR arithmetic Module Name: right_shift_combined
		if (OPCode == 5'b00100) regLO = regLOrotatel; else						//Rotate L Module Name: left_rotate
		if (OPCode == 5'b00101) regLO = regLOrotater; else						//Rotate R Module Name: left_rotate
		if (OPCode == 5'b00110) regLO = regLOlog_and; else						//AND Module Name: logical_and
		if (OPCode == 5'b00111) regLO = regLOlog_or; else						//OR Module Name: logical_or
		if (OPCode == 5'b01000) regLO = regLOnot; else							//NOT Module Name: NOT
		if (OPCode == 5'b01001) regLO = regLOneg; else							//Neg Module Name: twoCompliment
		if (OPCode == 5'b01010)begin													//Add Module Name: Hierarchical_CLA
			regLO = regLOadd;	
			regHI = regHIadd;
		end else
		if (OPCode == 5'b01011)begin													//Subtract Module Name: Hierarchical_CLA
			regLO = regLOsub;
			regHI = regHIsub;
		end else
		if (OPCode == 5'b01100)begin													//Multiply Module Name: boothMultiplier
			regLO = regLOmul;	
			regHI = regHImul;
		end else
		if (OPCode == 5'b01101)begin													//Divide Module Name: nonRestoringDivisionPosiNeg
			regLO = regLOdiv;	
			regHI = regHIdiv;
		end else
		if (OPCode == 5'b10000) regLO = regA; else								//Movi instruction
		if (OPCode == 5'b10001)begin													//Add Immediate Instruction
			regLO = regLOadd;	
			regHI = regHIadd;
		end else
		if (OPCode == 5'b10010) regLO = regLOlog_and; else 					//AND Immediate Module Name
		if (OPCode == 5'b10011) regLO = regLOlog_or;  else     				//OR Immediate Module Name
		if (OPCode == 5'b01111) regLO = regA; else								//Out Instruction
		if (OPCode == 5'b01110) regLO = regA; else								//In Instruction
		if (OPCode == 5'b10111) regLO = regA; else								//mfl Instruction
		if (OPCode == 5'b11110) regHI = regA;										//mfhi Instruction
	end
	
	//OPCodes 5'b10100 
	//        5'b10101
	//        5'b10110 are all blocked
	
	assign regZ[31:0]  = regLO[31:0];
	assign regZ[63:32] = regHI[31:0];
	
endmodule
