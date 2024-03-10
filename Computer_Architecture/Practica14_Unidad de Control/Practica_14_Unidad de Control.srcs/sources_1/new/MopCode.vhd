library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity MopCode is
	 generic (
		D : integer := 20;
		A : integer := 5);
    Port ( opCode : in  STD_LOGIC_VECTOR (A-1 downto 0);
           salidaD : out  STD_LOGIC_VECTOR (D-1 downto 0));
end MopCode;

architecture Behavioral of MOpcode is
--OPCODES--
--Tipo I
constant LI: std_logic_vector := x"00400";
constant LWI: std_logic_vector := x"04408";
constant LW: std_logic_vector := x"06531";
constant SWI: std_logic_vector := x"0800c";
constant SW: std_logic_vector := x"0A135";
constant ADDI: std_logic_vector	:= x"04533";
constant SUBI: std_logic_vector	:= x"04573";
constant ANDI: std_logic_vector := x"04503";
constant ORI: std_logic_vector := x"04513";
constant XORI: std_logic_vector := x"04523";
constant NANDI: std_logic_vector := x"045d3";
constant NORI: std_logic_vector := x"045c3";
constant XNORI: std_logic_vector := x"045a3";
constant BEQI: std_logic_vector	:= x"08071";
constant BNEI: std_logic_vector	:= x"08071";
constant BLTI: std_logic_vector	:= x"08071";
constant BLETI: std_logic_vector := x"08071";
constant BGTI: std_logic_vector	:= x"08071";
constant BGETI: std_logic_vector := x"08071";
constant SALTO: std_logic_vector := x"98333";--Saltos condicionales de los B's tipo I

--Tipo J
constant B: std_logic_vector := x"10000";
constant CALL: std_logic_vector	:= x"50000";

--Otras Instrucciones
constant RET: std_logic_vector := x"20000";
constant NOP: std_logic_vector := x"00000";


type banco is array (0 to (2**A)-1) of std_logic_vector(D-1 downto 0);
constant memoria: banco := (
	SALTO, 	--00
	LI, 	--01
	LWI, 	--02
	SWI, 	--03
	SW, 	--04
	ADDI, 	--05
	SUBI, 	--06
	ANDI, 	--07
	ORI, 	--08
	XORI, 	--09
	NANDI,	--10
	NORI, 	--11
	XNORI, 	--12
	BEQI, 	--13
	BNEI, 	--14
	BLTI, 	--15
	BLETI, 	--16
	BGTI, 	--17
	BGETI, 	--18
	B, 	    --19
	CALL, 	--20
	RET, 	--21
	NOP, 	--22
	LW, 	--23
	others =>(others => '0'));
begin
	salidaD <= memoria(conv_integer(opCode));
end Behavioral;