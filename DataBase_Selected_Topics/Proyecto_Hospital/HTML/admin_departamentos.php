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

//Borrar departamento
//Recoger los datos del formulario
if (isset($_POST['borrar'])) {
    $ID_Departamento = $_POST['ID_Departamento'];

    //Llamar al método para borrar
    $Informacion = Borrar_Departamento($ID_Departamento);
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

    <!--Importar scripts propios-->
    <script type="text/javascript" src="scripts/confirmar_borrado.js"></script>

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
                    El registro se borró de manera exitosa.
                </div>
            <?php
            }
            ?>
            <?php
            if ($Informacion == 6) { ?>
                <div class="alert alert-danger alert-dismissible fade show">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>Ha ocurrido un error.</strong> Borre las llaves foráneas e intente nuevamente.
                </div>
            <?php
            }
            ?>
            <div class="row">
                <div class="col-md-10">
                    <h1>Departamentos</h1>
                </div>
                <div>
                    <form action="admin_form_departamentos.php">
                        <button class="btn btn-outline-secondary" type="submit" name="submit" onclick="window.location.href='departamentos.php'"><i class="fas fa-plus"></i> Nuevo</button>
                    </form>
                </div>
            </div>
            <div id="Tabla" class="table table-responsive">
                <table class="table-striped table-hover">
                    <thead class="thead-light">
                        <tr>
                            <th scope="col">
                                <p>ID Departamento</p>
                            </th>
                            <th scope="col">
                                <p>Nombre</p>
                            </th>
                            <th scope="col">
                                <p>Numero de extensión</p>
                            </th>
                            <th></th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        //Iniciamos los querys para colocar la info de la base de datos
                        $Informacion_SQL = Mostrar_Departamentos();

                        while ($Fila = sqlsrv_fetch_array($Informacion_SQL, SQLSRV_FETCH_ASSOC)) {
                        ?>
                            <tr>
                                <td>
                                    <p><?php echo utf8_encode($Fila['ID_dep']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['nombre_dept']); ?></p>
                                </td>
                                <td>
                                    <p><?php echo utf8_encode($Fila['num_ext']); ?></p>
                                </td>
                                <td>
                                    <form action="edit_departamento.php" method="post">
                                        <input type="hidden" name="ID_Departamento" value="<?php echo utf8_encode($Fila['ID_dep']); ?>">
                                        <button class="btn btn-outline-secondary" type="submit" name="editar"><i class="fas fa-edit"></i></button>
                                    </form>
                                </td>
                                <td>
                                    <form action="#" method="post">
                                        <input type="hidden" name="ID_Departamento" value="<?php echo utf8_encode($Fila['ID_dep']); ?>">
                                        <button class="btn btn-outline-secondary" type="submit" name="borrar" onclick="return Confirmar_Borrado('<?php echo utf8_encode($Fila['ID_dep']); ?>')"><i class="fas fa-trash"></i></button>
                                    </form>
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