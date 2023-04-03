module D_flipflop (q, d, clr, clk, wren);
	input d;
	input	clr, clk, wren;
	output q;
	reg r;
	always @(posedge clk)
	begin
		if (wren) begin
			r = d;
		end
		if (clr) begin
			r = 1'b0;
		end
	end
	assign q = r;
endmodule
