LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
entity MopCode_tb is
end MopCode_tb;
 
architecture Behavioral of MopCode_tb is 

component MopCode is
    Port ( opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           salidaD : out  STD_LOGIC_VECTOR (19 downto 0));
end component;

--Inputs
signal opCode : STD_LOGIC_VECTOR(4 downto 0) := (others => '0');

--Outputs
signal salidaD : STD_LOGIC_VECTOR(19 downto 0);
 
begin
    -- Instantiate the Unit Under Test (UUT)
    uut: MopCode
        Port Map ( opCode => opCode,
                   salidaD => salidaD);
		  
    -- Stimulus process
    stim_proc: process
    begin		
        opCode <= "00001";--LI
        wait for 50 ns;	
		opCode <= "00011";--SWI
        wait for 50 ns;	
		opCode <= "00101";--ADDI
        wait for 50 ns;
		opCode <= "00110";--SUBI
        wait for 50 ns;	
		opCode <= "01001";--XORI
        wait for 50 ns;	
		opCode <= "01100";--XNORI
        wait for 50 ns;	
		opCode <= "01111";--BLTI
        wait for 50 ns;	
		opCode <= "10010";--BGETI
        wait for 50 ns;	
		opCode <= "10011";--B
        wait for 50 ns;	
		opCode <= "10100";--CALL
        wait for 50 ns;	
		opCode <= "10101";--RET
        wait for 50 ns;	
		opCode <= "10110";--NOP
        wait for 50 ns;
        wait;
    end process;
end Behavioral;