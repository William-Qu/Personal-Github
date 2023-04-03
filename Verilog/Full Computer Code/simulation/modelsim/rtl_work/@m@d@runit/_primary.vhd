library verilog;
use verilog.vl_types.all;
entity MDRunit is
    port(
        read            : in     vl_logic;
        clr             : in     vl_logic;
        clk             : in     vl_logic;
        wren            : in     vl_logic;
        BusMuxOut       : in     vl_logic_vector(31 downto 0);
        Mdatain         : in     vl_logic_vector(31 downto 0);
        MDRout          : out    vl_logic_vector(31 downto 0)
    );
end MDRunit;
