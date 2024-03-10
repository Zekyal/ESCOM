create database IPRecibeRespuesta;
use IPRecibeRespuesta;

create table Datos(
	IP_que_envia varchar(15) not null, 
	IP_que_recibe varchar(15) not null,
	MAC_IP_que_recibe varchar(20) not null
);
--INSERT into datos(IP_que_envia, IP_que_recibe, MAC_IP_que_recibe) 
--VALUES ("000.000.000.000", "000.000.000.001", "añldfjalkfja");


