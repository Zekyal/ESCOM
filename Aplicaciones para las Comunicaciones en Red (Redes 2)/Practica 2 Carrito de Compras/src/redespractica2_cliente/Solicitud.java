package redespractica2_cliente;

import Articulo.Articulo;
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.ObjectInputStream;
import java.net.Socket;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Solicitud extends JDialog{
    JPanel panel= new JPanel();
    int pto;
    String host;
    
    public Solicitud(Frame parent, boolean modal, int pto, String host){
        super(parent, "Solicitud de Direccion", modal); 
        setSize(200, 180);//Establecemos el tamaño de la ventana (ancho, largo)
        setLocationRelativeTo(null);//Establecemos la ventana en el centro
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);  
        this.pto= pto;
        this.host= host;
        
        iniciarComponentes();
        getContentPane().setLayout(new BorderLayout(0, 0));
        getContentPane().add(panel, BorderLayout.CENTER);
        panel.setLayout(new BorderLayout(0, 0));
    }
    
    public void iniciarComponentes(){
        JLabel puerto= new JLabel("Puerto:");
        puerto.setBounds(10, 10, 180, 15);
        puerto.setFont(new Font("Arial", 1, 15));
        puerto.setOpaque(false);
        
        JTextField areaPuerto= new JTextField();
        areaPuerto.setBounds(10, 30, 160, 20);

        JLabel hst= new JLabel("Host:");
        hst.setBounds(10, 55, 180, 15);
        hst.setFont(new Font("Arial", 1, 15));
        hst.setOpaque(false);
        
        JTextField areaHost= new JTextField();
        areaHost.setBounds(10, 75, 160, 20);
        
        JButton solicitar= new JButton("Solicitar");
        solicitar.setBounds(40, 105, 100, 30);
        
        ActionListener BotonSolicitar= new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {
                try{
                    pto= Integer.parseInt(areaPuerto.getText());
                    host= areaHost.getText().toString();
                    dispose();
                }catch (Exception e){
                    e.printStackTrace();
                    dispose();
                }
            }
        };
        
        solicitar.addActionListener(BotonSolicitar);
        
        panel.add(puerto);
        panel.add(areaPuerto);
        panel.add(hst);
        panel.add(areaHost);
        panel.add(solicitar);
    }
}
