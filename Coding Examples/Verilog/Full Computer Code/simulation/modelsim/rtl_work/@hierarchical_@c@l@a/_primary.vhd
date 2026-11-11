library verilog;
use verilog.vl_types.all;
entity Hierarchical_CLA is
    port(
        \Select\        : in     vl_logic;
        x               : in     vl_logic_vector(31 downto 0);
        y               : in     vl_logic_vector(31 downto 0);
        C_out           : out    vl_logic;
        S               : out    vl_logic_vector(31 downto 0)
    );
end Hierarchical_CLA;
