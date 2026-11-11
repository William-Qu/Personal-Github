library verilog;
use verilog.vl_types.all;
entity CLA_8inputs_updated is
    port(
        x0              : in     vl_logic;
        y0              : in     vl_logic;
        x1              : in     vl_logic;
        y1              : in     vl_logic;
        x2              : in     vl_logic;
        y2              : in     vl_logic;
        y3              : in     vl_logic;
        x3              : in     vl_logic;
        x4              : in     vl_logic;
        y4              : in     vl_logic;
        x5              : in     vl_logic;
        y5              : in     vl_logic;
        y6              : in     vl_logic;
        x6              : in     vl_logic;
        x7              : in     vl_logic;
        y7              : in     vl_logic;
        c_in            : in     vl_logic;
        c_out           : out    vl_logic;
        S7              : out    vl_logic;
        S6              : out    vl_logic;
        S5              : out    vl_logic;
        S4              : out    vl_logic;
        S3              : out    vl_logic;
        S2              : out    vl_logic;
        S1              : out    vl_logic;
        S0              : out    vl_logic
    );
end CLA_8inputs_updated;
