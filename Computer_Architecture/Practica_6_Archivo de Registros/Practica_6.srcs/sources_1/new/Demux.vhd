library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Demux is
	Port(writeReg: in std_logic_vector(3 downto 0);
		 WR: in std_logic;
	   	 L: out std_logic_vector(15 downto 0));
end Demux;

architecture Behavioral of Demux is
begin
	L(0) <= WR when writeReg = "0000" else '0';
	L(1) <= WR when writeReg = "0001" else '0';
	L(2) <= WR when writeReg = "0010" else '0';
	L(3) <= WR when writeReg = "0011" else '0';
	L(4) <= WR when writeReg = "0100" else '0';
	L(5) <= WR when writeReg = "0101" else '0';
	L(6) <= WR when writeReg = "0110" else '0';
	L(7) <= WR when writeReg = "0111" else '0';
	L(8) <= WR when writeReg = "1000" else '0';
	L(9) <= WR when writeReg = "1001" else '0';
	L(10) <= WR when writeReg = "1010" else '0';
	L(11) <= WR when writeReg = "1011" else '0';
	L(12) <= WR when writeReg = "1100" else '0';
	L(13) <= WR when writeReg = "1101" else '0';
	L(14) <= WR when writeReg = "1110" else '0';
	L(15) <= WR when writeReg = "1111" else '0';
end Behavioral;
