module four_sixteen_decoder (output [15:0] out, input [3:0] in);

   parameter temp = 16'b0000000000000001;

assign out = (in == 4'b0000) ? temp   :
             (in == 4'b0001) ? temp<<1:
             (in == 4'b0010) ? temp<<2:
             (in == 4'b0011) ? temp<<3:
             (in == 4'b0100) ? temp<<4:
             (in == 4'b0101) ? temp<<5:
             (in == 4'b0110) ? temp<<6:
             (in == 4'b0111) ? temp<<7:
             (in == 4'b1000) ? temp<<8:
             (in == 4'b1001) ? temp<<9:
             (in == 4'b1010) ? temp<<10:
             (in == 4'b1011) ? temp<<11:
             (in == 4'b1100) ? temp<<12:
             (in == 4'b1101) ? temp<<13:
             (in == 4'b1110) ? temp<<14:
             (in == 4'b1111) ? temp<<15: 
				  16'bxxxxxxxxxxxxxxxx;

endmodule