//Practica 3. Servicio de chat no bloqueante(Servidor)
package ServidorMulticast;

import Mensaje.Mensaje;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.SocketAddress;
import java.net.SocketException;
import java.net.StandardProtocolFamily;
import java.net.StandardSocketOptions;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Servidor{
    private static final String MCAST_INTF = "lo";
    public static final String MCAST_ADDR  = "230.1.1.1";
    public static final int MCAST_PORT = 4000;
    public static final int DGRAM_BUF_LEN=6400; //tamaño del buffer
    ArrayList<String> usuarios= new ArrayList<>();
    InetAddress group;
    InetSocketAddress pto;
    NetworkInterface ni;
    SocketAddress address;
    DatagramChannel channel;
    
    public Servidor() throws SocketException, IOException{
        try{
            group = InetAddress.getByName(MCAST_ADDR);//intenta resolver la direccion
            pto = new InetSocketAddress(MCAST_PORT);
            ni = NetworkInterface.getByName(MCAST_INTF);
            address = new InetSocketAddress(MCAST_ADDR, MCAST_PORT);
            
            //Declaración del socket no bloqueante de datagrama del servidor
            DatagramChannel channel = DatagramChannel.open(StandardProtocolFamily.INET);
            channel.configureBlocking(false);
            channel.setOption(StandardSocketOptions.SO_REUSEADDR, true);
            System.out.println("interfaz:"+ni.getName());
            channel.setOption(StandardSocketOptions.IP_MULTICAST_IF, ni);
            System.out.println("dir:: "+pto);
            channel.socket().bind(pto);
            //System.out.println("socket escuchando en el puerto"+pto);
            channel.join(group, ni);
            Selector selector = Selector.open();
            channel.register(selector,SelectionKey.OP_READ);
            ByteBuffer buffer = ByteBuffer.allocate(DGRAM_BUF_LEN);  

            for(;;){
                selector.select();
                Set readyKeys = selector.selectedKeys();
                Iterator it = readyKeys.iterator();
                
                while(it.hasNext()){
                    SelectionKey key = (SelectionKey)it.next();
                    it.remove();
                 
                    if(key.isReadable()){
                        buffer.clear();
                        System.out.println("capacidad buffer: "+buffer.limit());
                        SocketAddress client = channel.receive(buffer);
                        buffer.flip();
                        System.out.println(buffer.limit()+" bytes recibidos");
                        
                        if(buffer.hasArray() && buffer.limit()>=50){
                            //Se recibe un objeto de tipo mensaje desde alguno de los clientes que estén conectados
                            System.out.println("tam_buffer: "+buffer.limit());
                            ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(buffer.array()));
                            Object o = ois.readObject();  
                            
                            if(o instanceof Mensaje){
                                //System.out.println("Si es Mensaje");
                                Mensaje msg = (Mensaje)o;//convierte el paquete recibido a un objeto tipo Mensaje
                                System.out.println(msg.tipo+" "+msg.usuarioOrigen+" "+msg.mensaje);
                            
                                if(msg.tipo.equals("INICIO")){//verifica si el Mensaje es de tipo INICIO
                                    usuarios.add(msg.usuarioOrigen.trim());//añade al nuevo usuario conectado a la lista de Usuarios
                                    channel.register(selector,SelectionKey.OP_WRITE | SelectionKey.OP_READ);
                                    buffer = ByteBuffer.allocate(DGRAM_BUF_LEN);
                                    selector.select();
                                    readyKeys = selector.selectedKeys();
                                    it = readyKeys.iterator();
                                
                                    while(it.hasNext()){
                                        key = (SelectionKey)it.next();
                                        it.remove();
                                    
                                        if(key.isWritable()){
                                            buffer.clear();
                                            buffer.putInt(usuarios.size());
                                            buffer.flip();
                                            channel.send(buffer, address);
                                            buffer.clear();
                                        
                                            for(String user: usuarios){
                                                buffer.put(user.getBytes("UTF-16"));
                                                buffer.flip();
                                                channel.send(buffer, address);
                                                buffer.clear();
                                            }
                                        }
                                    }
                                }
                                else if(msg.tipo.equals("FIN")){   
                                    usuarios.remove(msg.usuarioOrigen.trim());//remueve al usuario que cerro sesion de la lista de Usuarios
                                    channel.register(selector,SelectionKey.OP_WRITE | SelectionKey.OP_READ);
                                    buffer = ByteBuffer.allocate(DGRAM_BUF_LEN);
                                    selector.select();
                                    readyKeys = selector.selectedKeys();
                                    it = readyKeys.iterator();
                                
                                    while(it.hasNext()){
                                        key = (SelectionKey)it.next();
                                        it.remove();
                                    
                                        if(key.isWritable()){
                                            buffer.clear();
                                            buffer.putInt(usuarios.size());
                                            buffer.flip();
                                            channel.send(buffer, address);
                                            buffer.clear();
                                        
                                            for(String user: usuarios){
                                                buffer.put(user.getBytes("UTF-16"));
                                                buffer.flip();
                                                channel.send(buffer, address);
                                                buffer.clear();
                                            }
                                        }
                                    }
                                }
                            }//instanceof
                        }//hasArray()  
                    }//isReadable()
                }//hasNext()  
            }//for
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }   
    
    public static void main(String[] args) throws IOException {
        Servidor s= new Servidor();
    }   
    
}

 