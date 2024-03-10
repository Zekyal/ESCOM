library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
  
entity Decodificador_Instruccion_tb is
end Decodificador_Instruccion_tb;
 
architecture Behavioral of Decodificador_Instruccion_tb is

component Decodificador_Instruccion is
    Port ( opCode : in STD_LOGIC_VECTOR (4 downto 0);
           TIPOR, BEQI, BNEQI, BLTI, BLETI, BGTI, BGETI : out STD_LOGIC);
end component;
    
--Inputs
signal opCode :STD_LOGIC_VECTOR(4 downto 0) := (others => '0');

--Outputs
signal TIPOR : STD_LOGIC;
signal BEQI : STD_LOGIC;
signal BNEQI : STD_LOGIC;
signal BLTI : STD_LOGIC;
signal BLETI : STD_LOGIC;
signal BGTI : STD_LOGIC;
signal BGETI : STD_LOGIC;
 
begin
    uut: Decodificador_Instruccion
    Port Map ( opCode => opCode,
               TIPOR => TIPOR,
               BEQI => BEQI,
               BNEQI => BNEQI,
               BLTI => BLTI,
               BLETI => BLETI,
               BGTI => BGTI,
               BGETI => BGETI);

    -- Stimulus process
    stim_proc: process
    begin		
        opCode <= "00001";--LI
        wait for 50 ns;	
		opCode <= "00000";--Tipo R
        wait for 50 ns;
		opCode <= "01101";--BEQI
        wait for 50 ns;
		opCode <= "01110";--BNEI
        wait for 50 ns;
		opCode <= "01111";--BLTI
        wait for 50 ns;
		opCode <= "10000";--BLETI
        wait for 50 ns;
		opCode <= "10001";--BGTI
        wait for 50 ns;
		opCode <= "10010";--BGETI
        wait for 50 ns;
        wait;
   end process;
end Behavioral;