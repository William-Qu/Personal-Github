// and datapath_tb.v file: ADD_tb.v
`timescale 1ns/10ps
module MovHiMovLoOutput;

	reg clr, clk, MDRRead, ALUen, incPC, BAOut; //Bits for enabling and disabling register functions
	reg R0out, R1out, R2out, R3out, R4out, R5out, R6out, R7out,R8out, R9out, R10out, R11out, R12out, R13out, R14out, R20out,HIout, LOout, ZHIout, ZLOout,PCout, MDRout, InportOut, Cout; //Output Select Signals for which register were taking data from
	reg r0ins, r1ins, r2ins, r3ins, r4ins, r5ins, r6ins, r7ins, r8ins, r9ins, r10ins, r11ins, r12ins, r13ins, r14ins, r20ins, HIins, LOins, ZHIins, ZLOins,PCins, MDRins, MARins, Inports, Outports, IRins; //Input Select Signals for which register were putting data into
	reg [31:0] MDRMDataIn;//MDR Data In register

	wire [31:0] OutportOut;

	parameter Default = 4'b0000, Reg_load1a = 4'b0001, Reg_load1b = 4'b0010, Reg_load2a = 4'b0011,
					Reg_load2b = 4'b0100, Reg_load3a = 4'b0101, Reg_load3b = 4'b0110, T0 = 4'b0111,
					T1 = 4'b1000, T2 = 4'b1001, T3 = 4'b1010, T4 = 4'b1011;
	reg [3:0] Present_state = Default;
	
	Bus Datapath(
		clr, clk, MDRRead, ALUen, incPC, BAOut,//Bits for enabling and disabling register functions
		R0out, R1out, R2out, R3out, R4out, R5out, R6out, R7out,R8out, R9out, R10out, R11out, R12out, R13out, R14out, R20out,HIout, LOout, ZHIout, ZLOout,PCout, MDRout, InportOut, Cout, //Output Select Signals for which register were taking data from
		r0ins, r1ins, r2ins, r3ins, r4ins, r5ins, r6ins, r7ins, r8ins, r9ins, r10ins, r11ins, r12ins, r13ins, r14ins, r20ins, HIins, LOins, ZHIins, ZLOins,PCins, MDRins, MARins, Inports, Outports, IRins, //Input Select Signals for which register were putting data into
		MDRMDataIn, OutportOut);

// add test logic here
initial
	begin
		clk = 0;
		forever #10 clk = ~ clk;
end

always @(posedge clk) // finite state machine; if clk rising-edge
	begin
		case (Present_state)
			Default 			:		#40 Present_state = Reg_load1a;
			Reg_load1a 		: 	   #40 Present_state = Reg_load1b;
			Reg_load1b 		: 		#40 Present_state = Reg_load2a;
			Reg_load2a 		: 		#40 Present_state = Reg_load2b;
			Reg_load2b 		: 		#40 Present_state = Reg_load3a;
			Reg_load3a 		: 		#40 Present_state = Reg_load3b;
			Reg_load3b 		: 		#40 Present_state = T0;
			T0 				: 		#40 Present_state = T1;
			T1 				: 		#40 Present_state = T2;
			T2 				: 		#40 Present_state = T3;
			T3 				: 		#40 Present_state = T4;
	endcase
 end

always @(Present_state) // do the required job in each state
	begin
		case (Present_state) // assert the required signals in each clk cycle
			Default: begin
								PCout <= 0; ZLOout <= 0; MDRout <= 0; incPC <= 0;// initialize the signals
								R4out <= 0; R5out <= 0; ZLOins <= 0; ZHIins <= 0; MARins <= 0;
								PCins <=0; MDRins <= 0; IRins <= 0; BAOut <= 0;
								MDRRead <= 0; clr <= 1; ALUen <= 1; InportOut <= 0;
								r0ins <= 0; r2ins <= 0; r3ins <= 0; MDRMDataIn <= 32'h00000000;
			end
			Reg_load1a: begin
								#10 clr <= 0;
								#20 MDRMDataIn <= 32'h00000012;
								#10 Inports <= 1;
								#20 Inports <= 0;
								#40
								#10 InportOut <= 1; HIins <= 1;
								#20 InportOut <= 0; HIins <= 0; // initialize R0 with the value $12
								#40
								#20 MDRMDataIn <= 32'h00000032;
								#10 Inports <= 1;
								#20 Inports <= 0;
								#40
								#10 InportOut <= 1; LOins <= 1;
								#20 InportOut <= 0; LOins <= 0; // initialize R0 with the value $12
								#40 //Mov from HI
								#10 HIout <= 1; ZHIins <= 1;
								#20 HIout <= 0; ZHIins <= 0; // initialize R0 with the value $12
								#40 //Mov from LO
								#10 LOout <= 1; ZLOins <= 1;
								#20 LOout <= 0; ZLOins <= 0; // initialize R0 with the value $12
								#40
								#10 ZLOout <= 1; Outports <= 1;
								#20 ZLOout <= 0; Outports <= 0; // initialize R0 with the value $12

								
			end
		endcase			
	end
endmodule  