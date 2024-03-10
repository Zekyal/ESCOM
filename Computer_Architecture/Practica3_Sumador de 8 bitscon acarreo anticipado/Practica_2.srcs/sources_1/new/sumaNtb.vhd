library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity sumaNtb is
--  Port ( );
end sumaNtb;

architecture Behavioral of sumaNtb is

component Practica_2 is
    Port ( a, b : in STD_LOGIC_VECTOR (7 downto 0);
           cin : in STD_LOGIC;
           cout : out STD_LOGIC;
           s : out STD_LOGIC_VECTOR (7 downto 0));
end component;

signal a : STD_LOGIC_VECTOR (7 downto 0) := (others => '0');
signal b : STD_LOGIC_VECTOR (7 downto 0) := (others => '0');
signal cin : STD_LOGIC := '0';
signal s : STD_LOGIC_VECTOR (7 downto 0);
signal cout : STD_LOGIC;

begin

    sumador: Practica_2 Port map(
        a => a,
        b => b,
        cin => cin,
        s => s,
        cout => cout
        );
        
    p1: process
        begin----------- 5+5
        a <= "00000101";
		b <= "00000101";
		cin <= '0';
        wait for 100 ns;--- 12+7
		a <= "00001100";
		b <= "00000111";
        wait for 100 ns;--- 9+5
		a <= "00001001";
		b <= "00000101";
        wait for 100 ns;--- 14+9
		a <= "00001110";
		b <= "00001001";
        wait for 100 ns;--- 4+2
		a <= "00000100";
		b <= "00000010";
        wait for 100 ns;--- 7+7
		a <= "00000111";
		b <= "00000111";
		wait for 100 ns;--- 15+5
		a <= "00001111";
		b <= "00000101";
		wait for 100 ns;--- 11+8
		a <= "00001011";
		b <= "00001000";
		wait for 100 ns;--- 1+4
		a <= "00000001";
		b <= "00000100";
		wait for 100 ns;
        wait;
   end process;

end Behavioral;
