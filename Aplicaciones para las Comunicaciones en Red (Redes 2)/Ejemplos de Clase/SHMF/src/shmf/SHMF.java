package shmf;//Servidor
import java.net.*;
import java.io.*;

public class SHMF {
    public static void main(String[] args) {
        try{
            ServerSocket s= new ServerSocket(1234);
            s.setReuseAddress(true);
            System.out.println("Servidor iniciado en el puerto "+s.getLocalPort()+" esperando cliente...");
            
            for(;;)
            {
                Socket cl= s.accept();
                System.out.println("Cleinte conectado desde "+cl.getInetAddress()+":"+cl.getPort()+" enviando mensaje");
                PrintWriter pw= new PrintWriter(new PrintWriter(new OutputStreamWriter(cl.getOutputStream())));
                pw.println("Hola mundo con socket de flujo bloqueante");
                pw.flush();
                System.out.println("Mensaje enviado...preparando para recibir un mensaje");
                BufferedReader br= new BufferedReader(new InputStreamReader(cl.getInputStream()));
                String msj= br.readLine();
                System.out.println("Mensaje recibido: "+msj+"\n Cerrando conexion");
                br.close();
                pw.close();
                cl.close();
            }//for
        }catch(Exception e){
            e.printStackTrace();
        }//catch
    }//main
}
