package Articulo;

import java.awt.Image;
import java.io.Serializable;
import javax.swing.ImageIcon;

public class Articulo implements Serializable{
    public String id;
    public String nombre;
    public String descripcion;
    public float precio;
    public String promocion;
    public String imagen;
    public int existencias;
    
    public Articulo(String id, String nombre, String descripcion, float precio, String promocion, int existencias, String imagen){
        this.id= id;
        this.nombre= nombre;
        this.descripcion= descripcion;
        this.precio= precio;
        this.promocion= promocion;
        this.existencias= existencias;
        this.imagen= imagen;
        
        if(this.descripcion==null)
            this.descripcion="Descripcion no disponoble :c";
    }
    
    public String imprimirDatos()
    {
        return ""+id+"/"+nombre+"/"+descripcion+"/"+precio+"/"+promocion+"/"+existencias;
    }
}
