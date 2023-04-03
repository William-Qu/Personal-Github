library verilog;
use verilog.vl_types.all;
entity Memory is
    port(
        clr             : in     vl_logic;
        clk             : in     vl_logic;
        write           : in     vl_logic;
        dataIn          : in     vl_logic_vector(31 downto 0);
        Addr            : in     vl_logic_vector(8 downto 0);
        dataOut         : out    vl_logic_vector(31 downto 0)
    );
end Memory;
