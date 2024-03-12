<?php
//Edición: 15/05/2022
?>

<nav class="navbar navbar-expand-lg bg-light navbar-light fixed-top">
    <a class="navbar-brand" href="index.php"><img src="imagenes/icon.PNG" style="height: 25px;"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav mr-auto">
        </ul>
    </div>
    <form action="cerrar_sesion.php" method="post" class="form-inline my-2 my-lg-0">
        <button class="btn btn-outline-danger my-2 my-sm-0" type="submit" name="CerrarSesion"><i class="fas fa-sign-out-alt"></i> Cerrar Sesión</button>
    </form>
</nav>