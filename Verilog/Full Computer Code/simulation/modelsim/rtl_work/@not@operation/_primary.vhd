library verilog;
use verilog.vl_types.all;
entity NotOperation is
    port(
        d               : in     vl_logic_vector(31 downto 0);
        q               : out    vl_logic_vector(31 downto 0)
    );
end NotOperation;
