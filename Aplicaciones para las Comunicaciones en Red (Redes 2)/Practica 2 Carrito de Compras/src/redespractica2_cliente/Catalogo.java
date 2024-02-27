package redespractica2_cliente;

import Articulo.Articulo;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
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

public class Catalogo extends JFrame{
    private ArrayList <Articulo> articulos= new ArrayList();//Arreglo de objetos de tipo Articulo
    //Lista para guardar el nunmero de elementos seleccionados por el usuario(Esto se hacepara evitar modificar el objeto Articulo)
    private Map<String, Integer> numproductos= new HashMap<>();
    private Map<String, Integer> existencia= new HashMap<>();//Hash Map para gusrdar las exitencias de todos los productos
    public Map<String, Articulo> listacarrito= new HashMap<>();//Lista de compra
    private Vector<Integer> contexist= new Vector<Integer>();//vector temporal para definir los elementos de las listas desplegables
    JScrollPane scroll= new JScrollPane();//Barra desplazadora
    JButton[] arregloBotones;//Botones VER CARRITO y COMPRAR
    JPanel panelPrincipal= new JPanel();//Panel donde se agruparan todos los paneles, para añadirles posteriorimente el scroll
    JPanel contenido= new JPanel();//Panel para el contenido del catalogo
    Carrito carr;//Objeto para la lista del carrito
    Solicitud solicitud;
    JFrame temp;//Reeferencia a el JFrame del Catalogo
    int numArt=0;//Nunmero de articulos que son recibidos;
    int pto;
    String host;
    
    public Catalogo(){
        super("Catalogo");
        setSize(1250, 700);//Establecemos el tamaño de la ventana (ancho, largo)
        setLocationRelativeTo(null);//Establecemos la ventana en el centro
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        temp= this;
        
        RecibirArticulos();
        iniciarComponentes();
        
        scroll.setViewportView(panelPrincipal);
        getContentPane().add(scroll, BorderLayout.CENTER);
    }
    
    //Proceso para recibir los articulos desde el servidor
    private void RecibirArticulos(){
        solicitud=new Solicitud(temp, true, pto, host);
        solicitud.setVisible(true);
        pto= solicitud.pto;
        host= solicitud.host;
                
        try{
            Socket cl = new Socket(host, pto);
            
            ObjectInputStream ois = new ObjectInputStream(cl.getInputStream());
            numArt= ois.readInt();//recibimos el entero que nos indica el numero de articulos que recibiremos
            System.out.println(numArt);
            
            for(int i=0; i<numArt; i++){//ciclo que recibira todos los objetos que el servidor le mande
                Articulo art= (Articulo)ois.readObject();
                articulos.add(art);
                existencia.put(art.id, art.existencias);
                //System.out.println("Recibi objeto: "+art.imprimirDatos());
            }  
        }catch(Exception e){
            e.printStackTrace();
            dispose();
        }
    }
     
    /*Definición de los elementos del grafico de el programa*/
    private void iniciarComponentes()
    {
        getContentPane().setLayout(new BorderLayout(0, 0));
        getContentPane().add(panelPrincipal, BorderLayout.CENTER);
        panelPrincipal.setLayout(new BorderLayout(0, 0));
        DefinirEncabezado();
        DefinirBotones();
        AñadirContenido();
    }
    
    /*Definición de los elementos del encabezado*/
    private void DefinirEncabezado(){
        JPanel encabezado= new JPanel();/*Crea un panel(es como poner una hoja sobre un escritorio, para asi escribir 
        sobre esta, y no sobre el escritorio directamente*/
        encabezado.setLayout(new FlowLayout(FlowLayout.LEFT, 70, 5));
        encabezado.setBackground(Color.BLACK);
            
        /*Elementos del Encabezado*/
        JLabel etiqDescripcion= new JLabel("Descripcion");
        etiqDescripcion.setFont(new Font("Castellar", 2, 14));
        etiqDescripcion.setForeground(Color.WHITE);
        
        JLabel etiqPrecio= new JLabel("Precio");
        etiqPrecio.setFont(new Font("Castellar", 2, 14));
        etiqPrecio.setForeground(Color.WHITE);
        
        JLabel etiqPromocion= new JLabel("Promocion");
        etiqPromocion.setFont(new Font("Castellar", 2, 14));
        etiqPromocion.setForeground(Color.WHITE);
        
        JLabel etiqNombre= new JLabel("Nombre");
        etiqNombre.setFont(new Font("Castellar", 2, 14));
        etiqNombre.setForeground(Color.WHITE);
        
        /*Formato y espaciado del encabezado*/
        encabezado.add(new JLabel("\t "));
        encabezado.add(new JLabel("\t                   "));
        encabezado.add(etiqNombre);
        encabezado.add(new JLabel("                "));
        encabezado.add(etiqDescripcion);
        encabezado.add(new JLabel(""));
        encabezado.add(etiqPrecio);
        encabezado.add(etiqPromocion);
        panelPrincipal.add(encabezado, BorderLayout.PAGE_START);
    }
    
