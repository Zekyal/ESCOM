//Practica 3. Servicio de chat no bloqueante(Cliente)
package ClienteMulticast;

import java.io.IOException;
import java.net.SocketException;

public class ClienteMulticast {
    public static void main(String[] args) throws SocketException, IOException {
        Cliente cl= new Cliente();
        cl.setVisible(true);//Hacemos visible la ventana
        new Thread(cl).start();
    }  
}
