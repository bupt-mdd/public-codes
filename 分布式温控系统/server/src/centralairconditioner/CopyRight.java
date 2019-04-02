package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class CopyRight extends JDialog implements ActionListener,WindowListener
{
	private MainUI fatherWin;
	private JPanel contentPane;
	private JButton btnNewButton;
	
	public CopyRight(MainUI fatherWin) {
		this.fatherWin=fatherWin;
		
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 285, 255);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		btnNewButton = new JButton("ok");
		btnNewButton.setBounds(165, 182, 93, 23);
		contentPane.add(btnNewButton);
		
		JPanel panel = new JPanel();
		panel.setBounds(10, 10, 248, 162);
		panel.setBorder(BorderFactory.createTitledBorder( "版权声明区"));
		contentPane.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("lalalalalalalalalala!");
		lblNewLabel.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel.setForeground(Color.MAGENTA);
		lblNewLabel.setBounds(28, 27, 212, 46);
		panel.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u8054\u7CFB\u65B9\u5F0F XXXXXXX");
		lblNewLabel_1.setForeground(Color.BLUE);
		lblNewLabel_1.setFont(new Font("宋体", Font.PLAIN, 14));
		lblNewLabel_1.setBounds(65, 69, 177, 35);
		panel.add(lblNewLabel_1);
		
		JLabel lblNewLabel_2 = new JLabel("\u90AE\u7BB1\uFF1A mdd950129@163.com");
		lblNewLabel_2.setFont(new Font("宋体", Font.PLAIN, 14));
		lblNewLabel_2.setForeground(Color.BLUE);
		lblNewLabel_2.setBounds(28, 104, 203, 35);
		panel.add(lblNewLabel_2);
		
		this.setVisible(true);
		
		this.btnNewButton.addActionListener(this);
		this.addWindowListener(this);
		this.fatherWin.setEnabled(false);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==this.btnNewButton)
		{
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
