<?php
//Crear conexión con MSSQL server
function Conectar()
{
     //Recopilamos la información del servidor
     $ServerName = "ipnserver.database.windows.net";
     $User = "BDadmin";
     $Pass = "DBroot777";
     $DB = "HospitalP";

     $ConnectionInfo = array("Database" => "$DB", "UID" => "$User", "PWD" => "$Pass");
     //Se declara la variable global para usarla en todo el sistema
     global $Conexion;
     $Conexion = sqlsrv_connect($ServerName, $ConnectionInfo);

     //Verificación de errores
     if ($Conexion) {
          return $Conexion;
     } else {
          echo "Conexión no se pudo establecer.<br />";
          die(print_r(sqlsrv_errors(), true));
     }
}

//Función para validar si el usuario cuenta con sesión iniciada
function Validar_Sesion()
{
     session_start();
     //Si el usuario está con sesión iniciada, mandarlo a su página principal
     if (isset($_SESSION['Usuario'])) {
          return 1;
     }
     //Si no, redirigir a la página de inicio de sesión
     else {
          header("Location: login.php");
          return 0;
     }
}

//Función que contiene las sentencias SQL de inicio de sesión
function Iniciar_Sesión($Correo, $Password)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     //Usamos COLLATE en el Query para diferenciar entre mayúsculas y minúsculas
     $Query = "SELECT ID_Persona, Tipo_usr FROM Persona WHERE Correo LIKE '$Correo' AND Contrasenia LIKE '$Password' COLLATE SQL_Latin1_General_CP1_CS_AS";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //Si la información es correcta
          if ($Informacion != NULL) {
               //Iniciar la sesión
               session_start();
               //Guardar hora de inicio de sesión
               date_default_timezone_set('America/Mexico_City');
               $_SESSION['Tiempo'] = time();
               //Recoge únicamente el usuario para identificar los registros y el tipo de usuario para redigir a la interfaz
               $_SESSION['Usuario'] = $Informacion['ID_Persona'];
               $_SESSION['Tipo_Usuario'] = $Informacion['Tipo_usr'];

               //Redirigimos al index para que lo mande a la página que le corresponde
               header("Location: index.php");
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Personas()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT ID_persona,(Nombre+' '+A_Paterno+' '+A_Materno) as Nombre, Fechanac, Sexo, Tel, Tipo_usr, Correo FROM Persona";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Pacientes()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT NSS, Status_pac, Cama, Tratamiento, Paciente.ID_persona,(Persona.Nombre+' '+Persona.A_Paterno+' '+Persona.A_Materno) as Nombre 
     FROM (Paciente INNER JOIN Persona ON Persona.ID_Persona = Paciente.Id_persona)";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Doctores()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT (Nombre+' '+A_Paterno+' '+A_Materno) as Nombre, Doctor.Id_persona, Cedula, Consultorio, Especialidad.nombre_esp as Especialidad, Departamento.nombre_dept as Departamento, Consultorio, Turno FROM 
     (((Persona INNER JOIN Doctor on Doctor.Id_persona = Persona.ID_persona) INNER JOIN Especialidad ON Especialidad.ID_esp = Doctor.Id_esp) INNER JOIN Departamento ON Doctor.Id_dep = Departamento.ID_dep)";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Departamentos()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Departamento";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Especialidades()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Especialidad";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Citas()
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT NSS_pac, Cedula_doc, Id_Cita, Fecha, Diagnostico FROM Cita ORDER BY Fecha DESC";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Doctor($ID_Persona)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT (Nombre+' '+A_Paterno+' '+A_Materno) as Nombre, Sexo,
     Persona.ID_persona, Doctor.Cedula, Doctor.Consultorio,
     Departamento.nombre_dept, Departamento.num_ext, Especialidad.nombre_esp, 
     Correo, Tel 
     FROM (((Doctor INNER JOIN Persona ON Persona.ID_persona = Doctor.Id_persona) 
     INNER JOIN Departamento ON Departamento.ID_dep = Doctor.Id_dep) INNER JOIN Especialidad ON Especialidad.ID_esp = Doctor.Id_esp)
     WHERE Doctor.Id_persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Citas_Proximas($Cedula)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT NSS_pac, (Persona.Nombre+' '+Persona.A_Paterno+' '+Persona.A_Paterno) as Nombre, Id_Cita, Fecha, Diagnostico FROM
     ((Cita INNER JOIN Paciente ON Paciente.NSS = Cita.NSS_pac) INNER JOIN Persona ON Persona.ID_persona = Paciente.Id_persona) WHERE Cedula_doc LIKE '$Cedula' AND Diagnostico LIKE ''
     ORDER BY Fecha DESC;";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Citas_Atendidas($Cedula)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT NSS_pac, (Persona.Nombre+' '+Persona.A_Paterno+' '+Persona.A_Paterno) as Nombre, Id_Cita, Fecha, Diagnostico FROM
     ((Cita INNER JOIN Paciente ON Paciente.NSS = Cita.NSS_pac) INNER JOIN Persona ON Persona.ID_persona = Paciente.Id_persona) 
     WHERE Cedula_doc LIKE '$Cedula' AND Diagnostico != '' ORDER BY Fecha DESC";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Paciente($ID_Persona)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Paciente.Id_persona, NSS, Status_pac, Cama, Tratamiento, (Persona.Nombre+' '+Persona.A_Paterno+' '+Persona.A_Materno) as Nombre,
     Persona.Fechanac, Persona.Sexo, Persona.Tel, Persona.Correo FROM (Persona INNER JOIN Paciente ON Paciente.Id_persona = Persona.ID_persona)
     WHERE Paciente.Id_persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Expediente($NSS)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Id_Cita, Fecha, Diagnostico,(Persona.Nombre+' '+Persona.A_Paterno+' '+Persona.A_Materno) as Nombre
     FROM ((Cita INNER JOIN Doctor ON Doctor.Cedula = Cita.Cedula_doc)
     INNER JOIN Persona ON Persona.ID_persona = Doctor.Id_persona)
     WHERE NSS_pac LIKE '$NSS' ORDER BY Fecha DESC";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Agregar_Persona($Nombre, $A_Paterno, $A_Materno, $Fecha_Nacimiento, $Sexo, $Telefono, $Tipo_Usuario, $Correo, $Password)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);
     $A_Paterno = utf8_decode($A_Paterno);
     $A_Materno = utf8_decode($A_Materno);
     $Password = utf8_decode($Password);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Correo FROM Persona WHERE Correo LIKE '$Correo'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR QUE SE ENCUENTRE LA PERSONA REGISTRADA
          //Si se encuentra el correo registrado
          if ($Informacion != NULL) {
               return 5;
          } else {
               $Query = "INSERT INTO Persona (Nombre, A_Paterno, A_Materno, Fechanac, Sexo, Tel, Tipo_usr, Correo, Contrasenia)
               VALUES ('$Nombre','$A_Paterno','$A_Materno','$Fecha_Nacimiento','$Sexo',$Telefono, '$Tipo_Usuario', '$Correo','$Password')";

               //Búsqueda del query en la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si truena mandamos error
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}

function Agregar_Paciente($ID_Persona, $NSS)
{
     $Estatus = "Alta";
     $Cama = "";
     $Tratamiento = "";
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Tipo_usr FROM Persona WHERE Id_persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR QUE SE ENCUENTRE LA PERSONA REGISTRADA
          //Si se encuentra el usuario registrado
          if ($Informacion != NULL) {
               $Tipo_Usuario = $Informacion['Tipo_usr'];

               //VALIDAMOS QUE EL TIPO DE USUARIO ES PACIENTE
               if ($Tipo_Usuario == 'Paciente') {
                    //Subimos la información a la base de datos
                    $Query = "INSERT INTO Paciente (Id_persona, NSS, Status_pac, Cama, Tratamiento)
                    VALUES ('$ID_Persona','$NSS','$Estatus','$Cama','$Tratamiento')";

                    //Introducimos el query a la base de datos
                    $RespuestaSQL = sqlsrv_query($Conexion, $Query);

                    //Si la base regresa null entonces el usuario ya se encuentra registrado
                    if ($RespuestaSQL === false) {
                         return 5;
                    } else {
                         return 0;
                    }
               }
               //Si el tipo de dato no es Paciente.
               else {
                    return 4;
               }
          }
          //Si la base de datos no muestra información. EL ID PERSONA NO SE ENCUENTRA REGISTRADO
          else {
               return 3;
          }
     }
}

