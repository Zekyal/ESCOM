package chmf;//Cliente
import java.net.*;
import java.io.*;

public class CHMF {
    public static void main(String[] args) {
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));//system.in sirve para hacero orientado a caracter
            int pto = 1234;
            InetAddress dst = null;//el usuario nos va a dar la dirección, si no pone una dirección válida, esta se quedara como null nuevamente
            while(true){
                System.out.println("Escribe la direccion");
                String host = br.readLine();
                try{
                    dst = InetAddress.getByName(host);
                }catch(UnknownHostException u){
                    System.err.println("Direccion no valida");
                    continue;
                }
                if(dst != null)
                      break;
            }
            Socket cl = new Socket(dst, pto);//abre un socket con el host que puso el usuario
            System.out.println("Conexion conel servidior establecida, recibiendo mensaje ");
            PrintWriter pw = new PrintWriter(new OutputStreamWriter(cl.getOutputStream()));
            BufferedReader br1 = new BufferedReader(new InputStreamReader(cl.getInputStream()));
            String msj = br1.readLine();
            System.out.println("Mensaje recibido:" + msj + "\n Devolviendo saludo...");
            pw.println("saludo devuelto uwu");
            pw.flush();
            System.out.println("Terminando aplicacion");
            br.close();
            br1.close();
            pw.close();
            cl.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
