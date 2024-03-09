package redespractica2_servidor;

import Articulo.Articulo;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextPane;
import javax.swing.SwingConstants;
import javax.swing.text.BadLocationException;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;
import redespractica2_cliente.Catalogo;

public class Ticket extends JFrame{
    ServerSocket s;
    ArrayList <Articulo> articulos= new ArrayList();//Arreglo de objetos de tipo Articulo
    ArrayList <Articulo> listacarrito= new ArrayList();//Lista de compra
    private Map<String, Integer> numproductos= new HashMap<>();
    JPanel panelPrincipal= new JPanel();
    JPanel contenido= new JPanel();
    JPanel encabezado= new JPanel();
    String linea= "";
    int numArt=0;
    int numCarrito=0;
    static float IVA= 0.16f;
        
    public Ticket(){
        super("Ticket de Compra");
        setSize(520, 900);//Establecemos el tamaño de la ventana (ancho, largo)
        setLocationRelativeTo(null);//Establecemos la ventana en el centro
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        
        for(int i=0; i<37; i++)
            linea= linea + "─";
        
        DefinirArticulos();
        EnviarArticulos();
        
        for(;;){
            RecibirListaCompras();
            panelPrincipal.removeAll();
            panelPrincipal.updateUI();
            setVisible(true);
            
            iniciarComponentes();
            ActualizarBaseDatos();
            listacarrito.clear();
            numproductos.clear();
        }
    }
    
    public void DefinirArticulos(){
        articulos.clear();
        Articulo dragon= new Articulo("drg", "dragon", "Una lagartija gigante que escupe mucho fueguito uwu y roba cositas brillantes :0", 1000.50f, "2x1", 10, "dragon.jpg");
        articulos.add(dragon);
        numArt++;
        
        Articulo asdasdasd= new Articulo("asd", "asdasdasd", null, 923.75f, null, 12, "dragon.jpg");
        articulos.add(asdasdasd);
        numArt++;
    }
    
