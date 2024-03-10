import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceMultMatrizRMI extends Remote{
    public float[][] multiplica_matrices(float[][] A,float[][] B, int N) throws RemoteException;
}
