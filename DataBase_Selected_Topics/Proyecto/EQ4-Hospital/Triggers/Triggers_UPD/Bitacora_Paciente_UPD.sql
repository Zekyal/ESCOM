CREATE TRIGGER TR_UPD_Paciente
ON Paciente
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesión del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@Id_persona INT
DECLARE @@NSS INT
DECLARE @@Status_pac VARCHAR(10)
DECLARE @@Cama INT
DECLARE @@Tratamiento VARCHAR(60)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@Id_persona_d INT
DECLARE @@NSS_d INT
DECLARE @@Status_pac_d VARCHAR(10)
DECLARE @@Cama_d INT
DECLARE @@Tratamiento_d VARCHAR(60)

--Declaramos el cursos que recorrerá las tuplas de inserted
declare cursor_inserta_persona cursor
for select  Id_persona,NSS,Status_pac,Cama,Tratamiento
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrerá las tuplas de deleted
declare cursor_borra_persona cursor
for select Id_persona,NSS,Status_pac,Cama,Tratamiento
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@Id_persona,@@NSS,@@Status_pac,@@Cama,@@Tratamiento
fetch next from cursor_borra_persona into  @@Id_persona_d,@@NSS_d,@@Status_pac_d,@@Cama_d,@@Tratamiento_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@NSS IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@Id_persona <> @@Id_persona_d
	BEGIN
		INSERT INTO Bitacora_paciente_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_persona,'Paciente','Id_Persona', @@Id_persona_d,@@Id_persona_d
	END
IF @@Status_pac <> @@Status_pac_d
	BEGIN
		INSERT INTO Bitacora_paciente_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_persona,'Paciente','Status_pac', @@Status_pac_d,@@Status_pac
	END
IF @@Cama <> @@Cama_d
	BEGIN
		INSERT INTO Bitacora_paciente_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_persona,'Paciente','Cama', @@Cama_d,@@Cama
	END

IF @@Tratamiento <> @@Tratamiento_d
	BEGIN
		INSERT INTO Bitacora_paciente_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Id_persona,'Paciente','Tratamiento', @@Status_pac_d,@@Status_pac
	END
END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@Id_persona,@@NSS,@@Status_pac,@@Cama,@@Tratamiento
fetch next from cursor_borra_persona into  @@Id_persona_d,@@NSS_d,@@Status_pac_d,@@Cama_d,@@Tratamiento_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona