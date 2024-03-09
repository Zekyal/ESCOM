package recibe;//Servidor (archivos)
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Recibe {
    public static void main(String[] args) {
        try{
            int pto=5678;
            ServerSocket s = new ServerSocket(pto);
            System.out.println("Servidor iniciado en el punto "+ pto + "esperando archivo...");
            for(;;){
                Socket cl = s.accept();
                DataInputStream dis = new DataInputStream(cl.getInputStream());
                String nombre = dis.readUTF();
                long tam = dis.readLong();
                System.out.println("preparando para recibir el archivo"+ nombre+ "de" + tam +"bytes desde"+ cl.getInetAddress()+":"+cl.getPort());
                DataOutputStream dos = new DataOutputStream(new FileOutputStream(nombre));//lectura del arcivo usando ell nombre que se recibio
                long rec = 0;
                int n = 0, porcentaje = 0;
                while(rec < tam){
                    byte[]b=new byte[3000];//fuera de localhost, es recomendable usar 1500 
                    n=dis.read(b);//Cantidad de btes que leyó, si ya no hay datos devuelve -1
                    dos.write(b,0,n);//escribir el buffer partiendo de 0 hasta la cantidad de bytes que pude leer
                    dos.flush();
                    rec = rec+n;
                    porcentaje =(int)((rec*100)/tam);
                    System.out.println("\r Recibido el "+porcentaje +"% del archivo");
                }
                File f = new File ("");//si no apunta a ningun lado, ent0onces apunta a la raíz de donde tengamos nuestroproyecto
                String dst = f.getAbsolutePath();//obtenemos rta del archivo
                /*--Versión altertiva de las dos línes de código anteriores:--
                    File f1=new file(dst+"\\archivo");
                    f1.mkdirs();
                    String ruta = f1.getAbsolutePath();
                */
                System.out.println("archivo recivido y descargado en la carpeta: "+ dst);
                dos.close();
                dis.close();
                cl.close();
            }//for
        }catch(Exception e){
            e.printStackTrace();
        }//catch
    }//main
}
