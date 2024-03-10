LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
 
entity UnidadControl_tb is
end UnidadControl_tb;

Architecture Behavioral of UnidadControl_tb is 
 
    component UnidadControl is
        Port ( clk, clr, INI, z, A0 : in STD_LOGIC;
               LA, LB, EA, EB, EC : out STD_LOGIC);
    end component;    

    --Inputs
    signal clk : STD_LOGIC := '0';
    signal clr : STD_LOGIC := '0';
    signal INI : STD_LOGIC := '0';
    signal A0 : STD_LOGIC := '0';
    signal z : STD_LOGIC := '0';

 	--Outputs
    signal LA : STD_LOGIC;
    signal LB : STD_LOGIC;
    signal EA : STD_LOGIC;
    signal EB : STD_LOGIC;
    signal EC : STD_LOGIC;

    -- Clock period definitions
    constant CLK_period : time := 10 ns;
 
begin
    -- Instantiate the Unit Under Test (UUT)
    uut: UnidadControl 
        Port Map ( clk => clk,
                   clr => clr,
                   INI => INI,
                   A0 => A0,
                   z => z,
                   LB => LB,
                   LA => LA,
                   EA => EA,
                   EB => EB,
                   EC => EC);

    -- Clock process definitions
    CLK_process :process
    begin
        clk <= '0';
        wait for CLK_period/2;
        clk <= '1';
		wait for CLK_period/2;
    end process;

    -- Stimulus process
    stim_proc: process
    begin		
        clr <= '1';
        wait for 30 ns;
		clr <= '0';
		wait for 10 ns;
		--estado 0 -> estado 1
		INI <= '1';
		A0 <= '1';
		z <= '0';
		wait for 50 ns;
		--estado 1 -> estado 2
		INI <= '1';
		A0 <= '0';
		z <= '1';
		wait for 50 ns;
		--estado 2 -> estado 0
		INI <= '0';
		wait for 50 ns;	
        wait;
   end process;
end Behavioral;