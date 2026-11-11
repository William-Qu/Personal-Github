// and datapath_tb.v file: ADD_tb.v
`timescale 1ns/10ps
module ADD_tb;

	reg clr, clk, Halt;
	reg [31:0] MDRMDataIn;
	wire [31:0] OutportOut;


	parameter Default = 4'b0000, Reg_load1a = 4'b0001, Reg_load1b = 4'b0010, Reg_load2a = 4'b0011,
					Reg_load2b = 4'b0100, Reg_load3a = 4'b0101, Reg_load3b = 4'b0110, T0 = 4'b0111,
					T1 = 4'b1000, T2 = 4'b1001, T3 = 4'b1010, T4 = 4'b1011;
					
	reg [3:0] Present_state = Default;
	
	ControlUnitBus CTRL (clr, clk, Halt, MDRMDataIn,OutportOut);
	
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
				clr <= 0; Halt <= 0; MDRMDataIn <= 0;
			end
			Reg_load1a: begin
								#20 clr <= 1;
								#20 clr <= 0;
								#40 MDRMDataIn <= 32'hAAAAAAAA;
								#40 clr <= 1;
								#10 clr <= 0;
								#40 Halt <= 1;
								#100 Halt <= 0;
								#40 Halt <= 1;
								#10 Halt <= 0;
								#10 MDRMDataIn <= 32'b0;
								#40 Halt <= 1;
								#100 Halt <= 0;
								#40 Halt <= 1;
								#10 Halt <= 0;
								#10 clr <= 1;
								#10 clr <= 0;
			end
		endcase
	end
endmodule  