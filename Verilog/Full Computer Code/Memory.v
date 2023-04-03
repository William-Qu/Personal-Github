module Memory(
input clr, clk, write,
input [31:0] dataIn,
input [8:0] Addr,
output [31:0] dataOut
);
			reg [31:0] RAMregisters[511:0];
			reg [31:0] dataOutTemp;

			initial begin
					$readmemb("C:/Users/789wi/Videos/ELEC-374/bin_memory_file.txt", RAMregisters);
			end
			
			always@(posedge clk)
			begin
				$display(RAMregisters[Addr]);
				if (write) RAMregisters[Addr] = dataIn;
				dataOutTemp = RAMregisters[Addr];
			end
			assign dataOut = dataOutTemp;
endmodule
