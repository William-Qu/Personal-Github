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
// CREATED		"Sun Feb 26 14:24:24 2023"

module Hierarchical_CLA(
	Select,
	x,
	y,
	C_out,
	S
);


input wire	Select;
input wire	[31:0] x;
input wire	[31:0] y;
output wire	C_out;
output wire	[31:0] S;

wire	[31:0] S_ALTERA_SYNTHESIZED;
wire	SYNTHESIZED_WIRE_0;
wire	SYNTHESIZED_WIRE_1;
wire	SYNTHESIZED_WIRE_2;
wire	SYNTHESIZED_WIRE_3;
wire	SYNTHESIZED_WIRE_4;
wire	SYNTHESIZED_WIRE_5;
wire	SYNTHESIZED_WIRE_6;
wire	SYNTHESIZED_WIRE_7;
wire	SYNTHESIZED_WIRE_8;
wire	SYNTHESIZED_WIRE_9;
wire	SYNTHESIZED_WIRE_10;
wire	SYNTHESIZED_WIRE_11;
wire	SYNTHESIZED_WIRE_12;
wire	SYNTHESIZED_WIRE_13;
wire	SYNTHESIZED_WIRE_14;
wire	SYNTHESIZED_WIRE_15;
wire	SYNTHESIZED_WIRE_16;
wire	SYNTHESIZED_WIRE_17;
wire	SYNTHESIZED_WIRE_18;
wire	SYNTHESIZED_WIRE_19;
wire	SYNTHESIZED_WIRE_20;
wire	SYNTHESIZED_WIRE_21;
wire	SYNTHESIZED_WIRE_22;
wire	SYNTHESIZED_WIRE_23;
wire	SYNTHESIZED_WIRE_24;
wire	SYNTHESIZED_WIRE_25;
wire	SYNTHESIZED_WIRE_26;
wire	SYNTHESIZED_WIRE_27;
wire	SYNTHESIZED_WIRE_28;
wire	SYNTHESIZED_WIRE_29;
wire	SYNTHESIZED_WIRE_30;
wire	SYNTHESIZED_WIRE_31;
wire	SYNTHESIZED_WIRE_32;
wire	SYNTHESIZED_WIRE_33;
wire	SYNTHESIZED_WIRE_34;
wire	SYNTHESIZED_WIRE_35;




assign	SYNTHESIZED_WIRE_22 = Select ^ y[3];

assign	SYNTHESIZED_WIRE_23 = Select ^ y[4];

assign	SYNTHESIZED_WIRE_24 = Select ^ y[5];

assign	SYNTHESIZED_WIRE_2 = Select ^ y[8];

assign	SYNTHESIZED_WIRE_3 = Select ^ y[9];

assign	SYNTHESIZED_WIRE_8 = Select ^ y[14];

assign	SYNTHESIZED_WIRE_9 = Select ^ y[15];

assign	SYNTHESIZED_WIRE_4 = Select ^ y[10];

assign	SYNTHESIZED_WIRE_5 = Select ^ y[11];

assign	SYNTHESIZED_WIRE_6 = Select ^ y[12];

assign	SYNTHESIZED_WIRE_7 = Select ^ y[13];

assign	SYNTHESIZED_WIRE_11 = Select ^ y[16];

assign	SYNTHESIZED_WIRE_12 = Select ^ y[17];

assign	SYNTHESIZED_WIRE_17 = Select ^ y[22];

assign	SYNTHESIZED_WIRE_18 = Select ^ y[23];

assign	SYNTHESIZED_WIRE_13 = Select ^ y[18];

assign	SYNTHESIZED_WIRE_14 = Select ^ y[19];

assign	SYNTHESIZED_WIRE_15 = Select ^ y[20];

assign	SYNTHESIZED_WIRE_16 = Select ^ y[21];

assign	SYNTHESIZED_WIRE_28 = Select ^ y[24];

assign	SYNTHESIZED_WIRE_29 = Select ^ y[25];

assign	SYNTHESIZED_WIRE_34 = Select ^ y[30];

assign	SYNTHESIZED_WIRE_35 = Select ^ y[31];

assign	SYNTHESIZED_WIRE_30 = Select ^ y[26];

assign	SYNTHESIZED_WIRE_31 = Select ^ y[27];

assign	SYNTHESIZED_WIRE_32 = Select ^ y[28];

assign	SYNTHESIZED_WIRE_33 = Select ^ y[29];

assign	C_out = Select ^ SYNTHESIZED_WIRE_0;


CLA_8inputs_updated	b2v_inst38(
	.c_in(SYNTHESIZED_WIRE_1),
	.x0(x[8]),
	.y0(SYNTHESIZED_WIRE_2),
	.x1(x[9]),
	.y1(SYNTHESIZED_WIRE_3),
	.x2(x[10]),
	.y2(SYNTHESIZED_WIRE_4),
	.x3(x[11]),
	.y3(SYNTHESIZED_WIRE_5),
	.x4(x[12]),
	.y4(SYNTHESIZED_WIRE_6),
	.x5(x[13]),
	.y5(SYNTHESIZED_WIRE_7),
	.x6(x[14]),
	.y6(SYNTHESIZED_WIRE_8),
	.x7(x[15]),
	.y7(SYNTHESIZED_WIRE_9),
	.S0(S_ALTERA_SYNTHESIZED[8]),
	.S1(S_ALTERA_SYNTHESIZED[9]),
	.S2(S_ALTERA_SYNTHESIZED[10]),
	.S3(S_ALTERA_SYNTHESIZED[11]),
	.S4(S_ALTERA_SYNTHESIZED[12]),
	.S5(S_ALTERA_SYNTHESIZED[13]),
	.S6(S_ALTERA_SYNTHESIZED[14]),
	.S7(S_ALTERA_SYNTHESIZED[15]),
	.c_out(SYNTHESIZED_WIRE_10));


