library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ALU_tb is
--  Port ( );
end ALU_tb;

architecture Behavioral of ALU_tb is

component ALU_Nbits is
    Port ( a,b : in STD_LOGIC_VECTOR (3 downto 0);
           aluop : in STD_LOGIC_VECTOR (3 downto 0);--3 downto 0
           res : out STD_LOGIC_VECTOR (3 downto 0);
           bn, z, co, ov : out STD_LOGIC );
end component;

--Inputs
signal a, b : std_logic_vector(3 downto 0) := (others => '0');
signal sela : std_logic := '0';
signal selb : std_logic := '0';
signal op : std_logic_vector(1 downto 0) := (others => '0');

--Outputs
signal res : std_logic_vector(3 downto 0);
signal bn, z, co, ov : std_logic;
begin
 
	-- Instantiate the Unit Under Test (UUT)
   uut: ALU_Nbits Port map (
          a => a,
          b => b,
          aluop(3) => sela,
          aluop(2) => selb,
          aluop(1 downto 0) => op,
          res => res,
          co => co,
          bn => bn,
          z => z,
          ov => ov
        );

   -- Stimulus process
    stim_proc: process
    begin		
        a <= "0101";
		b <= "1110";
		
		sela <= '0';
		selb <= '0';
		op 	<= "11";---suma
		wait for 100 ns;
		sela <= '0';
		selb <= '1';
		op 	<= "11";---resta
		wait for 100 ns;
		sela <= '0';
		selb <= '0';
		op 	<= "00";---AND
		wait for 100 ns;
		sela <= '1';
		selb <= '1';
		op 	<= "01";---NAND
		wait for 100 ns;
		sela <= '0';
		selb <= '0';
		op 	<= "01";---OR
		wait for 100 ns;
		sela <= '1';
		selb <= '1';
		op 	<= "00";---NOR
		wait for 100 ns;
		sela <= '0';
		selb <= '0';
		op 	<= "10";---XOR
		wait for 100 ns;
		sela <= '0';
		selb <= '1';
		op 	<= "10";---XNOR
		wait for 100 ns;
		
		b <= "0111";-----b=7
		
		sela <= '0';
		selb <= '0';
		op 	<= "11";---SUMA
		wait for 100 ns;
		
		b <= "0101";
		
		sela <= '0';
		selb <= '1';
		op 	<= "11";---resta
		wait for 100 ns;
		sela <= '1';
		selb <= '1';
		op 	<= "01";---NOT(NAND)
		wait for 100 ns;
		wait;
   end process;
end Behavioral;

