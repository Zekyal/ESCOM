library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity MemoriaDatos is
    generic (d : integer := 16);
    Port (dataIn: in  STD_LOGIC_VECTOR (d-1 downto 0);
          add : in  STD_LOGIC_VECTOR (d-1 downto 0);
          clk, WD : in  STD_LOGIC;
          dataOut : out  STD_LOGIC_VECTOR (d-1 downto 0));
end MemoriaDatos;

architecture Behavioral of MemoriaDatos is
    type banco is array (0 to (2**d)-1) of std_logic_vector(d-1 downto 0);
    signal memData : banco;--memoria del banco de memoria

    begin
        process(clk)
        begin 
            if (clk' event and clk = '1') then
                if (WD = '1') then
                    memData(conv_integer(add)) <= dataIn;
                end if;
            end if;
        end process;
  
    dataOut <= memData(conv_integer(add));
end Behavioral;