library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity cartaASM is
	Port ( INI, clk, clr : in  STD_LOGIC;
		   D : in  STD_LOGIC_VECTOR (8 downto 0);
		   A : out STD_LOGIC_VECTOR (8 downto 0);--Salida Arreglo
		   B : out STD_LOGIC_VECTOR (6 downto 0));--Salida Display(Mux)
end cartaASM;

Architecture Behavioral of cartaASM is

    component Arreglo is
        Port ( EA, LA, clk, clr : in  STD_LOGIC;
               DA : in  STD_LOGIC_VECTOR (8 downto 0);
               QA : out  STD_LOGIC_VECTOR (8 downto 0));
    end component;
	
    component Contador is
        Port ( clk, clr, LB, EB : in  STD_LOGIC;
               QB : out  STD_LOGIC_VECTOR (3 downto 0));
    end component;
	
    component Decodificador is
        Port ( QB : in  STD_LOGIC_VECTOR (3 downto 0);
               deco : out  STD_LOGIC_VECTOR(6 downto 0));
    end component;
	
    component Mux is
        Port ( deco : in  STD_LOGIC_VECTOR (6 downto 0);
		       OP: in STD_LOGIC;
		       Q : out  STD_LOGIC_VECTOR (6 downto 0));
    end component;
	
    component UnidadControl is
        Port ( clk, clr, INI, z, A0 : in STD_LOGIC;
               LA, LB, EA, EB, EC : out STD_LOGIC);
    end component;
	
    component BanderaZ is
        Port ( Cz : in  STD_LOGIC_VECTOR (8 downto 0);
               z : out  STD_LOGIC);
    end component;

    signal A0, z, LA, LB, EA, EB, EC: STD_LOGIC;
    signal B1: STD_LOGIC_VECTOR(3 DOWNTO 0);
    signal Cz: STD_LOGIC_VECTOR(8 downto 0);
    signal B_aux: STD_LOGIC_VECTOR(6 downto 0);--auxiliar de la salida del Dsiplay(B) para evitar corto circuito uwu
	
begin
	A <= Cz;
	A0 <= Cz(0);
	
	Bandera_Z : BanderaZ
	   Port map( Cz => Cz,
				 z => z);
		
	UC : UnidadControl
        Port Map( clk => clk,
				  clr => clr,
				  INI => INI, 
				  A0 => A0,
				  z => z,
				  LA => LA,-- A=D
				  LB => LB,-- B=0
				  EA => EA,-- A>>1
				  EB => EB,-- B++
				  EC => EC);-- Mostrar B
				
	Counter : Contador 
        Port Map( clk => clk,
				  clr => clr,
				  LB => LB, 
				  EB => EB,
				  QB => B1);
				
    Arreglo_9bits : Arreglo
        Port MAP( clk => clk,
				  clr => clr,
				  DA => D,
				  EA => EA, 
				  LA => LA,
				  QA => Cz);
				
	Decoder: Decodificador
        Port Map( QB => B1,
				  deco => B_aux);
				
	Multiplexor: Mux
        Port Map( deco => B_aux,
				  OP => EC,
				  Q => B);			
end Behavioral;

