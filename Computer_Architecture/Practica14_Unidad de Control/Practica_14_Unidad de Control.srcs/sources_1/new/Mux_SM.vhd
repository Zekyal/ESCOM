library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux_SM is
    Port ( MfunCode, MopCode : in  STD_LOGIC_VECTOR (19 downto 0);
           SM : in  STD_LOGIC;
           Microinstruccion : out  STD_LOGIC_VECTOR (19 downto 0));
end Mux_SM;

architecture Behavioral of Mux_SM is
begin
	Microinstruccion <= MopCode when SM = '1' else MfunCode;
end Behavioral;