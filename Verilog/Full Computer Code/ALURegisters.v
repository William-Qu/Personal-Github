module ALURegisters(
input clr, clk,
output [31:0] r0outf, r1outf, r2outf, r3outf, r4outf, r5outf, r6outf, r7outf, r8outf, r9outf, r10outf, r11outf, r12outf, r13outf, r14outf, r15outf,
input r0ins, r1ins, r2ins, r3ins, r4ins, r5ins, r6ins, r7ins, r8ins, r9ins, r10ins, r11ins, r12ins, r13ins, r14ins, r15ins,
input [31:0] BusMuxOut
);

//Create the general 32-bit registers for use in the ALU/Control Unit from our code with input and output wires
	generate 
		reg32bit gr0  (r0outf, BusMuxOut, clr, clk, r0ins);
		reg32bit gr1  (r1outf, BusMuxOut, clr, clk, r1ins);
		reg32bit gr2  (r2outf, BusMuxOut, clr, clk, r2ins);
		reg32bit gr3  (r3outf, BusMuxOut, clr, clk, r3ins);
		reg32bit gr4  (r4outf, BusMuxOut, clr, clk, r4ins);
		reg32bit gr5  (r5outf, BusMuxOut, clr, clk, r5ins);
		reg32bit gr6  (r6outf, BusMuxOut, clr, clk, r6ins);
		reg32bit gr7  (r7outf, BusMuxOut, clr, clk, r7ins);
		reg32bit gr8  (r8outf, BusMuxOut, clr, clk, r8ins);
		reg32bit gr9  (r9outf, BusMuxOut, clr, clk, r9ins);
		reg32bit gr10 (r10outf, BusMuxOut, clr, clk, r10ins);
		reg32bit gr11 (r11outf, BusMuxOut, clr, clk, r11ins);
		reg32bit gr12 (r12outf, BusMuxOut, clr, clk, r12ins);
		reg32bit gr13 (r13outf, BusMuxOut, clr, clk, r13ins);
		reg32bit gr14 (r14outf, BusMuxOut, clr, clk, r14ins);
		reg32bit gr15 (r15outf, BusMuxOut, clr, clk, r15ins);
	endgenerate
endmodule 