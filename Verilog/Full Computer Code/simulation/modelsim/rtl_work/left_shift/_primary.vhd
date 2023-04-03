library verilog;
use verilog.vl_types.all;
entity left_shift is
    port(
        clk             : in     vl_logic;
        clr             : in     vl_logic;
        D               : in     vl_logic_vector(31 downto 0);
        Q               : out    vl_logic_vector(31 downto 0)
    );
end left_shift;
