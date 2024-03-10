library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Carta_ASM_tb is
end Carta_ASM_tb;
 
architecture Behavioral of Carta_ASM_tb is 
 
component Carta_ASM is
    Port ( TIPOR, BEQ, BNEQ, BLT, BLE, BGT, BGET, NA : in STD_LOGIC;
           EQ, NEQ, LT, LE, GTI, GET : in STD_LOGIC;
           clk, clr : in STD_LOGIC;
           SDOPC, SM : out STD_LOGIC);
end component;
    
--Inputs
signal TIPOR : STD_LOGIC := '0';
signal BEQ : STD_LOGIC := '0';
signal BNEQ : STD_LOGIC := '0';
signal BLT : STD_LOGIC := '0';
signal BLE : STD_LOGIC := '0';
signal BGT : STD_LOGIC := '0';
signal BGET : STD_LOGIC := '0';
signal NA : STD_LOGIC := '0';
signal EQ : STD_LOGIC := '0';
signal NEQ : STD_LOGIC := '0';
signal LT : STD_LOGIC := '0';
signal LE : STD_LOGIC := '0';
signal GTI : STD_LOGIC := '0';
signal GET : STD_LOGIC := '0';
signal clk : STD_LOGIC := '0';
signal clr : STD_LOGIC := '0';

--Outputs
signal SDOPC : STD_LOGIC;
signal SM : STD_LOGIC;

-- Clock period definitions
constant CLK_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
    uut: Carta_ASM 
        Port Map ( TIPOR => TIPOR,
                   BEQ => BEQ,
                   BNEQ => BNEQ,
                   BLT => BLT,   
                   BLE => BLE,
                   BGT => BGT,
                   BGET => BGET,
                   NA => NA,
                   EQ => EQ,
                   NEQ => NEQ,
                   LT => LT,
                   LE => LE,
                   GTI => GTI,
                   GET => GET,
                   clk => clk,
                   clr => clr,
                   SDOPC => SDOPC,
                   SM => SM);

    -- Clock process definitions
    CLK_process :process
    begin
        clk <= '0';
		wait for CLK_period/2;
		clk <= '1';
		wait for CLK_period/2;
    end process;
	
    stim_proc: process
    begin	
        clr <= '1';
		wait for 20 ns;
		clr <= '0';
		BEQ <= '1';
		EQ <= '1';
        wait for CLK_period*5;
        wait;
    end process;
end Behavioral;