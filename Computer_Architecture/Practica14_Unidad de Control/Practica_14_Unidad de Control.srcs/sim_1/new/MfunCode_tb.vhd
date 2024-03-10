LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
entity MfunCode_tb is
end MfunCode_tb;
 
architecture Behavioral of MfunCode_tb is 

component MfunCode is
    Port ( funCode : in STD_LOGIC_VECTOR (3 downto 0);
           salidaD : out STD_LOGIC_VECTOR (19 downto 0));
end component;

--Inputs
signal funCode : STD_LOGIC_VECTOR(3 downto 0) := (others => '0');

--Outputs
signal salidaD : STD_LOGIC_VECTOR(19 downto 0);
 
begin
	-- Instantiate the Unit Under Test (UUT)
    uut: MfunCode
    Port Map ( funCode => funCode,
               salidaD => salidaD);
		  
    -- Stimulus process
    stim_proc: process
    begin		
        funCode <= x"0";
        wait for 50 ns;	
		funCode <= x"1";
        wait for 50 ns;	
		funCode <= x"2";
        wait for 50 ns;	
		funCode <= x"3";
        wait for 50 ns;	
		funCode <= x"4";
        wait for 50 ns;	
		funCode <= x"5";
        wait for 50 ns;	
		funCode <= x"6";
        wait for 50 ns;	
		funCode <= x"7";
        wait for 50 ns;	
		funCode <= x"8";
        wait for 50 ns;	
		funCode <= x"9";
        wait for 50 ns;	
		funCode <= x"A";
        wait for 50 ns;	
		funCode <= x"B";
        wait for 50 ns;
		funCode <= x"C";
        wait for 50 ns;	
		funCode <= x"D";
        wait for 50 ns;	
		funCode <= x"E";
        wait for 50 ns;
		funCode <= x"F";
        wait for 50 ns;	
        wait;
    end process;
end Behavioral;