library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ESCOMIPS is
    generic ( d : integer := 25;
			  x : integer := 16;
			  n: integer := 4;
              tam_Microinstruccion: integer:=20;
			  tam_OPCODE: integer:=5;
			  tam_FUNCODE: integer:=4);	
	Port ( clr0, clk: in STD_LOGIC;
		   PC, RD1, RD2, resALU, BusSR: out STD_LOGIC_VECTOR (15 downto 0));
--		   m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19: out STD_LOGIC);
--		   micro: out STD_LOGIC_VECTOR (tam_Microinstruccion-1 downto 0));
--		   instru : out STD_LOGIC_VECTOR (d-1 downto 0));
end ESCOMIPS;

architecture Behavioral of ESCOMIPS is

component Registro_clr is
    Port ( clk, rclr: in STD_LOGIC;
           clr: out STD_LOGIC);
end component;

component ALU_Nbits is
    Port ( a, b : in STD_LOGIC_VECTOR (x-1 downto 0);
           aluop : in STD_LOGIC_VECTOR (n-1 downto 0);--3 downto 0
           res : out STD_LOGIC_VECTOR (x-1 downto 0);
           bn, z, co, ov : out STD_LOGIC);
end component;

component ArchivodeRegistros is
    Port ( readReg1, readReg2, writeReg, shamt : in  STD_LOGIC_VECTOR (n-1 downto 0);
           writeData : in  STD_LOGIC_VECTOR (x-1 downto 0);
           readData1, readData2 : inout  STD_LOGIC_VECTOR (x-1 downto 0);
           WR, SHE, dir, clk , clr : in  STD_LOGIC);
end component;

component MemoriaDatos is
    Port (dataIn: in  STD_LOGIC_VECTOR (x-1 downto 0);
          dir : in  STD_LOGIC_VECTOR (9 downto 0);
          clk, WD : in  STD_LOGIC;
          dataOut : out  STD_LOGIC_VECTOR (x-1 downto 0));
end component;

component Pila_MemoriaPrograma is
	Port( PC_in : in  STD_LOGIC_VECTOR (x-1 downto 0);
		  clk, clr, UP, DW, WPC : in  STD_LOGIC;
		  PC_out : out  STD_LOGIC_VECTOR (x-1 downto 0);
		  Inst : out  STD_LOGIC_VECTOR (d-1 downto 0));
end component;

component UnidadControl is
    Port ( funCode : in  STD_LOGIC_VECTOR (tam_FUNCODE-1 downto 0);
           opCode : in  STD_LOGIC_VECTOR (tam_OPCODE-1 downto 0);
           banderas : in  STD_LOGIC_VECTOR (n-1 downto 0);
           clk, clr, LF: in  STD_LOGIC;
           Microinstruccion : out  STD_LOGIC_VECTOR (tam_Microinstruccion-1 downto 0));
end component;

component Mux2a1_16bits is
    Port ( e0, e1 : in  STD_LOGIC_VECTOR (x-1 downto 0);
		   condicion : in std_logic;
		   salida : out  STD_LOGIC_VECTOR (x-1 downto 0));
end component;

component Mux2a1_4bits is
    Port ( e0, e1 : in  STD_LOGIC_VECTOR (n-1 downto 0);
		   condicion : in  STD_LOGIC;
		   salida : out  STD_LOGIC_VECTOR (n-1 downto 0));
end component;

component extSigno is
  Port ( entrada: in  STD_LOGIC_VECTOR (11 downto 0);
         salida: out STD_LOGIC_VECTOR (x-1 downto 0));
end component;

component extDireccion is
  Port ( entrada: in  STD_LOGIC_VECTOR (11 downto 0);
         salida: out STD_LOGIC_VECTOR (x-1 downto 0));
end component;

signal clr, bn, z, co, ov, LF, SHE, DIR, WR, WD, UP, DW, WPC: STD_LOGIC;
signal SDMP, SR2, SWD, SEXT, SOP1, SOP2, SDMD, SR: STD_LOGIC;
signal a, b, res, writeData, readData1, readData2, PC_in, PC_out, sal_Signo, sal_Dir, extensor, dirMemData, dataOut, SR_Out: STD_LOGIC_VECTOR(x-1 downto 0);
signal Inst: STD_LOGIC_VECTOR(d-1 downto 0);
signal readReg1, readReg2, writeReg, shamt, aluop: STD_LOGIC_VECTOR (n-1 downto 0);

