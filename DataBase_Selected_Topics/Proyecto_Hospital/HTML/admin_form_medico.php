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
    $ID_Persona = $_POST['ID_Persona'];
    $Cedula = $_POST['Cedula'];
    $Turno = $_POST['Turno'];
    $Consultorio = $_POST['Consultorio'];
    $Departamento = $_POST['Departamento'];
    $Especialidad = $_POST['Especialidad'];

    //Llamar el método para iniciar sesión
    $Informacion = Agregar_Medico($ID_Persona, $Cedula, $Turno, $Consultorio, $Departamento, $Especialidad);
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
            if ($Informacion == 3) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>El ID Persona no se encuentra registrado.</strong> Por favor, intente nuevamente.
                </div>
            <?php
            }
            ?>
            <?php
            if ($Informacion == 4) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>El ID Persona indicado no es de tipo doctor.</strong> Por favor, intente nuevamente.
                </div>
            <?php
            }
            ?>
            <?php
            if ($Informacion == 5) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>El ID Persona / Cédula ya se encuentra registrado.</strong> Por favor, intente nuevamente.
                </div>
            <?php
            }
            ?>
            <div class="row">
                <div class="col">
                    <h1>Agregar Doctor</h1>
                </div>
            </div>
            <div class="container-fluid" id="Formulario">
                <form action="#" method="post">
                    <div class="form-group">
                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control" value="" id="ID_Persona" name="ID_Persona" placeholder="ID Persona" pattern="[0-9]{1,}" required>
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" value="" id="Cedula" name="Cedula" placeholder="Cédula (8 dígitos)" pattern="[0-9]{8}" maxlength="8" required>
                            </div>
                            <div class="col">
                                <select name="Turno" id="Turno" class="form-control">
                                    <option value="M">Matutino</option>
                                    <option value="V">Vespertino</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="row">
                            <div class="col">
                                <input type="text" class="form-control" value="" id="Consultorio" name="Consultorio" placeholder="Consultorio" pattern="[0-9]{1,3}" maxlength="3" required>
                            </div>
                            <div class="col">
                                <select name="Especialidad" id="Especialidad" class="form-control">
                                    <?php
                                    $Especialidades = Mostrar_Especialidades();
                                    while ($Fila = sqlsrv_fetch_array($Especialidades, SQLSRV_FETCH_ASSOC)) {
                                    ?>
                                        <option value="<?php echo utf8_encode($Fila['ID_esp']); ?>"><?php echo utf8_encode($Fila['nombre_esp']); ?></option>
                                    <?php
                                    }
                                    ?>
                                </select>
                            </div>
                            <div class="col">
                                <select name="Departamento" id="Departamento" class="form-control">
                                    <?php
                                    $Departamentos = Mostrar_Departamentos();
                                    while ($Fila = sqlsrv_fetch_array($Departamentos, SQLSRV_FETCH_ASSOC)) {
                                    ?>
                                        <option value="<?php echo utf8_encode($Fila['ID_dep']); ?>"><?php echo utf8_encode($Fila['nombre_dept']); ?></option>
                                    <?php
                                    }
                                    ?>
                                </select>
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
                                <form action="admin_medicos.php">
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