library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Nivel_tb is
end Nivel_tb;

architecture Behavioral of Nivel_tb is

component Nivel is
    Port ( clk, clr : in  STD_LOGIC;
           NA : out  STD_LOGIC);
end component;

--Inputs
signal clk : STD_LOGIC := '0';
signal clr : STD_LOGIC := '0';

--Outputs
signal NA : STD_LOGIC;

-- Clock period definitions
constant clk_period : time := 10 ns;
 
begin
 
	-- Instantiate the Unit Under Test (UUT)
    uut: Nivel 
    Port Map ( clk => clk,
               clr => clr,
               NA => NA);

    -- Clock process definitions
    clk_process :process
    begin
        clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
    end process;

    -- Stimulus process
    stim_proc: process
    begin		
        wait for 20 ns;
		clr <= '1';
		wait for 20 ns;
		clr <= '0';
		wait for 40 ns;
		wait for 20 ns;
		clr <= '1';
		wait for 25 ns;
		clr <= '0';
		wait for 40 ns;
        wait;
   end process;

end Behavioral;
