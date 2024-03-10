--1.Crear una funci�n que reciba como par�metro la fecha de nacimiento y devuelva la edad al d�a de hoy*/
--2.crear una funci�n que reciba la matr�cula de un avi�n y devuelva la siguiente fecha de mantenimiento */
/*3.crear una funci�n que reciba una fecha y muestre la siguiente informaci�n del vuelo m�s cercano:
	matr�cula del avi�n, nombre del vendedor, nombre del cliente, fecha de vuelo y precio del asiento*/
/*4.crear una funci�n que reciba el id de un cliente y el id de un vuelo y regrese el precio del vuelo 
considerando el descuento por tipo de cliente*/
/*5.Crear una funci�n que regrese el RFC de todas las personas de la base de datos o se especifique alg�n 
IdPersona para solo obtener el de una*/
/*6.crear una funci�n que reciba como par�metros el Id de un cliente, y una fecha inicio y fin. Como salida
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
/*7.Crear una funci�n que reciba como par�metro un sueldo base y que muestre el nombre completo de los empleados
que tengan un salario mayor o igual al par�metro de entrada de mostrar la cantidad de a�os que lleva el 
empleado desde su fecha de ingreso.*/
DROP FUNCTION Salario

CREATE FUNCTION dbo.Salario(@SueldoBase MONEY)
RETURNS @tbEmpleado TABLE(
	nombreEmpleado VARCHAR(100),
	antig�edadA�os INT
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
/*8.modificar la funci�n ObtenerDireccionEmpleado, en caso de que el Id proporcionado no tenga jefe, mostrar en la columna
direccion completa la siguiente leyenda "informaci�n confidencial"*/
/*9.crear una funci�n que devuelva el precio por asiento de todos los vuelos y que reciba un parametro opcional 
que indique si es temporada alta, en su caso aumentar 20% el precio por asiento*/

