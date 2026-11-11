library verilog;
use verilog.vl_types.all;
entity ALU is
    port(
        regA            : in     vl_logic_vector(31 downto 0);
        regB            : in     vl_logic_vector(31 downto 0);
        OPCode          : in     vl_logic_vector(4 downto 0);
        regZ            : out    vl_logic_vector(63 downto 0)
    );
end ALU;
