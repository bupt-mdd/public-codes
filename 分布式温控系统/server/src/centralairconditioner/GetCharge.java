package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class GetCharge extends JFrame implements WindowListener{

	private JFrame fatherWin;
	
	private JPanel contentPane;
	private JTextField textFieldStart;
	private JTextField textFieldEnd;
	private JLabel lblNewLabel_1;
	private JTextField txtXxx;
	private JLabel lblNewLabel_2;
	private JTextField textFieldExpense;
	private JLabel lblNewLabel_3;
	private CentralController controller;
	private JTextField textFieldRoom;
	private String start;
	private String end;
	private String roomNum;

	public GetCharge(JFrame fatherWin,CentralController controller,String start,String end,String roomNum) 
	{
		this.fatherWin=fatherWin;
		this.start = start;
		this.end = end;
		this.roomNum = roomNum;
		
		setTitle("\u8D26\u5355");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		this.controller = controller;
		this.setVisible(true);
		
		setBounds(100, 100, 296, 310);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel label = new JLabel("\u5165\u5E97\u65F6\u95F4 \uFF1A");
		label.setBounds(29, 100, 66, 15);
		contentPane.add(label);
		
		JLabel lblNewLabel = new JLabel("\u79BB\u5E97\u65F6\u95F4\uFF1A");
		lblNewLabel.setBounds(29, 135, 66, 15);
		contentPane.add(lblNewLabel);
		
		textFieldStart = new JTextField();
		textFieldStart.setEditable(false);
		textFieldStart.setBounds(119, 97, 124, 21);
		contentPane.add(textFieldStart);
		textFieldStart.setColumns(10);
		this.textFieldStart.setText(start);
		
		textFieldEnd = new JTextField();
		textFieldEnd.setEditable(false);
		textFieldEnd.setBounds(119, 129, 124, 21);
		contentPane.add(textFieldEnd);
		textFieldEnd.setColumns(10);
		this.textFieldEnd.setText(end);
		
		lblNewLabel_1 = new JLabel("\u987E\u5BA2\u59D3\u540D\uFF1A");
		lblNewLabel_1.setBounds(29, 30, 66, 15);
		contentPane.add(lblNewLabel_1);
		
		txtXxx = new JTextField();
		txtXxx.setEditable(false);
		txtXxx.setText("       XXX");
		txtXxx.setBounds(119, 27, 124, 21);
		contentPane.add(txtXxx);
		txtXxx.setColumns(10);
		
		lblNewLabel_2 = new JLabel("\u7A7A\u8C03\u6D88\u8017\u8D39\u7528\uFF1A");
		lblNewLabel_2.setBounds(29, 176, 98, 21);
		contentPane.add(lblNewLabel_2);
		
		textFieldExpense = new JTextField();
		textFieldExpense.setEditable(false);
		textFieldExpense.setBounds(119, 176, 124, 21);
		contentPane.add(textFieldExpense);
		textFieldExpense.setColumns(10);
		lblNewLabel_3 = new JLabel("\u6B22\u8FCE\u60A8\u518D\u6B21\u5149\u4E34\u672C\u5E97\uFF01");
		lblNewLabel_3.setFont(new Font("华文行楷", Font.BOLD, 17));
		lblNewLabel_3.setBounds(42, 220, 194, 30);
		contentPane.add(lblNewLabel_3);
		
		JLabel label_1 = new JLabel("\u623F\u95F4\u53F7\uFF1A");
		label_1.setBounds(29, 65, 54, 15);
		contentPane.add(label_1);
		
		textFieldRoom = new JTextField();
		textFieldRoom.setEditable(false);
		textFieldRoom.setBounds(119, 62, 124, 21);
		contentPane.add(textFieldRoom);
		textFieldRoom.setColumns(10);
		this.textFieldRoom.setText(roomNum);

		this.addWindowListener(this);
		this.fatherWin.setVisible(false);
	}
	
	public void getData() {
		Double expense = controller.countExpense(this.start,this.end,this.roomNum);
		if(expense == null)
			JOptionPane.showMessageDialog(this, "数据获取失败","警告",JOptionPane.WARNING_MESSAGE);
		else
			this.textFieldExpense.setText(expense+"");
	}

	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosing(WindowEvent e) {
		// TODO Auto-generated method stub
		this.fatherWin.setVisible(true);
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
