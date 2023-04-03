module ControlUnit(
input clk, clr, wren, 
input [31:0] IR,
output [31:0] r0outf, r1outf, r2outf, r3outf, r4outf, r5outf, r6outf, r7outf, r8outf, r9outf, r10outf, r11outf, r12outf, r13outf, r14outf, r15outf
);
//ControlUnit ctrlTest (clk, clr, wren, IR, reg0, reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12, reg13, reg14, reg15);
//Create the wires that will feed out of the ALU/Control Units General Registers
wire [31:0] r0out, r1out, r2out, r3out, r4out, r5out, r6out, r7out, r8out, r9out, r10out, r11out, r12out, r13out, r14out, r15out;

//These registers will feed into the ALU/Control Units General Registers
reg [31:0] r0in, r1in, r2in, r3in, r4in, r5in, r6in, r7in, r8in, r9in, r10in, r11in, r12in, r13in, r14in, r15in;

//Create the general 32-bit registers for use in the ALU/Control Unit from our code with input and output wires
	generate 
		reg32bit gr0  (r0out, r0in, clr, clk, wren);
		reg32bit gr1  (r1out, r1in, clr, clk, wren);
		reg32bit gr2  (r2out, r2in, clr, clk, wren);
		reg32bit gr3  (r3out, r3in, clr, clk, wren);
		reg32bit gr4  (r4out, r4in, clr, clk, wren);
		reg32bit gr5  (r5out, r5in, clr, clk, wren);
		reg32bit gr6  (r6out, r6in, clr, clk, wren);
		reg32bit gr7  (r7out, r7in, clr, clk, wren);
		reg32bit gr8  (r8out, r8in, clr, clk, wren);
		reg32bit gr9  (r9out, r9in, clr, clk, wren);
		reg32bit gr10 (r10out, r10in, clr, clk, wren);
		reg32bit gr11 (r11out, r11in, clr, clk, wren);
		reg32bit gr12 (r12out, r12in, clr, clk, wren);
		reg32bit gr13 (r13out, r13in, clr, clk, wren);
		reg32bit gr14 (r14out, r14in, clr, clk, wren);
		reg32bit gr15 (r15out, r15in, clr, clk, wren);
	endgenerate

//IR Block Broken up
wire [4:0] OPCode;
wire [3:0] regASel, regBSel, destSel;
reg [31:0] regA, regB, immVal;
wire [63:0] regZ;

//Break Up IR Input
assign OPCode = IR[31:27];
assign destSel = IR[26:23];
assign regASel = IR[22:19];
assign regBSel = IR[18:15];

//Temporary answers
wire [31:0] regLO, regHI;

//Using regASel and regBSel, get the contents of the correct registers into regA and regB
	always @ (*) begin
		immVal = IR[14:0];
	
		//Put contents of the correct register into regA using regASel
		if (regASel == 'b0000) regA = r0out[31:0]; else
		if (regASel == 'b0001) regA = r1out[31:0]; else
		if (regASel == 'b0010) regA = r2out[31:0]; else
		if (regASel == 'b0011) regA = r3out[31:0]; else
		if (regASel == 'b0100) regA = r4out[31:0]; else
		if (regASel == 'b0101) regA = r5out[31:0]; else
		if (regASel == 'b0110) regA = r6out[31:0]; else
		if (regASel == 'b0111) regA = r7out[31:0]; else
		if (regASel == 'b1000) regA = r8out[31:0]; else
		if (regASel == 'b1001) regA = r9out[31:0]; else
		if (regASel == 'b1010) regA = r10out[31:0]; else
		if (regASel == 'b1011) regA = r11out[31:0]; else
		if (regASel == 'b1100) regA = r12out[31:0]; else
		if (regASel == 'b1101) regA = r13out[31:0]; else
		if (regASel == 'b1110) regA = r14out[31:0]; else
		if (regASel == 'b1111) regA = r15out[31:0];
		
		if (OPCode[4] == 1'b1) regA = immVal;
		
		//Put contents of the correct register into regB using regBSel
		if (regBSel == 'b0000) regB = r0out[31:0]; else
		if (regBSel == 'b0001) regB = r1out[31:0]; else
		if (regBSel == 'b0010) regB = r2out[31:0]; else
		if (regBSel == 'b0011) regB = r3out[31:0]; else
		if (regBSel == 'b0100) regB = r4out[31:0]; else
		if (regBSel == 'b0101) regB = r5out[31:0]; else
		if (regBSel == 'b0110) regB = r6out[31:0]; else
		if (regBSel == 'b0111) regB = r7out[31:0]; else
		if (regBSel == 'b1000) regB = r8out[31:0]; else
		if (regBSel == 'b1001) regB = r9out[31:0]; else
		if (regBSel == 'b1010) regB = r10out[31:0]; else
		if (regBSel == 'b1011) regB = r11out[31:0]; else
		if (regBSel == 'b1100) regB = r12out[31:0]; else
		if (regBSel == 'b1101) regB = r13out[31:0]; else
		if (regBSel == 'b1110) regB = r14out[31:0]; else
		if (regBSel == 'b1111) regB = r15out[31:0];
	end

//Do the computation with an ALU unit and get the output in the Z register
	generate
		ALU compute (regA, regB, OPCode, regZ);
	endgenerate
	
//Split the Z register into regLO and regHI
assign regLO = regZ[31:0];
assign regHI = regZ[63:32];

//This always statement will be to determine which register to put the operations output into depending on destSel and if its not mult or div (Since these don't have a destination slot yet)
//NOTE: There may be overflow from addition, this will just be left in regHI
	always @ (*) begin
		//if (OPCode != 'b01100 && OPCode != 'b01101) begin //If not mult, or div, put regLO in proper register
			if (destSel == 'b0000) r0in <= regLO; else //r0 should always remain 0
			if (destSel == 'b0001) r1in <= regLO; else
			if (destSel == 'b0010) r2in <= regLO; else
			if (destSel == 'b0011) r3in <= regLO; else
			if (destSel == 'b0100) r4in <= regLO; else
			if (destSel == 'b0101) r5in <= regLO; else
			if (destSel == 'b0110) r6in <= regLO; else
			if (destSel == 'b0111) r7in <= regLO; else
			if (destSel == 'b1000) r8in <= regLO; else
			if (destSel == 'b1001) r9in <= regLO; else
			if (destSel == 'b1010) r10in <= regLO; else
			if (destSel == 'b1011) r11in <= regLO; else
			if (destSel == 'b1100) r12in <= regLO; else
			if (destSel == 'b1101) r13in <= regLO; else
			if (destSel == 'b1110) r14in <= regLO; else
			if (destSel == 'b1111) r15in <= regLO;
		//end
	end

assign r0outf = r0in;	
assign r1outf = r1in;	
assign r2outf = r2in;	
assign r3outf = r3in;	
assign r4outf = r4in;	
assign r5outf = r5in;	
assign r6outf = r6in;	
assign r7outf = r7in;	
assign r8outf = r8in;	
assign r9outf = r9in;	
assign r10outf = r10in;	
assign r11outf = r11in;	
assign r12outf = r12in;	
assign r13outf = r13in;	
assign r14outf = r14in;	
assign r15outf = r15in;	
	
endmodule
