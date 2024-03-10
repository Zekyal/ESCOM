LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
 
entity Contador_tb is
end Contador_tb;

Architecture Behavioral of Contador_tb is 

    component Contador is
        Port ( clk, clr, LB, EB : in STD_LOGIC;
               QB : out STD_LOGIC_VECTOR (3 downto 0));
    end component;      

    --Inputs
    signal clk : STD_LOGIC := '0';
    signal clr : STD_LOGIC := '0';
    signal LB : STD_LOGIC := '0';
    signal EB : STD_LOGIC := '0';

 	--Outputs
    signal QB : STD_LOGIC_VECTOR(3 downto 0);

    -- Clock period definitions
    constant CLK_period : time := 10 ns;
 
begin
	-- Instantiate the Unit Under Test (UUT)
    uut: Contador 
        Port Map ( clk => clk,
                   clr => clr,
                   LB => LB,
                   EB => EB,
                   QB => QB);

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
		wait for 30 ns;
		LB <= '0';
		EB <= '1';
        wait for 100 ns;
		EB <= '1';
		wait for 100 ns;
		EB <= '0';
		LB <= '1';
		wait for 100 ns;
		clr <= '1';
		wait for 30 ns;
		clr <= '0';
        wait;
   end process;
end Behavioral;
