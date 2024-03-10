library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux is
    Port( PCin0: in std_logic_vector(15 downto 0);
		  PCin1: in std_logic_vector(15 downto 0);
		  PCin2: in std_logic_vector(15 downto 0);
		  PCin3: in std_logic_vector(15 downto 0);
		  PCin4: in std_logic_vector(15 downto 0);
		  PCin5: in std_logic_vector(15 downto 0);
		  PCin6: in std_logic_vector(15 downto 0);
		  PCin7: in std_logic_vector(15 downto 0);
		  SP : in  STD_LOGIC_VECTOR (2 downto 0);
		  PC_out: out  STD_LOGIC_VECTOR (15 downto 0));
end Mux;

architecture Behavioral of Mux is

begin
    PC_out <= PCin0 when SP = "000" else
              PCin1 when SP = "001" else
			  PCin2 when SP = "010" else
			  PCin3 when SP = "011" else
		   	  PCin4 when SP = "100" else
			  PCin5 when SP = "101" else
			  PCin6 when SP = "110" else
			  PCin7;

end Behavioral;