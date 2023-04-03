module CON_FF (input [31:0] IR,
					input [31:0] bus,
					input CONin, clr, clk,
					output CONout);
					
		reg [3:0] decoder_output;
		wire [1:0] decoder_input;
		
		wire [4:0] OPCode;
		assign OPCode = IR[31:27];
		
		wire equal, notequal, equalorgreater, less, d; 
		
		assign equal = (bus == 32'b0) ? 1'b1 : 1'b0;
		assign notequal = (bus != 32'b0) ? 1'b1 : 1'b0;
		assign equalorgreater = (bus[31] == 1'b0) ? 1'b1 : 1'b0;
		assign less = (bus[31] == 1'b1) ? 1'b1 : 1'b0;
		
		always @ (*) begin
			case(OPCode)
				5'b11000	: decoder_output = 4'b0001;				//Branch Zero Instruction brzr
				5'b11001	: decoder_output = 4'b0010;				//Branch Non-Zero Instruction brnz
				5'b11010	: decoder_output = 4'b0100;				//Branch Positive Instruction brpl
				5'b11011	: decoder_output = 4'b1000;				//Branch Negative Instruction brmi
				default	: decoder_output = 4'b0000;
			endcase	
		end	
			
		assign d = ((decoder_output[0] & equal) | (decoder_output[1] & notequal) | (decoder_output[2] & equalorgreater) | (decoder_output[3] & less));

		D_flipflop flip (CONout, d, clr, clk, CONin);
endmodule
		
		
		