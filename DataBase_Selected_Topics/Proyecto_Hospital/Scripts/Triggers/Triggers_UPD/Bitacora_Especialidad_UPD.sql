CREATE TRIGGER TR_UPD_Especialidad
ON Especialidad
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesi�n del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@ID_esp INT
DECLARE @@nombre_esp VARCHAR(50)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@ID_esp_d INT
DECLARE @@nombre_esp_d VARCHAR(50)

--Declaramos el cursos que recorrer� las tuplas de inserted
declare cursor_inserta_persona cursor
for select  ID_esp,nombre_esp
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrer� las tuplas de deleted
declare cursor_borra_persona cursor
for select ID_esp,nombre_esp
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@ID_esp,@@nombre_esp
fetch next from cursor_borra_persona into  @@ID_esp_d,@@nombre_esp_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@ID_esp IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@nombre_esp <> @@nombre_esp_d
	BEGIN
		INSERT INTO Bitacora_Especialidad_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_esp,'Especialidad','Nombre', @@nombre_esp_d,@@nombre_esp
	END

END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@ID_esp,@@nombre_esp
fetch next from cursor_borra_persona into  @@ID_esp_d, @@nombre_esp_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona
