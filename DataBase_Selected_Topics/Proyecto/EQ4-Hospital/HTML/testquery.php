<?php
//Importar el archivo de funciones
include ("funciones.php");

//Variable de conexión
$conn = Conectar();

//Ejemplo de Query
print "<h2>Query Example 1 | Fetching by Associate Array</h2>";
$sql = "SELECT * FROM Persona";
print "SQL: $sql<br><br>";

//sqlsrv_query es una función para hacer la conexión con la base de datos e introducir el query
$result = sqlsrv_query($conn, $sql);

//Si truena mandamos error
if($result === false) {
    die(print_r(sqlsrv_errors(), true));
}

//Hacemos fetch array de los datos
while($row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)) {
    print(utf8_encode($row['Nombre']));
    print" ";
    print(utf8_encode($row['A_Paterno']));
    print" ";
    print(utf8_encode($row['A_Materno']));
    print" ";
    print "<br>";
}
