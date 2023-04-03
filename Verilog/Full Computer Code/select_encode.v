module select_encode(input [31:0] IR,
							input Gra, Grb, Grc,
							input Rin_input, Rout_input, BAout,
							output [31:0] C_sign_extend,
							output [15:0] Rin_output,
							output [15:0] Rout_output);
							
	wire [15:0] decoder_output;
	wire [4:0] decoder_input;
	
								       //Ra							 Rb							Rc
	assign decoder_input = ((IR[26:23]&{4{Gra}}) | (IR[22:19]&{4{Grb}}) | (IR[18:15]&{4{Grc}}));
	
	four_sixteen_decoder decode (decoder_output, decoder_input);
	
	assign Rin_output = decoder_output & {16{Rin_input}};
	assign Rout_output = decoder_output & ({16{Rout_input | BAout}});
	assign C_sign_extend = {{13{IR[18]}}, IR[18:0]};
	
endmodule
	
	
	
	
