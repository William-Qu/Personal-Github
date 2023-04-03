library verilog;
use verilog.vl_types.all;
entity boothMultiplier is
    port(
        multiplier      : in     vl_logic_vector(31 downto 0);
        multiplicand    : in     vl_logic_vector(31 downto 0);
        ansHI           : out    vl_logic_vector(31 downto 0);
        ansLO           : out    vl_logic_vector(31 downto 0)
    );
end boothMultiplier;
