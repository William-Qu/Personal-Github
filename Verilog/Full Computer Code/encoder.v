module encoder(R0out, R1out, R2out, R3out, 
						  R4out, R5out, R6out, R7out,
						  R8out, R9out, R10out, R11out, 
						  R12out, R13out, R14out, R15out,
						  HIout, LOout, ZHIout, ZLOout,
						  PCout, MDRout, InPortOut, Cout, d);
	input R0out, R1out, R2out, R3out, R4out, R5out, R6out, R7out,R8out, R9out, R10out, R11out, R12out, R13out, R14out, R15out,HIout, LOout, ZHIout, ZLOout,PCout, MDRout, InPortOut, Cout;
	output [4:0] d;
	reg [4:0]d;
	always @(R0out or R1out or R2out or R3out or R4out or R5out or R6out or R7out or R8out or R9out or R10out or R11out or R12out or R13out or R14out or R15out or HIout or LOout or ZHIout or ZLOout or PCout or MDRout or InPortOut or Cout)
	begin
		if (R0out)							d = 5'b00000; 
		else if (R1out)		 			d = 5'b00001; 
		else if (R2out)		 			d = 5'b00010; 
		else if (R3out)		 			d = 5'b00011; 
		else if (R4out)		 			d = 5'b00100; 
		else if (R5out)		 			d = 5'b00101; 
		else if (R6out)		 			d = 5'b00110; 
		else if (R7out)		 			d = 5'b00111; 
		else if (R8out)		 			d = 5'b01000; 
		else if (R9out)		 			d = 5'b01001; 
		else if (R10out)			 		d = 5'b01010; 
		else if (R11out)			 		d = 5'b01011; 
		else if (R12out)			 		d = 5'b01100; 
		else if (R13out)			 		d = 5'b01101; 
		else if (R14out)			 		d = 5'b01110; 
		else if (R15out)		 			d = 5'b01111; 
		else if (HIout) 		 			d = 5'b10000; 
		else if (LOout) 		 			d = 5'b10001; 
		else if (ZHIout) 					d = 5'b10010; 
		else if (ZLOout)		 			d = 5'b10011; 
		else if (PCout) 		 			d = 5'b10100; 
		else if (MDRout) 					d = 5'b10101; 
		else if (InPortOut) 			 	d = 5'b10110; 
		else if (Cout)						d = 5'b10111; 
	end
endmodule