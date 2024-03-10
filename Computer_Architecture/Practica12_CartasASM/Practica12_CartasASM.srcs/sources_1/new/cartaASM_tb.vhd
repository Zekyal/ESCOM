LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
 
entity cartaASM_tb is
end cartaASM_tb;

Architecture Behavioral of cartaASM_tb is 

    component cartaASM is
        Port ( INI, clk, clr : in  STD_LOGIC;
		       D : in  STD_LOGIC_VECTOR (8 downto 0);
		       A : out STD_LOGIC_VECTOR (8 downto 0);
		       B : out STD_LOGIC_VECTOR (6 downto 0));
    end component;   
    
    --Inputs
    signal clk : STD_LOGIC := '0';
    signal clr : STD_LOGIC := '0';
    signal INI : STD_LOGIC := '0';
	signal D : STD_LOGIC_VECTOR(8 downto 0) := (others => '0');

 	--Outputs
    signal A : STD_LOGIC_VECTOR(8 downto 0);
    signal B : STD_LOGIC_VECTOR(6 downto 0);

    -- Clock period definitions
    constant CLK_period : time := 10 ns;
 
begin
    -- Instantiate the Unit Under Test (UUT)
    uut: cartaASM 
        Port Map ( clk => clk,
                   clr => clr,
                   INI => INI,
                   D => D,
                   A => A,
                   B => B);

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
		wait for 10 ns;
		clr <= '0';
		d <= "101101011";-- inciso a
		wait for 50 ns;
		ini <= '1';
		wait for 150 ns;
		ini <= '0';
		d <= "000011101";--inciso b
		wait for 50 ns;
		ini <= '1';
		wait for 150 ns;
		ini <= '0';
		d <= "000010000";--inciso c
		wait for 50 ns;
		ini <= '1';
		wait for 150 ns;
		ini <= '0';
		d <= "100001000";--inciso d
		wait for 50 ns;
		ini <= '1';
		wait for 150 ns;
		ini <= '0';
		d <= "000000000";--inciso e
		wait for 50 ns;
        wait;
   end process;
end Behavioral;