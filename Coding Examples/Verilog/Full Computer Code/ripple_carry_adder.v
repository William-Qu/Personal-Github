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
// CREATED		"Sun Feb 26 14:58:58 2023"

module ripple_carry_adder(
	subtract,
	Cin,
	x,
	y,
	Cout,
	s
);


input wire	subtract;
input wire	Cin;
input wire	[31:0] x;
input wire	[31:0] y;
output wire	Cout;
output wire	[31:0] s;

wire	[31:0] s_ALTERA_SYNTHESIZED;
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
wire	SYNTHESIZED_WIRE_50;
wire	SYNTHESIZED_WIRE_51;
wire	SYNTHESIZED_WIRE_52;
wire	SYNTHESIZED_WIRE_53;
wire	SYNTHESIZED_WIRE_54;
wire	SYNTHESIZED_WIRE_55;
wire	SYNTHESIZED_WIRE_56;
wire	SYNTHESIZED_WIRE_57;
wire	SYNTHESIZED_WIRE_58;
wire	SYNTHESIZED_WIRE_59;
wire	SYNTHESIZED_WIRE_60;
wire	SYNTHESIZED_WIRE_61;
wire	SYNTHESIZED_WIRE_62;
wire	SYNTHESIZED_WIRE_63;
wire	SYNTHESIZED_WIRE_64;





full_adder	b2v_inst(
	.c_in(SYNTHESIZED_WIRE_0),
	.xi(x[31]),
	.yi(SYNTHESIZED_WIRE_1),
	.si(s_ALTERA_SYNTHESIZED[31]),
	.c_out(SYNTHESIZED_WIRE_56));


full_adder	b2v_inst1(
	.c_in(SYNTHESIZED_WIRE_2),
	.xi(x[30]),
	.yi(SYNTHESIZED_WIRE_3),
	.si(s_ALTERA_SYNTHESIZED[30]),
	.c_out(SYNTHESIZED_WIRE_0));


full_adder	b2v_inst10(
	.c_in(SYNTHESIZED_WIRE_4),
	.xi(x[21]),
	.yi(SYNTHESIZED_WIRE_5),
	.si(s_ALTERA_SYNTHESIZED[21]),
	.c_out(SYNTHESIZED_WIRE_63));


full_adder	b2v_inst11(
	.c_in(SYNTHESIZED_WIRE_6),
	.xi(x[20]),
	.yi(SYNTHESIZED_WIRE_7),
	.si(s_ALTERA_SYNTHESIZED[20]),
	.c_out(SYNTHESIZED_WIRE_4));


full_adder	b2v_inst12(
	.c_in(SYNTHESIZED_WIRE_8),
	.xi(x[19]),
	.yi(SYNTHESIZED_WIRE_9),
	.si(s_ALTERA_SYNTHESIZED[19]),
	.c_out(SYNTHESIZED_WIRE_6));


full_adder	b2v_inst13(
	.c_in(SYNTHESIZED_WIRE_10),
	.xi(x[18]),
	.yi(SYNTHESIZED_WIRE_11),
	.si(s_ALTERA_SYNTHESIZED[18]),
	.c_out(SYNTHESIZED_WIRE_8));


full_adder	b2v_inst14(
	.c_in(SYNTHESIZED_WIRE_12),
	.xi(x[17]),
	.yi(SYNTHESIZED_WIRE_13),
	.si(s_ALTERA_SYNTHESIZED[17]),
	.c_out(SYNTHESIZED_WIRE_10));


full_adder	b2v_inst15(
	.c_in(SYNTHESIZED_WIRE_14),
	.xi(x[16]),
	.yi(SYNTHESIZED_WIRE_15),
	.si(s_ALTERA_SYNTHESIZED[16]),
	.c_out(SYNTHESIZED_WIRE_12));


full_adder	b2v_inst16(
	.c_in(SYNTHESIZED_WIRE_16),
	.xi(x[15]),
	.yi(SYNTHESIZED_WIRE_17),
	.si(s_ALTERA_SYNTHESIZED[15]),
	.c_out(SYNTHESIZED_WIRE_14));


full_adder	b2v_inst17(
	.c_in(SYNTHESIZED_WIRE_18),
	.xi(x[14]),
	.yi(SYNTHESIZED_WIRE_19),
	.si(s_ALTERA_SYNTHESIZED[14]),
	.c_out(SYNTHESIZED_WIRE_16));


full_adder	b2v_inst18(
	.c_in(SYNTHESIZED_WIRE_20),
	.xi(x[13]),
	.yi(SYNTHESIZED_WIRE_21),
	.si(s_ALTERA_SYNTHESIZED[13]),
	.c_out(SYNTHESIZED_WIRE_18));


