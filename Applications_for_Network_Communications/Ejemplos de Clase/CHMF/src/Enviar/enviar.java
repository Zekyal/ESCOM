package Enviar;//Cliente (archivos)
import java.net.*;
import java.io.*;
import javax.swing.JFileChooser;

public class enviar {
    public static void main(String[] args) {
        // TODO code application logic here
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
            System.out.println("Coneexion con servidiro establecida... mostrando caja de seleccion");
            JFileChooser jf = new JFileChooser();//muestra todos los directorios en una ventana y da la opcion de Aceotar o Cancelar
            int r = jf.showOpenDialog(null);//devuelve el valor de la constante de la opcion que se eligio en la ventana de directorios
            //jf.requestFocus();//usar en caso de que el sistema operativo no abra la ventana de directorios en primer plano
            if(r == JFileChooser.APPROVE_OPTION){//Si se selecciono un archivo
                File f = jf.getSelectedFile();//Devuelve una referencia al acrchivo
                String nombre = f.getName();//Nombre del archivo
                long tam = f.length();//Tmaño del archivo
                String ruta = f.getAbsolutePath();//Ruta absoluta del archivo
                DataOutputStream dos = new DataOutputStream(cl.getOutputStream());//enviar datos del archivo
                DataInputStream dis = new DataInputStream(new FileInputStream(ruta));//FileInputStream(ruta) orienta el flujo orientado a bytes hacia un archio, y le da la ruta de este
                dos.writeUTF(nombre);//envia el nombre del archivo
                dos.flush();//evita que las dos escrituras se tomen como una sola 
                dos.writeLong(tam);//envia el tamaño del archivo
                dos.flush();
                int n, porcentaje;
                long env = 0;
                
                while(env < tam){//transmite el contenido del archivo (bytes enviandos < tamaño del archivo)
                    byte[] b = new byte[3000];//buffer por el vual se transportaran los datos, en este caso lee 3000 bytes maximo
                    n = dis.read(b);//devueve la cantidad de bytes que se pudieron leer
                    dos.write(b,0, n);//indica que se escribiran los bytes del buffer(b), desde el byte 0, hsta el byte n
                    dos.flush();
                    env = env + n;//incrementar variable env
                    porcentaje = (int)((env*100)/tam);//porcentaje de cuanto lleva enviado 
                    System.out.print("Se ha enviado el "+porcentaje+"% del archivo "+ruta+" :0");
                }//while
                
                System.out.println("Archivo enviado");
                dis.close();
                dos.close();
                cl.close();
                br.close();
            }//if 
        }catch(Exception e){
            e.printStackTrace();
        }//catch
    }//main
}

