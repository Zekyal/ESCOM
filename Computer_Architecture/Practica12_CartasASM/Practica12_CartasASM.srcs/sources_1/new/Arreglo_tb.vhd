LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
 
entity Arreglo_tb is
end Arreglo_tb;

Architecture Behavioral of Arreglo_tb is 
 
    component Arreglo is
        Port ( EA, LA, clk, clr : in  STD_LOGIC;
               DA : in  STD_LOGIC_VECTOR (8 downto 0);
               QA : out  STD_LOGIC_VECTOR (8 downto 0));
    end component;     

    --Inputs
	signal clk : STD_LOGIC := '0';
	signal clr : STD_LOGIC := '0';
    signal EA : STD_LOGIC := '0';
    signal LA : STD_LOGIC := '0';
    signal DA : STD_LOGIC_VECTOR (8 downto 0) := (others => '1');

 	--Outputs
    signal QA : STD_LOGIC_VECTOR(8 downto 0);

    -- Clock period definitions
    constant CLK_period : time := 10 ns;
 
begin
	-- Instantiate the Unit Under Test (UUT)
    uut: Arreglo 
        Port Map ( clk => clk,
                   clr => clr,
                   EA => EA,
                   LA => LA,   
                   DA => DA,
                   QA => QA);

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
        LA <= '1';
        wait for 10 ns;	
		LA <= '0';
        wait for 10 ns;
		clr <= '1';
        wait for 10 ns;	
		clr <= '0';
        wait for 10 ns;
        LA <= '1';
        wait for 10 ns;	
		LA <= '0';
        wait for 10 ns;
		EA <= '1';
        wait for 30 ns;	
		EA <= '0';
        wait for 10 ns;
		EA <= '1';
        wait for 30 ns;
		EA <= '0';
        wait for 10 ns;
        wait;
   end process;
end Behavioral;