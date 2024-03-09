package redespractica2_cliente;

import Articulo.Articulo;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.SwingConstants;
import javax.swing.text.BadLocationException;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;

public class Carrito extends JDialog{
    private Map<String, Integer> existencia= new HashMap<>();
    private Map<String, Articulo> listacarrito= new HashMap<>();//Lista del productos del carrito
    private Map<String, Integer> numproductos= new HashMap<>();//Numero de productos de los articulos seleccionados por el usuario
    JScrollPane scroll= new JScrollPane();
    JButton[] botonesEliminar;//Para botones X
    JButton[] botonesAgregar;//Para botones >
    JButton[] botonesQuitar;//Para botones <
    JPanel panelPrincipal= new JPanel();
    JButton comprar;
    String prueba;
    
    public Carrito(Frame parent, boolean modal, Map<String, Articulo> listacarrito, Map<String, Integer> numproductos, Map<String, Integer> existencia){
        super(parent, "Lista de Compras", modal); 
        setSize(760, 700);//Establecemos el tamaño de la ventana (ancho, largo)
        setLocationRelativeTo(null);//Establecemos la ventana en el centro
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);        
        this.listacarrito= listacarrito;
        this.numproductos= numproductos;
        this.existencia= existencia;
        
        iniciarComponentes();
        
