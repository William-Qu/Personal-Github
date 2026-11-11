module two_four_decoder (output [3:0] out, input [1:0] in);

   parameter temp = 4'b0001;

assign out = (in == 4'b00) ? temp   :
             (in == 4'b01) ? temp<<1:
             (in == 4'b10) ? temp<<2:
             (in == 4'b11) ? temp<<3:
					4'bxxxx;

endmodule