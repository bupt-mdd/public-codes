package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.JButton;
import javax.swing.DefaultComboBoxModel;

public class selectYear extends JFrame implements ActionListener,WindowListener {

	private MainUI fatherWin;
	
	private JPanel contentPane;
	private CentralController controller;
    private JComboBox comboBox;
    private JButton btnOk ;
	private Object String;
	
	public selectYear(MainUI fatherWin,CentralController controller) {
		
		this.fatherWin=fatherWin;
		
		setTitle("select");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 247, 110);
		this.setVisible(true);
		this.controller = controller;
		
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel label = new JLabel("\u8BF7\u9009\u62E9\u4E00\u4E2A\u5E74\u4EFD\uFF1A ");
		label.setBounds(10, 10, 110, 15);
		contentPane.add(label);
		
		comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"2013", "2014", "2015", "2016", "2017", "2018", "2019"}));
		comboBox.setSelectedIndex(3);
		comboBox.setBounds(130, 7, 75, 21);
		contentPane.add(comboBox);
		
		btnOk = new JButton("ok");
		btnOk.setBounds(68, 38, 93, 23);
		contentPane.add(btnOk);
		this.setResizable(false);
		
		this.btnOk.addActionListener(this);
		this.addWindowListener(this);
		this.fatherWin.setEnabled(false);
		
	}
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == this.btnOk){
		  String year = (String)this.comboBox.getSelectedItem();
		  new Chart(this,this.controller,year,year);
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
