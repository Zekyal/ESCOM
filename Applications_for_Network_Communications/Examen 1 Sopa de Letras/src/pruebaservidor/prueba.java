package pruebaservidor;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Hashtable;
import java.util.Random;

public class prueba {
    public static void main(String[] args) {
        ServerSocket serv;
        Socket sock;
        int NumPal = 14;
        try{
            serv = new ServerSocket(6000);
            String[]palabras = {"ESCOM",        "REDES",        "REPROBADO",    "ETS",              "EXAMEN",
                                "MEMES",        "MATEMATICAS",  "ELECTRONICA",  "LISTAS",           "TURING",
                                "OTAKU",        "ANIME",        "PROFEPASEMEUWU",       "SAES",             "SMASH",  
                                "ARQUITECTURA", "CALCULO",      "CHAIROS",      "TORTAS",           "ECONOMIA",
                                "COMPILADORES", "OPERATIVOS",   "MICROS",       "VICTORMORENO",     "SOCIALES", 
                                "TAREAS",       "MANDRAKE",     "LINEAL",       "KERMES",           "PROBABILIDAD", 
                                "DISCRETAS",    "FISICA",       "AVANZADAS",    "BASESDEDATOS",     "POO", 
                                "ANALOGICA",    "WEB",          "ADMIN",        "INGENIERIA",      "ALGORITMOS",   
                                "OPTATIVA",     "SEÑALES",      "SISTEMAS",     "LIDERAZGO",        "ELECTIVA",
                                "TTERMINAL",    "COMPUTADORA",  "SOFTWARE",     "PROYECTO",         "SALVASEMESTRE",
                                "PROFESIONAL",  "NIVEL",        "ALGEBRA",      "RIDLEY",           "SAMUS",
                                "MARIO",        "LUIGI",        "BOWSER",       "NINTENDO",         "SONIC",
                                "YOUTUBE",      "JULIOPROFE",   "WINDOWS",      "LINUX",            "BATIZ"};
            //Dir coordenadas;
            String[] x = {"","","","","","","","","","","","","",""};
            String[] y = {"","","","","","","","","","","","","",""};
            while(true){
                sock = serv.accept();
                DataOutputStream dos= new DataOutputStream(sock.getOutputStream());
                DataInputStream dis = new DataInputStream(sock.getInputStream());
                System.out.println("Conexion establecida...");
            //--------------------------------------------------------------------------------------------------------------------------------------
                char b=dis.readChar();
                switch (b) {
                    case 0:
                        System.out.println("Enviando palabras");
                        for(int i=0; i<NumPal; i++){
                            int numero = (int) (Math.random() * palabras.length);
                            
                            dos.flush();
                            dos.writeUTF(palabras[numero]);
                            dos.flush();
                            
                        }   System.out.println("Enviado :)");
                        break;
                    case 1:
                        System.out.println("Coordenadas de respuestas: ");
                        for(int i=0; i<NumPal; i++){
                            x[i] =x[i]+ dis.readUTF();
                            y[i] =y[i]+ dis.readUTF();
                            //coordenadas.add(x, y);
                            System.out.println((i+1)+". "+x[i]+", "+y[i]);
                            dos.writeBoolean(true);
                        }   break;
                    case 2:
                        System.out.println("Verificando respuestas...");
                        boolean[]reg={  false,false,false,false,false,
                                        false,false,false,false,false,
                                        false,false,false,false,true};
                        while(true){
                            String res = dis.readUTF().toUpperCase();
                            System.out.println("res: "+res);
                            char[]c = res.toCharArray();
                            String x1="", y1="";
                            int j=0;
                            while(c[j]!=','){
                                x1 =x1+c[j];
                                j++;
                            }j++;
                            while(j<c.length){
                                y1 =y1+c[j];
                                j++;
                            }
                            boolean cor = false;
                            
                            for(int k=0; k<14; k++){
                                if(x[k].equals(x1) && y[k].equals(y1)){
                                    if(reg[k]==true){
                                        dos.writeUTF("PALABRA YA ENCONTRADA >:c");
                                        cor = reg[k];
                                        break;
                                    }
                                    else{
                                        dos.writeUTF("CORRECTO!!!");
                                        reg[k]=true;
                                        cor = reg[k];
                                        break;
                                    }
                                }
                            }
                            if(cor == false)
                                dos.writeUTF("NO UWU");
                            if(new algo().validarReg(reg, NumPal)){
                                dos.writeUTF("FIN DEL JUEGO");
                                dos.close();
                                dis.close();
                            }else{
                                dos.writeUTF("-------");
                            }
                        }
                    default:
                        break;
                }
            //--------------------------------------------------------------------------------------------------------------------------------------
                System.out.println("Conexion terminada...");
                sock.close();
            }
            //--------------------------------------------------------------------------------------------------------------------------------------
            //--------------------------------------------------------------------------------------------------------------------------------------
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}

class algo{
    boolean validarReg(boolean[]b, int n){
        for(int i=0; i<n; i++)
            if(!b[i])
                return false;
        return true;
    }
}