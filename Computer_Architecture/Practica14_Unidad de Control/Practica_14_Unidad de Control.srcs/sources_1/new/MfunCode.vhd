library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity MfunCode is
	 generic (
		D : integer := 20;
		A : integer := 4);
    Port ( funCode : in  STD_LOGIC_VECTOR (A-1 downto 0);
           salidaD : out  STD_LOGIC_VECTOR (D-1 downto 0));
end MfunCode;

architecture Behavioral of MfunCode is
	constant ADD: std_logic_vector := X"04433";
	constant SUB: std_logic_vector := X"04473";	
	constant OpAND: std_logic_vector := X"04403"; 
	constant OpOR: 	std_logic_vector := X"04413";
	constant OpXOR: std_logic_vector := X"04423";
	constant OpNAND: std_logic_vector := X"044d3";
	constant OpNOR: std_logic_vector := X"044c3";
	constant OpXNOR: std_logic_vector := X"044a3";
	constant OpNOT: std_logic_vector := X"044d3";
	constant OpSLL: std_logic_vector := X"01400";
	constant OpSRL: std_logic_vector := X"01c00";
	
	type banco is array (0 to (2**A)-1) of std_logic_vector(D-1 downto 0);
	constant memoria : banco := (
		ADD,	--00
		SUB,	--01
		OpAND,	--02
		OpOR,	--03
		OpXOR,	--04
		OpNAND,	--05
		OpNOR,	--06
		OpXNOR,	--07
		OpNOT,	--08	
		OpSLL,	--09
		OpSRL,	--10
		others => (others => '0'));
begin
	salidaD <= memoria(conv_integer(funCode));
end Behavioral;