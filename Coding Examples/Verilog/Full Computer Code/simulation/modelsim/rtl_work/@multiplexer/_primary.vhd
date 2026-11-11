library verilog;
use verilog.vl_types.all;
entity Multiplexer is
    port(
        r0out           : in     vl_logic_vector(31 downto 0);
        r1out           : in     vl_logic_vector(31 downto 0);
        r2out           : in     vl_logic_vector(31 downto 0);
        r3out           : in     vl_logic_vector(31 downto 0);
        r4out           : in     vl_logic_vector(31 downto 0);
        r5out           : in     vl_logic_vector(31 downto 0);
        r6out           : in     vl_logic_vector(31 downto 0);
        r7out           : in     vl_logic_vector(31 downto 0);
        r8out           : in     vl_logic_vector(31 downto 0);
        r9out           : in     vl_logic_vector(31 downto 0);
        r10out          : in     vl_logic_vector(31 downto 0);
        r11out          : in     vl_logic_vector(31 downto 0);
        r12out          : in     vl_logic_vector(31 downto 0);
        r13out          : in     vl_logic_vector(31 downto 0);
        r14out          : in     vl_logic_vector(31 downto 0);
        r15out          : in     vl_logic_vector(31 downto 0);
        RegHiOut        : in     vl_logic_vector(31 downto 0);
        RegLoOut        : in     vl_logic_vector(31 downto 0);
        ZHiOut          : in     vl_logic_vector(31 downto 0);
        ZLoOut          : in     vl_logic_vector(31 downto 0);
        PCOut           : in     vl_logic_vector(31 downto 0);
        MDROut          : in     vl_logic_vector(31 downto 0);
        RegInportOut    : in     vl_logic_vector(31 downto 0);
        CLoOut          : in     vl_logic_vector(31 downto 0);
        EnOut           : in     vl_logic_vector(4 downto 0);
        BusMuxOut       : out    vl_logic_vector(31 downto 0)
    );
end Multiplexer;
