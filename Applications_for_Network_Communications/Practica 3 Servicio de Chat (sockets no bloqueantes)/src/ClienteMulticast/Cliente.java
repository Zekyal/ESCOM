//Practica 3. Servicio de chat no bloqueante(Cliente)
package ClienteMulticast;

import Mensaje.Mensaje;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedInputStream;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;
import java.net.SocketAddress;
import java.net.SocketException;
import java.net.StandardProtocolFamily;
import java.net.StandardSocketOptions;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JPopupMenu;
import javax.swing.JTextField;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.WindowConstants;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;

public class Cliente extends JFrame implements Runnable{  
    //Definicion de emoticonos para el chat
    public static final String owo= "oωo";
    public static final String flechaDerecha= "→";
    public static final String flechaBidireccional= "↔";
    public static final String flechaIzquierda= "←";
    public static final String caritaFeliz= "";
    public static final String caritaSeria= "";
    public static final String caritaTriste= "";
    public static final String avion= "";//emt-:plane
    public static final String estrella= "";//emt-:star
    public static final String comunismo= "☭";//emt-:commie
    
    //Variables Globales
    private static final String MCAST_INTF = "lo";
    public static final String MCAST_ADDR  = "230.1.1.1";
    public static final int MCAST_PORT = 4000;
    public static final int DGRAM_BUF_LEN=6400; //tamaño del buffer
    public String nombreUsuario;
    public String usuarioDestino;
    public String tipo= null;
    public ArrayList<String> users= new ArrayList<>();
    InetAddress group;
    SocketAddress address;
    NetworkInterface ni;
    DatagramChannel channel ;
    Selector selector = Selector.open();
    InetSocketAddress pto;
    Mensaje mensaje;
    JFrame temp;
            
