module twoCompliment(input [31:0] d,output [31:0] q);
	assign q = ~d + 1'b1;
endmodule
