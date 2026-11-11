module Multiplexer(
input [31:0] r0out, r1out, r2out, r3out, r4out, r5out, r6out, r7out, r8out, r9out, r10out, r11out, r12out, r13out, r14out, r15out,RegHiOut,RegLoOut,ZHiOut,ZLoOut,PCOut,MDROut,RegInportOut,CLoOut,
input [4:0] EnOut,
output [31:0] BusMuxOut
);
	reg [31:0] BusMuxOutTemp, EnOutTemp;

	//Set the temporary BusMuxOut to be the correct output depending on the logic signal
	always @ (*) begin
		EnOutTemp <= EnOut;
	
		if (EnOutTemp == 5'b00000) BusMuxOutTemp <= r0out; else    
		if (EnOutTemp == 5'b00001) BusMuxOutTemp <= r1out; else    
		if (EnOutTemp == 5'b00010) BusMuxOutTemp <= r2out; else    
		if (EnOutTemp == 5'b00011) BusMuxOutTemp <= r3out; else   
		if (EnOutTemp == 5'b00100) BusMuxOutTemp <= r4out; else   
		if (EnOutTemp == 5'b00101) BusMuxOutTemp <= r5out; else   
		if (EnOutTemp == 5'b00110) BusMuxOutTemp <= r6out; else   
		if (EnOutTemp == 5'b00111) BusMuxOutTemp <= r7out; else   
		if (EnOutTemp == 5'b01000) BusMuxOutTemp <= r8out; else   
		if (EnOutTemp == 5'b01001) BusMuxOutTemp <= r9out; else   
		if (EnOutTemp == 5'b01010) BusMuxOutTemp <= r10out; else    
		if (EnOutTemp == 5'b01011) BusMuxOutTemp <= r11out; else    
		if (EnOutTemp == 5'b01100) BusMuxOutTemp <= r12out; else    
		if (EnOutTemp == 5'b01101) BusMuxOutTemp <= r13out; else    
		if (EnOutTemp == 5'b01110) BusMuxOutTemp <= r14out; else    
		if (EnOutTemp == 5'b01111) BusMuxOutTemp <= r15out; else    
		if (EnOutTemp == 5'b10000) BusMuxOutTemp <= RegHiOut; else
		if (EnOutTemp == 5'b10001) BusMuxOutTemp <= RegLoOut; else
		if (EnOutTemp == 5'b10010) BusMuxOutTemp <= ZHiOut; else
		if (EnOutTemp == 5'b10011) BusMuxOutTemp <= ZLoOut; else
		if (EnOutTemp == 5'b10100) BusMuxOutTemp <= PCOut; else
		if (EnOutTemp == 5'b10101) BusMuxOutTemp <= MDROut; else
		if (EnOutTemp == 5'b10110) BusMuxOutTemp <= RegInportOut; else
		if (EnOutTemp == 5'b10111) BusMuxOutTemp <= CLoOut;
		else BusMuxOutTemp <= 32'hFFFFFFFF;
	end
	
	assign BusMuxOut = BusMuxOutTemp [31:0];
	
endmodule 