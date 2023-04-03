module reg32bit (q, d, clr, clk, wren);
	input [31:0] d;
	input	clr, clk, wren;
	output [31:0] q;
	reg [31:0] r;
	always @(posedge clk)
	begin
		if (wren) begin
			r <= d;
		end
		if (clr) begin
			r <= 32'b0;
		end
	end
	assign q = r;
endmodule
