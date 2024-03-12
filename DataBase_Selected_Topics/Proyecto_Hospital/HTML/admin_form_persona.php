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
if (isset($_POST['submit'])) {
    $Nombre = $_POST['Nombre'];
    $A_Paterno = $_POST['A_Paterno'];
    $A_Materno = $_POST['A_Materno'];
    $Fecha_Nacimiento = $_POST['Fecha_Nacimiento'];
    $Sexo = $_POST['Sexo'];
    $Telefono = $_POST['Telefono'];
    $Correo = $_POST['Correo'];
    $Tipo_Usuario = $_POST['Tipo_Usuario'];
    $Password = $_POST['Password'];

    //Llamar el método para iniciar sesión
    $Informacion = Agregar_Persona($Nombre, $A_Paterno, $A_Materno, $Fecha_Nacimiento, $Sexo, $Telefono, $Tipo_Usuario, $Correo, $Password);
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
                    El registro se completó de manera exitosa.
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
            <?php
            if ($Informacion == 5) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>El Correo ya se encuentra registrado.</strong> Por favor, intente nuevamente.
                </div>
            <?php
            }
            ?>
            <div class="row">
                <div class="col">
                    <h1>Agregar Persona</h1>
                </div>
            </div>
            <div class="container-fluid" id="Formulario">
                <form action="#" method="post">
                <input type="hidden" name="ID_Persona" value="<?php echo utf8_encode($Fila['ID_persona']); ?>">
                    <div class="form-group">
                        <div class="row">
                            <div class="col-md-4">
                                <input type="text" class="form-control" value="" id="Nombre" name="Nombre" placeholder="Nombre" pattern="[A-Za-zÀ-ÿ ]{3,12}" maxlength="12" required>
                            </div>
                            <div class="col-md-4">
                                <input type="text" class="form-control" value="" id="A_Paterno" name="A_Paterno" placeholder="Apellido Paterno" pattern="[A-Za-zÀ-ÿ ]{3,12}" maxlength="12" required>
                            </div>
                            <div class="col-md-4">
                                <input type="text" class="form-control" value="" id="A_Materno" name="A_Materno" placeholder="Apellido Materno" pattern="[A-Za-zÀ-ÿ ]{3,12}" maxlength="12">
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="row">
                            <div class="col-md-4">
                                <input type="date" class="form-control" value="" id="Fecha_Nacimiento" name="Fecha_Nacimiento" placeholder="Fecha de Nacimiento" min="1922-01-01" max="2022-06-16" required>
                            </div>
                            <div class="col-md-4">
                                <select class="form-control" name="Sexo" id="Sexo" aria-placeholder="Sexo">
                                    <option value="M">Mujer</option>
                                    <option value="H">Hombre</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <input type="text" class="form-control" value="" id="Telefono" name="Telefono" placeholder="Teléfono (10-12 dígitos)" pattern="[0-9]{10,12}" maxlength="12">
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="row">
                            <div class="col-md-4">
                                <input type="email" class="form-control" value="" id="Correo" name="Correo" placeholder="Correo" pattern="[A-Za-z0-9@._-,]{1,32}" required>
                            </div>
                            <div class="col-md-4">
                                <select class="form-control" name="Tipo_Usuario" id="Tipo_Usuario" aria-placeholder="Tipo de Usuario">
                                    <option value="ADMIN">Administrador</option>
                                    <option value="Recepcionista">Recepcionista</option>
                                    <option value="Doctor">Doctor</option>
                                    <option value="Paciente">Paciente</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <input type="password" class="form-control" value="" id="Password" name="Password" placeholder="Contraseña" maxlength="8" required>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer text-center boton container">
                        <div class="row">
                            <div class="col">
                                <form action="#" method="post">
                                    <button class="btn btn-outline-primary" type="submit" name="submit"> Agregar</button>
                                </form>
                            </div>
                            <div class="col">
                                <form action="admin_personas.php">
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