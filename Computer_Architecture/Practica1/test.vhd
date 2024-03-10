LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
ENTITY test IS
END test;
 
ARCHITECTURE behavior OF test IS 
 
    COMPONENT practica1
    PORT(
         a : IN  std_logic_vector(3 downto 0);
         b : IN  std_logic_vector(3 downto 0);
         cin : IN  std_logic;
         s : OUT  std_logic_vector(3 downto 0);
         cout : OUT  std_logic
        );
    END COMPONENT;
    
   --Inputs
   signal a : std_logic_vector(3 downto 0) := (others => '0');
   signal b : std_logic_vector(3 downto 0) := (others => '0');
   signal cin : std_logic := '0';

 	--Outputs
   signal s : std_logic_vector(3 downto 0);
   signal cout : std_logic;
 
BEGIN
 
   uut: practica1 PORT MAP (
          a => a,
          b => b,
          cin => cin,
          s => s,
          cout => cout
        );

   -- Stimulus process
   stim_proc: process
   begin---------------- 5+5
      a <= "0101";
		b <= "0101";
		cin <= '0';
      wait for 5 ps;--- 12+8
		a <= "1100";
		b <= "1000";
		cin <= '0';
      wait for 5 ps;--- 9+5
		a <= "1001";
		b <= "0101";
		cin <= '0';
      wait for 5 ps;--- 10-9
		a <= "1010";
		b <= "1001";
		cin <= '1';
      wait for 5 ps;--- 4+2
		a <= "0100";
		b <= "0010";
		cin <= '0';
      wait for 5 ps;--- 7-9
		a <= "0111";
		b <= "1001";
		cin <= '1';
		wait for 5 ps;--- 15-15
		a <= "1111";
		b <= "1111";
		cin <= '1';
		wait for 5 ps;--- 11-8
		a <= "1011";
		b <= "1000";
		cin <= '1';
		wait for 5 ps;--- 1-4
		a <= "0001";
		b <= "0100";
		cin <= '1';
		wait for 5 ps;
		a <= "0001";
		b <= "0001";
		cin <= '1';
      wait for 5 ps;
      wait;
   end process;

END;
