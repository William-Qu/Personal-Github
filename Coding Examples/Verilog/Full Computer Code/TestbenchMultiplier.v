`timescale 1ns/10ps
module TestbenchMultiplier;
	reg [31:0] mp, mc; //mp = dd, mc = ds
	wire [31:0] HI, LO;
	
	nonRestoringDivisionPosiNeg two (mp, mc, LO, HI);
	
	initial 
	begin 
		//case 0
		mc <= 'h00000000;
		mp <= 'h00000000;
		#10 $display("HI = %b", HI);
		#10 $display("LO = %b", LO);
		//case 1
		mc <= 'hFFFFFFFF;
		mp <= 'hFFFFFFFF;
		#10 $display("HI = %b", HI);
		#10 $display("LO = %b", LO);
		//case 2
		mc <= 'h00000002;
		mp <= 'hFFFFFFFC;
		#10 $display("HI = %b", HI);
		#10 $display("LO = %b", LO);
	end
endmodule 