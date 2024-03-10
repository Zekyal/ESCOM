library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ALU_Nbits is
    generic (n: integer := 15);
    Port ( a,b : in STD_LOGIC_VECTOR (n downto 0);
           aluop : in STD_LOGIC_VECTOR (3 downto 0);--3 downto 0
           res : out STD_LOGIC_VECTOR (n downto 0);
           bn, z, co, ov : out STD_LOGIC);
end ALU_Nbits;

architecture Behavioral of ALU_Nbits is

component ALU_1bit is
    Port ( a, b, sela, selb, cin : in STD_LOGIC;
           op : in STD_LOGIC_VECTOR (1 downto 0);
           res : out STD_LOGIC;
           cout : out STD_LOGIC);
end component;

signal c: std_logic_vector(n+1 downto 0);
signal aux: std_logic_vector(n downto 0); --se usa en vez de res, porque res es de salida

begin
    c(0) <= aluop(2);
   
    ciclo: for i in 0 to n generate
        bitA: ALU_1bit Port map(
            a => a(i),
            b => b(i),
            sela => aluop(3),
            selb => aluop(2) ,
            cin => c(i),
            op  => aluop(1 downto 0),
            res => aux(i),
            cout => c(i+1)
        );
    end generate;
    
    bn <= aux(n); --signo
    co <= c(n+1) when aluop(1 downto 0) = "11" else '0'; --carry
    z<= '1' when aux="0000000000000000" else '0';
    ov <= c(n+1) xor c(n); --overflow
    res <= aux;
end Behavioral;