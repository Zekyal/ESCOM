library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ESCOMIPS_tb is
end ESCOMIPS_tb;

architecture Behavioral of ESCOMIPS_tb is

component ESCOMIPS is
	Port ( clr0, clk: in STD_LOGIC;
		   PC, RD1, RD2, resALU, BusSR: out STD_LOGIC_VECTOR (15 downto 0));
--		   m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19: out STD_LOGIC);
--		   micro: out STD_LOGIC_VECTOR(19 downto 0));
--		   instru : out STD_LOGIC_VECTOR (24 downto 0));
end component;

--Inputs
signal clr0 : std_logic := '0';
signal clk : std_logic := '0';

--Outputs
signal PC : std_logic_vector(15 downto 0);
signal RD1 : std_logic_vector(15 downto 0);
signal RD2 : std_logic_vector(15 downto 0);
signal resALU : std_logic_vector(15 downto 0);
signal BusSR : std_logic_vector(15 downto 0);
--signal m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19: STD_LOGIC;
--signal micro: std_logic_vector(19 downto 0);
--signal instru : STD_LOGIC_VECTOR (24 downto 0);

-- Clock period definitions
constant clk_period : time := 10 ns;
 
begin
    -- Instantiate the Unit Under Test (UUT)
    uut: ESCOMIPS
        Port Map ( clr0 => clr0,
                   clk => clk,
                   PC => PC,
                   RD1 => RD1,
                   RD2 => RD2,
                   resALU => resALU,
                   BusSR => BusSR);
--                   m0 => m0,
--                   m1 => m1,
--                   m2 => m2,
--                   m3 => m3,
--                   m4 => m4,
--                   m5 => m5,
--                   m6 => m6,
--                   m7 => m7,
--                   m8 => m8,
--                   m9 => m9,
--                   m10 => m10,
--                   m11 => m11,
--                   m12 => m12,
--                   m13 => m13,
--                   m14 => m14,
--                   m15 => m15,
--                   m16 => m16,
--                   m17 => m17,
--                   m18 => m18,
--                   m19 => m19);
--                   micro => micro);
--                   instru => instru);

    -- Clock process definitions
    clk_process :process
    begin
        clk <= '1';
		wait for 1 ns;
		clk <= '0';
		wait for 1 ns;
    end process;
 
    -- Stimulus process
    stim_proc: process
    begin		
        clr0 <= '1';
        wait for 4 ns;	
		clr0 <= '0';
        wait;
    end process;
end Behavioral;