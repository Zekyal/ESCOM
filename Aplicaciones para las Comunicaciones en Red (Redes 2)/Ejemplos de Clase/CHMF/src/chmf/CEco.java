package chmf;//Cliente Eco
import java.net.*;
import java.io.*;

public class CEco{
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
            PrintWriter pw= new PrintWriter(new OutputStreamWriter(cl.getOutputStream()));
            BufferedReader br1= new BufferedReader(new InputStreamReader(cl.getInputStream()));
            
            while(true){//No se sabe cuanto caracteres va a meter el cliente, por lo que se hace un ciclo infinito para leer todo hasta que llegue a un salto de linea
                System.out.println("Escribe una cadena, <Enter> para enviar, o\"cerrar\" para terminar...");
                String msj= br.readLine();//Revisa si encuentra un salto de linea
                pw.println(msj);//Envia el mensaje
                pw.flush();
                
                if(msj.compareToIgnoreCase("cerrar")==0){//Validar si el comando es "Cerrar"
                    System.out.println("Termina programa :c");
                    br.close();
                    br1.close();
                    pw.close();
                    cl.close();
                    System.exit(0);
                }
                else{
                    String eco=br1.readLine();
                    System.out.println("Eco recibido"+eco);
                }//else
            }//while
        }catch(Exception e){
            e.printStackTrace();
        }//catch
    }//main         
}
                    