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
// CREATED		"Sun Feb 26 15:06:20 2023"

module CLA_8inputs_updated(
	x0,
	y0,
	x1,
	y1,
	x2,
	y2,
	y3,
	x3,
	x4,
	y4,
	x5,
	y5,
	y6,
	x6,
	x7,
	y7,
	c_in,
	c_out,
	S7,
	S6,
	S5,
	S4,
	S3,
	S2,
	S1,
	S0
);


input wire	x0;
input wire	y0;
input wire	x1;
input wire	y1;
input wire	x2;
input wire	y2;
input wire	y3;
input wire	x3;
input wire	x4;
input wire	y4;
input wire	x5;
input wire	y5;
input wire	y6;
input wire	x6;
input wire	x7;
input wire	y7;
input wire	c_in;
output wire	c_out;
output wire	S7;
output wire	S6;
output wire	S5;
output wire	S4;
output wire	S3;
output wire	S2;
output wire	S1;
output wire	S0;

wire	cin;
wire	g0;
wire	g1;
wire	g2;
wire	g3;
wire	g4;
wire	g5;
wire	p0;
wire	p1;
wire	p2;
wire	p3;
wire	p4;
wire	p5;
wire	p6;
wire	SYNTHESIZED_WIRE_67;
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
wire	SYNTHESIZED_WIRE_36;
wire	SYNTHESIZED_WIRE_37;
wire	SYNTHESIZED_WIRE_38;
wire	SYNTHESIZED_WIRE_39;
wire	SYNTHESIZED_WIRE_40;
wire	SYNTHESIZED_WIRE_41;
wire	SYNTHESIZED_WIRE_42;
wire	SYNTHESIZED_WIRE_43;
wire	SYNTHESIZED_WIRE_44;
wire	SYNTHESIZED_WIRE_45;
wire	SYNTHESIZED_WIRE_46;
wire	SYNTHESIZED_WIRE_47;
wire	SYNTHESIZED_WIRE_48;
wire	SYNTHESIZED_WIRE_49;
wire	SYNTHESIZED_WIRE_68;
wire	SYNTHESIZED_WIRE_51;
wire	SYNTHESIZED_WIRE_52;
wire	SYNTHESIZED_WIRE_53;
wire	SYNTHESIZED_WIRE_54;
wire	SYNTHESIZED_WIRE_55;
wire	SYNTHESIZED_WIRE_56;
wire	SYNTHESIZED_WIRE_57;
wire	SYNTHESIZED_WIRE_63;
wire	SYNTHESIZED_WIRE_66;





P_G_block	b2v_inst(
	.xi(x0),
	.yi(y0),
	.Gi(g0),
	.Pi(p0));

assign	SYNTHESIZED_WIRE_9 = p1 & p3 & p2 & p4 & SYNTHESIZED_WIRE_67 & p6 & g0 & p5;

assign	SYNTHESIZED_WIRE_2 = p0 & p2 & p1 & p3 & p6 & p5 & SYNTHESIZED_WIRE_67 & p4;

assign	SYNTHESIZED_WIRE_10 = SYNTHESIZED_WIRE_2 & cin;

assign	SYNTHESIZED_WIRE_11 = SYNTHESIZED_WIRE_3 | SYNTHESIZED_WIRE_4 | SYNTHESIZED_WIRE_5 | SYNTHESIZED_WIRE_6 | SYNTHESIZED_WIRE_7 | SYNTHESIZED_WIRE_8 | SYNTHESIZED_WIRE_9 | SYNTHESIZED_WIRE_10;

assign	c_out = SYNTHESIZED_WIRE_11 | SYNTHESIZED_WIRE_12;

assign	S0 = cin ^ p0;

assign	S1 = SYNTHESIZED_WIRE_13 ^ p1;

assign	S2 = SYNTHESIZED_WIRE_14 ^ p2;

assign	S4 = SYNTHESIZED_WIRE_15 ^ p4;

assign	S3 = SYNTHESIZED_WIRE_16 ^ p3;

assign	S5 = SYNTHESIZED_WIRE_17 ^ p5;

assign	S6 = SYNTHESIZED_WIRE_18 ^ p6;

assign	S7 = SYNTHESIZED_WIRE_19 ^ SYNTHESIZED_WIRE_67;


P_G_block	b2v_inst35(
	.xi(x1),
	.yi(y1),
	.Gi(g1),
	.Pi(p1));


P_G_block	b2v_inst36(
	.xi(x2),
	.yi(y2),
	.Gi(g2),
	.Pi(p2));


P_G_block	b2v_inst37(
	.xi(x3),
	.yi(y3),
	.Gi(g3),
	.Pi(p3));


P_G_block	b2v_inst38(
	.xi(x4),
	.yi(y4),
	.Gi(g4),
	.Pi(p4));


P_G_block	b2v_inst39(
	.xi(x5),
	.yi(y5),
	.Gi(g5),
	.Pi(p5));


P_G_block	b2v_inst40(
	.xi(x6),
	.yi(y6),
	.Gi(SYNTHESIZED_WIRE_68),
	.Pi(p6));


P_G_block	b2v_inst41(
	.xi(x7),
	.yi(y7),
	.Gi(SYNTHESIZED_WIRE_12),
	.Pi(SYNTHESIZED_WIRE_67));

assign	SYNTHESIZED_WIRE_21 = p0 & cin;

assign	SYNTHESIZED_WIRE_13 = SYNTHESIZED_WIRE_21 | g0;

assign	SYNTHESIZED_WIRE_22 = p1 & g0;

assign	SYNTHESIZED_WIRE_23 = cin & p0 & p1;

assign	SYNTHESIZED_WIRE_14 = SYNTHESIZED_WIRE_22 | SYNTHESIZED_WIRE_23 | g1;

