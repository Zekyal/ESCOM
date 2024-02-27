package clienteo;//Cliente (objetos)
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class ClienteO {

    public static void main(String[] args) {
        try{
            int pto = 8000;
            String host = "localhost";
            Socket cl = new Socket(host, pto);
            System.out.println("Conexion con el servidor establecida, comienza intercambio de objetos...");
            ObjectOutputStream oos = new ObjectOutputStream(cl.getOutputStream());
            ObjectInputStream ois = new ObjectInputStream(cl.getInputStream());
            Dato o1 = new Dato(1, 2.0f, "tres");//instancia de clase Dato, definida anteriorimente
            System.out.println("Enviando objetos con la sig. informacion -> v1: "+ o1.getv1()+ " v2: "+ o1.getv2()+" v3: "+ o1.getv3());
            oos.writeObject(o1);
            oos.flush();
            Dato o2=(Dato)ois.readObject();//(Dato) convierte al tipo de objeto(en este caso Dato :v) que sabemos que va a recibir
            /*En caso de que no se conozca de que instancia es el objeto:
            Object o=ois.readObject();
            if(o instanceof Dato)//instanceof es un comando para determinar si un objeto es una nstancia de una clase
                Dato d=(Dato)o;
            if(o instanceof X)
                X d=(X)o;
            ...
            */
            System.out.println("Objeto recibido con la sig info. -> v1: "+ o2.getv1()+" v2: "+ o2.getv2() +" v3: " + o2.getv3());
            System.out.println("termina programa");
            ois.close();
            oos.close();
            cl.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
}
