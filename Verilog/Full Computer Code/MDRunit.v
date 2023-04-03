module MDRunit(
	input read, clr, clk, wren, 
	input [31:0] BusMuxOut, Mdatain,
	output [31:0] MDRout
	);
	
	reg [31:0]MuxOut;
	
	always @ (*) begin
		MuxOut = read ? Mdatain : BusMuxOut;
	end
	
	reg32bit MDR (MDRout, MuxOut, clr, clk, wren);
	
endmodule