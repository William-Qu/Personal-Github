library verilog;
use verilog.vl_types.all;
entity dff_Q is
    port(
        D               : in     vl_logic;
        clk             : in     vl_logic;
        clr             : in     vl_logic;
        Q               : out    vl_logic
    );
end dff_Q;