function Agregar_Medico($ID_Persona, $Cedula, $Turno, $Consultorio, $Departamento, $Especialidad)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Tipo_usr FROM Persona WHERE Id_persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR QUE SE ENCUENTRE LA PERSONA REGISTRADA
          //Si se encuentra el usuario registrado
          if ($Informacion != NULL) {
               $Tipo_Usuario = $Informacion['Tipo_usr'];

               //VALIDAMOS QUE EL TIPO DE USUARIO ES DOCTOR
               if ($Tipo_Usuario == 'Doctor') {
                    //Subimos la información a la base de datos
                    $Query = "INSERT INTO Doctor (Id_persona, Id_esp, Id_dep, Cedula, Consultorio, Turno)
                    VALUES ('$ID_Persona','$Especialidad','$Departamento','$Cedula','$Consultorio','$Turno')";

                    //Introducimos el query a la base de datos
                    $RespuestaSQL = sqlsrv_query($Conexion, $Query);

                    //Si la base regresa null entonces el usuario ya se encuentra registrado
                    if ($RespuestaSQL === false) {
                         return 5;
                    } else {
                         return 0;
                    }
               }
               //Si el tipo de dato no es Paciente.
               else {
                    return 4;
               }
          }
          //Si la base de datos no muestra información. EL ID PERSONA NO SE ENCUENTRA REGISTRADO
          else {
               return 3;
          }
     }
}

function Agregar_Departamento($Nombre, $Extension)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);
     $Extension = utf8_decode($Extension);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT nombre_dept, num_ext FROM Departamento WHERE nombre_dept LIKE '$Nombre' OR num_ext LIKE '$Extension'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR SI SE ENCUENTRE LA EXTENSION O EL DEPARTAMENTO
          //Si se encuentra el algun registro mandar error
          if ($Informacion != NULL) {
               return 5;
          } else {
               //Subimos la información a la base de datos
               $Query = "INSERT INTO Departamento VALUES ($Extension,'$Nombre')";

               //Introducimos el query a la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si la base regresa null entonces el departamento ya se encuentra registrado
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}

function Agregar_Especialidad($Nombre)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT nombre_esp FROM Especialidad WHERE nombre_esp LIKE '$Nombre'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR SI SE ENCUENTRA LA ESPECIALIDAD
          //Si se encuentra el algun registro mandar error
          if ($Informacion != NULL) {
               return 5;
          } else {
               //Subimos la información a la base de datos
               $Query = "INSERT INTO Especialidad VALUES ('$Nombre')";

               //Introducimos el query a la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si la base regresa null entonces el departamento ya se encuentra registrado
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}

function Borrar_Persona($ID_Persona)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "DELETE FROM Persona WHERE ID_persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 6;
     } else {
          return 0;
     }
}

function Borrar_Paciente($NSS)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "DELETE FROM Paciente WHERE NSS LIKE '$NSS'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 6;
     } else {
          return 0;
     }
}

function Borrar_Doctor($Cedula)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "DELETE FROM Doctor WHERE Cedula LIKE '$Cedula'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 6;
     } else {
          return 0;
     }
}

function Borrar_Departamento($ID_Departamento)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "DELETE FROM Departamento WHERE ID_dep LIKE '$ID_Departamento'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 6;
     } else {
          return 0;
     }
}

function Borrar_Especialidad($ID_Especialidad)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "DELETE FROM Especialidad WHERE ID_esp LIKE '$ID_Especialidad'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 6;
     } else {
          return 0;
     }
}

function Mostrar_Persona_Edit($ID_Persona)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Persona WHERE ID_Persona LIKE '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 0;
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Paciente_Edit($NSS)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Paciente WHERE NSS = '$NSS'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Mostrar_Doctor_Edit($Cedula)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT (Nombre+' '+A_Paterno+' '+A_Materno) as Nombre, Doctor.Id_persona, Cedula, Consultorio, Especialidad.nombre_esp as Especialidad, Departamento.nombre_dept as Departamento, Consultorio, Turno FROM 
     (((Persona INNER JOIN Doctor on Doctor.Id_persona = Persona.ID_persona) INNER JOIN Especialidad ON Especialidad.ID_esp = Doctor.Id_esp) INNER JOIN Departamento ON Doctor.Id_dep = Departamento.ID_dep) WHERE Cedula LIKE '$Cedula'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Edit_Persona($ID_Persona, $Nombre, $A_Paterno, $A_Materno, $Fecha_Nacimiento, $Sexo, $Telefono, $Tipo_Usuario, $Correo, $Password)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);
     $A_Paterno = utf8_decode($A_Paterno);
     $A_Materno = utf8_decode($A_Materno);
     $Password = utf8_decode($Password);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT Correo FROM Persona WHERE Correo LIKE '$Correo' AND ID_persona != '$ID_Persona'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR QUE SE ENCUENTRE LA PERSONA REGISTRADA
          //Si se encuentra el correo registrado
          if ($Informacion != NULL) {
               return 5;
          } else {
               $Query = "UPDATE Persona SET 
               Nombre = '$Nombre', 
               A_Paterno = '$A_Paterno',
               A_Materno = '$A_Materno', 
               Fechanac = '$Fecha_Nacimiento', 
               Sexo = '$Sexo', 
               Tel = '$Telefono', 
               Tipo_usr = '$Tipo_Usuario', 
               Correo = '$Correo', 
               Contrasenia = '$Password'
               WHERE ID_persona LIKE '$ID_Persona'";

               //Búsqueda del query en la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si truena mandamos error
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}

function Editar_Paciente($NSS, $Estatus, $Cama, $Tratamiento)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();
     
     $Query = "UPDATE Paciente SET
                    Status_pac = '$Estatus', 
                    Cama = '$Cama', 
                    Tratamiento = '$Tratamiento'
                    WHERE NSS LIKE '$NSS'";

     //Introducimos el query a la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          return 0;
     }
}

function Editar_Doctor($Cedula, $Turno, $Consultorio, $Especialidad, $Departamento)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();
     
     $Query = "UPDATE Doctor SET
                    Turno = '$Turno', 
                    Consultorio = '$Consultorio',
                    Id_esp = '$Especialidad', 
                    Id_dep = '$Departamento'
                    WHERE Cedula LIKE '$Cedula'";

     //Introducimos el query a la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          return 0;
     }
}

function Mostrar_Departamento_Edit($ID_Departamento)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Departamento WHERE Id_dep LIKE '$ID_Departamento'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Edit_Departamento($ID_Departamento, $Nombre, $Extension)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);
     $Extension = utf8_decode($Extension);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT nombre_dept, num_ext FROM Departamento WHERE (nombre_dept LIKE '$Nombre' AND ID_dep != '$ID_Departamento') OR (num_ext LIKE '$Extension' AND ID_dep != '$ID_Departamento')";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR SI SE ENCUENTRE LA EXTENSION O EL DEPARTAMENTO
          //Si se encuentra el algun registro mandar error
          if ($Informacion != NULL) {
               return 5;
          } else {
               //Subimos la información a la base de datos
               $Query = "UPDATE Departamento SET num_ext = '$Extension', nombre_dept = '$Nombre' WHERE ID_dep = '$ID_Departamento'";

               //Introducimos el query a la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si la base regresa null entonces el departamento ya se encuentra registrado
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}

function Mostrar_Especialidad_Edit($ID_Especialidad)
{
     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT * FROM Especialidad WHERE ID_esp LIKE '$ID_Especialidad'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          die(print_r(sqlsrv_errors(), true));
     } else {
          //Si la información es correcta
          if ($RespuestaSQL != NULL) {
               return $RespuestaSQL;
          }
          //Si la base de datos no muestra información
          else {
               return 0;
          }
     }
}

function Editar_Especialidad($ID_Especialidad, $Nombre)
{
     //Decodificar variables para usar acentos
     $Nombre = utf8_decode($Nombre);

     //Guardamos la variable de conexión con la BD 
     $Conexion = Conectar();

     $Query = "SELECT nombre_esp FROM Especialidad WHERE nombre_esp LIKE '$Nombre' AND ID_esp != '$ID_Especialidad'";

     //Búsqueda del query en la base de datos
     $RespuestaSQL = sqlsrv_query($Conexion, $Query);

     //Si truena mandamos error
     if ($RespuestaSQL === false) {
          return 2;
     } else {
          //Hacemos feth de la información
          $Informacion = sqlsrv_fetch_array($RespuestaSQL, SQLSRV_FETCH_ASSOC);

          //VALIDAR SI SE ENCUENTRA LA ESPECIALIDAD
          //Si se encuentra el algun registro mandar error
          if ($Informacion != NULL) {
               return 5;
          } else {
               //Subimos la información a la base de datos
               $Query = "UPDATE Especialidad SET nombre_esp = '$Nombre' WHERE ID_esp LIKE '$ID_Especialidad'";

               //Introducimos el query a la base de datos
               $RespuestaSQL = sqlsrv_query($Conexion, $Query);

               //Si la base regresa null entonces el departamento ya se encuentra registrado
               if ($RespuestaSQL === false) {
                    return 2;
               } else {
                    return 0;
               }
          }
     }
}