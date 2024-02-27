package ClienteMulticast;

public class ClienteMulticast {
    public static void main(String[] args) {
        Cliente cl= new Cliente();
        cl.setVisible(true);//Hacemos visible la ventana
        new Thread(cl).start();
    }  
}
