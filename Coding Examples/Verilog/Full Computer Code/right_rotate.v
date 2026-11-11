// Copyright (C) 1991-2013 Altera Corporation
// Your use of Altera Corporation's design tools, logic functions 
// and other software and tools, and its AMPP partner logic 
// functions, and any output files from any of the foregoing 
// (including device programming or simulation files), and any 
// associated documentation or information are expressly subject 
// to the terms and conditions of the Altera Program License 
// Subscription Agreement, Altera MegaCore Function License 
// Agreement, or other applicable license agreement, including, 
// without limitation, that your use is for the sole purpose of 
// programming logic devices manufactured by Altera and sold by 
// Altera or its authorized distributors.  Please refer to the 
// applicable agreement for further details.

// PROGRAM		"Quartus II 64-Bit"
// VERSION		"Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Full Version"
// CREATED		"Sun Feb 26 14:49:33 2023"

module right_rotate(
	clk,
	clr,
	D,
	Q
);


input wire	clk;
input wire	clr;
input wire	[31:0] D;
output wire	[31:0] Q;

wire	[31:0] Q_ALTERA_SYNTHESIZED;





dff_Q	b2v_inst35(
	.D(D[0]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[31]));


dff_Q	b2v_inst38(
	.D(D[1]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[0]));


dff_Q	b2v_inst39(
	.D(D[2]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[1]));


dff_Q	b2v_inst40(
	.D(D[3]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[2]));


dff_Q	b2v_inst41(
	.D(D[4]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[3]));


dff_Q	b2v_inst42(
	.D(D[5]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[4]));


dff_Q	b2v_inst43(
	.D(D[6]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[5]));


dff_Q	b2v_inst44(
	.D(D[7]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[6]));


dff_Q	b2v_inst45(
	.D(D[8]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[7]));


dff_Q	b2v_inst48(
	.D(D[9]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[8]));


dff_Q	b2v_inst49(
	.D(D[10]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[9]));


dff_Q	b2v_inst50(
	.D(D[11]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[10]));


dff_Q	b2v_inst51(
	.D(D[12]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[11]));


dff_Q	b2v_inst52(
	.D(D[13]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[12]));


dff_Q	b2v_inst53(
	.D(D[14]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[13]));


dff_Q	b2v_inst54(
	.D(D[15]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[14]));


dff_Q	b2v_inst55(
	.D(D[16]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[15]));


dff_Q	b2v_inst56(
	.D(D[17]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[16]));


dff_Q	b2v_inst57(
	.D(D[18]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[17]));


dff_Q	b2v_inst58(
	.D(D[19]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[18]));


dff_Q	b2v_inst59(
	.D(D[20]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[19]));


dff_Q	b2v_inst60(
	.D(D[21]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[20]));


dff_Q	b2v_inst61(
	.D(D[22]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[21]));


dff_Q	b2v_inst63(
	.D(D[23]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[22]));


dff_Q	b2v_inst64(
	.D(D[24]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[23]));


dff_Q	b2v_inst65(
	.D(D[25]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[24]));


dff_Q	b2v_inst66(
	.D(D[26]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[25]));


dff_Q	b2v_inst67(
	.D(D[27]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[26]));


dff_Q	b2v_inst68(
	.D(D[28]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[27]));


dff_Q	b2v_inst69(
	.D(D[29]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[28]));


dff_Q	b2v_inst70(
	.D(D[30]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[29]));


dff_Q	b2v_inst71(
	.D(D[31]),
	.clk(clk),
	.clr(clr),
	.Q(Q_ALTERA_SYNTHESIZED[30]));

assign	Q = Q_ALTERA_SYNTHESIZED;

endmodule
