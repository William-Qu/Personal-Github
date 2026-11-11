`timescale 1ns/10ps
module TestbenchControlUnit;
	reg [31:0] IR;
	reg clk, clr, wren;
	wire [31:0] reg0, reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12, reg13, reg14, reg15;
	
	//if (OPCode == 'b00001)	//SHL Module Name: left_shift
	//if (OPCode == 'b00010)	//SHR logical Module Name: right_shift_combined
	//if (OPCode == 'b00011)	//SHR arithmetic Module Name: right_shift_combined
	//if (OPCode == 'b00100)	//Rotate L Module Name: left_rotate
	//if (OPCode == 'b00101)	//Rotate R Module Name: left_rotate
	//if (OPCode == 'b00110)	//AND Module Name: logical_and
	//if (OPCode == 'b00111)	//OR Module Name: logical_or
	//if (OPCode == 'b01000)	//NOT Module Name: NOT
	//if (OPCode == 'b01001)	//Neg Module Name: twoCompliment
	//if (OPCode == 'b01010)	//Add Module Name: Hierarchical_CLA
	//if (OPCode == 'b01011)	//Subtract Module Name: Hierarchical_CLA
	//if (OPCode == 'b01100)	//Multiply Module Name: boothMultiplier
	//if (OPCode == 'b01101)	//Divide Module Name: nonRestoringDivisionPosiNeg
	//if (OPCode == 'b10000)	//mov Instruction
	
	ControlUnit ctrlTest (clk, clr, wren, IR, reg0, reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12, reg13, reg14, reg15);
	
	initial
	begin
		clk = 0;
		forever #10 clk = ~clk;
	end
	
	initial 
	begin 
		//case 0 -- MOV RA
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b10000000100000000000000010001101;
		clr <= 1'b0;
		wren <= 1'b1;
		#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 1 -- MOV RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b10000001000000000000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 2 -- ADD RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01010000000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 3 -- AND RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00110001100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 4 -- OR RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00111010000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 5 -- SUB RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01011010100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 6 -- MUL RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01100011000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 7 -- DIV RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01101011100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 8 -- SHRL RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00010100000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 9 -- SHRA RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00011100100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 10 -- SHL RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00001101000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 11 -- ROR RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00101101100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 12 -- ROL RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b00100110000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 13 -- NEG RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01001110100010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|
		//case 14 -- NOT RA, RB
		//        |IR ||DT||RA||RB||  IMMEDIATE  |
		IR <= 32'b01000111000010010000000000101001;
		clr <= 1'b0;
		wren <= 1'b1;
		
#40 $display("Output reg 0 = %b", reg0);			//|
		$display("Output reg 1 = %b", reg1);			//|
		$display("Output reg 2 = %b", reg2);			//|
		$display("Output reg 3 = %b", reg3);			//|
		$display("Output reg 4 = %b", reg4);			//|
		$display("Output reg 5 = %b", reg5);			//|
		$display("Output reg 6 = %b", reg6);			//|
		$display("Output reg 7 = %b", reg7);			//|
		$display("Output reg 8 = %b", reg8);			//|
		$display("Output reg 9 = %b", reg9);			//|
		$display("Output reg 10 = %b", reg10);		//|
		$display("Output reg 11 = %b", reg11);		//|
		$display("Output reg 12 = %b", reg12);		//|
		$display("Output reg 13 = %b", reg13);		//|
		$display("Output reg 14 = %b", reg14);		//|
		$display("Output reg 15 = %b", reg15);		//|

	end
endmodule 