full_adder	b2v_inst19(
	.c_in(SYNTHESIZED_WIRE_22),
	.xi(x[12]),
	.yi(SYNTHESIZED_WIRE_23),
	.si(s_ALTERA_SYNTHESIZED[12]),
	.c_out(SYNTHESIZED_WIRE_20));


full_adder	b2v_inst2(
	.c_in(SYNTHESIZED_WIRE_24),
	.xi(x[29]),
	.yi(SYNTHESIZED_WIRE_25),
	.si(s_ALTERA_SYNTHESIZED[29]),
	.c_out(SYNTHESIZED_WIRE_2));


full_adder	b2v_inst20(
	.c_in(SYNTHESIZED_WIRE_26),
	.xi(x[11]),
	.yi(SYNTHESIZED_WIRE_27),
	.si(s_ALTERA_SYNTHESIZED[11]),
	.c_out(SYNTHESIZED_WIRE_22));


full_adder	b2v_inst21(
	.c_in(SYNTHESIZED_WIRE_28),
	.xi(x[10]),
	.yi(SYNTHESIZED_WIRE_29),
	.si(s_ALTERA_SYNTHESIZED[10]),
	.c_out(SYNTHESIZED_WIRE_26));


full_adder	b2v_inst22(
	.c_in(SYNTHESIZED_WIRE_30),
	.xi(x[9]),
	.yi(SYNTHESIZED_WIRE_31),
	.si(s_ALTERA_SYNTHESIZED[9]),
	.c_out(SYNTHESIZED_WIRE_28));


full_adder	b2v_inst23(
	.c_in(SYNTHESIZED_WIRE_32),
	.xi(x[8]),
	.yi(SYNTHESIZED_WIRE_33),
	.si(s_ALTERA_SYNTHESIZED[8]),
	.c_out(SYNTHESIZED_WIRE_30));


full_adder	b2v_inst24(
	.c_in(SYNTHESIZED_WIRE_34),
	.xi(x[7]),
	.yi(SYNTHESIZED_WIRE_35),
	.si(s_ALTERA_SYNTHESIZED[7]),
	.c_out(SYNTHESIZED_WIRE_32));


full_adder	b2v_inst25(
	.c_in(SYNTHESIZED_WIRE_36),
	.xi(x[6]),
	.yi(SYNTHESIZED_WIRE_37),
	.si(s_ALTERA_SYNTHESIZED[6]),
	.c_out(SYNTHESIZED_WIRE_34));


full_adder	b2v_inst26(
	.c_in(SYNTHESIZED_WIRE_38),
	.xi(x[5]),
	.yi(SYNTHESIZED_WIRE_39),
	.si(s_ALTERA_SYNTHESIZED[5]),
	.c_out(SYNTHESIZED_WIRE_36));


full_adder	b2v_inst27(
	.c_in(SYNTHESIZED_WIRE_40),
	.xi(x[4]),
	.yi(SYNTHESIZED_WIRE_41),
	.si(s_ALTERA_SYNTHESIZED[4]),
	.c_out(SYNTHESIZED_WIRE_38));


full_adder	b2v_inst28(
	.c_in(SYNTHESIZED_WIRE_42),
	.xi(x[3]),
	.yi(SYNTHESIZED_WIRE_43),
	.si(s_ALTERA_SYNTHESIZED[3]),
	.c_out(SYNTHESIZED_WIRE_40));


full_adder	b2v_inst29(
	.c_in(SYNTHESIZED_WIRE_44),
	.xi(x[2]),
	.yi(SYNTHESIZED_WIRE_45),
	.si(s_ALTERA_SYNTHESIZED[2]),
	.c_out(SYNTHESIZED_WIRE_42));


full_adder	b2v_inst3(
	.c_in(SYNTHESIZED_WIRE_46),
	.xi(x[28]),
	.yi(SYNTHESIZED_WIRE_47),
	.si(s_ALTERA_SYNTHESIZED[28]),
	.c_out(SYNTHESIZED_WIRE_24));


full_adder	b2v_inst30(
	.c_in(SYNTHESIZED_WIRE_48),
	.xi(x[1]),
	.yi(SYNTHESIZED_WIRE_49),
	.si(s_ALTERA_SYNTHESIZED[1]),
	.c_out(SYNTHESIZED_WIRE_44));


full_adder	b2v_inst31(
	.c_in(SYNTHESIZED_WIRE_50),
	.xi(x[0]),
	.yi(SYNTHESIZED_WIRE_51),
	.si(s_ALTERA_SYNTHESIZED[0]),
	.c_out(SYNTHESIZED_WIRE_48));

assign	SYNTHESIZED_WIRE_1 = y[31] ^ subtract;

