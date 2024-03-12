<?php
//Incluir archivos de funciones
include("funciones.php");

//Validar que la sesión no se haya iniciado aún
session_start();
if (isset($_SESSION['Usuario'])) {
    header("Location: index.php");
}

//Inicializar variable de información
$Informacion = 1;

//Recoger los datos del formulario
if (isset($_POST['submit'])) {
    $Correo = $_POST['Usuario'];
    $Password = $_POST['Password'];

    //Llamar el método para iniciar sesión
    $Informacion = Iniciar_Sesión($Correo, $Password);
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
    <link rel="stylesheet" href="css/login.css">

    <!--Importar css local de bootstrap-->
    <link rel="stylesheet" href="css/bootstrap/css/bootstrap.min.css">

    <!--Importar scripts locales de bootstrap-->
    <script src="css/bootstrap/js/bootstrap.min.js"></script>
    <script src="css/bootstrap/js/jquery-3.5.1.min.js"></script>
    <script src="css/bootstrap/js/popper.min.js"></script>

    <!-- Kit de iconos Fontawesome-->
    <script src="https://kit.fontawesome.com/aff0d426de.js"></script>

    <!--Importar liberías para la barra de navegación-->
    <script src="css/navbar/jquery.min.js"></script>
    <script src="css/navbar/bootstrap.min.js"></script>

    <!--Icono de la página-->
    <link rel="icon" href="imagenes/icon.png">

    <title>Iniciar Sesión</title>
</head>

<body>
    <?php
    if ($Informacion == 0) { ?>
        <div class="alert alert-danger alert-dismissible fade show">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Error</strong>, correo o contraseña incorrectos. Intente nuevamente.
        </div>
    <?php
    }
    ?>
    <div class="container-lg">
        <div class="row justify-content-center align-items-center vh-100">
            <div id="Contenido" class="col-md-7">
                <div id="Logo" class="text-center">
                    <img src="imagenes/logo.png" id="LogoImg" class="img-fluid" alt="Logo El Burrito Blanco">
                </div>
                <h1 id="Titulo_Formulario">Bienvenido</h1>
                <div id="Formulario">
                    <form action="#" method="post">
                        <div class="form-group">
                            <div class="input-group input-group-lg">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fa fa-user"></i></span>
                                </div>
                                <input id="Usuario" class="form-control" type="text" name="Usuario" placeholder="Correo">
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="input-group input-group-lg">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-key"></i></span>
                                </div>
                                <input id="Password" class="form-control" type="password" name="Password" placeholder="Contraseña">
                            </div>
                        </div>
                        <div class="text-center boton">
                            <button class="btn btn-outline-primary" type="submit" name="submit"><i class="fas fa-sign-in-alt"></i> Iniciar sesión</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>

</html>