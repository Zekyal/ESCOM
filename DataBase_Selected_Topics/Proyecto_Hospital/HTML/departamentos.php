<?php
//Incluir archivos de funciones
include("funciones.php");

//Validar que la sesión no se haya iniciado aún
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd>
<html>
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
        <div class="container-lg">
            <div class="row justify-content-center align-items-center vh-100">
                <div id="Contenido" class="col-md-7">
                    <h1 id="Titulo_Formulario">Añadir departamento</h1>
                    <div id="Formulario">
                        <form action="##" method="post">
                            <div class="form-group">
                                <div class="input-group input-group-lg">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">Nombre</span>
                                    </div>
                                    <input id="Usuario" class="form-control" type="text" name="Usuario" placeholder="Nombre del departamento">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group input-group-lg">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">Numero de extensión</span>
                                    </div>
                                    <input id="Password" class="form-control" type="password" name="Password" placeholder="# de extensión">
                                </div>
                            </div>
                            <div class="card-footer text-center">
                                <button class="btn btn-success" type="submit" name="submit"> Agregar</button>
                                <button class="btn btn-danger" type="submit" name="submit"> Cancelar</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>