assign	SYNTHESIZED_WIRE_26 = g1 & p2;

assign	SYNTHESIZED_WIRE_24 = g0 & p1 & p2;

assign	SYNTHESIZED_WIRE_25 = cin & p0 & p1 & p2;

assign	SYNTHESIZED_WIRE_16 = g2 | SYNTHESIZED_WIRE_24 | SYNTHESIZED_WIRE_25 | SYNTHESIZED_WIRE_26;

assign	SYNTHESIZED_WIRE_28 = g2 & p3;

assign	SYNTHESIZED_WIRE_31 = g1 & p2 & p3;

assign	SYNTHESIZED_WIRE_29 = g0 & p1 & p2 & p3;

assign	SYNTHESIZED_WIRE_27 = p0 & p1 & p2 & p3;

assign	SYNTHESIZED_WIRE_30 = SYNTHESIZED_WIRE_27 & cin;

assign	SYNTHESIZED_WIRE_32 = SYNTHESIZED_WIRE_28 | SYNTHESIZED_WIRE_29 | SYNTHESIZED_WIRE_30 | SYNTHESIZED_WIRE_31;

assign	SYNTHESIZED_WIRE_15 = SYNTHESIZED_WIRE_32 | g3;

assign	SYNTHESIZED_WIRE_35 = g3 & p4;

assign	SYNTHESIZED_WIRE_34 = g2 & p3 & p4;

assign	SYNTHESIZED_WIRE_36 = g1 & p2 & p3 & p4;

assign	SYNTHESIZED_WIRE_33 = p1 & p2 & p3 & p4;

assign	SYNTHESIZED_WIRE_37 = SYNTHESIZED_WIRE_33 & g0;

assign	SYNTHESIZED_WIRE_38 = p2 & p0 & p1 & p3 & p4 & cin;

assign	SYNTHESIZED_WIRE_41 = g4 & p5;

assign	SYNTHESIZED_WIRE_17 = g4 | SYNTHESIZED_WIRE_34 | SYNTHESIZED_WIRE_35 | SYNTHESIZED_WIRE_36 | SYNTHESIZED_WIRE_37 | SYNTHESIZED_WIRE_38;

assign	SYNTHESIZED_WIRE_43 = p4 & p5 & g3;

assign	SYNTHESIZED_WIRE_42 = p3 & p4 & p5 & g2;

assign	SYNTHESIZED_WIRE_39 = p2 & p3 & p4 & p5;

assign	SYNTHESIZED_WIRE_44 = SYNTHESIZED_WIRE_39 & g1;

assign	SYNTHESIZED_WIRE_45 = p3 & p1 & p2 & p4 & p5 & g0;

assign	SYNTHESIZED_WIRE_40 = p2 & p0 & p1 & p3 & p4 & p5;

assign	SYNTHESIZED_WIRE_46 = SYNTHESIZED_WIRE_40 & cin;

assign	SYNTHESIZED_WIRE_47 = SYNTHESIZED_WIRE_41 | SYNTHESIZED_WIRE_42 | SYNTHESIZED_WIRE_43 | SYNTHESIZED_WIRE_44 | SYNTHESIZED_WIRE_45 | SYNTHESIZED_WIRE_46;

assign	SYNTHESIZED_WIRE_18 = SYNTHESIZED_WIRE_47 | g5;

assign	SYNTHESIZED_WIRE_52 = g5 & p6;

assign	SYNTHESIZED_WIRE_51 = p5 & p6 & g4;

assign	SYNTHESIZED_WIRE_53 = p4 & p5 & p6 & g3;

assign	SYNTHESIZED_WIRE_48 = p3 & p4 & p5 & p6;

assign	SYNTHESIZED_WIRE_55 = SYNTHESIZED_WIRE_48 & g2;

assign	SYNTHESIZED_WIRE_54 = p4 & p2 & p3 & p5 & p6 & g1;

assign	SYNTHESIZED_WIRE_49 = p3 & p1 & p2 & p4 & p5 & p6;

assign	SYNTHESIZED_WIRE_56 = SYNTHESIZED_WIRE_49 & g0;

assign	SYNTHESIZED_WIRE_57 = p0 & p2 & p1 & p3 & p6 & p5 & cin & p4;

assign	SYNTHESIZED_WIRE_19 = SYNTHESIZED_WIRE_68 | SYNTHESIZED_WIRE_51 | SYNTHESIZED_WIRE_52 | SYNTHESIZED_WIRE_53 | SYNTHESIZED_WIRE_54 | SYNTHESIZED_WIRE_55 | SYNTHESIZED_WIRE_56 | SYNTHESIZED_WIRE_57;

assign	SYNTHESIZED_WIRE_3 = SYNTHESIZED_WIRE_67 & SYNTHESIZED_WIRE_68;

assign	SYNTHESIZED_WIRE_5 = p6 & SYNTHESIZED_WIRE_67 & g5;

assign	SYNTHESIZED_WIRE_4 = p5 & p6 & SYNTHESIZED_WIRE_67 & g4;

assign	SYNTHESIZED_WIRE_63 = p4 & p5 & p6 & SYNTHESIZED_WIRE_67;

assign	SYNTHESIZED_WIRE_6 = SYNTHESIZED_WIRE_63 & g3;

assign	SYNTHESIZED_WIRE_8 = p5 & p3 & p4 & p6 & SYNTHESIZED_WIRE_67 & g2;

assign	SYNTHESIZED_WIRE_66 = p4 & p2 & p3 & p5 & p6 & SYNTHESIZED_WIRE_67;

assign	SYNTHESIZED_WIRE_7 = SYNTHESIZED_WIRE_66 & g1;

assign	cin = c_in;

endmodule
