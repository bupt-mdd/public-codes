package centralairconditioner;


import javax.swing.*;
import hysun.util.DateChooser;
import java.awt.*;
import java.awt.event.*;
import java.text.SimpleDateFormat;
 
public class selectDate extends JFrame implements ActionListener,WindowListener {
 
	private MainUI fatherWin;
	
	private JButton selectbutton;
	private JButton btnOk;
	private final DateChooser dc;
	private final JTextField textfield;
	private JPanel panel ;
	private CentralController controller;
	private java.util.Calendar cal;
    private static final SimpleDateFormat FORMATTER = 
                                              new SimpleDateFormat("yyyy.MM.dd");
 
    public selectDate(MainUI fatherWin,CentralController controller) {
    	
    	this.fatherWin=fatherWin;
    	
        dc = new DateChooser(this, true);
        this.controller = controller;
        
        textfield = new JTextField();
        getContentPane().add(textfield, BorderLayout.NORTH);
 
        panel = new JPanel();
        selectbutton = new JButton("Select Date");
        panel.add(selectbutton);
        getContentPane().add(panel);
        
        btnOk = new JButton("ok");
        panel.add(btnOk);
 
        this.selectbutton.addActionListener(this);
        this.btnOk.addActionListener(this);
        this.addWindowListener(this);
        
        pack();
        setLocationRelativeTo(null);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setVisible(true);
        this.setResizable(false);
        this.fatherWin.setEnabled(false);
    }
    
    public void actionPerformed(ActionEvent e) {
    	if(e.getSource() == selectbutton){
	        dc.setLocationRelativeTo(textfield);
//	    	System.out.println("....");
	        dc.setVisible(true);
	        cal = dc.getSelectedDate();
	        if (cal != null) {
	            textfield.setText(FORMATTER.format(cal.getTime()));
	        }
    	}
        else if(e.getSource() == btnOk){
        	String s = this.textfield.getText();
        	//System.out.println("aaa");
        	dc.dispose();
        	
        	new Chart(this,this.controller,s).setVisible(true);
        }

    }

	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosing(WindowEvent e) {
		// TODO Auto-generated method stub
		this.fatherWin.setEnabled(true);
		this.fatherWin.requestFocus();
	}

	@Override
	public void windowClosed(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowIconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowDeiconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowActivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowDeactivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

}