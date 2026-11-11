library verilog;
use verilog.vl_types.all;
entity ControlUnitBus is
    generic(
        ResetState      : vl_logic_vector(0 to 2) := (Hi0, Hi0, Hi0);
        T0              : vl_logic_vector(0 to 2) := (Hi0, Hi0, Hi1);
        T1              : vl_logic_vector(0 to 2) := (Hi0, Hi1, Hi0);
        T2              : vl_logic_vector(0 to 2) := (Hi0, Hi1, Hi1);
        T3              : vl_logic_vector(0 to 2) := (Hi1, Hi0, Hi0);
        T4              : vl_logic_vector(0 to 2) := (Hi1, Hi0, Hi1);
        T5              : vl_logic_vector(0 to 2) := (Hi1, Hi1, Hi0);
        TempState       : vl_logic_vector(0 to 2) := (Hi1, Hi1, Hi1)
    );
    port(
        clr             : in     vl_logic;
        clk             : in     vl_logic;
        Halt            : in     vl_logic;
        MDRMDataIn      : in     vl_logic_vector(31 downto 0);
        OutportOut      : out    vl_logic_vector(31 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of ResetState : constant is 1;
    attribute mti_svvh_generic_type of T0 : constant is 1;
    attribute mti_svvh_generic_type of T1 : constant is 1;
    attribute mti_svvh_generic_type of T2 : constant is 1;
    attribute mti_svvh_generic_type of T3 : constant is 1;
    attribute mti_svvh_generic_type of T4 : constant is 1;
    attribute mti_svvh_generic_type of T5 : constant is 1;
    attribute mti_svvh_generic_type of TempState : constant is 1;
end ControlUnitBus;
