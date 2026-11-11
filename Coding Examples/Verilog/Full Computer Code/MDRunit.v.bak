module MDRunit(
	input read, clr, clk, wren, 
	input [31:0] BusMuxOut, Mdatain,
	output [31:0] MRDout);
	wire [31:0]MuxOut;
	
	assign MuxOut = read ? BusMuxOut : Mdatain;
	
	reg32bit MDR (MDRout, MuxOut, clr, clk, wren);
	
endmodule