package Mensaje;

import java.io.Serializable;

public class Mensaje implements Serializable{
    public String tipo;
    public String usuarioOrigen;
    public String usuarioDestino;
    public String mensaje;
    
    //INICIO, PUBLICO
    public Mensaje(String tipo, String usuarioOrigen){
        this.tipo= tipo;
        this.usuarioOrigen= usuarioOrigen;
        this.mensaje= mensaje;
    }
    
    public Mensaje(String tipo, String usuarioOrigen, String mensaje){
        this.tipo= tipo;
        this.usuarioOrigen= usuarioOrigen;
        this.mensaje= mensaje;
    }
    
    //PRIVADOS
    public Mensaje(String tipo, String usuarioOrigen, String usuarioDestino, String mensaje){
        this.tipo= tipo;
        this.usuarioOrigen= usuarioOrigen;
        this.usuarioDestino= usuarioDestino;
        this.mensaje= mensaje;
    }
}