    /*Definición de los botones CARRITO y COMPRAR*/
    private void DefinirBotones(){
        JPanel botones= new JPanel();
        botones.setBackground(Color.BLACK);
        botones.setLayout(new FlowLayout());
        
        /*Botones*/
        JButton carrito=new JButton("Ver Carrito");
        JButton comprar=new JButton("Comprar");
        
        ActionListener BotonComprar= new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
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
            }
        };
        
        ActionListener VerCarrito= new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){ 
                //System.out.println("Antes de carrito");
                //System.out.println("Lista del carrito"+listacarrito.keySet()+" | "+listacarrito.values().toString());
                //System.out.println("Lista del carrito"+numproductos.keySet()+" | "+numproductos.values());
                carr=new Carrito(temp, true, listacarrito, numproductos, existencia);
                carr.setVisible(true);
                //System.out.println("Despues de carrito");
                //System.out.println("Lista del carrito"+listacarrito.keySet()+" | "+listacarrito.values().toString());
                //System.out.println("Lista del carrito"+numproductos.keySet()+" | "+numproductos.values());
                AñadirContenido();
            }
        };
        
                
        comprar.addActionListener(BotonComprar);
        carrito.addActionListener(VerCarrito);
        botones.add(carrito);
        botones.add(comprar);
        panelPrincipal.add(botones, BorderLayout.PAGE_END);
    }

    private void AñadirContenido(){
        contenido.removeAll();
        arregloBotones= new JButton[numArt];
        contenido.setLayout(null);
        contenido.setOpaque(false);
        int i=0;

        for(Articulo a: articulos){
            /*---DECLARACION DE ELEMENTOS GRAFICOS DE LA LISTA DE ARTICULOS---*/
            /*Imagen del articulo*/
            ImageIcon imagen= new ImageIcon(getClass().getResource("/Imagenes/"+a.imagen));
            JLabel etiqImagen= new JLabel();
            
            //(x, y, w, h)
            etiqImagen.setBounds(20, 10+(i*160), 150, 150);
            etiqImagen.setIcon(new ImageIcon(imagen.getImage().getScaledInstance(etiqImagen.getWidth(), etiqImagen.getHeight(), Image.SCALE_SMOOTH)));
            
            /*Nombre del articulo*/
            JTextPane nomImagen=new JTextPane();
            nomImagen.setEditable(false);
            StyledDocument doc = nomImagen.getStyledDocument();
            SimpleAttributeSet center = new SimpleAttributeSet(); 
            StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER); 
            doc.setParagraphAttributes(0, doc.getLength(), center, false);
            
            try {
                nomImagen.getStyledDocument().insertString(nomImagen.getStyledDocument().getLength(), a.nombre, center);
            } catch (BadLocationException ex) {
                Logger.getLogger(Catalogo.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            //(this x= x+w+30=200, this y= 10+(i*h+10), this w(varia), this h= h)
            nomImagen.setBounds(200, 10+(i*160), 200, 150);
            nomImagen.setFont(new Font("Arial", 1, 20));
            nomImagen.setOpaque(false);//set a true para pruebas de espaciado de Labels
            //nomImagen.setBackground(Color.BLUE);
            
            /*Descripcion del articulo*/
            JTextPane descripcion= new JTextPane();
            descripcion.setEditable(false);
            
            try {
                descripcion.getStyledDocument().insertString(descripcion.getStyledDocument().getLength(), a.descripcion, center);
            } catch (BadLocationException ex) {
                Logger.getLogger(Catalogo.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            //(this x= x+w+20=420, this y= 10+(i*h+10), this w(varia), this h= h)
            descripcion.setBounds(420, 10+(i*160), 300, 150);
            descripcion.setOpaque(false);
            //descripcion.setBackground(Color.GREEN);
            
            /*Precio del producto*/
            JLabel precio=new JLabel("$"+a.precio, SwingConstants.CENTER);//"float");
            precio.setBounds(740, 10+(i*160), 120, 150);
            precio.setOpaque(false);
            //precio.setBackground(Color.YELLOW);
            
            /*Promoción del producto*/
            JLabel promocion;
            
            if(a.promocion== null)
                promocion=new JLabel("N/A", SwingConstants.CENTER);
            else
                promocion=new JLabel(a.promocion, SwingConstants.CENTER);//("0x0");
            
            promocion.setBounds(880, 10+(i*160), 130, 150);
            promocion.setOpaque(false);
            //promocion.setBackground(Color.ORANGE);
            
            /*Existencias del producto (lista desplegable)*/
            contexist.clear();
            a.existencias= existencia.get(a.id);
            
            for(int j=0; j<=existencia.get(a.id); j++)
                contexist.add(j);
            
            JComboBox listexist= new JComboBox(contexist.toArray());//(a.id))
            //System.out.println("Exitencias de "+a.nombre+" es "+existencia.get(a.id).getItemCount());
            listexist.setSelectedIndex(0);
            listexist.setBounds(1030, 58+(i*160), 70, 25);
            
            /*Boton AGREGAR*/
            arregloBotones[i]=new JButton("AGREGAR");
            arregloBotones[i].setBounds(1120, 58+(i*160), 100, 25);
            
            if(a.existencias==0)
                arregloBotones[i].setEnabled(false);
            else
                arregloBotones[i].setEnabled(true);
            
            /*Adicion de los elementos al panel*/    
            contenido.add(etiqImagen);
            contenido.add(nomImagen);
            contenido.add(descripcion);
            contenido.add(precio);
            contenido.add(promocion);
            contenido.add(listexist);
            contenido.add(arregloBotones[i]);
            //panelPrincipal.add(Vscroll);
            
            /*Acción del boton AGREGAR*/
            ActionListener Agregar= new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    /*Si las existencias llegan a 0, el boton de Agregar se desactiva*/
                    if(a.existencias==0){
                        JButton esteBoton= (JButton)e.getSource();
                        esteBoton.setEnabled(false);
                    }
                    String temp= listexist.getSelectedItem().toString();/*Obtenemos el valor del numero de articulos
                    de la lista desplegable y la convertimos en enteros*/
                    //System.out.print(a.existencias+"-"+Integer.parseInt(temp)+"=");
                    
                    a.existencias= a.existencias-Integer.parseInt(temp);
                    existencia.replace(a.id, existencia.get(a.id), existencia.get(a.id)-Integer.parseInt(temp));
                    //System.out.println(existencia.get(a.id));
                    
                    /*Si el elemento no esta en la lista del carrito y el numero de articulos que seleccionamos es mayor a
                    0, este se añade a la lista del carrito de compra*/
                    if(!listacarrito.containsKey(a.id) && Integer.parseInt(temp)!=0){
                        //float preciofinal= a.precio*Integer.parseInt(temp);
                        listacarrito.put(a.id, a);//Guardampos el producto en la lista del carrito
                        numproductos.put(a.id, Integer.parseInt(temp));//Guardamos el numero de productos que el cliente selecciono
                        System.out.println("Agrege: "+a.nombre+" "+a.precio+"x"+numproductos.get(a.id)+"="+a.precio*numproductos.get(a.id));
                    }
                    /*Si el producto ya se halla en la lista del carrito, simplemente añade el numero de productos solicitados por el
                    cliente a los ya existentes*/
                    else{
                        numproductos.put(a.id, numproductos.get(a.id)+Integer.parseInt(temp));
                        System.out.println("Actualice: "+a.nombre+" "+a.precio+"x"+numproductos.get(a.id)+"="+a.precio*numproductos.get(a.id));
                    }
                    
                    /*Si las existencias llegan a 0, el boton de Agregar se desactiva*/
                    if(a.existencias==0){
                        JButton esteBoton= (JButton)e.getSource();
                        esteBoton.setEnabled(false);
                    }
                    
                    /*Se remueven los elementos de la lista desplegable equivalentes a el numero de productos que el 
                    cliente a solicitado*/
                    for(int k=0; k<Integer.parseInt(temp); k++)
                        listexist.removeItemAt(listexist.getItemCount()-1);

                    listexist.setSelectedIndex(0);    
                }
            };
            
            arregloBotones[i].addActionListener(Agregar);
            i++;
        }
        
        panelPrincipal.add(contenido);
        panelPrincipal.updateUI();
    }
}
