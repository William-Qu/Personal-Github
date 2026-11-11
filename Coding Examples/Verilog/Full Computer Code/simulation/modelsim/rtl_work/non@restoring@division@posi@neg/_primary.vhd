library verilog;
use verilog.vl_types.all;
entity nonRestoringDivisionPosiNeg is
    port(
        dividend        : in     vl_logic_vector(31 downto 0);
        divisor         : in     vl_logic_vector(31 downto 0);
        quotient        : out    vl_logic_vector(31 downto 0);
        remainder       : out    vl_logic_vector(31 downto 0)
    );
end nonRestoringDivisionPosiNeg;
