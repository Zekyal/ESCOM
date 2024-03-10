<?php
//Edición: 15/05/2022
include("funciones.php");

//Validaremos que el usuario con sesión iniciada pertenece a esta página
$Sesion = Validar_Sesion();
if ($Sesion == 1) {
    $Usuario = $_SESSION['Usuario'];
    $Tipo_Usuario = $_SESSION['Tipo_Usuario'];

    if ($Tipo_Usuario != "Paciente") {
        //Lo regresamos a la página que le corresponde
        header("Location: index.php");
    }
}

//Iniciamos los querys para colocar la info de la base de datos
$Informacion_SQL = Mostrar_Paciente($Usuario);

//Hacemos fetch de la información para mostrarla
$Fila = sqlsrv_fetch_array($Informacion_SQL, SQLSRV_FETCH_ASSOC);
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd>
<html lang="es">

<head>
    <!--Asignar lenguaje-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    <!--Asignación para trabajar en dispositivos móviles-->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!--Importar css propios-->
    <link rel="stylesheet" href="css/general.css">

    <!--Importar css local de bootstrap-->
    <link rel="stylesheet" href="css/bootstrap/css/bootstrap.min.css">

    <!--Importar scripts locales de bootstrap-->
    <script src="css/bootstrap/js/bootstrap.min.js"></script>
    <script src="css/bootstrap/js/jquery-3.5.1.min.js"></script>
    <script src="css/bootstrap/js/popper.min.js"></script>

    <!-- Kit de iconos Fontawesome-->
    <script src="https://kit.fontawesome.com/aff0d426de.js" crossorigin="anonymous"></script>

    <!--Importar liberías para la barra de navegación-->
    <script src="css/navbar/jquery.min.js"></script>
    <script src="css/navbar/bootstrap.min.js"></script>

    <!--Icono de la página-->
    <link rel="icon" href="imagenes/icon.png">

    <title>Paciente</title>
</head>

<body>
    <?php include("header_paciente.php") ?>
    <div class="container-fluid" id="Principal" style="margin-top: 80px;">
        <div id="Contenido">
            <div id="Datos_Personales">
                <div class="row">
                    <div class="col-md-12">
                        <h1><?php echo utf8_encode($Fila['Nombre']); ?></h1>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4">
                        <p><b>NSS: </b><?php echo utf8_encode($NSS = $Fila['NSS']); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>ID Persona: </b><?php echo utf8_encode($Fila['Id_persona']); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>Sexo: </b><?php echo utf8_encode($Fila['Sexo']); ?></p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4">
                        <p><b>Fecha de Nacimiento: </b><?php echo date_format($Fila['Fechanac'], 'd/m/Y'); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>Estatus: </b><?php echo utf8_encode($Fila['Status_pac']); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>Tratamiento </b><?php echo utf8_encode($Fila['Tratamiento']); ?></p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4">
                        <p><b>Cama: </b><?php echo utf8_encode($Fila['Cama']); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>Teléfono: </b><?php echo utf8_encode($Fila['Tel']); ?></p>
                    </div>
                    <div class="col-md-4">
                        <p><b>Correo: </b><?php echo utf8_encode($Fila['Correo']); ?></p>
                    </div>
                </div>
            </div>
            <div id="Tabla" class="table table-responsive">
                <h2>Expediente</h2>
                <table class="table-striped table-hover">
                    <thead class="thead-light">
                        <tr>
                            <th scope="col">
                                <p>ID Cita</p>
                            </th>
                            <th scope="col">
                                <p>Fecha</p>
                            </th>
                            <th scope="col">
                                <p>Doctor asignado</p>
                            </th>
                            <th scope="col">
                                <p>Diagnóstico</p>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        //Obtenemos la info de las citas
                        $Informacion_SQL = Mostrar_Expediente($NSS);
                        while ($Fila = sqlsrv_fetch_array($Informacion_SQL, SQLSRV_FETCH_ASSOC)) {
                        ?>
                            <tr>
                                <td>
                                    <p><?php echo utf8_encode($Fila['Id_Cita']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo date_format($Fila['Fecha'], 'd/m/Y'); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['Nombre']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['Diagnostico']); ?></p>
                                </td>
                            </tr>
                        <?php
                        }
                        ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>

</html>