        scroll.setViewportView(panelPrincipal);
        getContentPane().add(scroll, BorderLayout.CENTER); 
    }
    
    private void iniciarComponentes()
    {
        getContentPane().setLayout(new BorderLayout(0, 0));
        getContentPane().add(panelPrincipal, BorderLayout.CENTER);
        panelPrincipal.setLayout(new BorderLayout(0, 0));
        DefinirEncabezado();
        DefinirBotones();
        AñadirContenido();
    }
    
    private void DefinirEncabezado(){
        JPanel encabezado= new JPanel();
        encabezado.setLayout(new FlowLayout(FlowLayout.LEFT, 40, 5));
        encabezado.setBackground(Color.BLACK);
            
        /*Elementos del Encabezado*/
        JLabel etiqNombre= new JLabel("Nombre");
        etiqNombre.setFont(new Font("Castellar", 2, 14));
        etiqNombre.setForeground(Color.WHITE);
        
        JLabel etiqCantidad= new JLabel("Cantidad");
        etiqCantidad.setFont(new Font("Castellar", 2, 14));
        etiqCantidad.setForeground(Color.WHITE);
        
        JLabel etiqPromocion= new JLabel("Descuento");
        etiqPromocion.setFont(new Font("Castellar", 2, 14));
        etiqPromocion.setForeground(Color.WHITE);
        
        JLabel etiqPrecio= new JLabel("$ Total");
        etiqPrecio.setFont(new Font("Castellar", 2, 14));
        etiqPrecio.setForeground(Color.WHITE);
        
        /*Formato y espaciado del encabezado*/
        encabezado.add(new JLabel("                  "));
        encabezado.add(new JLabel(""));
        encabezado.add(etiqNombre);
        encabezado.add(new JLabel(""));
        encabezado.add(etiqCantidad);
        encabezado.add(etiqPromocion);
        encabezado.add(etiqPrecio);
        panelPrincipal.add(encabezado, BorderLayout.PAGE_START);
    }
    
    private void DefinirBotones(){
        JPanel botones= new JPanel();
        botones.setBackground(Color.BLACK);
        botones.setLayout(new FlowLayout());
        
        /*Botones*/
        JButton regresar=new JButton("Regresar");
        comprar=new JButton("Comprar");
        
        ActionListener BotonComprar= new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
                    int pto= 9090;
                    String host= "localhost";
                    Socket cl = new Socket(host, pto);
            
                    ObjectOutputStream oos = new ObjectOutputStream(cl.getOutputStream());
                    oos.writeInt(listacarrito.size());
                    
                    for(String key : listacarrito.keySet()){
                        oos.writeObject(listacarrito.get(key));
                        oos.writeInt(numproductos.get(key));
                        oos.flush();
                    }
                    oos.close();
                    cl.close();
                }catch(Exception a){
                    a.printStackTrace();
                }
                
                listacarrito.clear();
                numproductos.clear();
                dispose();
            }  
        };
        
        ActionListener BotonRegresar= new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){ 
                dispose();
            }
        };
        
        regresar.addActionListener(BotonRegresar);       
        comprar.addActionListener(BotonComprar);
        botones.add(regresar);
        botones.add(comprar);
        panelPrincipal.add(botones, BorderLayout.PAGE_END);
    }
    
    private void AñadirContenido(){
        JPanel contenido= new JPanel();
        botonesEliminar= new JButton[listacarrito.size()];
        botonesAgregar= new JButton[listacarrito.size()];
        botonesQuitar= new JButton[listacarrito.size()];
        contenido.setLayout(null);
        contenido.setOpaque(false);
        int i=0;

        for(String key : listacarrito.keySet()){
            /*---DECLARACION DE ELEMENTOS GRAFICOS DEL CARRITO---*/
            /*Imagen del articulo*/
            ImageIcon imagen= new ImageIcon(getClass().getResource("/Imagenes/"+listacarrito.get(key).imagen));
            JLabel etiqImagen= new JLabel();
            
            //(x, y, w, h)
            etiqImagen.setBounds(10, 10+(i*110), 100, 100);
            etiqImagen.setIcon(new ImageIcon(imagen.getImage().getScaledInstance(etiqImagen.getWidth(), etiqImagen.getHeight(), Image.SCALE_SMOOTH)));
            
            /*Nombre del articulo*/
            JTextPane nomImagen=new JTextPane();
            nomImagen.setEditable(false);
            StyledDocument doc = nomImagen.getStyledDocument();
            SimpleAttributeSet center = new SimpleAttributeSet(); 
            StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER); 
            doc.setParagraphAttributes(0, doc.getLength(), center, false);
            
            try {
                nomImagen.getStyledDocument().insertString(nomImagen.getStyledDocument().getLength(), listacarrito.get(key).nombre, center);
            } catch (BadLocationException ex) {
                Logger.getLogger(Catalogo.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            //(this x= x+w+10=120, this y= 10+(i*h+10), this w(varia), this h= h)
            nomImagen.setBounds(120, 10+(i*110), 180, 100);
            nomImagen.setFont(new Font("Arial", 1, 20));
            nomImagen.setOpaque(false);
            //nomImagen.setBackground(Color.YELLOW);
            
            /*Boton <*/
            botonesQuitar[i]=new JButton("<");
            botonesQuitar[i].setBounds(300, 30+(i*110), 41, 50);
            
            /*Cantidad del producto*/
            JLabel cantidad=new JLabel(numproductos.get(key).toString(), SwingConstants.CENTER);//"float");
            cantidad.setBounds(341, 10+(i*110), 50, 100);
            cantidad.setOpaque(false);
            //cantidad.setBackground(Color.BLUE);
            
            /*Boton >*/
            botonesAgregar[i]=new JButton(">");
            botonesAgregar[i].setBounds(391, 30+(i*110), 41, 50);
            
            if(existencia.get(key)!=0)
                botonesAgregar[i].setEnabled(true);
            else
                botonesAgregar[i].setEnabled(false);
            
            /*Promoción del producto*/
            JLabel promocion;
            
            if(listacarrito.get(key).promocion== null)
                promocion=new JLabel("N/A", SwingConstants.CENTER);
            else
                promocion=new JLabel(listacarrito.get(key).promocion, SwingConstants.CENTER);//("0x0");
            
            promocion.setBounds(440, 10+(i*110), 110, 100);
            promocion.setOpaque(false);
            //promocion.setBackground(Color.ORANGE);
            
            /*Precio del producto*/
            float precioT;
            int div, res;
            int[] promo= new int[2];

            if(listacarrito.get(key).promocion!=null){
                promo= ObtenerPromocion(listacarrito.get(key).promocion);
                div= numproductos.get(key)/promo[0];
                res= numproductos.get(key)%promo[0];
                precioT= (div*(listacarrito.get(key).precio*promo[1]))+(res*listacarrito.get(key).precio);
            }
            else
                precioT= listacarrito.get(key).precio*numproductos.get(key);
            
            JLabel precioTotal=new JLabel("$"+precioT, SwingConstants.CENTER);//"float");
            precioTotal.setBounds(560, 10+(i*110), 110, 100);
            precioTotal.setOpaque(false);
            //precioTotal.setBackground(Color.WHITE);
            
            /*Boton X*/
            botonesEliminar[i]=new JButton("X");
            botonesEliminar[i].setBounds(680, 30+(i*110), 50, 50);
            
            /*Adicion de los elementos al panel*/    
            contenido.add(etiqImagen);
            contenido.add(nomImagen);
            contenido.add(cantidad);
            contenido.add(promocion);
            contenido.add(precioTotal);
            contenido.add(botonesEliminar[i]);
            contenido.add(botonesAgregar[i]);
            contenido.add(botonesQuitar[i]);
                       
            /*Acción del boton X*/
            ActionListener Eliminar= new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    JLabel NA;
                    //total= existencias sobrantes + productos solicitados por el cliente
                    existencia.replace(key, existencia.get(key)+numproductos.get(key));//Sumamos los productos solicitados por el cliente, al del numero de existencias
                    listacarrito.remove(key);//Removemos el articulo de la lista del carrito
                    numproductos.remove(key);//Removemos la cantidad solicitada de productos por el cliente, de dicha lista
                    contenido.removeAll();
                    
                    //Refrescamos el panel de contenido
                    //Si la lista del carrito se queda vacia, le informamos al usuarios con un mensaje, que su carrito esta vacio, y desactivamos el boton Comprar
                    if(listacarrito.isEmpty()){
                        NA= new JLabel("No hay articulos en el carrito", SwingConstants.CENTER);
                        NA.setBounds(0, 10, 760, 100);
                        NA.setFont(new Font("Arial", 2, 25));
                        NA.setForeground(Color.RED);
                        contenido.add(NA);
                        comprar.setEnabled(false);
                        contenido.updateUI();
                        panelPrincipal.updateUI();
                    }
                    else
                        AñadirContenido();
                }
            };
            
            /*Acción del boton +*/
            ActionListener Agregar= new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    float precioT;
                    int div, res;
                    int[] promo= new int[2];
                    existencia.replace(key, existencia.get(key), existencia.get(key)-1);//Restamos 1 existencia
                    numproductos.replace(key, numproductos.get(key), numproductos.get(key)+1);//Sumamos 1 producto solicitado por el cliente
                    listacarrito.get(key).existencias= listacarrito.get(key).existencias-1;
                    cantidad.setText(numproductos.get(key).toString());
                    
                    if(listacarrito.get(key).promocion!=null){
                        promo= ObtenerPromocion(listacarrito.get(key).promocion);
                        div= numproductos.get(key)/promo[0];
                        res= numproductos.get(key)%promo[0];
                        precioT= (div*(listacarrito.get(key).precio*promo[1]))+(res*listacarrito.get(key).precio);
                    }
                    else
                        precioT= listacarrito.get(key).precio*numproductos.get(key);
                    
                    precioTotal.setText("$"+Float.toString(precioT));
                    
                    if(existencia.get(key)==0){
                        JButton esteBoton= (JButton)e.getSource();
                        esteBoton.setEnabled(false);
                    }
                }
            };
            
            /*Acción del boton -*/
            ActionListener Quitar= new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    float precioT;
                    int div, res;
                    int[] promo= new int[2];
                    existencia.replace(key, existencia.get(key), existencia.get(key)+1);//Sumamos 1 existencia
                    numproductos.replace(key, numproductos.get(key), numproductos.get(key)-1);//Restamos 1 producto solicitado por el cliente
                    listacarrito.get(key).existencias= listacarrito.get(key).existencias+1;
                    cantidad.setText(numproductos.get(key).toString());
                    
                    if(listacarrito.get(key).promocion!=null){
                        promo= ObtenerPromocion(listacarrito.get(key).promocion);
                        div= numproductos.get(key)/promo[0];
                        res= numproductos.get(key)%promo[0];
                        precioT= (div*(listacarrito.get(key).precio*promo[1]))+(res*listacarrito.get(key).precio);
                    }
                    else
                        precioT= listacarrito.get(key).precio*numproductos.get(key);
                    
                    precioTotal.setText("$"+Float.toString(precioT));
                    
                    if(numproductos.get(key)==0){
                        JLabel NA;
                        existencia.replace(key, existencia.get(key)+numproductos.get(key));
                        listacarrito.remove(key);
                        numproductos.remove(key);
                        contenido.removeAll();
                        
                        if(listacarrito.isEmpty()){
                            NA= new JLabel("No hay articulos en el carrito", SwingConstants.CENTER);
                            NA.setBounds(0, 10, 760, 100);
                            NA.setFont(new Font("Arial", 2, 25));
                            NA.setForeground(Color.RED);
                            contenido.add(NA);
                            comprar.setEnabled(false);
                            contenido.updateUI();
                            panelPrincipal.updateUI();
                        }
                        else
                            AñadirContenido();
                        
                        panelPrincipal.updateUI();
                    }
                    if(existencia.get(key)==1){
                        contenido.removeAll();
                        AñadirContenido();
                        contenido.updateUI();
                        panelPrincipal.updateUI();
                    }
                }
            };
            
            botonesEliminar[i].addActionListener(Eliminar);
            botonesAgregar[i].addActionListener(Agregar);
            botonesQuitar[i].addActionListener(Quitar);
            i++;
        }
        
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
            i++;
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
}
