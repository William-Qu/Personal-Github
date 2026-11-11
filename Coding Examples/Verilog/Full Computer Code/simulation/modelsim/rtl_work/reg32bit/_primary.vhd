library verilog;
use verilog.vl_types.all;
entity reg32bit is
    port(
        q               : out    vl_logic_vector(31 downto 0);
        d               : in     vl_logic_vector(31 downto 0);
        clr             : in     vl_logic;
        clk             : in     vl_logic;
        wren            : in     vl_logic
    );
end reg32bit;