CLA_8inputs_updated	b2v_inst39(
	.c_in(SYNTHESIZED_WIRE_10),
	.x0(x[16]),
	.y0(SYNTHESIZED_WIRE_11),
	.x1(x[17]),
	.y1(SYNTHESIZED_WIRE_12),
	.x2(x[18]),
	.y2(SYNTHESIZED_WIRE_13),
	.x3(x[19]),
	.y3(SYNTHESIZED_WIRE_14),
	.x4(x[20]),
	.y4(SYNTHESIZED_WIRE_15),
	.x5(x[21]),
	.y5(SYNTHESIZED_WIRE_16),
	.x6(x[22]),
	.y6(SYNTHESIZED_WIRE_17),
	.x7(x[23]),
	.y7(SYNTHESIZED_WIRE_18),
	.S0(S_ALTERA_SYNTHESIZED[16]),
	.S1(S_ALTERA_SYNTHESIZED[17]),
	.S2(S_ALTERA_SYNTHESIZED[18]),
	.S3(S_ALTERA_SYNTHESIZED[19]),
	.S4(S_ALTERA_SYNTHESIZED[20]),
	.S5(S_ALTERA_SYNTHESIZED[21]),
	.S6(S_ALTERA_SYNTHESIZED[22]),
	.S7(S_ALTERA_SYNTHESIZED[23]),
	.c_out(SYNTHESIZED_WIRE_27));


CLA_8inputs_updated	b2v_inst4(
	.c_in(Select),
	.x0(x[0]),
	.y0(SYNTHESIZED_WIRE_19),
	.x1(x[1]),
	.y1(SYNTHESIZED_WIRE_20),
	.x2(x[2]),
	.y2(SYNTHESIZED_WIRE_21),
	.x3(x[3]),
	.y3(SYNTHESIZED_WIRE_22),
	.x4(x[4]),
	.y4(SYNTHESIZED_WIRE_23),
	.x5(x[5]),
	.y5(SYNTHESIZED_WIRE_24),
	.x6(x[6]),
	.y6(SYNTHESIZED_WIRE_25),
	.x7(x[7]),
	.y7(SYNTHESIZED_WIRE_26),
	.S0(S_ALTERA_SYNTHESIZED[0]),
	.S1(S_ALTERA_SYNTHESIZED[1]),
	.S2(S_ALTERA_SYNTHESIZED[2]),
	.S3(S_ALTERA_SYNTHESIZED[3]),
	.S4(S_ALTERA_SYNTHESIZED[4]),
	.S5(S_ALTERA_SYNTHESIZED[5]),
	.S6(S_ALTERA_SYNTHESIZED[6]),
	.S7(S_ALTERA_SYNTHESIZED[7]),
	.c_out(SYNTHESIZED_WIRE_1));


CLA_8inputs_updated	b2v_inst40(
	.c_in(SYNTHESIZED_WIRE_27),
	.x0(x[24]),
	.y0(SYNTHESIZED_WIRE_28),
	.x1(x[25]),
	.y1(SYNTHESIZED_WIRE_29),
	.x2(x[26]),
	.y2(SYNTHESIZED_WIRE_30),
	.x3(x[27]),
	.y3(SYNTHESIZED_WIRE_31),
	.x4(x[28]),
	.y4(SYNTHESIZED_WIRE_32),
	.x5(x[29]),
	.y5(SYNTHESIZED_WIRE_33),
	.x6(x[30]),
	.y6(SYNTHESIZED_WIRE_34),
	.x7(x[31]),
	.y7(SYNTHESIZED_WIRE_35),
	.S0(S_ALTERA_SYNTHESIZED[24]),
	.S1(S_ALTERA_SYNTHESIZED[25]),
	.S2(S_ALTERA_SYNTHESIZED[26]),
	.S3(S_ALTERA_SYNTHESIZED[27]),
	.S4(S_ALTERA_SYNTHESIZED[28]),
	.S5(S_ALTERA_SYNTHESIZED[29]),
	.S6(S_ALTERA_SYNTHESIZED[30]),
	.S7(S_ALTERA_SYNTHESIZED[31]),
	.c_out(SYNTHESIZED_WIRE_0));

assign	SYNTHESIZED_WIRE_19 = Select ^ y[0];

assign	SYNTHESIZED_WIRE_20 = Select ^ y[1];

assign	SYNTHESIZED_WIRE_25 = Select ^ y[6];

assign	SYNTHESIZED_WIRE_26 = Select ^ y[7];

assign	SYNTHESIZED_WIRE_21 = Select ^ y[2];

assign	S = S_ALTERA_SYNTHESIZED;

endmodule
