-- 1. Obtener todos los empleados que se dieron de alta entre una determinada fecha inicial y fecha final y que pertenecen a un determinada aerolinea 
SELECT * FROM Empleado
SELECT * FROM Persona
SELECT * FROM Aerolinea

ALTER PROC SEL_empleadoFechaAlta(
		@fechaInicial datetime,
		@fechaFinal datetime
)
AS
	SELECT E.idEmpleado, P.nombre, P.paterno, P.materno, E.fechaIngreso AS fechaAlta, A.Nombre AS aerolinea FROM Empleado E
	INNER JOIN Persona P 
	ON P.IdPersona = E.idPersona
	INNER JOIN Aerolinea A
	ON A.AerolineaId = E.AerolineaId
	WHERE E.fechaIngreso > @fechaInicial AND E.fechaIngreso < @fechaFinal

EXEC SEL_empleadoFechaAlta '20050501', '20100908'
EXEC SEL_empleadoFechaAlta '20080101', '20090101'


-- 2. Crear un procedimiento que inserte un empleado y valide su previa existencia 
SELECT * FROM Empleado
SELECT * FROM Persona
SELECT * FROM Direccion

ALTER PROC INS_empleado (
	@nombre varchar(50), --
	@paterno varchar(50), --
	@materno varchar(50), --
	@telefono varchar(50),
	@nacimiento datetime,
	@sexo bit,
	@calle varchar(50), --
	@numero varchar(10), --
	@colonia varchar(50), --
	@codigoPostal varchar(50), --
	@tipoEmpleado int,
	@sueldo money
)
AS
	BEGIN
		DECLARE @idDireccion int, @idPersona int
		SELECT @idDireccion = direccionId FROM Direccion WHERE calle = @calle AND numero = @numero AND colonia = @colonia AND codigoPostal = @codigoPostal
		
		IF (ISNULL(@idDireccion, 0) <> 0)
			BEGIN
				IF NOT EXISTS(	SELECT * FROM Persona
								WHERE nombre = @nombre 
								AND paterno = @paterno
								AND materno = @materno)
					BEGIN
						INSERT INTO Persona VALUES(@nombre, @paterno, @materno, @idDireccion, @telefono, @nacimiento, @sexo)
						SELECT TOP 1 @idPersona = IdPersona FROM Persona ORDER BY IdPersona DESC
						INSERT INTO Empleado(idPersona, idTipoEmpleado, fechaIngreso, sueldo) VALUES(@idPersona, @tipoEmpleado, GETDATE(), @sueldo)
					END
				ELSE
					SELECT 'ERROR: Este empleado ya se encuetra registrado en la base de datos' AS error
			END
		ELSE
			BEGIN
				INSERT INTO Direccion VALUES(@calle, @numero, @colonia, @codigoPostal)
				SELECT TOP 1 @idDireccion = direccionId FROM Direccion ORDER BY direccionId DESC
				INSERT INTO Persona VALUES(@nombre, @paterno, @materno, @idDireccion , @telefono, @nacimiento, @sexo)
				SELECT TOP 1 @idPersona = IdPersona FROM Persona ORDER BY IdPersona DESC
				INSERT INTO Empleado(idPersona, idTipoEmpleado, fechaIngreso, sueldo) VALUES(@idPersona, @tipoEmpleado, GETDATE(), @sueldo)
			END
	END

EXEC INS_empleado 'Martín', 'Carmona', 'Bautista', '23633162', '1980-10-17 00:00:00.000', 0, 'Álvaro Obregón', 34, 'Roma', '06700', 3, 1700
EXEC INS_empleado 'Mario', 'Santillana', 'Bautista', '23633162', '1980-10-17 00:00:00.000', 0, 'Álvaro Obregón', 34, 'Roma', '06700', 3, 1700
EXEC INS_empleado 'Mario', 'Santillana', 'Bautista', '23633162', '1980-10-17 00:00:00.000', 0, 'Pesos', 55, 'Heroes de Cerro Prieto', '07960', 3, 1700
DELETE FROM Persona WHERE IdPersona = 1028
DELETE FROM Direccion WHERE direccionId = 24

-- 3. Crear un procemimiento que recupere el nombre de empleado, cantidad de empleados y idEmpleado a partir del idAerolinea 
CREATE PROCEDURE empleadosAerolineaID @idAerolinea int
AS
	BEGIN
		DECLARE @tablaEmpleados TABLE(									
			idAerolinea INT,
			idEmpleado INT,
			NombreEmpleado VARCHAR(100)
		)
	
		INSERT INTO @tablaEmpleados 
		SELECT a.AerolineaId, e.idEmpleado, p.nombre + ' ' + p.paterno + ' ' + ISNULL(p.materno, '') FROM Aerolinea a
		INNER JOIN Empleado e
		ON a.AerolineaId = e.AerolineaId
		INNER JOIN Persona p
		ON e.idPersona = p.IdPersona
		WHERE a.AerolineaId = @idAerolinea

		DECLARE @idAero AS VARCHAR(2) 
		SELECT @idAero = CONVERT(varchar, idAerolinea) FROM @tablaEmpleados

		SELECT 'La cantidad de empleados que trabajan en la Aerolinea con ID ' + @idAero + ' es:' + STR(COUNT(*)) AS NumeroEmpleados FROM @tablaEmpleados
		SELECT idEmpleado, NombreEmpleado FROM @tablaEmpleados
	END

EXEC empleadosAerolineaID @idAerolinea = 5 
EXEC empleadosAerolineaID 3 
DROP PROCEDURE empleadosAerolineaID;

-- 4. Crear un procedimiento igual que el anterior, pero que recupera también las personas que trabajan en dicha aerolinea, pasandole como parámetro el nombre.
CREATE PROCEDURE empleadosAerolineaNom @nomAerolinea varchar(50)
AS
	BEGIN
		DECLARE @tablaEmpleados TABLE(
			NombreAerolinea VARCHAR(50),
			idEmpleado INT,
			NombreEmpleado VARCHAR(100)
		)
	
		INSERT INTO @tablaEmpleados 
		SELECT a.Nombre, e.idEmpleado, p.nombre + ' ' + p.paterno + ' ' + ISNULL(p.materno, '') FROM Aerolinea a
		INNER JOIN Empleado e
		ON a.AerolineaId = e.AerolineaId
		INNER JOIN Persona p
		ON e.idPersona = p.IdPersona
		WHERE a.Nombre = @nomAerolinea

		DECLARE @nombreAerolinea AS VARCHAR(50) 
		SELECT @nombreAerolinea = NombreAerolinea FROM @tablaEmpleados

		SELECT 'La cantidad de empleados que trabajan en la Aerolinea ' + @nombreAerolinea + ' es:' + STR(COUNT(*)) AS NumeroEmpleados FROM @tablaEmpleados
		SELECT idEmpleado, NombreEmpleado FROM @tablaEmpleados
	END

EXEC empleadosAerolineaNom @nomAerolinea = 'Volaris'
EXEC empleadosAerolineaNom 'InterJet'
DROP PROCEDURE empleadosAerolineaNom;

-- 5. Crear un procedimiento  para devoler sueldo, tipo de empleado y jefe pasandole el apellido.
-- 6. Crear un procedimiento igual al anterior, pero si no le pasamos ningún valor, mostrará los datos de todos los empleados.
-- 7. Crear un procedimiento para mostrar el sueldo, tipo de empleado y nombre del departamento de todos los empleados que contengan en su apellido el valor que le pasemos como parámetro