assign	SYNTHESIZED_WIRE_3 = y[30] ^ subtract;

assign	SYNTHESIZED_WIRE_25 = y[29] ^ subtract;

assign	SYNTHESIZED_WIRE_47 = y[28] ^ subtract;

assign	SYNTHESIZED_WIRE_53 = y[27] ^ subtract;

assign	SYNTHESIZED_WIRE_55 = y[26] ^ subtract;

assign	SYNTHESIZED_WIRE_58 = y[25] ^ subtract;


full_adder	b2v_inst4(
	.c_in(SYNTHESIZED_WIRE_52),
	.xi(x[27]),
	.yi(SYNTHESIZED_WIRE_53),
	.si(s_ALTERA_SYNTHESIZED[27]),
	.c_out(SYNTHESIZED_WIRE_46));

assign	SYNTHESIZED_WIRE_60 = y[24] ^ subtract;

assign	SYNTHESIZED_WIRE_62 = y[23] ^ subtract;

assign	SYNTHESIZED_WIRE_64 = y[22] ^ subtract;

assign	SYNTHESIZED_WIRE_5 = y[21] ^ subtract;

assign	SYNTHESIZED_WIRE_7 = y[20] ^ subtract;

assign	SYNTHESIZED_WIRE_9 = y[19] ^ subtract;

assign	SYNTHESIZED_WIRE_11 = y[18] ^ subtract;

assign	SYNTHESIZED_WIRE_13 = y[17] ^ subtract;

assign	SYNTHESIZED_WIRE_15 = y[16] ^ subtract;

assign	SYNTHESIZED_WIRE_17 = y[15] ^ subtract;


full_adder	b2v_inst5(
	.c_in(SYNTHESIZED_WIRE_54),
	.xi(x[26]),
	.yi(SYNTHESIZED_WIRE_55),
	.si(s_ALTERA_SYNTHESIZED[26]),
	.c_out(SYNTHESIZED_WIRE_52));

assign	SYNTHESIZED_WIRE_19 = y[14] ^ subtract;

assign	SYNTHESIZED_WIRE_21 = y[13] ^ subtract;

assign	Cout = subtract ^ SYNTHESIZED_WIRE_56;

assign	SYNTHESIZED_WIRE_27 = y[11] ^ subtract;

assign	SYNTHESIZED_WIRE_29 = y[10] ^ subtract;

assign	SYNTHESIZED_WIRE_31 = y[9] ^ subtract;

assign	SYNTHESIZED_WIRE_33 = y[8] ^ subtract;

assign	SYNTHESIZED_WIRE_35 = y[7] ^ subtract;

assign	SYNTHESIZED_WIRE_37 = y[6] ^ subtract;

assign	SYNTHESIZED_WIRE_39 = y[5] ^ subtract;


full_adder	b2v_inst6(
	.c_in(SYNTHESIZED_WIRE_57),
	.xi(x[25]),
	.yi(SYNTHESIZED_WIRE_58),
	.si(s_ALTERA_SYNTHESIZED[25]),
	.c_out(SYNTHESIZED_WIRE_54));

assign	SYNTHESIZED_WIRE_41 = y[4] ^ subtract;

assign	SYNTHESIZED_WIRE_43 = y[3] ^ subtract;

assign	SYNTHESIZED_WIRE_45 = y[2] ^ subtract;

assign	SYNTHESIZED_WIRE_49 = y[1] ^ subtract;

assign	SYNTHESIZED_WIRE_51 = y[0] ^ subtract;

assign	SYNTHESIZED_WIRE_23 = y[12] ^ subtract;

assign	SYNTHESIZED_WIRE_50 = subtract ^ Cin;


full_adder	b2v_inst7(
	.c_in(SYNTHESIZED_WIRE_59),
	.xi(x[24]),
	.yi(SYNTHESIZED_WIRE_60),
	.si(s_ALTERA_SYNTHESIZED[24]),
	.c_out(SYNTHESIZED_WIRE_57));


full_adder	b2v_inst8(
	.c_in(SYNTHESIZED_WIRE_61),
	.xi(x[23]),
	.yi(SYNTHESIZED_WIRE_62),
	.si(s_ALTERA_SYNTHESIZED[23]),
	.c_out(SYNTHESIZED_WIRE_59));


full_adder	b2v_inst9(
	.c_in(SYNTHESIZED_WIRE_63),
	.xi(x[22]),
	.yi(SYNTHESIZED_WIRE_64),
	.si(s_ALTERA_SYNTHESIZED[22]),
	.c_out(SYNTHESIZED_WIRE_61));

assign	s = s_ALTERA_SYNTHESIZED;

endmodule
