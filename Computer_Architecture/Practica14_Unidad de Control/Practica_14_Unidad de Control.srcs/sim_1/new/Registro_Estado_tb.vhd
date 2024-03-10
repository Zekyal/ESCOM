library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Registro_Estado_tb is
end Registro_Estado_tb;

architecture Behavioral of Registro_Estado_tb is

component Registro_Estado is
    Port ( clk, clr, LF : in  STD_LOGIC;
           banderas : in  STD_LOGIC_VECTOR (3 downto 0);
           Q : out  STD_LOGIC_VECTOR (3 downto 0));
end component;

--Inputs
signal clk : STD_LOGIC := '0';
signal clr : STD_LOGIC := '0';
signal LF : STD_LOGIC := '0';
signal banderas : STD_LOGIC_VECTOR(3 downto 0) := (others => '0');

--Outputs
signal Q : STD_LOGIC_VECTOR(3 downto 0);

-- Clock period definitions
constant CLK_period : time := 10 ns;

begin
    -- Instantiate the Unit Under Test (UUT)
    uut: Registro_Estado
        Port Map ( clk => clk,
                   clr => clr,
                   LF => LF,
                   banderas => banderas,
                   Q => Q);
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
		wait for 20 ns;
		clr <= '0';	
		banderas <= "0110";
		LF <= '1';
        wait for 50 ns;	
		banderas <= "1010";
		LF <= '0';
        wait for 50 ns;	
		LF <= '1';
        wait for 50 ns;
		banderas <= "1001";
		LF <= '0';
        wait for 50 ns;	
		LF <= '1';
        wait for 50 ns;	
        wait;
    end process;
end Behavioral;