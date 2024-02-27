package ServidorMulticast;

import ClienteMulticast.Cliente;
import Mensaje.Mensaje;
import java.io.BufferedInputStream;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Servidor{
    public static final String MCAST_ADDR  = "230.1.1.1";
    public static final int MCAST_PORT = 4000;
    public static final int DGRAM_BUF_LEN=6400; //tamaño del buffer
    ArrayList<String> usuarios= new ArrayList<>();
    InetAddress group =null;
    
    public Servidor(){
        try{
            group = InetAddress.getByName(MCAST_ADDR);//intenta resolver la direccion
    	}catch(UnknownHostException e){
            e.printStackTrace();
            System.exit(1);
        }
        
        for(;;){
            try{
                byte[] buf = new byte[DGRAM_BUF_LEN];//crea arreglo de bytes 
                DatagramPacket packet= new DatagramPacket(buf, buf.length);//crea el datagram packet a recibir
                MulticastSocket socket= new MulticastSocket(MCAST_PORT); //socket tipo multicast
                socket.setReuseAddress(true);
                socket.joinGroup(group);//se une al grupo
                socket.receive(packet);//recibe un Mensaje
                
                ByteArrayInputStream bais = new ByteArrayInputStream(buf);
                ObjectInputStream ois = new ObjectInputStream(new BufferedInputStream(bais));
                Mensaje msg = (Mensaje)ois.readObject();//convierte el paquete recibido a un objeto tipo Mensaje
                
                if(msg.tipo.equals("INICIO")){//verifica si el Mensaje es de tipo INICIO
                    usuarios.add(msg.usuarioOrigen);//añade al nuevo usuario conectado a la lista de Usuarios
                    DatagramPacket packet2 = new DatagramPacket(Integer.toString(usuarios.size()).getBytes(), Integer.toString(usuarios.size()).length(), group, MCAST_PORT);
                    System.out.println(new String(packet.getData()));
                    socket.send(packet2);//se envia el numero de usuarios conectados al cliente
                
                    //se realiza el envio de cada uno de los clientes conectados a todos los clientes
                    for(String user: usuarios){
                        DatagramPacket packet3 = new DatagramPacket(user.getBytes(), user.length(), group, MCAST_PORT);
                        socket.send(packet3);
                    }
                }
                else if(msg.tipo.equals("FIN")){   
                    usuarios.remove(msg.usuarioOrigen);//remueve al usuario que cerro sesion de la lista de Usuarios
                    DatagramPacket packet2 = new DatagramPacket(Integer.toString(usuarios.size()).getBytes(), Integer.toString(usuarios.size()).length(), group, MCAST_PORT);
                    System.out.println(new String(packet2.getData()));
                    socket.send(packet2);//se envia el numero de usuarios conectados al cliente
                
                    //se realiza el envio de cada uno de los clientes conectados a todos los clientes
                    for(String user: usuarios){
                        DatagramPacket packet3 = new DatagramPacket(user.getBytes(), user.length(), group, MCAST_PORT);
                        socket.send(packet3);
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException ex) {
                Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
            }
        }   
    }
    
    public static void main(String[] args) {
        Servidor s= new Servidor();
    }   
    
}

 