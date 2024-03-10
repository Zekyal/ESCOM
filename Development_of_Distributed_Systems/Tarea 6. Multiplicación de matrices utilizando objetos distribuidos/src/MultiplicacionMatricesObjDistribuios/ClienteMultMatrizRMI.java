import java.rmi.Naming;

public class ClienteMultMatrizRMI{
    static int N = 8;
    static float[][] A= new float[N][N];
    static float[][] B= new float[N][N];
    static float[][] C= new float[N][N];
        
    public static void main(String args[]) throws Exception{
        int i, j, k;
        double checksum = 0;
        
        String url1 = "rmi://10.0.0.5/MatrizObjDist";
        String url2 = "rmi://10.0.0.6/MatrizObjDist";
        // obtiene una referencia que "apunta" al objeto remoto asociado a la URL
        InterfaceMultMatrizRMI r1 = (InterfaceMultMatrizRMI)Naming.lookup(url1);
        InterfaceMultMatrizRMI r2 = (InterfaceMultMatrizRMI)Naming.lookup(url2);
        
        //inicializa las matrices A y B
	for (i=0; i<N; i++) 
            for(j=0; j<N; j++){
		A[i][j]=i-3*j;
		B[i][j]=i+3*j;
		C[i][j]=0;
            }
        
        //Imprimir Matrices
        if(N==8){
            System.out.println("----Matriz A----\n");
            ImprimirMatriz(A);
            System.out.println("\n----Matriz B----\n");
            ImprimirMatriz(B);
        }
            
        //Transpone la matriz B, la matriz transpuesta queda en B
        for(i=0; i<N; i++)
            for(j=0; j<i; j++){
                float x = B[i][j];
                B[i][j]=B[j][i];
                B[j][i]=x;
            }
        
        float[][] A1 = separa_matriz(A,0);
        float[][] A2 = separa_matriz(A,N/2);  
        float[][] B1 = separa_matriz(B,0);
        float[][] B2 = separa_matriz(B,N/2);
        
        float[][] C1 = r1.multiplica_matrices(A1,B1,N);
        float[][] C2 = r1.multiplica_matrices(A1,B2,N);
        float[][] C3 = r2.multiplica_matrices(A2,B1,N);
        float[][] C4 = r2.multiplica_matrices(A2,B2,N);

        acomoda_matriz(C,C1,0,0);
        acomoda_matriz(C,C2,0,N/2);
        acomoda_matriz(C,C3,N/2,0);
        acomoda_matriz(C,C4,N/2,N/2);
        
        if(N==8){
            System.out.println("----Matriz C----\n");
            ImprimirMatriz(C);
        }
        
        //Checksum
        for (i=0; i<N; i++) 
            for(j=0; j<N; j++)
                checksum = checksum + C[i][j];
            
        System.out.println("\nChecksum: "+checksum);
    }
    
    static float[][] separa_matriz(float[][] A,int inicio)
    {
        float[][] M = new float[N/2][N];
        
        for (int i = 0; i < N/2; i++)
            for (int j = 0; j < N; j++)
                M[i][j] = A[i + inicio][j];
        
        return M;
    }
    
    static void acomoda_matriz(float[][] C,float[][] A,int renglon,int columna){
        for (int i = 0; i < N/2; i++)
            for (int j = 0; j < N/2; j++)
                C[i + renglon][j + columna] = A[i][j];
    }
    
    public static void ImprimirMatriz(float[][] matriz){
        for (int i=0; i<N; i++){ 
            System.out.print("|");
            for(int j=0; j<N; j++)                
                System.out.print(matriz[i][j]+"\t|");
            System.out.println();   
        }
    }
}
