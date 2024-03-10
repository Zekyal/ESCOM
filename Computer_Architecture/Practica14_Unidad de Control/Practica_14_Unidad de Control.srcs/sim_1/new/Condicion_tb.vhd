library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
  
entity Condicion_tb IS
end Condicion_tb;
 
architecture Behavioral of Condicion_tb is 

component Condicion is
    Port ( Q : in  STD_LOGIC_VECTOR (3 downto 0);
           EQ, NEQ, LT, LE, GTI, GET : out  STD_LOGIC);
end component;
    
--Inputs
signal Q : STD_LOGIC_VECTOR (3 downto 0) := (others => '0');
--Outputs
signal EQ : STD_LOGIC;
signal NEQ : STD_LOGIC;
signal LT : STD_LOGIC;
signal LE : STD_LOGIC;
signal GTI : STD_LOGIC;
signal GET : STD_LOGIC;
   
begin
    -- Instantiate the Unit Under Test (UUT)
    uut: Condicion 
        Port Map ( Q => Q,
                   EQ => EQ,
                   NEQ => NEQ,
                   LT => LT,
                   LE => LE,
                   GTI => GTI,
                   GET => GET);

   -- Stimulus process
   stim_proc: process
   begin		
      Q <= "0000";
      wait for 50 ns;	
      Q <= "0010";
      wait for 50 ns;	
	  Q <= "0100";
      wait for 50 ns;	
      Q <= "1000";
      wait for 50 ns;
	  Q <= "0110";
      wait for 50 ns;
      Q <= "1001";
      wait for 50 ns;
	  Q <= "1010";
      wait for 50 ns;	
      wait;
   end process;
end Behavioral;