begin
    CLR_reg: Registro_clr
        Port Map ( clk => clk,
                   rclr =>clr0,
                   clr => clr);
    
    Unidad_Control: UnidadControl --(0, N, Z, C) 
        Port Map ( banderas(3) => ov,
				   banderas(2) => bn,
				   banderas(1) => z,
				   banderas(0) => co,
				   LF => LF,
				   clk => clk,
				   clr => clr,
					
				   opCode  => Inst(24 downto 20),
				   funCode => Inst(3 downto 0),
					
				   Microinstruccion(19) => SDMP,
				   Microinstruccion(18) => UP,
				   Microinstruccion(17) => DW,
				   Microinstruccion(16) => WPC,
				   Microinstruccion(15) => SR2,
				   Microinstruccion(14) => SWD,
			       Microinstruccion(13) => SEXT,
				   Microinstruccion(12) => SHE,
				   Microinstruccion(11) => DIR,
				   Microinstruccion(10) => WR,
				   Microinstruccion(9) => SOP1,
				   Microinstruccion(8) => SOP2,
				   Microinstruccion(7) => aluop(3),
				   Microinstruccion(6) => aluop(2),
				   Microinstruccion(5) => aluop(1),
				   Microinstruccion(4) => aluop(0),
				   Microinstruccion(3) => SDMD,
				   Microinstruccion(2) => WD,
				   Microinstruccion(1) => SR,
				   Microinstruccion(0) => LF);

	Pila_y_MemoriaPrograma: Pila_MemoriaPrograma
        Port map( PC_in => PC_in,
		  		  clk => clk,
				  clr => clr, 
				  UP => UP, 
				  DW => DW, 
				  WPC => WPC,
				  PC_out => PC_out,
				  Inst => Inst);

	mux_SR2: mux2a1_4bits 
        Port map( e1 => Inst(19 downto 16),
				  e0 => Inst(11 downto 8),
				  condicion => SR2,
				  salida => readReg2);

	Mux_SWD: Mux2a1_16bits
        Port map( e1 => SR_Out,
				  e0 => Inst(15 downto 0),
				  condicion => SWD,
				  salida => writeData);

	Extensor_Signo: extSigno
	   Port Map ( entrada => Inst(11 downto 0),
	              salida => sal_Signo);

	Extensor_Direccion: extDireccion
	   Port Map ( entrada => Inst(11 downto 0),
	              salida => sal_Dir);
	              				  				  
	Mux_SEXT: Mux2a1_16bits 
        Port map( e1 => sal_Dir,
				  e0 => sal_Signo,
				  condicion => sext,
				  salida => extensor);
				  
	Achivo_Registros: ArchivodeRegistros 
	   Port map( readReg1 => Inst(15 downto 12),
				 readReg2 => readReg2,
				 writeReg => Inst(19 downto 16),
				 shamt => Inst(7 downto 4), 
				 writeData => writeData,
				 readData1 => readData1,
				 readData2 => readData2,
				 WR => WR,
				 SHE => SHE, 
				 dir => dir,
				 clk => clk, 
				 clr => clr);
				 
    Mux_SOP1: Mux2a1_16bits
        Port map( e1 => PC_out,
				  e0 => readData1,
				  condicion => SOP1,
				  salida => a);
	
	muxSOP2: Mux2a1_16bits 
        Port map( e1 => extensor,
				  e0 => readData2,
				  condicion => SOP2,
				  salida => b);				 

	ALU: ALU_Nbits
	   Port map( a => a,
				 b => b,
				 aluop => aluop,					
				 res => res,
				 co => co,
				 bn => bn,
				 z => z,
				 ov => ov);

	muxSDMD: Mux2a1_16bits 
        Port map( e1 => Inst(15 downto 0),
				  e0 => res,
				  condicion => SDMD,
				  salida => dirMemData);
				 
    Memoria_Datos: MemoriaDatos
        Port map( dataIn => readData2,
		      	  dir => dirMemData(9 downto 0),
			      clk => clk, 
			      WD => WD,
				  dataOut => dataOut);

	muxSR: Mux2a1_16bits 
        Port map( e1 => res,
				  e0 => dataOut,
				  condicion => SR,
				  salida => SR_Out);

    Mux_SDMP: Mux2a1_16bits 
        Port map( e1 => SR_Out,
				  e0 => Inst(15 downto 0),
				  condicion => SDMP,
				  salida => PC_in);
					
--	--ASIGNACIONES DIRECTAS (Archivo de Registros)
--	readReg1 <= Inst(15 downto 12);--ReadRegister1
--	writeReg <= Inst(19 downto 16);--WriteRegister
--	shamt <= Inst(7 downto 4);--shamt
	
	--ASIGNACION DE SALIDAS
	PC <= PC_Out;
	RD1 <= readData1;
	RD2 <= readData2;
	resALU <= res;
	BusSr <= SR_Out;
--	m0 <= SDMP;
--	m1 <= UP;
--	m2 <= DW;
--	m3 <= WPC;
--	m4 <= SR2;
--	m5 <= SWD;
--	m6 <= SEXT;
--	m7 <= SHE;
--	m8 <= DIR;
--	m9 <= WR;
--	m10 <= SOP1;
--	m11 <= SOP2;
--	m12 <= aluop(3);
--	m13 <= aluop(2);
--	m14 <= aluop(1);
--	m15 <= aluop(0);
--	m16 <= SDMD;
--	m17 <= WR;
--	m18 <= SR;
--	m19 <= LF;
--	instru <= Inst;
	
end Behavioral;