CREATE TRIGGER TR_UPD_Persona
ON Persona
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesión del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@ID_Persona INT
DECLARE @@Nombre VARCHAR(12)
DECLARE @@A_Paterno VARCHAR(12)
DECLARE @@A_Materno VARCHAR(12)
DECLARE @@Fechanac DATETIME
DECLARE @@Sexo VARCHAR(1)
DECLARE @@Tel VARCHAR(12)
DECLARE @@Correo VARCHAR(32)
DECLARE @@Contrasenia VARCHAR(8)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@ID_Persona_d INT
DECLARE @@Nombre_d VARCHAR(12)
DECLARE @@A_Paterno_d VARCHAR(12)
DECLARE @@A_Materno_d VARCHAR(12)
DECLARE @@Fechanac_d DATETIME
DECLARE @@Sexo_d VARCHAR(1)
DECLARE @@Tel_d VARCHAR(12)
DECLARE @@Correo_d VARCHAR(32)
DECLARE @@Contrasenia_d VARCHAR(8)

--Declaramos el cursos que recorrerá las tuplas de inserted
declare cursor_inserta_persona cursor
for select  ID_Persona,nombre,A_Paterno,A_materno,Fechanac,Sexo,Tel,Correo,Contrasenia 
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrerá las tuplas de deleted
declare cursor_borra_persona cursor
for select ID_Persona,nombre,A_Paterno,A_materno,Fechanac,Sexo,Tel,Correo,Contrasenia 
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@ID_Persona,@@Nombre,@@A_Paterno,@@A_Materno,@@Fechanac,@@Sexo,@@Tel,@@Correo,@@Contrasenia
fetch next from cursor_borra_persona into  @@ID_Persona_d,@@Nombre_d,@@A_Paterno_d,@@A_Materno_d,@@Fechanac_d,@@Sexo_d,@@Tel_d,@@Correo_d,@@Contrasenia_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@ID_Persona IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@Nombre <> @@Nombre_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Nombre', @@Nombre_d,@@Nombre
	END
IF @@A_Paterno <> @@A_Paterno_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','A_Paterno', @@A_Paterno_d,@@A_Paterno
	END
IF @@A_Materno <> @@A_Materno_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','A_Materno', @@A_Materno_d,@@A_Materno
	END

IF @@Fechanac <> @@Fechanac_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Fechanac', @@Fechanac_d,@@Fechanac
	END

IF @@Sexo <> @@Sexo_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Sexo', @@Sexo_d,@@Sexo
	END

IF @@Tel <> @@Tel_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Tel', @@Tel_d,@@Tel
	END

IF @@Correo <> @@Correo_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Correo', @@Correo_d,@@Correo
	END

IF @@Contrasenia <> @@Contrasenia_d
	BEGIN
		INSERT INTO Bitacora_persona_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_Persona,'Persona','Contrasenia', @@Contrasenia_d,@@Contrasenia
	END

END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@ID_Persona,@@Nombre,@@A_Paterno,@@A_Materno,@@Fechanac,@@Sexo,@@Tel,@@Correo,@@Contrasenia
fetch next from cursor_borra_persona into  @@ID_Persona_d,@@Nombre_d,@@A_Paterno_d,@@A_Materno_d,@@Fechanac_d,@@Sexo_d,@@Tel_d,@@Correo_d,@@Contrasenia_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona