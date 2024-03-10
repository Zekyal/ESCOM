function Confirmar_Borrado(ID) {
    var respuesta = confirm("¿Desea borrar el registro con ID: " + ID + "?");

    if (respuesta == true) {
        return true;
    } else {
        return false;
    }
}
