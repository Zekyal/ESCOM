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

//Inicializar variable de información para el control de errores
$Informacion = 1;

//Recoger los datos del formulario
if (isset($_POST['editar'])) {
    $NSS = $_POST['NSS'];
}

//Recoger los datos del formulario
if (isset($_POST['submit'])) {
    $NSS = $_POST['NSS'];
    $Estado = $_POST['Estado'];
    $Cama = $_POST['Cama'];
    $Tratamiento = $_POST['Tratamiento'];

    //Llamar el método para editar
    $Informacion = Editar_Paciente($NSS, $Estado, $Cama, $Tratamiento);
}
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

    <!--Importar liberías para la barra de navegación-->
    <script src="css/navbar/jquery.min.js"></script>
    <script src="css/navbar/bootstrap.min.js"></script>

    <!--Icono de la página-->
    <link rel="icon" href="imagenes/icon.png">

    <title>Dashboard</title>
</head>

<body>
    <div class="container-fluid" id="Principal">
        <?php include("navbar.php"); ?>
        <div id="Contenido" style="margin-left: 25%; margin-right:5%;">
            <?php
            if ($Informacion == 0) { ?>
                <div class="alert alert-success alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    La edición se completó de manera exitosa.
                </div>
            <?php
            }
            ?>
            <?php
            if ($Informacion == 2) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>Ha ocurrido un error.</strong> Por favor, intente nuevamente.
                </div>
            <?php
            }
            ?>
            <div class="row">
                <div class="col">
                    <h1>Editar Paciente: ID <b><?php echo utf8_encode($NSS); ?></b></h1>
                </div>
            </div>
            <?php
            //Buscamos los datos para mostrarlos
            $Fila = sqlsrv_fetch_array(Mostrar_Paciente_Edit($NSS), SQLSRV_FETCH_ASSOC);
            ?>
            <div class="container-fluid" id="Formulario">
                <form action="#" method="post">
                    <input type="hidden" name="NSS" value="<?php echo utf8_encode($NSS); ?>">
                    <div class="form-group">
                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control" value="<?php echo utf8_encode($Fila['Status_pac']); ?>" id="Estado" name="Estado" placeholder="Estado" pattern="[A-Za-zÀ-ÿ0-9 ]{3,10}" maxlength="10" required>
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" value="<?php echo utf8_encode($Fila['Cama']); ?>" id="Cama" name="Cama" placeholder="Cama" pattern="[0-9]{1,3}" maxlength="3">
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" value="<?php echo utf8_encode($Fila['Tratamiento']); ?>" id="Tratamiento" name="Tratamiento" placeholder="Tratamiento" pattern="[A-Za-zÀ-ÿ0-9.,-/ ]{3,60}" maxlength="60" required>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer text-center boton container">
                        <div class="row">
                            <div class="col">
                                <form action="#" method="post">
                                    <button class="btn btn-outline-primary" type="submit" name="submit"> Editar</button>
                                </form>
                            </div>
                            <div class="col">
                                <form action="admin_pacientes.php">
                                    <button class="btn btn-outline-danger" type="submit" name="submit"> Cancelar</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>

</html>