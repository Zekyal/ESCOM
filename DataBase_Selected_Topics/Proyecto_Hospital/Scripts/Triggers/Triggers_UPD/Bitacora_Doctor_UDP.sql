CREATE TRIGGER TR_UPD_Doctor
ON Doctor
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesión del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@Id_persona INT
DECLARE @@Id_esp INT
DECLARE @@Id_dep VARCHAR(10)
DECLARE @@Cedula INT
DECLARE @@Consultorio VARCHAR(60)
DECLARE @@Turno CHAR(1)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@Id_persona_d INT
DECLARE @@Id_esp_d INT
DECLARE @@Id_dep_d VARCHAR(10)
DECLARE @@Cedula_d INT
DECLARE @@Consultorio_d VARCHAR(60)
DECLARE @@Turno_d CHAR(1)
--Declaramos el cursos que recorrerá las tuplas de inserted
declare cursor_inserta_persona cursor
for select  Id_persona,Id_esp,Id_dep,Cedula,Consultorio,Turno
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrerá las tuplas de deleted
declare cursor_borra_persona cursor
for select Id_persona,Id_esp,Id_dep,Cedula,Consultorio,Turno
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@Id_persona,@@Id_esp,@@Id_dep,@@Cedula,@@Consultorio,@@Turno
fetch next from cursor_borra_persona into  @@Id_persona_d,@@Id_esp_d,@@Id_dep_d,@@Cedula_d,@@Consultorio_d,@@Turno_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@Cedula IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@Id_persona <> @@Id_persona_d
	BEGIN
		INSERT INTO Bitacora_Doctor_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Cedula,'Doctor','Id_Persona', @@Id_persona_d,@@Id_persona_d
	END
IF @@Id_esp <> @@Id_esp_d
	BEGIN
		INSERT INTO Bitacora_Doctor_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Cedula,'Doctor','Id_esp', @@Id_esp_d,@@Id_esp
	END
IF @@Id_dep <> @@Id_dep_d
	BEGIN
		INSERT INTO Bitacora_Doctor_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Cedula,'Doctor','Id Departamento', @@Id_dep_d,@@Id_dep
	END

IF @@Consultorio <> @@Consultorio_d
	BEGIN
		INSERT INTO Bitacora_Doctor_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Cedula,'Doctor','Consultorio', @@Consultorio_d,@@Consultorio
	END

IF @@Turno <> @@Turno_d
	BEGIN
		INSERT INTO Bitacora_Doctor_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@Cedula,'Doctor','Turno', @@Turno_d,@@Turno
	END
END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@Id_persona,@@Id_esp,@@Id_dep,@@Cedula,@@Consultorio,@@Turno
fetch next from cursor_borra_persona into  @@Id_persona_d,@@Id_esp_d,@@Id_dep_d,@@Cedula_d,@@Consultorio_d,@@Turno_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona

