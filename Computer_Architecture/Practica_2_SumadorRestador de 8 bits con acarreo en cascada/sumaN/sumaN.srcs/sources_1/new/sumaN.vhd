library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity sumaN is
    generic(
        n: integer := 8
    );--se pone como generico para que lo reconozca la arquitectura
    
    Port ( a, b : in STD_LOGIC_VECTOR (n-1 downto 0);
           cin : in STD_LOGIC;
           s : out STD_LOGIC_VECTOR (n-1 downto 0);
           cout : out STD_LOGIC);
end sumaN;

architecture Behavioral of sumaN is

component suma1 is
    Port ( a, b, cin : in STD_LOGIC;
           s : out STD_LOGIC;
           cout : out STD_LOGIC);
end component;

signal c: std_logic_vector (n downto 0);
signal eb: std_logic_vector (n-1 downto 0);
begin
    c(0) <= cin;
    
    ciclo: for i in 0 to n-1 generate
        eb(i) <= b(i) xor c(0);
        
        bit1: suma1 Port map(
        a => a(i),
        b => eb(i), -- xor c(0),
        cin => c(i),
        s => s(i),
        cout => c(i+1)
        );
    end generate;
      
      cout <= c(n);

end Behavioral;
