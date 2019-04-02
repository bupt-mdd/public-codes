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
import javax.swing.JComboBox;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.DefaultComboBoxModel;

public class selectMonth extends JFrame implements ActionListener,WindowListener {

	private MainUI fatherWin;
	
	private JPanel contentPane;
	private JComboBox comboBox_month;
	private JButton btnOk;
	private JComboBox comboBox_year;
	private JLabel label;
	private CentralController controller;

	public selectMonth(MainUI fatherWin,CentralController controller) {
		
		this.fatherWin=fatherWin;
		
		setTitle("select Month");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 260, 137);
		this.controller = controller;
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		
		comboBox_month = new JComboBox();
		comboBox_month.setModel(new DefaultComboBoxModel(new String[] {"January ", "February ", "March ", "April ", "May ", "June ", "July ", "August ", "September ", "October ", "November ", "December"}));
		comboBox_month.setSelectedIndex(0);
		comboBox_month.setBounds(126, 35, 108, 21);
		contentPane.add(comboBox_month);
		
		JLabel lblNewLabel = new JLabel("\u8BF7\u9009\u62E9\u4E00\u4E2A\u6708\u4EFD\uFF1A");
		lblNewLabel.setBounds(20, 10, 96, 15);
		contentPane.add(lblNewLabel);
		
		btnOk = new JButton("ok");
		btnOk.setBounds(70, 66, 108, 23);
		contentPane.add(btnOk);
		
		comboBox_year = new JComboBox();
		comboBox_year.setModel(new DefaultComboBoxModel(new String[] {"2013", "2014", "2015", "2016", "2017", "2018", "2019"}));
		comboBox_year.setSelectedIndex(3);
		comboBox_year.setBounds(20, 35, 53, 21);
		contentPane.add(comboBox_year);
		
		label = new JLabel("\u5E74");
		label.setBounds(83, 38, 26, 15);
		contentPane.add(label);
		this.setVisible(true);
		this.setResizable(false);
		
		this.btnOk.addActionListener(this);
		this.addWindowListener(this);
		
		this.fatherWin.setEnabled(false);
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == this.btnOk){
		    String year = (String)this.comboBox_year.getSelectedItem();
			int month = this.comboBox_month.getSelectedIndex()+1;
			new Chart(this,this.controller,year,month);
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
