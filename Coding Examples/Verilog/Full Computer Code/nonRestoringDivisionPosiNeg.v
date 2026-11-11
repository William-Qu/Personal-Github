module nonRestoringDivisionPosiNeg(
input [31:0] dividend, divisor,
output [31:0] quotient, remainder
);
integer i;

reg [31:0] M, divisorTwos, A, Q; //divisorTwos is (-1 * M)
wire [31:0] tempM, divisorTwostemp;

//Find the twos compliment of the divisor
twoCompliment two (divisor, divisorTwostemp);

assign tempM = divisor[31:0];
	
	always @ (*) begin
		A = 32'b00000000000000000000000000000000;
		M = 32'b00000000000000000000000000000000;
		Q = 32'b00000000000000000000000000000000;
		//Set divisorTwos using divisorTwostemp
		divisorTwos = divisorTwostemp;
	
		//Initialize Q and M depending on if the given divisor is positive or negative
		for (i=0; i<32; i=i+1) 
				begin
					Q = dividend[31] ? !(dividend) : dividend;
					
					if (divisor[31] == 0) begin
						M[i] = divisor[i]; 
					end
					else if (divisor[31] == 1) begin
						M[i] = divisorTwos[i];
						divisorTwos[i] = tempM[i];						
					end
				end
		
		if (dividend[31] == 1) Q = Q + 'b1;
		//Step 1 of the Non-Restoring Division Algorithm (Done 32 times)
		for (i=0; i<32; i=i+1)
				begin
					//Shift A and Q left one binary position
					A = A << 1;
					A[0] = Q[31];
					Q = Q << 1;
					
					//If A >= 0, subtract M from A, else if A < 0, add M to A
					if (A[31] == 0) A = A + divisorTwos; //A >= 0
					else if (A[31] == 1) A = A + divisor; //A < 0
					
					//Now, if A >= 0, set Q[0] to 1, else if A < 0 set Q[0] to 0
					if (A[31] == 0) Q[0] = 1; //A >= 0
					else if (A[31] == 1) Q[0] = 0; //A < 0
				end
		
		//If A < 0, add M to A to ensure a positive remainder
		if (A[31] == 1) A = A + divisor;
		
		//Determine whether the outputs should be positive or negative (positives we don't do anything
		//if (divisor[31] == 1 && dividend[31] == 1) ; else
		if ((divisor[31] == 0 && dividend[31] == 1) || (divisor[31] == 1 && dividend[31] == 0))begin
			for (i=0; i<32; i=i+1) 
			begin
				Q[i] = !(Q[i]);
				A[i] = !(A[i]);
			end
			Q = Q + 'b1;
			A = A + 'b1;
		end
		//if (divisor[31] == 0 && dividend[31] == 0) ;
	end
	
	//Set the outputs (quotient = Q and remainder = A)
	assign quotient = Q[31:0];
	assign remainder = A[31:0];

endmodule 