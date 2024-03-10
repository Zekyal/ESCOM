library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;

entity MemoriaPrograma is
	generic (d : integer := 25;
		     a : integer := 16);
    Port (PC : in  STD_LOGIC_VECTOR (a-1 downto 0);
          Inst : out  STD_LOGIC_VECTOR (d-1 downto 0));
end MemoriaPrograma;

architecture Behavioral of MemoriaPrograma is
    --INSTRUCCIONES
    --Tipo I
    constant LI : std_logic_vector(4 downto 0) :=  	"00001";
    constant LWI : std_logic_vector(4 downto 0) := 	"00010";
    constant LW : std_logic_vector(4 downto 0) :=  	"10111";
    constant SWI : std_logic_vector(4 downto 0) := 	"00011";
    constant SW : std_logic_vector(4 downto 0) :=  	"00100";

    constant ADDI : std_logic_vector(4 downto 0):= 	"00101";
    constant SUBI : std_logic_vector(4 downto 0):= 	"00110";

    constant ANDI: std_logic_vector(4 downto 0) :=  "00111";
    constant ORI : std_logic_vector(4 downto 0) :=  "01000";
    constant XORI : std_logic_vector(4 downto 0) := "01001";
    constant NANDI : std_logic_vector(4 downto 0):= "01010";
    constant NORI: std_logic_vector(4 downto 0) :=  "01011";
    constant XNORI : std_logic_vector(4 downto 0):= "01100";

    constant BEQI : std_logic_vector(4 downto 0):= 	"01101";
    constant BNEI : std_logic_vector(4 downto 0):= 	"01110";
    constant BLTI : std_logic_vector(4 downto 0):= 	"01111";
    constant BLETI : std_logic_vector(4 downto 0):=	"10000";
    constant BGTI : std_logic_vector(4 downto 0):= 	"10001";
    constant BGETI : std_logic_vector(4 downto 0):=	"10010";

    --Tipo R
    constant TR  : std_logic_vector(4 downto 0) := 	"00000";--Operación Tipo R
    constant ADD : std_logic_vector(3 downto 0) := 	"0000";
    constant SUB : std_logic_vector(3 downto 0) := 	"0001";

    constant OpAND : std_logic_vector(3 downto 0) :=  "0010";
    constant OpOR : std_logic_vector(3 downto 0) :=   "0011"; 
    constant OpXOR : std_logic_vector(3 downto 0) :=  "0100";
    constant OpNAND: std_logic_vector(3 downto 0) :=  "0101";
    constant OpNOR : std_logic_vector(3 downto 0) :=  "0110";
    constant OpXNOR : std_logic_vector(3 downto 0) := "0111";
    constant OpNOT : std_logic_vector(3 downto 0) :=  "1000";

    constant OpSLL : std_logic_vector(3 downto 0) :=  "1001";
    constant OpSRL : std_logic_vector(3 downto 0) :=  "1010";

    --Tipo J
    constant B: std_logic_vector(4 downto 0):=     "10011";
    constant CALL : std_logic_vector(4 downto 0):= "10100";
    
    --Otros
    constant RET : std_logic_vector(4 downto 0):= "10101";
    constant NOP : std_logic_vector(4 downto 0):= "10110";
    
    --Sin Uso
    constant SU : std_logic_vector(3 downto 0) := "0000";--Sin Uso

    --REGISTROS
    constant R0 : std_logic_vector(3 downto 0) := "0000";
    constant R1 : std_logic_vector(3 downto 0) := "0001";
    constant R2 : std_logic_vector(3 downto 0) := "0010";
    constant R3 : std_logic_vector(3 downto 0) := "0011";
    constant R4 : std_logic_vector(3 downto 0) := "0100";
    constant R5 : std_logic_vector(3 downto 0) := "0101";
    constant R6 : std_logic_vector(3 downto 0) := "0110";
    constant R7 : std_logic_vector(3 downto 0) := "0111";
    constant R8 : std_logic_vector(3 downto 0) := "1000";
    constant R9 : std_logic_vector(3 downto 0) := "1001";
    constant R10 : std_logic_vector(3 downto 0) := "1010";
    constant R11 : std_logic_vector(3 downto 0) := "1011";
    constant R12 : std_logic_vector(3 downto 0) := "1100";
    constant R13 : std_logic_vector(3 downto 0) := "1101";
    constant R14 : std_logic_vector(3 downto 0) := "1110";
    constant R15 : std_logic_vector(3 downto 0) := "1111";

    --COMANDOS :0
    type banco is array (0 to (2**a)-1) of std_logic_vector(d-1 downto 0);
    constant memProg : banco := (
        LI&R0&x"0000", 	    --0 LI R0, #0
        LI&R1&x"0001", 		--1 LI R1, #1
        LI&R2&x"0000", 	    --2 LI R2, #0
        LI&R3&x"000c", 		--3 LI R3, #12
        TR&R4&R0&R1&SU&ADD, --4 Ciclo: ADD R4, R0, R1(R4 = R0 + R1)
        SWI&R4&x"0048", 	--5 SWI R4, 72(mem[72] = R4)
        ADDI&R0&R1&x"000", --6 ADDI R0, R1, #0 (R0 = R1)
        SUBI&R1&R4&x"000",	--7 SUBI R1, R4, #0 (R1 = R4)
        ADDI&R2&R2&x"001", --8 ADDI R2, R2, #1 (R2 = R2 +1)
        BNEI&R3&R2&x"004", --9 BNEI R3, R2, Ciclo (R2 != R3)
        NOP&SU&SU&SU&SU&SU, --10 fin: NOP
        B&SU&x"000a",       --11 B fin
        others => (others => '0'));
    
    begin
	   Inst <= memProg(conv_integer(PC));
end Behavioral;