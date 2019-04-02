package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.text.ParseException;
import java.text.SimpleDateFormat;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;

public class selectChargeTime extends JFrame implements WindowListener,ActionListener {

	private MainUI fatherWin;
	
	private JPanel contentPane;
	private JTextField textFieldStart;
	private JTextField textFieldEnd;
	private JButton btnOk;
	private JButton btnCancel;
	private SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm");
    private CentralController controller;
    private JLabel label_2;
    private JTextField textFieldRoom;
	
	public selectChargeTime(MainUI fatherWin,CentralController controller) 
	{
		this.fatherWin=fatherWin;
		
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 270, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		this.controller = controller;
		this.setVisible(true);
		
		JLabel lblyyyymmddHhmm = new JLabel(" \u8BF7\u8F93\u5165\u5165\u4F4F\u65F6\u95F4\uFF1A");
		lblyyyymmddHhmm.setBounds(10, 27, 109, 15);
		contentPane.add(lblyyyymmddHhmm);
		
		JLabel lblNewLabel = new JLabel("(\u683C\u5F0F\uFF1Ayyyy-MM-dd HH:mm)");
		lblNewLabel.setBounds(20, 60, 163, 15);
		contentPane.add(lblNewLabel);
		
		textFieldStart = new JTextField();
		textFieldStart.setBounds(113, 24, 131, 21);
		contentPane.add(textFieldStart);
		textFieldStart.setColumns(10);
		
		JLabel label = new JLabel("\u8BF7\u8F93\u5165\u79BB\u5E97\u65F6\u95F4\uFF1A");
		label.setBounds(20, 99, 96, 15);
		contentPane.add(label);
		
		textFieldEnd = new JTextField();
		textFieldEnd.setBounds(113, 96, 131, 21);
		contentPane.add(textFieldEnd);
		textFieldEnd.setColumns(10);
		
		JLabel label_1 = new JLabel("(\u683C\u5F0F\uFF1Ayyyy-MM-dd HH:mm)");
		label_1.setBounds(20, 136, 163, 15);
		contentPane.add(label_1);
		
		btnOk = new JButton("\u786E\u5B9A");
		btnOk.setBounds(10, 209, 93, 23);
		contentPane.add(btnOk);
		
		btnCancel = new JButton("\u53D6\u6D88");
		btnCancel.setBounds(151, 209, 93, 23);
		contentPane.add(btnCancel);
		
		label_2 = new JLabel("\u8BF7\u8F93\u5165\u623F\u95F4\u53F7:");
		label_2.setBounds(20, 172, 85, 15);
		contentPane.add(label_2);
		
		textFieldRoom = new JTextField();
		textFieldRoom.setBounds(117, 169, 127, 21);
		contentPane.add(textFieldRoom);
		textFieldRoom.setColumns(10);
		this.setResizable(false);
		this.btnOk.addActionListener(this);
		this.btnCancel.addActionListener(this);
		this.addWindowListener(this);
		
		this.fatherWin.setEnabled(false);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == this.btnOk){
			String start = this.textFieldStart.getText();
			String end = this.textFieldEnd.getText();
			String roomNum = this.textFieldRoom.getText();
			try{
				format.setLenient(false);
				format.parse(start);
				format.parse(end);
				GetCharge temp = new GetCharge(this,controller,start,end,roomNum);
				temp.repaint();
				temp.getData();
			}
			catch(ParseException e1){
				JOptionPane.showMessageDialog(null, "输入的日期格式不正确！","警告",JOptionPane.WARNING_MESSAGE);
			}
		}
		else if(e.getSource() == this.btnCancel){
			this.fatherWin.setEnabled(true);
			this.fatherWin.requestFocus();
			this.dispose();
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
