module boothMultiplier(
input [31:0] multiplier, multiplicand, 
output [31:0] ansHI, ansLO
);
	integer i;

	reg [63:0] ans;
	reg [32:0] mrShifted; //This is the register that is prepared for the booth algorithm counting

	reg [63:0] mc, mcTwos; //The 64 bit register of the Multiplicand and the Twos Compliment of the Multiplicand (1 * M and -1 * M)
	reg [63:0] dmc, dmcTwos; //The doubled Twos Compliment of the Multiplicand (2 * M and -2 * M)

	wire [31:0] mcTemp, mcTempTwos; //Temporary 32 bit twos compliment of 
	
	twoCompliment two (multiplicand, mcTempTwos);
	assign mcTemp = multiplicand;
	
	
	always @ (*) begin
		ans = 64'h0000000000000000;
		mcTwos = 64'hFFFFFFFFFFFFFFFF; //Set this register to all 1's
		
		//Prep all registers into their 64 bit counterparts with the correct values
		mc = mcTemp;
		mcTwos = mcTempTwos;
		dmc = mc <<< 1;
		dmcTwos = mcTwos <<< 1;
		mrShifted = multiplier <<< 1;
		

		//At this point all of the multiplicand values should be prepped, and so should the mrShifted register
		for (i=1; i<33; i=i+2) 
			begin
				if (mrShifted[i+1] == 0 && mrShifted[i] == 0 && mrShifted[i-1] == 0) ans = ans + (0); else
				if (mrShifted[i+1] == 0 && mrShifted[i] == 0 && mrShifted[i-1] == 1) ans = ans + (mc <<< i-1); else
				if (mrShifted[i+1] == 0 && mrShifted[i] == 1 && mrShifted[i-1] == 0) ans = ans + (mc <<< i-1); else
				if (mrShifted[i+1] == 0 && mrShifted[i] == 1 && mrShifted[i-1] == 1) ans = ans + (dmc <<< i-1); else
				if (mrShifted[i+1] == 1 && mrShifted[i] == 0 && mrShifted[i-1] == 0) ans = ans + (dmcTwos <<< i-1); else
				if (mrShifted[i+1] == 1 && mrShifted[i] == 0 && mrShifted[i-1] == 1) ans = ans + (mcTwos <<< i-1); else
				if (mrShifted[i+1] == 1 && mrShifted[i] == 1 && mrShifted[i-1] == 0) ans = ans + (mcTwos <<< i-1); else
				if (mrShifted[i+1] == 1 && mrShifted[i] == 1 && mrShifted[i-1] == 1) ans = ans + (0);
			end

		//At this point the multiplication should be done for the signed mc and mr, and the answer should be stored in the 64 bit ans register
	end 
	
	//At this point the answer from the ans register should be split into the output registers ansHI and ansLO
	assign ansHI = ans[63:32];
	assign ansLO = ans[31:0];
endmodule
