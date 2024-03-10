CREATE TRIGGER TR_UPD_DEPARTAMENTO
ON Departamento
AFTER UPDATE --TRIGGER DE TIPO UPDATE 
AS  
set nocount on   --Para que no cuente las filas afectadas de la sesión del usuario 
---------------------------------------------
-----------VALORES NUEVOS--------------------
---------------------------------------------
DECLARE @@ID_dep INT
DECLARE @@num_ext INT
DECLARE @@nombre_dept VARCHAR(40)

---------------------------------------------
-----------VALORES ANTIGUOS------------------
---------------------------------------------
DECLARE @@ID_dep_d INT
DECLARE @@num_ext_d INT
DECLARE @@nombre_dept_d VARCHAR(40)

--Declaramos el cursos que recorrerá las tuplas de inserted
declare cursor_inserta_persona cursor
for select  ID_dep,num_ext,nombre_dept
 FROM inserted   --TABLA INSERTED
for read only
open cursor_inserta_persona


--Declaramos el cursos que recorrerá las tuplas de deleted
declare cursor_borra_persona cursor
for select ID_dep,num_ext,nombre_dept
 FROM deleted --TABLA DELETED
for read only

open cursor_borra_persona
--Llenamos variables
fetch next from cursor_inserta_persona into @@ID_dep,@@num_ext,@@nombre_dept
fetch next from cursor_borra_persona into  @@ID_dep_d,@@num_ext_d,@@nombre_dept_d

while (@@fetch_status <> -1) /* no sea eof*/
BEGIN

IF @@ID_dep IS NOT NULL 
BEGIN  --valida si el registro no es nullo
IF @@num_ext <> @@num_ext_d
	BEGIN
		INSERT INTO Bitacora_Departamento_UPD (operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_dep,'Departamento','num_ext', @@num_ext_d,@@num_ext
	END
IF @@nombre_dept <> @@nombre_dept_d
	BEGIN
		INSERT INTO Bitacora_Departamento_UPD(operacion, usuario, host,modificado,PK,tabla,campo,valor,valor_nuevo)
		SELECT 'UPDATE',SUSER_NAME(),@@SERVERNAME,GETDATE(),@@ID_dep,'Departamento','nombre_dept', @@nombre_dept_d,@@nombre_dept
	END


END --cierra begin valida si el registro no es nullo

-- Incrementamos el registro
fetch next from cursor_inserta_persona into @@ID_dep,@@num_ext,@@nombre_dept
fetch next from cursor_borra_persona into  @@ID_dep_d,@@num_ext_d,@@nombre_dept_d

END -- Cierra While

-- Se cierra Cursor  "SIEMPRE DEBE HACERSE"
close cursor_inserta_persona
deallocate  cursor_inserta_persona

close cursor_borra_persona
deallocate  cursor_borra_persona