    public void EnviarArticulos(){
        try{
            s= new ServerSocket(9090);
            s.setReuseAddress(true);
            Socket cl= s.accept();
            
            ObjectOutputStream oos = new ObjectOutputStream(cl.getOutputStream());
            oos.writeInt(numArt);
            oos.flush();
            
            for(int i=0; i<numArt; i++){
                oos.writeObject(articulos.get(i));
                oos.flush();
                System.out.println("Envie Objeto: "+articulos.get(i).imprimirDatos());
            }
            
            oos.close();
            cl.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    public void RecibirListaCompras(){
        try{
            Socket cl= s.accept();
            
            ObjectInputStream ois = new ObjectInputStream(cl.getInputStream());
            numCarrito= ois.readInt();
           
            for(int i=0; i<numCarrito; i++){
                Articulo art= (Articulo)ois.readObject();
                listacarrito.add(art);
                numproductos.put(art.id, (ois.readInt()));
            }
            
            ois.close();
            cl.close();

        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    public void iniciarComponentes(){  
        getContentPane().setLayout(new BorderLayout(0, 0));
        getContentPane().add(panelPrincipal, BorderLayout.CENTER);
        panelPrincipal.setLayout(new BorderLayout(0, 0));
        DefinirEncabezado();
        GenerarTicket();
    }
    
    public void DefinirEncabezado(){
        encabezado.removeAll();
        encabezado.updateUI();
        encabezado.setLayout(null);
        encabezado.setOpaque(false);
        
        Date date = new Date();
        DateFormat fecha = new SimpleDateFormat("dd/MM/yyyy    HH:mm:ss");
        
        JLabel line= new JLabel(linea);
        line.setBounds(10, 10, 485, 10);
        line.setOpaque(false);
        //line.setBackground(Color.blue);
        
        JLabel titulo= new JLabel("TICKET DE COMPRA", SwingConstants.CENTER);
        titulo.setBounds(10, 25, 485, 20);
        titulo.setFont(new Font("Calibri", 1, 27));
        //titulo.setOpaque(false);
        
        JLabel line2= new JLabel(linea);
        line2.setBounds(10, 45, 485, 10);
        line2.setOpaque(false);
        //line2.setBackground(Color.yellow);
        
        JLabel diahora= new JLabel("Fecha: " + fecha.format(date), SwingConstants.LEFT);
        diahora.setBounds(10, 65, 480, 15);
        diahora.setFont(new Font("Arial", 0, 15));
        diahora.setOpaque(false);
        diahora.setBackground(Color.GREEN);
        
        JLabel line3= new JLabel(linea);
        line3.setBounds(10, 90, 485, 10);
        line3.setOpaque(false);
        //line3.setBackground(Color.red);
        
        JLabel etiqProducto = new JLabel("Producto:", SwingConstants.LEFT);
        etiqProducto.setBounds(10, 105, 200, 15);
        etiqProducto.setFont(new Font("Arial", 1, 15));
        etiqProducto.setOpaque(false);
        //etiqProducto.setBackground(Color.DARK_GRAY);
        
        JLabel etiqCantidad = new JLabel("Cant.:", SwingConstants.LEFT);
        etiqCantidad.setBounds(260, 105, 60, 15);
        etiqCantidad.setFont(new Font("Arial", 1, 15));
        etiqCantidad.setOpaque(false);
        //etiqCantidad.setBackground(Color.DARK_GRAY);
        
        JLabel etiqPrecioU = new JLabel("Precio:", SwingConstants.LEFT);
        etiqPrecioU.setBounds(330, 105, 70, 15);
        etiqPrecioU.setFont(new Font("Arial", 1, 15));
        etiqPrecioU.setOpaque(false);
        //etiqPrecioU.setBackground(Color.DARK_GRAY);
        
        JLabel etiqPrecioT = new JLabel("Total:", SwingConstants.LEFT);
        etiqPrecioT.setBounds(410, 105, 80, 15);
        etiqPrecioT.setFont(new Font("Arial", 1, 15));
        etiqPrecioT.setOpaque(false);
        //etiqPrecioT.setBackground(Color.DARK_GRAY);
        
        JLabel line4= new JLabel(linea);
        line4.setBounds(10, 125, 485, 10);
        line4.setOpaque(false);
        //line4.setBackground(Color.red);
        
        encabezado.add(line);
        encabezado.add(titulo);
        encabezado.add(line2);
        encabezado.add(diahora);
        encabezado.add(line3);
        encabezado.add(etiqProducto);
        encabezado.add(etiqCantidad);
        encabezado.add(etiqPrecioU);
        encabezado.add(etiqPrecioT);
        encabezado.add(line4);
        encabezado.updateUI();
        panelPrincipal.add(encabezado);
        panelPrincipal.updateUI();
    }
    
    public void GenerarTicket(){
        contenido.removeAll();
        contenido.setLayout(null);
        contenido.setOpaque(false);
        int i=0;
        float subtotal=0, iva=0, total=0;

        for(Articulo a : listacarrito){
            /*---DECLARACION DE ELEMENTOS DEL TICKET---*/
            /*Nombre del articulo*/
            JTextPane nomImagen=new JTextPane();
            nomImagen.setEditable(false);
            StyledDocument doc = nomImagen.getStyledDocument();
            SimpleAttributeSet left = new SimpleAttributeSet(); 
            StyleConstants.setAlignment(left, StyleConstants.ALIGN_LEFT); 
            doc.setParagraphAttributes(0, doc.getLength(), left, false);
            
            try {
                nomImagen.getStyledDocument().insertString(nomImagen.getStyledDocument().getLength(), a.nombre, left);
            } catch (BadLocationException ex) {
                Logger.getLogger(Catalogo.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            nomImagen.setBounds(10, 140+(i*25), 200, 20);
            nomImagen.setFont(new Font("Arial", 0, 15));
            nomImagen.setOpaque(false);
            
            /*Cantidad del producto*/
            JLabel cantidad=new JLabel(numproductos.get(a.id).toString(), SwingConstants.LEFT);
            cantidad.setBounds(260, 140+(i*25), 60, 15);
            cantidad.setOpaque(false);
            
            /*Precio unitario del producto*/
            JLabel precioUnit=new JLabel("$"+a.precio, SwingConstants.LEFT);
            precioUnit.setBounds(330, 140+(i*25), 80, 15);
            precioUnit.setOpaque(false);
            
            /*Precio total del producto*/
            float precioT=0;
            int div, res;
            int[] promo= new int[2];

            if(a.promocion!=null){
                promo= ObtenerPromocion(a.promocion);
                div= numproductos.get(a.id)/promo[0];
                res= numproductos.get(a.id)%promo[0];
                precioT= (div*(a.precio*promo[1]))+(res*a.precio);
            }
            else
                precioT= a.precio*numproductos.get(a.id);
            
            JLabel precioTotal=new JLabel("$"+precioT, SwingConstants.LEFT);
            precioTotal.setBounds(410, 140+(i*25), 80, 15);
            precioTotal.setOpaque(false);
            subtotal= subtotal+precioT;
            
            /*Adicion de los elementos al panel*/    
            contenido.add(nomImagen);
            contenido.add(cantidad);
            contenido.add(precioUnit);
            contenido.add(precioTotal);
            i++;
        }
        
        JLabel line= new JLabel(linea);
        line.setBounds(10, 140+(i*20), 485, 10);
        line.setOpaque(false);
        i++;
        
        JLabel etiqSubtotal = new JLabel("Subtotal", SwingConstants.LEFT);
        etiqSubtotal.setBounds(10, 140+(i*20), 150, 15);
        etiqSubtotal.setFont(new Font("Arial", 1, 15));
        etiqSubtotal.setOpaque(false);
        
        JLabel etiqIVA = new JLabel("IVA(16%):", SwingConstants.LEFT);
        etiqIVA.setBounds(180, 140+(i*20), 140, 15);
        etiqIVA.setFont(new Font("Arial", 1, 15));
        etiqIVA.setOpaque(false);
        
        JLabel etiqTotal = new JLabel("Total", SwingConstants.LEFT);
        etiqTotal.setBounds(340, 140+(i*20), 150, 15);
        etiqTotal.setFont(new Font("Arial", 1, 15));
        etiqTotal.setOpaque(false);
        i++;
        
        JLabel line2= new JLabel(linea);
        line2.setBounds(10, 140+(i*20), 485, 10);
        line2.setOpaque(false);
        i++;
        
        JLabel sub=new JLabel("$"+subtotal, SwingConstants.LEFT);
        sub.setBounds(10, 140+(i*20), 150, 15);
        sub.setOpaque(false);
        
        iva= subtotal*IVA;
        JLabel iv=new JLabel("$"+iva, SwingConstants.LEFT);
        iv.setBounds(180, 140+(i*20), 140, 15);
        iv.setOpaque(false);
        
        total= subtotal+iva;
        JLabel tot=new JLabel("$"+total, SwingConstants.LEFT);
        tot.setBounds(340, 140+(i*20), 150, 15);
        tot.setOpaque(false);
        
        contenido.add(line);
        contenido.add(etiqSubtotal);
        contenido.add(etiqIVA);
        contenido.add(etiqTotal);
        contenido.add(line2);
        contenido.add(sub);
        contenido.add(iv);
        contenido.add(tot);
        
        contenido.updateUI();
        panelPrincipal.add(contenido);  
        panelPrincipal.updateUI();
    }
    
    private int[] ObtenerPromocion(String promocion){
        int i=0;
        int[] valores= new int[2];
        String temp= "";
        char c= '\0';
        
        System.out.println(promocion.charAt(1));
        
        while(c!='x'){
            temp= temp + promocion.charAt(i);
            c= promocion.charAt(i+1);
            i++; ;
        }
        
        valores[0]= Integer.parseInt(temp);
        temp= "";
        i++;
        
        while(i<= promocion.length()-1){
            temp= temp + promocion.charAt(i);
            i++; 
        }
         
        valores[1]= Integer.parseInt(temp);

        return valores;
    }
    
    public void ActualizarBaseDatos(){
        for(Articulo a: listacarrito){
            //System.out.println(a.nombre+" "+a.existencias);
            /*Comparar a.id, con cada id de articulo en la base de datos hasta que encuentre a.id en esta. Una vez hecho esto, cambiar el valor de existencias de el articulo, con 
            la de a.existencias*/
        }
    }
}
