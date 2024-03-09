package servidoro;//Servidor (objetos)
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ServidorO {
    public static void main(String[] args) {
        try{
            ServerSocket s= new ServerSocket(8000);
            s.setReuseAddress(true);
            System.out.println("Servidor iniciado en el puerto "+s.getLocalPort()+" esperando cliente...");
            
            for(;;)
            {
                Socket cl= s.accept();
                System.out.println("Conexion con el servidor establecida, comienza intercambio de objetos...");
                ObjectInputStream ois = new ObjectInputStream(cl.getInputStream());
                ObjectOutputStream oos = new ObjectOutputStream(cl.getOutputStream());
                Dato o1=(Dato)ois.readObject();
                System.out.println("Objeto recibido con la sig info. -> v1: "+ o1.getv1()+" v2: "+ o1.getv2() +" v3: " + o1.getv3());
                Dato o2 = new Dato(1, 2.0f, "tres");//instancia de clase Dato, definida anteriorimente
                System.out.println("Enviando objetos con la sig. informacion -> v1: "+ o2.getv1()+ " v2: "+ o2.getv2()+" v3: "+ o2.getv3());
                oos.writeObject(o2);
                oos.flush();
                ois.close();
                oos.close();
                cl.close();
            }//for
        }catch(Exception e){
            e.printStackTrace();
        }//catch
    }
    
}
