library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity BarrelShifter_tb is
end BarrelShifter_tb;

architecture Behavioral of BarrelShifter_tb is
    component BarrelShifter
    Port(dato : IN  std_logic_vector(15 downto 0);
         shift : IN  std_logic_vector(3 downto 0);
         dir : IN  std_logic;
         res : OUT  std_logic_vector(15 downto 0)
        );
    end component;
    
    signal dato : std_logic_vector(15 downto 0) := (others => '0');
    signal shift : std_logic_vector(3 downto 0) := (others => '0');
    signal dir : std_logic := '0';
    signal res : std_logic_vector(15 downto 0);
   
    begin
    uut: barrelShifter PORT MAP (
        dato => dato,
        shift => shift,
        dir => dir,
        res => res
    );

    stim_proc: process
    begin		
        dato<= x"fff9";
		dir<= '1';
		shift <= "0000";
		wait for 30 ns;
		shift <= "0001";
		wait for 30 ns;
		shift <= "0010";
		wait for 30 ns;
		shift <= "0011";
		wait for 30 ns;
		shift <= "0100";
		wait for 30 ns;
		shift <= "0101";
		wait for 30 ns;
		shift <= "1000";
		wait for 30 ns;
		
		dato<= x"9fff";
		dir<= '0';
		shift <= "0000";
		wait for 30 ns;
		shift <= "0001";
		wait for 30 ns;
		shift <= "0010";
		wait for 30 ns;
		shift <= "0011";
		wait for 30 ns;
		shift <= "0100";
		wait for 30 ns;
		shift <= "0101";
		wait for 30 ns;
		shift <= "1000";
		wait for 30 ns;
      wait;
   end process;
end Behavioral;
