library verilog;
use verilog.vl_types.all;
entity P_G_block is
    port(
        xi              : in     vl_logic;
        yi              : in     vl_logic;
        Gi              : out    vl_logic;
        Pi              : out    vl_logic
    );
end P_G_block;
