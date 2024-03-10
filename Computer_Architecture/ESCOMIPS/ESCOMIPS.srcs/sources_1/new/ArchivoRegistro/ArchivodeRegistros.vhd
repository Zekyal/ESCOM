library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ArchivodeRegistros is
        generic(n: integer := 3;
				t: integer := 15);
		Port(readReg1, readReg2, writeReg, shamt : in  STD_LOGIC_VECTOR (n downto 0);
             writeData : in  STD_LOGIC_VECTOR (t downto 0);
             readData1, readData2 : inout  STD_LOGIC_VECTOR (t downto 0);
             WR, SHE, dir, clk , clr : in  STD_LOGIC);
end ArchivodeRegistros;

architecture Behavioral of ArchivodeRegistros is
    component Registro is
		 Port(d : in STD_LOGIC_VECTOR (15 downto 0);
              q : out STD_LOGIC_VECTOR (15 downto 0);
              clr, clk, l : in STD_LOGIC);
	end component;
	
	component BarrelShifter is
		 Port(dato : in  STD_LOGIC_VECTOR (t downto 0);
              shift : in  STD_LOGIC_VECTOR (n downto 0);--bits a recorrer
              dir : in  STD_LOGIC;--direccion del corrimiento
              res : out  STD_LOGIC_VECTOR (t downto 0));--salida (despues de corrimiento)
	end component;
	
	component Multiplexor_16ch is
		  Port(r0: in std_logic_vector(15 downto 0);
			   r1: in std_logic_vector(15 downto 0);
 			   r2: in std_logic_vector(15 downto 0);
	 		   r3: in std_logic_vector(15 downto 0);
		 	   r4: in std_logic_vector(15 downto 0);
			   r5: in std_logic_vector(15 downto 0);
			   r6: in std_logic_vector(15 downto 0);
			   r7: in std_logic_vector(15 downto 0);
			   r8: in std_logic_vector(15 downto 0);
			   r9: in std_logic_vector(15 downto 0);
			   r10: in std_logic_vector(15 downto 0);
			   r11: in std_logic_vector(15 downto 0);
			   r12: in std_logic_vector(15 downto 0);
			   r13: in std_logic_vector(15 downto 0);
			   r14: in std_logic_vector(15 downto 0);
			   r15: in std_logic_vector(15 downto 0);
			   readReg : in  STD_LOGIC_VECTOR (3 downto 0);
			   readData : out  STD_LOGIC_VECTOR (15 downto 0));
	end component;
	
	component Demux is
		Port(writeReg: in std_logic_vector(3 downto 0);
		     WR: in std_logic;
	   	     L: out std_logic_vector(15 downto 0));
	end component;
	
	type vectores is array (0 to t) of std_logic_vector(t downto 0);
	signal banco: vectores;
	signal dex, smux, data: std_logic_vector(t downto 0);
	
    begin
	   barrel_S: BarrelShifter Port map( 
	       dato => readData1,
		   shift => shamt,
		   dir => dir,
		   res => smux);
		
	   data <= smux when SHE = '1' else writeData;--Multiplexor 2 canales
	
	   dmux: Demux Port map(	
	       writeReg => writeReg,
		   WR => WR,
		   L => dex);
		
	   regs: for i in 0 to t generate
	       reg: Registro Port map(
	           d => data,
               clk => clk, 
		       clr => clr, 
		       l => dex(i),
               q => banco(i));
	   end generate;
	
	   mux1: Multiplexor_16ch Port map(
	       r0 => banco(0),
		   r1 => banco(1),
		   r2 => banco(2),
		   r3 => banco(3),
		   r4 => banco(4),
		   r5 => banco(5),
		   r6 => banco(6),
		   r7 => banco(7),
		   r8 => banco(8),
		   r9 => banco(9),
		   r10 => banco(10),
		   r11 => banco(11),
		   r12 => banco(12),
		   r13 => banco(13),
		   r14 => banco(14),
		   r15 => banco(15),
		   readReg => readReg1,
		   readData => readData1);
	
	   mux2: Multiplexor_16ch Port map(
	       r0 => banco(0),
		   r1 => banco(1),
		   r2 => banco(2),
		   r3 => banco(3),
		   r4 => banco(4),
		   r5 => banco(5),
		   r6 => banco(6),
		   r7 => banco(7),
		   r8 => banco(8),
		   r9 => banco(9),
		   r10 => banco(10),
		   r11 => banco(11),
		   r12 => banco(12),
		   r13 => banco(13),
		   r14 => banco(14),
		   r15 => banco(15),
		   readReg => readReg2,
		   readData => readData2);
end Behavioral;