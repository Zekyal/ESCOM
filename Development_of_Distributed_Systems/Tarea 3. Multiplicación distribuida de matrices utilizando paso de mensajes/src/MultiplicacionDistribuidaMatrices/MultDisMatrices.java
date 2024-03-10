import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class MultDisMatrices {
    static Object lock = new Object();
    static int N = 4;
    static int[][] A= new int[N][N];
    static int[][] B= new int[N][N];
    static int[][] C= new int[N][N];
    
    static class Worker extends Thread{
        Socket conexion;

        Worker(Socket conexion){
            this.conexion = conexion;
        }
        
        public void run(){
            //Algoritmo 1
            try {
                //Declaración de matrices A1, A2, B1, B2
                int[][] A1= new int[N/2][N];
                int[][] B1= new int[N/2][N];
                int[][] A2= new int[N/2][N];
                int[][] B2= new int[N/2][N];               
                
                //Declaracion de variables para evio y recibimiento de datos
                DataInputStream entrada = new DataInputStream(conexion.getInputStream());
                DataOutputStream salida = new DataOutputStream(conexion.getOutputStream());
                //Recibimos el npumero del nodo que se ejecuto desde el cliente
                int x=0, i=0, j=0;
                x = entrada.readInt();
                
                switch(x){
                    //NODO 1
                    case 1:
                        for(i=0; i<N/2; i++)
                            for(j=0; j<N; j++){
                                A1[i][j] = A[i][j];
                                B1[i][j] = B[i][j]; 
                                salida.writeInt(A1[i][j]);//Enviar la matriz A1 al nodo 1
                                salida.writeInt(B1[i][j]);//Enviar la matriz B1 al nodo 1
                            }        
                        break;
                    //NODO 2
                    case 2:
                        for(i=0; i<N/2; i++)
                            for(j=0; j<N; j++){
                                A1[i][j] = A[i][j];
                                salida.writeInt(A1[i][j]);//Enviar la matriz A1 al nodo 2
                            }
                        
                        for(i=N/2; i<N; i++)
                            for(j=0; j<N; j++){
                                B2[i-(N/2)][j] = B[i][j]; 
                                salida.writeInt(B2[i-(N/2)][j]);//Enviar la matriz B2 al nodo 2
                            } 
                        break;
                    //NODO 3
                    case 3:
                        for(i=N/2; i<N; i++)
                            for(j=0; j<N; j++){
                                A2[i-(N/2)][j] = A[i][j];
                                salida.writeInt(A2[i-(N/2)][j]);//Enviar la matriz A2 al nodo 3
                            } 
                        
                        for(i=0; i<N/2; i++)
                            for(j=0; j<N; j++){
                                B1[i][j] = B[i][j]; 
                                salida.writeInt(B1[i][j]);//Enviar la matriz B1 al nodo 3
                            }  
                        break;
                    //NODO 4
                    case 4:
                        for(i=N/2; i<N; i++)
                            for(j=0; j<N; j++){
                                A2[i-(N/2)][j] = A[i][j];
                                B2[i-(N/2)][j] = B[i][j]; 
                                salida.writeInt(A2[i-(N/2)][j]);//Enviar la matriz A2 al nodo 4
                                salida.writeInt(B2[i-(N/2)][j]);//Enviar la matriz B2 al nodo 4
                            } 
                        break;
                    default:
                        break;
                }
                
                synchronized(lock){
                    switch(x){
                        //NODO 1
                        case 1:
                            //Recibe la matriz C1 del nodo 1
                            for(i=0; i<(N/2); i++){
                                for(j=0; j<(N/2); j++){  
                                    C[i][j] = entrada.readInt();
                                }
                            }
                            break;
                        //NODO 2
                        case 2:
                            //Recibe la matriz C2 del nodo 2
                            for(i=0; i<(N/2); i++){
                                for(j=(N/2); j<N; j++){  
                                    C[i][j] = entrada.readInt();
                                }
                            }
                            break;
                        //NODO 3
                        case 3:
                            //Recibe la matriz C3 del nodo 3
                            for(i=(N/2); i<N; i++){
                                for(j=0; j<(N/2); j++){  
                                    C[i][j] = entrada.readInt();
                                }
                            }
                            break;
                        //NODO 4
                        case 4:
                            //Recibe la matriz C4 del nodo 4
                            for(i=(N/2); i<N; i++){
                                for(j=(N/2); j<N; j++){  
                                    C[i][j] = entrada.readInt();
                                }
                            }
                            break;
                        default:
                            break;
                    }
                }
            
                entrada.close();
                salida.close();
                conexion.close();
            }catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    
    public static void main(String[] args) throws Exception{
        if (args.length != 1){
            System.err.println("Uso:");
            System.err.println("java MultiplicacionDistribuidaMatrices <nodo>");
            System.exit(0);
        }  
        
        int nodo = Integer.valueOf(args[0]);
        int i=0, j=0, k=0;
       
        if(nodo==0){
            //inicializa las matrices A y B
            for (i=0; i<N; i++) 
                for(j=0; j<N; j++){
                    A[i][j] = 3*i+2*j;
                    B[i][j] = 3*i-2*j;
                    C[i][j] = 0;
                }
            
            int[][] tempB = new int[N][N];
            if(N==4){            
                for(i=0; i<N; i++)
                    for(j=0; j<N; j++)
                        tempB[i][j] = B[i][j];
            }
            
            //Transpone la matriz B, la matriz transpuesta queda en B
            for(i=0; i<N; i++)
                for(j=0; j<i; j++){
                    int x = B[i][j];
                    B[i][j]=B[j][i];
                    B[j][i]=x;
                }
                
            //Inicializacion del nodo servidor
            ServerSocket servidor = new ServerSocket(50000);
            Worker w[] = new Worker[4];//Aceptaremos 4 clientes
            long checksum = 0;
            j=0;
            
            //Espera y aceptación de cada nodo cliente que se vca conectar al nodo servidor
            while(j!=4){
                Socket conexion = servidor.accept();
                w[j] = new Worker(conexion);
                w[j].start();
                j++;
            }
            
            j=0;
                
            //Espera a que cada hilo se termine de ejecutar antes de inicia la ejecución del siguiente
            while(j!=4){
                w[j].join();
                j++;
            }
            
            //Imprimir Matrices
            if(N==4){
                System.out.println("----Matriz A----\n");
                ImprimirMatriz(A);
                System.out.println("\n----Matriz B----\n");
                ImprimirMatriz(tempB);
                System.out.println("\n----Matriz C----\n");
                ImprimirMatriz(C);
            }
            
            //Checksum
            for (i=0; i<N; i++) 
                for(j=0; j<N; j++)
                    checksum = checksum + C[i][j];
            
            System.out.println("\nChecksum: "+checksum);
        }else{
            Socket conexion = null;
            
            for(;;)
                try
                {
                    conexion = new Socket("localhost",50000);
                    break;
                }
                catch (Exception e)
                {
                    Thread.sleep(100);
                }
            
            //Declaracion de variables para evio y recibimiento de datos
            DataInputStream entrada = new DataInputStream(conexion.getInputStream());
            DataOutputStream salida = new DataOutputStream(conexion.getOutputStream());
            //Enviamos el numero del nodo en que se ejecuta el cliente al servidor
            salida.writeInt(nodo);
            //Declaracion de Matrices
            int[][] mA= new int[N/2][N];
            int[][] mB= new int[N/2][N];
            int[][] mC= new int[N/2][N/2];   
            
            switch(nodo){
                //NODO 1
                case 1:
                    for(i=0; i<(N/2); i++)
                        for(j=0; j<N; j++){
                            mA[i][j] = entrada.readInt();//Recibir del nodo 0 la matriz A1.
                            mB[i][j] = entrada.readInt();//Recibir del nodo 0 la matriz B1. 
                        }
                    break;
                //NODO 2
                case 2:
                    for(i=0; i<(N/2); i++)
                        for(j=0; j<N; j++)
                            mA[i][j] = entrada.readInt();//Recibir del nodo 0 la matriz A1
                                
                            
                    for(i=(N/2); i<N; i++)
                        for(j=0; j<N; j++)
                            mB[i-(N/2)][j] = entrada.readInt();//Recibir del nodo 0 la matriz B2

                    break;
                //NODO 3
                case 3:
                    for(i=(N/2); i<N; i++)
                        for(j=0; j<N; j++)
                            mA[i-(N/2)][j] = entrada.readInt();//Recibir del nodo 0 la matriz A2
                        
                    for(i=0; i<(N/2); i++)
                        for(j=0; j<N; j++)
                            mB[i][j] = entrada.readInt();//Recibir del nodo 0 la matriz B1
                                
                    break;
                //NODO 4
                case 4:
                    for(i=(N/2); i<N; i++)
                        for(j=0; j<N; j++){
                            mA[i-(N/2)][j] = entrada.readInt();//Recibir del nodo 0 la matriz A2.
                            mB[i-(N/2)][j] = entrada.readInt();//Recibir del nodo 0 la matriz B2. 
                        } 
                    break;
                default:
                    break; 
            }
            
            //Realizar el producto C1=A1xB1 (renglón por renglon)
            for (i=0; i<(N/2); i++){
                for (j=0; j<(N/2); j++){
                    for (k = 0; k < N; k++){
                        mC[i][j] += mA[i][k]*mB[j][k];
                    }
                }
            }
                    
            //Enviar la matriz C1 al nodo 0
            for(i=0; i<(N/2); i++){
                for(j=0; j<(N/2); j++){  
                    salida.writeInt(mC[i][j]);
                }
            }
            
            entrada.close();
            salida.close();
            conexion.close();
        }
    }
    
    public static void ImprimirMatriz(int[][] matriz){
        for (int i=0; i<N; i++){ 
            System.out.print("|");
            for(int j=0; j<N; j++){                
                if(j!=3)
                    System.out.print(matriz[i][j]+" "); 
                else
                    System.out.print(matriz[i][j]);
            }
            System.out.print("|\n");
        }
    }
}
