`timescale 1ns/10ps
module ControlUnitBus(
input clr, clk, Halt,
input [31:0] MDRMDataIn,
output [31:0] OutportOut
);

	parameter ResetState = 3'b000, T0 = 3'b001, T1 = 3'b010, T2 = 3'b011, T3 = 3'b100, T4 = 3'b101, T5 = 3'b110, TempState = 3'b111;
	
	reg [2:0] PresentState;
	reg [2:0] StateHolder;
	
	//Registers that feed into the bus module
	reg MDRRead, ALUen, incPC, BAOut, AddressCounterEnable; //Bits for enabling and disabling register functions
	reg R0out, R1out, R2out, R3out, R4out, R5out, R6out, R7out,R8out, R9out, R10out, R11out, R12out, R13out, R14out, R15out,HIout, LOout, ZHIout, ZLOout,PCout, MDRout, InportOut, Cout; //Output Select Signals for which register were taking data from
	reg r0ins, r1ins, r2ins, r3ins, r4ins, r5ins, r6ins, r7ins, r8ins, r9ins, r10ins, r11ins, r12ins, r13ins, r14ins, r15ins, HIins, LOins, ZHIins, ZLOins,PCins, MDRins, MARins, Inports, Outports, IRins; //Input Select Signals for which register were putting data into
	
	wire [31:0] IROut; //Outport Output Signal to output signals to a display
	wire [14:0] ImmVal;
	wire [4:0] OPCode;
	wire [3:0] destSel, regASel, regBSel;
	
	//Breaking up of the IR register
	assign OPCode = IROut[31:27];
	assign destSel = IROut[26:23];
	assign regASel = IROut[22:19];
	assign regBSel = IROut[18:15];
	assign ImmVal = IROut[14:0];

	//Create any necessary hardware
	generate
		Bus B(clr, clk, MDRRead, ALUen, incPC, BAOut, AddressCounterEnable, R0out, R1out, R2out, R3out, R4out, R5out, R6out, R7out,R8out, R9out, R10out, R11out, R12out, R13out, R14out, R15out,HIout, LOout, ZHIout, ZLOout,PCout, MDRout, InportOut, Cout, r0ins, r1ins, r2ins, r3ins, r4ins, r5ins, r6ins, r7ins, r8ins, r9ins, r10ins, r11ins, r12ins, r13ins, r14ins, r15ins, HIins, LOins, ZHIins, ZLOins,PCins, MDRins, MARins, Inports, Outports, IRins, MDRMDataIn, OutportOut, IROut);
	endgenerate
		
	//Clk cycles operational loop
	always @ (posedge clk, posedge clr, posedge Halt) begin
		if (clr) PresentState = ResetState;
		else if (Halt) begin
			if (PresentState != TempState) StateHolder = PresentState - 2;
			PresentState = TempState;
			incPC = 0;
		end
		else begin
			if (PresentState == TempState) begin
				if (StateHolder == T0) incPC = 1;
				PresentState = StateHolder;
			end
			case (PresentState)
				ResetState : begin
									MDRRead = 0; ALUen = 1; incPC = 0; BAOut = 0; AddressCounterEnable = 0;
									R0out = 0; R1out = 0; R2out = 0; R3out = 0; R4out = 0; R5out = 0; R6out = 0; R7out = 0;R8out = 0; R9out = 0; R10out = 0; R11out = 0; R12out = 0; R13out = 0; R14out = 0; R15out = 0;HIout = 0; LOout = 0; ZHIout = 0; ZLOout = 0;PCout = 0; MDRout = 0; InportOut = 0; Cout = 0; 
									r0ins = 0; r1ins = 0; r2ins = 0; r3ins = 0; r4ins = 0; r5ins = 0; r6ins = 0; r7ins = 0; r8ins = 0; r9ins = 0; r10ins = 0; r11ins = 0; r12ins = 0; r13ins = 0; r14ins = 0; r15ins = 0; HIins = 0; LOins = 0; ZHIins = 0; ZLOins = 0;PCins = 0; MDRins = 0; MARins = 0; Inports = 0; Outports = 0; IRins = 0; 
									//MDRMDataIn = 0;
									StateHolder = 3'b0;
									if (~clr) PresentState = T0;	
								end
				T0	:	begin //In this cycle, we will PCOut, MARins, IncPC, and ZLOins are set to 1 (Increment PC)
							PCout = 1;
							AddressCounterEnable = 1;
							MARins = 1;
							incPC = 1;
							ZLOins = 1;
							
							PresentState = T1;
						end
				T1	:	begin //In this cycle, we will ZLOout, PCins, MDRRead, MDRins are set to 1 (Get the new instruction from memory)
							PCout = 0; AddressCounterEnable = 0; MARins = 0; incPC = 0; ZLOins = 0; //Clear last state
							ZLOout = 1;
							//PCins = 1;
							MDRRead = 1;
							MDRins = 1;
							
							PresentState = T2;
						end
				T2	:	begin //In this cycle, we will MDRout, IRins are set to 1 (Put new instruction into IR)
							ZLOout = 0; MDRRead = 0; MDRins = 0; //PCins = 0;
							MDRout = 1;
							IRins = 1;
							
							PresentState = T3;
						end
				T3	:	begin //In this cycle, we will get the answer from either the ALU or the branch instruction
							MDRout = 0; IRins = 0;
							Cout = 1;
							ZLOins = 1;
							
							PresentState = T4;
						end
				T4	:	begin //In this cycle, we will place the answer in the correct register
							Cout = 0; ZLOins = 0;
							ZLOout = 1;
							if (destSel == 4'b0000) r0ins = 1;
							if (destSel == 4'b0001) r1ins = 1;
							if (destSel == 4'b0010) r2ins = 1;
							if (destSel == 4'b0011) r3ins = 1;
							if (destSel == 4'b0100) r4ins = 1;
							if (destSel == 4'b0101) r5ins = 1;
							if (destSel == 4'b0110) r6ins = 1;
							if (destSel == 4'b0111) r7ins = 1;
							if (destSel == 4'b1000) r8ins = 1;
							if (destSel == 4'b1001) r9ins = 1;
							if (destSel == 4'b1010) r10ins = 1;
							if (destSel == 4'b1011) r11ins = 1;
							if (destSel == 4'b1100) r12ins = 1;
							if (destSel == 4'b1101) r13ins = 1;
							if (destSel == 4'b1110) r14ins = 1;
							if (destSel == 4'b1111) r15ins = 1;
							
							PresentState = ResetState;
						end
				T5 : PresentState = ResetState;
				TempState : PresentState = ResetState;
			endcase
		end
	end

endmodule 