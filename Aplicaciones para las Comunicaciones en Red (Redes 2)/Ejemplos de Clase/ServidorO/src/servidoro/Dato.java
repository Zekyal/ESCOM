package servidoro;
import java.io.Serializable;
public class Dato implements Serializable{
/*Envia Datos Serializables(cuando se generen instancias de esta, estas se van a convertir en instancias de bytes, 
las cuales serán enviadas por el cliente*/
    //Todos los datos nativos son serailizables
    int v1;
    float v2;
    String v3;
    /*Si le añadimos la palabra "transient"(se hace mas en la parte del servidor en caso de que unicamene se busque manejar del lado
    del servidor, y no del cliente) antes de un tipo de dato (ej. trasient float v2), el objeto no se hace serializable y al momento 
    de que se enviado o recibido por el cliente, estos datos serán llenados con datos por omisión por el constructor(primitivo 0 
    objeto null)*/
    public Dato(int v1, float v2, String v3){
        this.v1 = v1;
        this.v2 = v2;
        this.v3 = v3;
    }
    int getv1(){
        return this.v1;
    }
    float getv2(){
        return this.v2;
    }
    String getv3(){
        return this.v3;
    }
}
