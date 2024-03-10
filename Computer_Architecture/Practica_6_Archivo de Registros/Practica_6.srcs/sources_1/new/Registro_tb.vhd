library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Registro_tb IS
end Registro_tb;
 
architecture Behaviour of Registro_tb is
    component Registro
    Port ( d : in STD_LOGIC_VECTOR (15 downto 0);
           q : out STD_LOGIC_VECTOR (15 downto 0);
           clr, clk, l : in STD_LOGIC);
    end component;
    
    signal d : std_logic_vector(15 downto 0) := (others => '0');
    signal l : std_logic := '0';
    signal clk : std_logic := '0';
    signal clr : std_logic := '0';
    signal q : std_logic_vector(15 downto 0);
    constant CLK_period : time := 10 ns;
 
    begin
        uut: registro Port Map (
            d => d,
            q => q,
            l => l,
            clk => clk,
            clr => clr
        );

    CLK_process :Process
    begin
		clk <= '0';
		wait for CLK_period/2;
		clk <= '1';
		wait for CLK_period/2;
    end process;
 
    stim_proc: process
    begin		
        wait for 30 ns;
        clr <= '1';
		wait for 40 ns;
		clr <= '0';
		d <= x"AB00";
		l <= '1';
		wait for 50 ns;
		l <= '0';
		d <= x"1234";
        wait;
    end process;
end Behaviour;
