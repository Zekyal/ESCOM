import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

public class PI {
    static Object lock = new Object();
    static double pi = 0;
    
    static class Worker extends Thread{
        Socket conexion;

        Worker(Socket conexion){
            this.conexion = conexion;
        }
        
        public void run(){
            //Algoritmo 1
            try {
                DataInputStream entrada = new DataInputStream(conexion.getInputStream());
                DataOutputStream salida = new DataOutputStream(conexion.getOutputStream());
                double x=0;
                x = entrada.readDouble();
                System.out.println("Suma recibida: " + x);
                
                synchronized(lock){
                    pi = x+pi;
                }
                
                entrada.close();
                salida.close();
                conexion.close();
            }catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
        
    public static void main(String[] args) throws Exception{
        if (args.length != 1){
            System.err.println("Uso:");
            System.err.println("java pi <nodo>");
            System.exit(0);
        }
    
        int nodo = Integer.valueOf(args[0]);
        
        if(nodo==0){
            //Algoritmo 2
            ServerSocket servidor = new ServerSocket(50000);
            Worker w[] = new Worker[4];
            int i=0;
            
            while(i!=4){
                Socket conexion = servidor.accept();
                w[i] = new Worker(conexion);
                w[i].start();
                i++;
            }
            
            i=0;
            
            while(i!=4){
                w[i].join();
                i++;
            }
            
            System.out.println("PI = "+pi);
        }else{
            Socket conexion = null;
            
            for(;;)
                try
                {
                    conexion = new Socket("localhost",50000);
                    break;
                }
                catch (Exception e)
                {
                    Thread.sleep(100);
                }
            
            DataInputStream entrada = new DataInputStream(conexion.getInputStream());
            DataOutputStream salida = new DataOutputStream(conexion.getOutputStream());
            double suma = 0;
            int i=0;
            
            while(i!=10000000){
                suma = 4.0/(8*i+2*(nodo-2)+3)+suma;
                i++;
            }
            
            suma = nodo%2==0?-suma:suma;
            salida.writeDouble(suma);
            
            entrada.close();
            salida.close();
            conexion.close();
        }
    }
    
}
