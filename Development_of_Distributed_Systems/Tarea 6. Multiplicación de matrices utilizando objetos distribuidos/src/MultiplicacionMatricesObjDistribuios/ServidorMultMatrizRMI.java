import java.rmi.Naming;

public class ServidorMultMatrizRMI {
    public static void main(String[] args) throws Exception{
    String url = "rmi://localhost/MatrizObjDist";
    ClaseMultMatrizRMI obj = new  ClaseMultMatrizRMI();

    // registra la instancia en el rmiregistry
    Naming.rebind(url,obj);
  }
}
