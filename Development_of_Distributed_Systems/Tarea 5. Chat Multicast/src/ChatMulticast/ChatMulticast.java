import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.nio.charset.Charset;

public class chatMulticast {
    static class Worker extends Thread{
        public void run(){           
            // En un ciclo infinito se recibirán los mensajes enviados al grupo 
            // 230.0.0.0 a través del puerto 50000 y se desplegarán en la pantalla.
            for(;;){
                try{
                    InetAddress group = InetAddress.getByName("230.0.0.0");//intenta resolver la direccion
                    MulticastSocket socket = new MulticastSocket(50000);
                    socket.setReuseAddress(true);
                    socket.joinGroup(group);//se une al grupo
                    byte[] buffer = recibe_mensaje_multicast(socket, 9800);
                    System.out.println(new String(buffer, Charset.forName("windows-1252")).trim());
                    socket.leaveGroup(group);
                    socket.close();
                }catch(Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
    
    public static void main(String[] args) throws Exception
    {
        if (args.length != 1)
        {
            System.err.println("Se requiere ingresar un nombre de usuario");
            System.exit(1);
        }
        
        Worker w = new Worker();
        w.start();
        String nombre = args[0];
        BufferedReader msg = new BufferedReader(new InputStreamReader(System.in));
        
        // En un ciclo infinito se leerá cada mensaje del teclado y se enviará el mensaje al
        // grupo 230.0.0.0 a través del puerto 50000.
        for(;;){
            String mensaje = nombre + ": " + msg.readLine();
            envia_mensaje_multicast(mensaje.getBytes(), "230.0.0.0", 50000);
        }
    }
    
    static void envia_mensaje_multicast(byte[] buffer,String ip,int puerto) throws IOException{
        DatagramSocket socket = new DatagramSocket();
        socket.send(new DatagramPacket(buffer,buffer.length,InetAddress.getByName(ip),puerto));
        socket.close();
    }
    
    static byte[] recibe_mensaje_multicast(MulticastSocket socket,int longitud_mensaje) throws IOException{
        byte[] buffer = new byte[longitud_mensaje];
        DatagramPacket paquete = new DatagramPacket(buffer,buffer.length);
        socket.receive(paquete);
        return paquete.getData();
    }
}