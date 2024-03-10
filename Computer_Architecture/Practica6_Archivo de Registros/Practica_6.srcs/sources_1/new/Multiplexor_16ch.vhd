library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Multiplexor_16ch is
		 Port(r0: in std_logic_vector(15 downto 0);
			  r1: in std_logic_vector(15 downto 0);
			  r2: in std_logic_vector(15 downto 0);
			  r3: in std_logic_vector(15 downto 0);
			  r4: in std_logic_vector(15 downto 0);
			  r5: in std_logic_vector(15 downto 0);
			  r6: in std_logic_vector(15 downto 0);
			  r7: in std_logic_vector(15 downto 0);
			  r8: in std_logic_vector(15 downto 0);
			  r9: in std_logic_vector(15 downto 0);
			  r10: in std_logic_vector(15 downto 0);
			  r11: in std_logic_vector(15 downto 0);
			  r12: in std_logic_vector(15 downto 0);
			  r13: in std_logic_vector(15 downto 0);
			  r14: in std_logic_vector(15 downto 0);
			  r15: in std_logic_vector(15 downto 0);
			  readReg : in  STD_LOGIC_VECTOR (3 downto 0);
			  readData : out  STD_LOGIC_VECTOR (15 downto 0));
end Multiplexor_16ch;

architecture Behavioral of Multiplexor_16ch is
begin
    readData <= r0 when readReg = "0000" else
				r1 when readReg = "0001" else
				r2 when readReg = "0010" else
				r3 when readReg = "0011" else
				r4 when readReg = "0100" else
				r5 when readReg = "0101" else
				r6 when readReg = "0110" else
				r7 when readReg = "0111" else
				r8 when readReg = "1000" else
				r9 when readReg = "1001" else
				r10 when readReg = "1010" else
				r11 when readReg = "1011" else
				r12 when readReg = "1100" else
				r13 when readReg = "1101" else
				r14 when readReg = "1110" else
				r15;
end Behavioral;
