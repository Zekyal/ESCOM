--1.Crear una función que reciba como parámetro la fecha de nacimiento y devuelva la edad al día de hoy*/
--2.crear una función que reciba la matrícula de un avión y devuelva la siguiente fecha de mantenimiento */
/*3.crear una función que reciba una fecha y muestre la siguiente información del vuelo más cercano:
	matrícula del avión, nombre del vendedor, nombre del cliente, fecha de vuelo y precio del asiento*/
/*4.crear una función que reciba el id de un cliente y el id de un vuelo y regrese el precio del vuelo 
considerando el descuento por tipo de cliente*/
/*5.Crear una función que regrese el RFC de todas las personas de la base de datos o se especifique algún 
IdPersona para solo obtener el de una*/
/*6.crear una función que reciba como parámetros el Id de un cliente, y una fecha inicio y fin. Como salida
debe indicar cuantas veces ha viajado*/
DROP FUNCTION NumViajes

CREATE FUNCTION dbo.NumViajes (@IdCliente INT, @FechaInicio DATE, @FechaFinal DATE)
RETURNS INT
AS
	BEGIN
		DECLARE @cantViajes INT
		SELECT @cantViajes = COUNT(*) FROM Venta venta
		INNER JOIN Vuelo vuelo
		ON venta.idVuelo = vuelo.idVuelo
		WHERE idCliente = @IdCliente AND fechaVuelo BETWEEN @FechaInicio AND @FechaFinal
		RETURN @cantViajes
	END

SELECT dbo.NumViajes(1, '2014-01-01', '2014-12-31') AS viajesRealizados 
/*7.Crear una función que reciba como parámetro un sueldo base y que muestre el nombre completo de los empleados
que tengan un salario mayor o igual al parámetro de entrada de mostrar la cantidad de años que lleva el 
empleado desde su fecha de ingreso.*/
DROP FUNCTION Salario

CREATE FUNCTION dbo.Salario(@SueldoBase MONEY)
RETURNS @tbEmpleado TABLE(
	nombreEmpleado VARCHAR(100),
	antigüedadAños INT
)
AS
BEGIN
	INSERT INTO @tbEmpleado
	SELECT nombre + ' ' + paterno + ' ' + ISNULL(materno, ''), DATEDIFF(year, fechaIngreso, GETDATE())  FROM Empleado e
	INNER JOIN Persona p
	ON e.idPersona = p.IdPersona
	WHERE sueldo >= @SueldoBase
	RETURN
END

SELECT * FROM Salario(40000)
/*8.modificar la funciòn ObtenerDireccionEmpleado, en caso de que el Id proporcionado no tenga jefe, mostrar en la columna
direccion completa la siguiente leyenda "información confidencial"*/
/*9.crear una función que devuelva el precio por asiento de todos los vuelos y que reciba un parametro opcional 
que indique si es temporada alta, en su caso aumentar 20% el precio por asiento*/

