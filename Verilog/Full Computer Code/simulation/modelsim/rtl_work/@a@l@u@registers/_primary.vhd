library verilog;
use verilog.vl_types.all;
entity ALURegisters is
    port(
        clr             : in     vl_logic;
        clk             : in     vl_logic;
        r0outf          : out    vl_logic_vector(31 downto 0);
        r1outf          : out    vl_logic_vector(31 downto 0);
        r2outf          : out    vl_logic_vector(31 downto 0);
        r3outf          : out    vl_logic_vector(31 downto 0);
        r4outf          : out    vl_logic_vector(31 downto 0);
        r5outf          : out    vl_logic_vector(31 downto 0);
        r6outf          : out    vl_logic_vector(31 downto 0);
        r7outf          : out    vl_logic_vector(31 downto 0);
        r8outf          : out    vl_logic_vector(31 downto 0);
        r9outf          : out    vl_logic_vector(31 downto 0);
        r10outf         : out    vl_logic_vector(31 downto 0);
        r11outf         : out    vl_logic_vector(31 downto 0);
        r12outf         : out    vl_logic_vector(31 downto 0);
        r13outf         : out    vl_logic_vector(31 downto 0);
        r14outf         : out    vl_logic_vector(31 downto 0);
        r15outf         : out    vl_logic_vector(31 downto 0);
        r0ins           : in     vl_logic;
        r1ins           : in     vl_logic;
        r2ins           : in     vl_logic;
        r3ins           : in     vl_logic;
        r4ins           : in     vl_logic;
        r5ins           : in     vl_logic;
        r6ins           : in     vl_logic;
        r7ins           : in     vl_logic;
        r8ins           : in     vl_logic;
        r9ins           : in     vl_logic;
        r10ins          : in     vl_logic;
        r11ins          : in     vl_logic;
        r12ins          : in     vl_logic;
        r13ins          : in     vl_logic;
        r14ins          : in     vl_logic;
        r15ins          : in     vl_logic;
        BusMuxOut       : in     vl_logic_vector(31 downto 0)
    );
end ALURegisters;