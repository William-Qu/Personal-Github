module NotOperation(input [31:0] d,output reg [31:0] q);
	integer i;
	always @ (*) 
		begin
			for (i=0; i<32; i=i+1) 
			begin
				q[i] = !(d[i]);
			end
		end	
endmodule