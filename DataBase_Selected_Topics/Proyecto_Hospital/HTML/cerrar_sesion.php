<?php
//Código para liberar las variables de sesión
session_start();

unset($_SESSION['Usuario']);
unset($_SESSION['Tipo_Usuario']);
unset($_SESSION['Tiempo']);
session_destroy();

header("Location: index.php");
return 0;
