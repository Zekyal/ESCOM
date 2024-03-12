CREATE TRIGGER TR_UPD_CITA
ON Cita
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesión del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@NSS_pac INT
DECLARE @@Cedula_doc INT
DECLARE @@Id_Cita INT
DECLARE @@Fecha DATETIME
DECLARE @@Diagnostico VARCHAR(60)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@NSS_pac_d INT
DECLARE @@Cedula_doc_d INT
DECLARE @@Id_Cita_d INT
DECLARE @@Fecha_d DATETIME
DECLARE @@Diagnostico_d VARCHAR(60)

--Declaramos el cursos que recorrerá las tuplas de inserted
declare cursor_inserta_persona cursor
for select  NSS_pac,Cedula_doc,Id_Cita,Fecha,Diagnostico
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrerá las tuplas de deleted
declare cursor_borra_persona cursor
for select NSS_pac,Cedula_doc,Id_Cita,Fecha,Diagnostico
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@NSS_pac,@@Cedula_doc,@@Id_Cita,@@Fecha,@@Diagnostico
fetch next from cursor_borra_persona into  @@NSS_pac_d,@@Cedula_doc_d,@@Id_Cita_d,@@Fecha_d,@@Diagnostico_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@Id_Cita IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@NSS_pac <> @@NSS_pac_d
	BEGIN
		INSERT INTO Bitacora_Cita_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_Cita,'Cita','NSS_pac', @@NSS_pac_d,@@NSS_pac
	END
IF @@Cedula_doc <> @@Cedula_doc_d
	BEGIN
		INSERT INTO Bitacora_Cita_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_Cita,'Cita','Cedula_doc', @@Cedula_doc_d,@@Cedula_doc
	END
IF @@Fecha <> @@Fecha_d
	BEGIN
		INSERT INTO Bitacora_Cita_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_Cita,'Cita','Fecha', @@Fecha_d,@@Fecha
	END
IF @@Diagnostico <> @@Diagnostico_d
	BEGIN
		INSERT INTO Bitacora_Cita_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_Cita,'Cita','Diagnostico', @@Diagnostico_d,@@Diagnostico
	END

END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@NSS_pac,@@Cedula_doc,@@Id_Cita,@@Fecha,@@Diagnostico
fetch next from cursor_borra_persona into  @@NSS_pac_d,@@Cedula_doc_d,@@Id_Cita_d,@@Fecha_d,@@Diagnostico_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona