package examenredes2_cliente;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Hashtable;

public class Sopa_Letras {
    private Hashtable<Integer, String> palabras= null;
    private String[] matriz= null;
    private final int NUM_PAL= 14;
    private final int lado= 15;
    private final int NUM_LABEL= lado*lado;
    
    //Constantes brújula para el acomodo de palabras
    private final int N = -lado;
    private final int S = lado;
    private final int W = -1;
    private final int E = 1;
    private final int NE = -lado + 1;
    private final int SE = lado + 1;
    private final int NW = -lado - 1;
    private final int SW = lado - 1;
    
    public String[]
            cordX={ "","","","","","","","","","","","","",""}, 
            cordY={ "","","","","","","","","","","","","",""};
    public int counter=0;
    
    public Sopa_Letras(){
        ObtenerPalabras();
        AcomodarPalabras();
        EnviarCoordenadas(cordX, cordY);
        LLenarMatriz();
        ImprimirMatriz();
        EnviarRespuesta();
    }
        
    private void ObtenerPalabras(){
        palabras= new Hashtable<Integer, String>(NUM_PAL);
                
        try{
            int pto= 6000;
            String host= "localhost";
            Socket cl= new Socket(host, pto);
            DataInputStream dis = new DataInputStream(cl.getInputStream());
            DataOutputStream dos = new DataOutputStream(cl.getOutputStream());
            dos.writeChar(0);
            dos.flush();
            System.out.println("PALABRAS A ENCONTRAR ☺");
            System.out.println("----------------------");
            
            for(int i=0; i<NUM_PAL; i++){
                String pal= dis.readUTF();
                pal=pal.toUpperCase();//convertimos las letras de las palabras a mayuscula
                palabras.put(i, pal);//añadimos palabra recibida a la tabla hash
                System.out.println(i+1+". "+palabras.get(i));
            }
            
            dos.close();
            dis.close();
            cl.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    private void AcomodarPalabras(){
        matriz= new String[NUM_LABEL];
        String pal_selecc= new String("");
        
        for(int i=0; i<NUM_PAL; i++){
            pal_selecc= palabras.get(i);//extraemos la palabra en la posicion i de la tabla hash de palabras
            char[] letras_pal= pal_selecc.toCharArray();//convertimos la palabra extraída a un arreglo de caracteres
            //System.out.print(pal_selecc+": ");
            
            int ciclo=0;
            int direcciones[]= {N, S, E, W, NE, SE, NW, SW};
            
            while(ciclo<1000){
                int posicion_ini= (int)(java.lang.Math.random()*(lado*lado));//posicion inicial aleatoria
                int direccion=(int)(java.lang.Math.random()*direcciones.length);//direccion de brujula aleatoria
                
                if(this.PosicionarPalabra(direcciones[direccion], letras_pal, posicion_ini))
                    break;
                
                ciclo++;
            }
            
        }
    }
    
    private void LLenarMatriz(){
        for(int i=0; i<NUM_LABEL; i++){
            if(matriz[i]==null){
                int numAleat=(int)Math.floor(Math.random()*(90-65)+65);
                matriz[i]= String.valueOf((char)numAleat);/**/
                //matriz[i]= String.valueOf(".");
            }
            
        }
    }
    
    private void ImprimirMatriz(){
        int j=0;
        System.out.println("\n\n\t  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O ");
        System.out.println("\t┌─────────────────────────────┐");
        System.out.print(j+"\t│");
        
        for(int i=1; i<=NUM_LABEL; i++){
            System.out.print(" "+matriz[i-1]+" ");
            
            if(i%15==0){
                System.out.print("  │\n");
                j++;
                
                if(i==NUM_LABEL)
                    break;
                System.out.print(j+"\t│");
            }
        }    
        System.out.println("\t└─────────────────────────────┘");
    }
    
    private boolean PosicionarPalabra(int brujula, char[] letras_pal, int posicion){
        int nuevapos= posicion;
        
        for(int i=0; i<letras_pal.length; i++){
            try{
                //valida que la posicion 
                if(matriz[nuevapos]==null || matriz[nuevapos].equals(letras_pal[i])){
                    if(!Comprobar_Limites(nuevapos, brujula))
                        return false;
                    
                    nuevapos= nuevapos+brujula;
                }
                else
                    return false;
            }catch (Exception e){
                return false;
            }
        }
        
        int pos= posicion, x, y;
        
        for(int j=0; j<letras_pal.length; j++){
            matriz[pos]=String.valueOf(letras_pal[j]);
            pos=pos+brujula;
        }
        
        //oie Zet acuerdate de no mover estas weas xdxdxd
        x=posicion%15;
        y=posicion/15;
        String cord_ini= ObtenerCoordenadas(x, y);
        x=(pos-brujula)%15;
        y=(pos-brujula)/15;
        String cord_final= ObtenerCoordenadas(x, y);
        //System.out.println(cord_ini+","+cord_final);
        cordX[counter] = cord_ini;
        cordY[counter] = cord_final;
        counter++;
        return true;
    }
    
    private boolean Comprobar_Limites(int posicion, int brujula){
        switch (brujula){
            case N:
                if(posicion<lado)
                    return false;
                return true; 
            case S:
                if(posicion+lado>(lado*lado))
                    return false;
                return true;
            case E:
                if(java.lang.Math.IEEEremainder(posicion+1,lado)== 0)
                    return false;
                return true;
            case W:
                if(java.lang.Math.IEEEremainder(posicion,lado)== 0)
                    return false;
                return true;
            case NE:
                if(posicion<lado)//NORTE
                    return false;
                if(java.lang.Math.IEEEremainder(posicion+1,lado)== 0)//ESTE
                    return false;
                return true;
            case SE:
                if(posicion+lado>(lado*lado))//SUR
                    return false;
                if(java.lang.Math.IEEEremainder(posicion+1,lado)== 0)//ESTE
                    return false;
                return true;
            case SW:
                if(posicion+lado>(lado*lado))//SUR
                    return false;
                if(java.lang.Math.IEEEremainder(posicion,lado)== 0)//OESTE
                    return false;
                return true;
            case NW:
                if(posicion<lado)//NORTE
                    return false;
                if(java.lang.Math.IEEEremainder(posicion,lado)== 0)//OESTE
                    return false;
                return true;
            default:
                break;
        }
        
        return false;
    }
    
    private String ObtenerCoordenadas(int x, int y){
        String cord_x=null, cord_y=null;
        
        switch(x){
            case 0: cord_x="A"; break;
            case 1: cord_x="B"; break;
            case 2: cord_x="C"; break;
            case 3: cord_x="D"; break;
            case 4: cord_x="E"; break;
            case 5: cord_x="F"; break;
            case 6: cord_x="G"; break;
            case 7: cord_x="H"; break;
            case 8: cord_x="I"; break;
            case 9: cord_x="J"; break;
            case 10: cord_x="K"; break;
            case 11: cord_x="L"; break;
            case 12: cord_x="M"; break;
            case 13: cord_x="N"; break;
            case 14: cord_x="O"; break;   
            default: System.out.println("Error en asignación de coordenada x");  break;
        }
        
        switch(y){
            case 0: cord_y="0"; break;
            case 1: cord_y="1"; break;
            case 2: cord_y="2"; break;
            case 3: cord_y="3"; break;
            case 4: cord_y="4"; break;
            case 5: cord_y="5"; break;
            case 6: cord_y="6"; break;
            case 7: cord_y="7"; break;
            case 8: cord_y="8"; break;
            case 9: cord_y="9"; break;
            case 10: cord_y="10"; break;
            case 11: cord_y="11"; break;
            case 12: cord_y="12"; break;
            case 13: cord_y="13"; break;
            case 14: cord_y="14"; break;
            default: System.out.println("Error en asignación de coordenada y"); break;
        }
        
        return cord_x+cord_y;
    }
    
    private void EnviarCoordenadas(String[] cord_x, String[] cord_y){
        try{
            int pto= 6000;
            String host= "localhost";
            Socket cl= new Socket(host, pto);
            DataOutputStream dos = new DataOutputStream(cl.getOutputStream());
            DataInputStream dis = new DataInputStream(cl.getInputStream());
            
            dos.writeChar(1);//
            dos.flush();
            for(int i=0; i<NUM_PAL; i++){
                //System.out.println("--"+cord_x[i] + ", "+cord_y[i]);
                dos.flush();
                dos.writeUTF(cord_x[i]);
                dos.flush();
                dos.writeUTF(cord_y[i]);
                dos.flush();
                
                boolean b =false;
                while(true){
                    if(b)break;
                    b= dis.readBoolean();
                }
                dos.flush();
            }
            
            dis.close();
            dos.close();
            cl.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    private void EnviarRespuesta(){
        try{
            int pto= 6000;
            String host= "localhost";
            Socket cl= new Socket(host, pto);
            DataOutputStream dos = new DataOutputStream(cl.getOutputStream());
            DataInputStream dis = new DataInputStream(cl.getInputStream());
            
            dos.writeChar(2);//
            dos.flush();
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Las respuestas deben ser coordenadas. Ej A1, A5");
            
            while(true){
                System.out.print("Respuesta: ");
                String R=br.readLine();
                
                dos.flush();
                dos.writeUTF(QuitaEspacio(R));
                dos.flush();
                
                String servR =dis.readUTF();
                System.out.println(servR);
                servR = null;
                
                servR = dis.readUTF();
                System.out.println(servR);
                if("FIN DEL JUEGO".equals(servR)){
                    dos.close();
                    dis.close();
                    cl.close();
                    break;
                }
                    
            }/**/
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    String QuitaEspacio(String palabra){
        char[]c = palabra.toCharArray();
        String pal="";
        for(int i=0; i<c.length; i++)
            if(c[i]!=' ' && c[i]!='\t')
                pal=pal+c[i];
        return pal;
    }
}

