<?php
//Edición: 15/05/2022
include("funciones.php");

//Validaremos que el usuario con sesión iniciada pertenece a esta página
$Sesion = Validar_Sesion();
if ($Sesion == 1) {
    $Usuario = $_SESSION['Usuario'];
    $Tipo_Usuario = $_SESSION['Tipo_Usuario'];

    if ($Tipo_Usuario != "ADMIN") {
        //Lo regresamos a la página que le corresponde
        header("Location: index.php");
    }
}

//Iniciamos los querys para colocar la info de la base de datos
$Informacion_SQL = Mostrar_Citas();
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

    <!--Importar barra lateral-->
    <link rel="stylesheet" type="text/css" href="css/sidenav.css">

    <!--Icono de la página-->
    <link rel="icon" href="imagenes/icon.png">

    <title>Dashboard</title>
</head>

<body>
    <div class="container-fluid" id="Principal">
        <?php include("navbar.php"); ?>

        <div id="Contenido" style="margin-left: 25%; margin-right:5%;">
            <div class="row">
                <div class="col-md-10">
                    <h1>Citas</h1>
                </div>
                <div>
                    <button class="btn btn-outline-secondary" type="submit" name="submit"><i class="fas fa-plus"></i> Nuevo</button>
                </div>
            </div>
            <div id="Tabla" class="table table-responsive">
                <table class="table-striped table-hover">
                    <thead class="thead-light">
                        <tr>
                            <th scope="col">
                                <p>ID Cita</p>
                            </th>
                            <th scope="col">
                                <p>NSS Paciente</p>
                            </th>
                            <th scope="col">
                                <p>Cédula Doctor</p>
                            </th>
                            <th scope="col">
                                <p>Fecha</p>
                            </th>
                            <th scope="col">
                                <p>Diagnóstico</p>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        while ($Fila = sqlsrv_fetch_array($Informacion_SQL, SQLSRV_FETCH_ASSOC)) {
                        ?>
                            <tr>
                                <td>
                                    <p><?php echo utf8_encode($Fila['Id_Cita']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['NSS_pac']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['Cedula_doc']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo date_format($Fila['Fecha'],'d/m/Y H:i'); ?></p>
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