    public Cliente() throws SocketException, IOException{
        super("Chat Multicast");
        this.setResizable(false);//no permite redimensionar la ventana
        this.setLocationRelativeTo(null);//inicia la ventana en el centro de la pantalla
        temp= this;
                
    	try{
            group = InetAddress.getByName(MCAST_ADDR);//intenta resolver la direccion
            address = new InetSocketAddress(MCAST_ADDR, MCAST_PORT);
            ni = NetworkInterface.getByName(MCAST_INTF);
            pto = new InetSocketAddress(MCAST_PORT);
            
            channel= DatagramChannel.open(StandardProtocolFamily.INET);
            channel.configureBlocking(false);
            channel.setOption(StandardSocketOptions.SO_REUSEADDR, true);
            channel.setOption(StandardSocketOptions.IP_MULTICAST_IF, ni);
            channel.setOption(StandardSocketOptions.IP_MULTICAST_TTL, 128);
            channel.socket().bind(pto);//se declara para que el canal pueda escuchar el mensaje de todos los clientes y el servidor. Si se quita, solo escuchara los del servidor
            channel.join(group, ni);
        }catch(UnknownHostException e){
            e.printStackTrace();
            System.exit(1);
        } 
        
        LogIn();
        initComponents();
        Usuarios.setLayout(null);
        
        this.addWindowListener(new WindowAdapter(){
            /*Devuelven un int: 0 (Sí), 1(No)*/
            public void windowClosing(WindowEvent e){
                int i= JOptionPane.showConfirmDialog(null, "Esta seguro que desea salir?", "Cerrar Sesión", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE);
                
                if(i==JOptionPane.YES_OPTION){
                    LogOut();
                    temp.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);//cierra aplicacion
                }
                else
                    temp.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
            }
        });
    }
    
    //Funcion que le abrira el dialogo para pedirle al usuario su nombre de usuario, y mandara un objeto Mensaje de tipo INICIO a los demas clientes
    private void LogIn() throws IOException{
        Login login= new Login(this, true);//Dialogo donde se le pedirá al usuario su nombre de uuario
        login.setVisible(true);
        nombreUsuario= login.nombreUsuario;//obtenemos el nombre de usuario
        
        if(login.nombreUsuario== null){//si el nombre de usuario de login es null cerrara la aplicacion y marcará ERROR
            System.out.println("ERROR: Nombre de Usuario no Válido");
            System.exit(1);
        }
        
        mensaje= new Mensaje("INICIO", nombreUsuario);//creamos el objeto Mensaje de tipo INICIO

        try{
            System.out.println("interfaz: "+ni.getName());
            channel.register(selector,SelectionKey.OP_WRITE);
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);//convierte en bytes el objeto a mandar
            oos.writeObject(mensaje);
            oos.flush();
            byte[] data = baos.toByteArray();
            ByteBuffer buffer = ByteBuffer.wrap(data);
            System.out.println(buffer.limit()+" bytes a ser enviados a"+((InetSocketAddress)address).getAddress()+":"+((InetSocketAddress)address).getPort());
            //System.out.println(buffer.array()+" "+buffer.hasArray()+" "+buffer.toString());
           // while(true){
            selector.select();
            Iterator<SelectionKey>it = selector.selectedKeys().iterator();
          
            while(it.hasNext()){
                SelectionKey key = (SelectionKey)it.next();
                it.remove();
                
                if(key.isWritable()){
                    //System.out.println(buffer.limit());
                    channel.send(buffer, address);
                    buffer.clear();
                    continue;
                  //  break;
                }
                else{
                    System.out.println("ERROR al realizar conexión");
                    System.exit(1);
                }
            }
          //  }
        }catch(IOException e){
            e.printStackTrace();
            System.exit(1);
    	}
    }
    
    // Funcion que enviara un mensaje de finde sesión tanto al servidor, como los demas clientes
    public void LogOut(){
        mensaje= new Mensaje("FIN", nombreUsuario);//creamos el objeto Mensaje de tipo FIN

        try{
            channel.register(selector, SelectionKey.OP_WRITE);
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);//convierte en bytes el objeto a mandar
            oos.writeObject(mensaje);
            oos.flush();
            byte[] data = baos.toByteArray();
            ByteBuffer buffer = ByteBuffer.wrap(data);
            
            //espera 5 segundos para recibir la conexión(servidor y clientes)
            selector.select();
            Iterator<SelectionKey>it = selector.selectedKeys().iterator();
          
            while(it.hasNext()){
                SelectionKey key = (SelectionKey)it.next();
                it.remove();
                
                if(key.isWritable()){
                    //System.out.println(buffer.limit());
                    channel.send(buffer, address);
                    buffer.clear();
                    continue;
                }
                else{
                    System.out.println("ERROR al realizar conexión");
                    System.exit(1);
                }
            }
        }catch(IOException e){
            e.printStackTrace();
            System.exit(1);
    	}
    }
    
    //Función que recibirá cada unos de los mensajes que sean enviados desde otros usuarios, analizara que tipo de mensaje es, y los mostrara con cierto formato segun sea el caso
    public void RecibirMensaje(){
        try{
            //Definicion para el formato NEGRITAS
            StyledDocument doc = Chat.getStyledDocument();
            SimpleAttributeSet negritas = new SimpleAttributeSet();
            StyleConstants.setBold(negritas, true);
            
            channel.register(selector, SelectionKey.OP_READ | SelectionKey.OP_WRITE);
            ByteBuffer buffer = ByteBuffer.allocate(DGRAM_BUF_LEN);
            selector.select();
            Iterator<SelectionKey>it = selector.selectedKeys().iterator();
            
            while(it.hasNext()){
                SelectionKey key = (SelectionKey)it.next();
                it.remove();
                
                if(key.isReadable()){
                    buffer.clear();
                    channel.receive(buffer);
                    buffer.flip();
                    
                    if(buffer.hasArray() && buffer.limit()>=50){
                        ByteArrayInputStream bais = new ByteArrayInputStream(buffer.array());
                        ObjectInputStream ois = new ObjectInputStream(new BufferedInputStream(bais));
                        Mensaje msg = (Mensaje)ois.readObject();//convierte el paquete recibido a un objeto tipo Mensaje
                        //System.out.println(msg.tipo+" "+msg.tipo.equals("INICIO")+" "+msg.usuarioOrigen+" "+msg.mensaje);
                        
                        //Mensaje de Inicio de Sesión de un Usuario
                        if(msg.tipo.equals("INICIO")){  
                            buffer.clear();
                            channel.register(selector, SelectionKey.OP_READ | SelectionKey.OP_WRITE);
                            selector.select();
                            it = selector.selectedKeys().iterator();
                            
                            while(it.hasNext()){
                                key = (SelectionKey)it.next();
                                it.remove();
                                    
                                if(key.isReadable()){
                                    channel.receive(buffer);
                                    buffer.flip();
                                    int numUsuarios= buffer.getInt();
                                    //System.out.println(numUsuarios);
                                    
                                    for(int i=0; i<numUsuarios; i++){
                                        buffer.clear();
                                        channel.receive(buffer);
                                        buffer.flip();
                                        //System.out.println(buffer.limit());
                                        String usuario= Charset.forName("UTF-16").newDecoder().decode(buffer).toString();
                                        //System.out.println(usuario);
                    
                                        //si el usuario no se encontraba previamente en la lista de usaurios conectados local, se procede a añadirlo, de lo contrario no se añade y se pasa al siguiente
                                        if(!users.contains(usuario))
                                            users.add(usuario);
                                    }
                    
                                    ActualizarUsuarios();
                                    System.out.println("<inicio>"+msg.usuarioOrigen);  

                                    //Imprimimos el mensaje en el chat
                                    try{
                                        doc.insertString(doc.getLength(), "El usuario <"+msg.usuarioOrigen+"> ha inciado sesión\n", negritas);
                                    }
                                    catch(Exception e){ 
                                        e.printStackTrace();
                                    }
                                }//is Readable      
                            }//hasNext
                        }//if INICIO
                        //Mensaje Publico al grupo
                        else if(msg.tipo.equals("PUBLICO")){   
                            System.out.println("<msj><"+msg.usuarioOrigen+">: "+msg.mensaje);
                
                             //Imprimimos el mensaje en el chat
                            try{
                                doc.insertString(doc.getLength(), msg.usuarioOrigen+": ", negritas);
                                doc.insertString(doc.getLength(), Emoticonos(msg.mensaje)+"\n", null);
                            }
                            catch(Exception e){ 
                                e.printStackTrace();
                            }
                        }//if PUBLICO
                        //Mensaje Privado a un usuario del grupo en particular
                        else if(msg.tipo.equals("PRIVADO")){
                            if(nombreUsuario.equals(msg.usuarioDestino.trim()) || msg.usuarioOrigen.equals(nombreUsuario)){
                                System.out.println("<privado><"+msg.usuarioOrigen+"><"+msg.usuarioDestino+">: "+msg.mensaje);
                    
                                //Imprimimos el mensaje en el chat
                                try{
                                    doc.insertString(doc.getLength(), msg.usuarioOrigen+" (mensaje privado a "+msg.usuarioDestino+"): ", negritas);
                                    doc.insertString(doc.getLength(), Emoticonos(msg.mensaje)+"\n", null);
                                }
                                catch(Exception e){ 
                                    e.printStackTrace();
                                }
                            }
                        }//if PRIVADO
                        //Mensaje de Cerrado de Sesión de un Usuario
                        else if(msg.tipo.equals("FIN")){  
                            users.clear();//vacia la lista de usuarios, para posteriorimente llenarla de nuevo
                            buffer.clear();
                            channel.register(selector, SelectionKey.OP_READ | SelectionKey.OP_WRITE);
                            selector.select();
                            it = selector.selectedKeys().iterator();
                            
                            while(it.hasNext()){
                                key = (SelectionKey)it.next();
                                it.remove();
                                    
                                if(key.isReadable()){
                                    channel.receive(buffer);
                                    buffer.flip();
                                    int numUsuarios= buffer.getInt();
                                    //System.out.println(numUsuarios);
                                    
                                    for(int i=0; i<numUsuarios; i++){
                                        buffer.clear();
                                        channel.receive(buffer);
                                        buffer.flip();
                                        //System.out.println(buffer.limit());
                                        String usuario= Charset.forName("UTF-16").newDecoder().decode(buffer).toString();
                                        //System.out.println(usuario);
                                        users.add(usuario);
                                    }
                    
                                    ActualizarUsuarios();
                                    System.out.println("<fin>"+msg.usuarioOrigen);  

                                    //Imprimimos el mensaje en el chat
                                    try{
                                        doc.insertString(doc.getLength(), "El usuario <"+msg.usuarioOrigen+"> ha finalizado sesión\n", negritas);
                                    }
                                    catch(Exception e){ 
                                        e.printStackTrace();
                                    }
                                }//isReadable      
                            }//hasNext
                        }//if FIN
                    }//hasArray
                }//isReadable
            }//while
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    //Funcion que se encargará de actualizar la lista de usuarios mostrada en el modo gráfico del ptorgrama
    public void ActualizarUsuarios(){
        int i=0;
        Usuarios.removeAll();//remueve todos los elementos del grafico donde se muestra la lista de usuarios
        
        JTextField mainUser = new JTextField("  "+nombreUsuario);
        mainUser.setEditable(false);
        mainUser.setBounds(0, i*30, Usuarios.getWidth(), 30);
        mainUser.setBackground(java.awt.Color.GREEN);
        mainUser.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(51, 204, 0)));
        Usuarios.add(mainUser);
        i++;
        
        //Ciclo que se ecargará de generar areas de texto no editables, donde se mostrará el nombre de cada uno de los usuarios conectados
        for(String user: users){
            //Si el usuario de la lista es el mismo que el nombre de usuario de este cliente
            if(!user.equals(nombreUsuario)){
                JTextField textField = new JTextField("  "+user);
                textField.setEditable(false);
                textField.setBounds(0, i*30, Usuarios.getWidth(), 30);
                textField.setBackground(java.awt.Color.cyan);
                textField.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 153, 255)));
                
                //Declaracion del menu que se mostrara al dar click derecho en el area de texto donde se mostrará el usuario
                JPopupMenu popup = new JPopupMenu();
                textField.add(popup);
                textField.setComponentPopupMenu(popup);
                JMenuItem msgPrivado = new JMenuItem("Mensaje Privado");  
                popup.add(msgPrivado);
                
                msgPrivado.addActionListener(new ActionListener(){
                    public void actionPerformed(ActionEvent ae) {
                        tipo= "PRIVADO";
                        usuarioDestino= user;
                        jLabel1.setFont(new Font("Arial", Font.ITALIC, 12));
                        jLabel1.setText("<html><p>Mensaje Privado:\n"+nombreUsuario+" - "+usuarioDestino+"</p></html>");
                        //System.out.println(usuarioDestino);
                    }
                });
                            
                Usuarios.add(textField);
                i++;
            }
        }

        Usuarios.revalidate();
        Usuarios.repaint();
    }
    
    public String Emoticonos(String mensaje){
        int i= 0, tam= mensaje.length();
        char c;
        String msgEmoticono= "";
        
        while(i<tam){
            c = mensaje.charAt(i);
            
            //en caso de que haya un espacio o haya un inicio de texto, habra una posibilidad de que se genere un emoticono
            if(c== ' ' || i==0){
                if(c== ' '){
                    msgEmoticono= msgEmoticono+c;
                    i++; 
                    c = mensaje.charAt(i);
                }
                
                //EMOTICON OWO
                if(c == 'o' && mensaje.charAt(i+1)== 'w' && mensaje.charAt(i+2)== 'o'){
                    if((i+3)>=mensaje.length() || mensaje.charAt(i+3)==' '){
                        msgEmoticono= msgEmoticono+owo;
                        i= i+2;
                    }
                    else
                        msgEmoticono= msgEmoticono+c;
                }
                //EMOTICONO ->
                else if(c== '-' && mensaje.charAt(i+1)== '>'){
                    if((i+2)>=mensaje.length() || mensaje.charAt(i+2)==' '){
                        msgEmoticono= msgEmoticono+flechaDerecha;
                        i++;
                    }
                    else
                        msgEmoticono= msgEmoticono+c;
                }
                //EMOTICONO FLECHAS <-, <->
                else if(c=='<'&& mensaje.charAt(i+1)== '-'){
                    //EMOTICONO <-
                    if((i+2)>=mensaje.length() || mensaje.charAt(i+2)==' '){
                        msgEmoticono= msgEmoticono+flechaIzquierda;
                        i++;
                    }
                    //EMOTICONO <->
                    else if(mensaje.charAt(i+2)== '>'){
                        if((i+3)>=mensaje.length() || mensaje.charAt(i+3)==' '){
                            msgEmoticono= msgEmoticono+flechaBidireccional;
                            i= i+2;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    else
                        msgEmoticono= msgEmoticono+c;
                }
                //EMOTICONOS DE CARITAS
                else if(c==':'){
                    //EMOTICONO :)
                    if(mensaje.charAt(i+1)== ')'){
                        if((i+2)>=mensaje.length() || mensaje.charAt(i+2)==' '){
                            msgEmoticono= msgEmoticono+caritaFeliz;
                            i++;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    //EMOTICONO :/
                    else if(mensaje.charAt(i+1)== '/'){
                        if((i+2)>=mensaje.length() || mensaje.charAt(i+2)==' '){
                            msgEmoticono= msgEmoticono+caritaSeria;
                            i++;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    //EMOTICONO :(
                    else if(mensaje.charAt(i+1)== '('){
                        if((i+2)>=mensaje.length() || mensaje.charAt(i+2)==' '){
                            msgEmoticono= msgEmoticono+caritaTriste;
                            i++;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    else
                        msgEmoticono= msgEmoticono+c;
                }
                //EMOTICONOS TIPO emt-:
                else if(c=='e' && mensaje.charAt(i+1)== 'm' && mensaje.charAt(i+2)== 't' && mensaje.charAt(i+3)== '-' && mensaje.charAt(i+4)== ':'){
                    //EMOTICONO avion()
                    if(mensaje.charAt(i+5)== 'p' && mensaje.charAt(i+6)== 'l' && mensaje.charAt(i+7)== 'a' && mensaje.charAt(i+8)== 'n' && mensaje.charAt(i+9)== 'e'){
                        if((i+10)>=mensaje.length() || mensaje.charAt(i+10)==' '){
                            msgEmoticono= msgEmoticono+avion;
                            i= i+9;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    //EMOTICONO estrella()
                    else if(mensaje.charAt(i+5)== 's' && mensaje.charAt(i+6)== 't' && mensaje.charAt(i+7)== 'a' && mensaje.charAt(i+8)== 'r'){
                        if((i+9)>=mensaje.length() || mensaje.charAt(i+9)==' '){
                            msgEmoticono= msgEmoticono+estrella;
                            i= i+8;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    //EMOTICONO comunismo(☭)
                    else if(mensaje.charAt(i+5)== 'c' && mensaje.charAt(i+6)== 'o' && mensaje.charAt(i+7)== 'm' && mensaje.charAt(i+8)== 'm' && mensaje.charAt(i+9)== 'i' && mensaje.charAt(i+10)== 'e'){
                        if((i+11)>=mensaje.length() || mensaje.charAt(i+11)==' '){
                            msgEmoticono= msgEmoticono+comunismo;
                            i= i+10;
                        }
                        else
                            msgEmoticono= msgEmoticono+c;
                    }
                    else
                        msgEmoticono= msgEmoticono+c;
                }
                else
                    msgEmoticono= msgEmoticono+c;
            }
            else
                msgEmoticono= msgEmoticono+c;
            
            i++;
        }
        
        return msgEmoticono;
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPopupMenu1 = new javax.swing.JPopupMenu();
        msgGrupal = new javax.swing.JMenuItem();
        jPanel1 = new javax.swing.JPanel();
        AreaTexto = new java.awt.TextArea();
        botonEnviar = new javax.swing.JButton();
        UserScrollPane = new java.awt.ScrollPane();
        Usuarios = new javax.swing.JPanel();
        jScrollPane1 = new javax.swing.JScrollPane();
        Chat = new javax.swing.JTextPane();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();

        msgGrupal.setText("Mensaje al Grupo");
        msgGrupal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                msgGrupalActionPerformed(evt);
            }
        });
        jPopupMenu1.add(msgGrupal);

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(0, 255, 255));

        jPanel1.setBackground(javax.swing.UIManager.getDefaults().getColor("InternalFrame.activeTitleBackground"));
        jPanel1.setAutoscrolls(true);

        botonEnviar.setBackground(javax.swing.UIManager.getDefaults().getColor("FormattedTextField.selectionBackground"));
        botonEnviar.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        botonEnviar.setText("ENVIAR");
        botonEnviar.setBorder(javax.swing.BorderFactory.createBevelBorder(javax.swing.border.BevelBorder.RAISED));
        botonEnviar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botonEnviarActionPerformed(evt);
            }
        });

        UserScrollPane.setBackground(new java.awt.Color(255, 255, 255));

        Usuarios.setBackground(new java.awt.Color(255, 255, 255));

        javax.swing.GroupLayout UsuariosLayout = new javax.swing.GroupLayout(Usuarios);
        Usuarios.setLayout(UsuariosLayout);
        UsuariosLayout.setHorizontalGroup(
            UsuariosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 191, Short.MAX_VALUE)
        );
        UsuariosLayout.setVerticalGroup(
            UsuariosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 313, Short.MAX_VALUE)
        );

        UserScrollPane.add(Usuarios);

        Chat.setEditable(false);
        Chat.setFont(new java.awt.Font("Segoe UI Emoji", 0, 14)); // NOI18N
        Chat.setComponentPopupMenu(jPopupMenu1);
        jScrollPane1.setViewportView(Chat);

        jLabel1.setFont(new java.awt.Font("Arial", 2, 24)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(255, 0, 0));
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("Chat Grupal");
        jLabel1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(255, 0, 0)));

        jLabel2.setFont(new java.awt.Font("Calibri", 1, 14)); // NOI18N
        jLabel2.setText("Usuarios Conectados:");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(AreaTexto, javax.swing.GroupLayout.DEFAULT_SIZE, 363, Short.MAX_VALUE)
                    .addComponent(jScrollPane1))
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(UserScrollPane, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jLabel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jLabel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addContainerGap())
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 55, Short.MAX_VALUE)
                        .addComponent(botonEnviar, javax.swing.GroupLayout.PREFERRED_SIZE, 113, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(43, 43, 43))))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(16, 16, 16)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jLabel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel2)
                        .addGap(3, 3, 3)
                        .addComponent(UserScrollPane, javax.swing.GroupLayout.PREFERRED_SIZE, 313, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(botonEnviar, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 303, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(AreaTexto, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    //Acción que realiza el botón ENVIAR
    private void botonEnviarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botonEnviarActionPerformed
        if(!AreaTexto.getText().equals("")){    
            //Definición del tipo de mensaje a enviar
            if(tipo== "PRIVADO"){
                mensaje= new Mensaje("PRIVADO", nombreUsuario, usuarioDestino, AreaTexto.getText());
                tipo= null;
                jLabel1.setFont(new Font("Arial", Font.ITALIC, 24));
                jLabel1.setText("Chat Grupal");
            }
            else//tipo== null
                mensaje= new Mensaje("PUBLICO", nombreUsuario, AreaTexto.getText());
        
            try{
                channel.register(selector, SelectionKey.OP_READ | SelectionKey.OP_WRITE);
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
                ObjectOutputStream oos = new ObjectOutputStream(baos);//convierte en bytes el objeto a mandar
                oos.writeObject(mensaje);
                oos.flush();
                byte[] data = baos.toByteArray();
                ByteBuffer buffer = ByteBuffer.wrap(data);
            
                //espera 5 segundos para recibir la conexión(servidor y clientes)
                selector.select();
                Iterator<SelectionKey>it = selector.selectedKeys().iterator();
                
                while(it.hasNext()){
                    SelectionKey key = (SelectionKey)it.next();
                    it.remove();
                    
                    if(key.isWritable()){
                        //System.out.println(buffer.limit());
                        channel.send(buffer, address);
                        buffer.clear();
                        AreaTexto.setText("");
                        continue;
                    }
                    else{
                        System.out.println("ERROR al realizar conexión");
                        System.exit(1);
                    }
                }
            }catch(IOException e){
                e.printStackTrace();
                System.exit(1);
            }
        }//if
    }//GEN-LAST:event_botonEnviarActionPerformed

    private void msgGrupalActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_msgGrupalActionPerformed
        tipo= null;
        jLabel1.setFont(new Font("Arial", Font.ITALIC, 24));
        jLabel1.setText("Chat Grupal");
    }//GEN-LAST:event_msgGrupalActionPerformed

public void run(){  
    while(true)
        RecibirMensaje();
}

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private java.awt.TextArea AreaTexto;
    private javax.swing.JTextPane Chat;
    private java.awt.ScrollPane UserScrollPane;
    private javax.swing.JPanel Usuarios;
    private javax.swing.JButton botonEnviar;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPopupMenu jPopupMenu1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JMenuItem msgGrupal;
    // End of variables declaration//GEN-END:variables
}
