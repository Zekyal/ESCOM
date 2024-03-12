<?php
//Código para redirigir al usuario al inicio de sesión
//Validar que la sesión esté iniciada
include("funciones.php");
$Valido = Validar_Sesion();

//Si está iniciada comprobar el tipo de usuario que está iniciado
if ($Valido == 1) {
    $Tipo_Usuario = $_SESSION['Tipo_Usuario'];

    if ($Tipo_Usuario == "ADMIN")
        header("Location: admin_personas.php");
    else if ($Tipo_Usuario == "Recepcionista")
        header("Location: #");
    else if ($Tipo_Usuario == "Doctor")
        header("Location: doctor.php");
    else if ($Tipo_Usuario == "Paciente")
        header("Location: paciente.php");    
}
