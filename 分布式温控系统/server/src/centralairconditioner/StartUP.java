package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import sun.misc.BASE64Encoder;
import javax.swing.JToolBar;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPasswordField;

public class StartUP extends JFrame implements ActionListener
{

	private JPanel contentPane;
	private JTextField userName;
	private JPasswordField password;

	private JRadioButton loginCheck;
	private JRadioButton registerCheck;
	private JButton ok;
	private JButton cancel;
	/**
	 * Create the frame.
	 */
	public StartUP() {
		setTitle("\u9274\u6743\u8BA4\u8BC1");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 370, 275);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(21, 10, 304, 67);
		panel.setBorder(BorderFactory.createTitledBorder( "操作类型"));
		contentPane.add(panel);
		panel.setLayout(null);
		
		loginCheck = new JRadioButton("\u767B\u5F55");
		loginCheck.setBounds(35, 26, 121, 23);
		panel.add(loginCheck);
		
		registerCheck = new JRadioButton("\u6CE8\u518C");
		registerCheck.setBounds(199, 26, 121, 23);
		panel.add(registerCheck);
		
		userName = new JTextField();
		userName.setBounds(149, 87, 176, 21);
		contentPane.add(userName);
		userName.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("\u7528\u6237\u540D\uFF1A");
		lblNewLabel.setBounds(44, 90, 54, 15);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u5BC6\u7801\uFF1A");
		lblNewLabel_1.setBounds(44, 135, 54, 15);
		contentPane.add(lblNewLabel_1);
		
		ok = new JButton("\u786E\u8BA4");
		ok.setBounds(44, 193, 93, 23);
		contentPane.add(ok);
		
		cancel = new JButton("\u53D6\u6D88");
		cancel.setBounds(217, 193, 93, 23);
		contentPane.add(cancel);
		
		password = new JPasswordField();
		password.setBounds(149, 132, 176, 21);
		contentPane.add(password);
		
		this.setResizable(false);
		this.loginCheck.setSelected(true);
		//设置监听
		this.loginCheck.addActionListener(this);
		this.registerCheck.addActionListener(this);
		this.ok.addActionListener(this);
		this.cancel.addActionListener(this);
	}
	
	public String EncoderByMd5(String str) throws NoSuchAlgorithmException, UnsupportedEncodingException
	{
		 //确定计算方法
		MessageDigest md5=MessageDigest.getInstance("MD5");
		BASE64Encoder base64en = new BASE64Encoder();
		//加密后的字符串
		String newstr=base64en.encode(md5.digest(str.getBytes("utf-8")));
		return newstr;
	}
	
	public boolean checkPassword(String newpasswd,String oldpasswd) throws NoSuchAlgorithmException, UnsupportedEncodingException
	{
		 if(EncoderByMd5(newpasswd).equals(oldpasswd))
		 {
			 return true;
		 }
		 else
		 {
			 return false;
		 }
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==this.loginCheck)
		{
			this.registerCheck.setSelected(false);
		}
		else if(e.getSource()==this.registerCheck)
		{
			this.loginCheck.setSelected(false);
		}
		else if(e.getSource()==this.ok)
		{
			if(this.registerCheck.isSelected())
			{
				String passwordMd5=null;
				String userName=this.userName.getText();
				String password=this.password.getText();
				try 
				{
					passwordMd5=EncoderByMd5(password);
				} catch (NoSuchAlgorithmException | UnsupportedEncodingException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				String sqlStr="select Password from UserInfo where UserName='"+userName+"'";
				ResultSet result=DBAccess.getInstance().selectInf(sqlStr);
				try {
					int count=0;
					while(result.next())
					{
						count++;
					}
					if(count==0)
					{
						sqlStr="insert into UserInfo values ('"+userName+"','"+passwordMd5+"')";
						DBAccess.getInstance().exeSql(sqlStr);
						JOptionPane.showMessageDialog(null, "注册成功,可以进行登录","信息",JOptionPane.INFORMATION_MESSAGE);
						this.userName.setText("");
						this.password.setText("");
						this.loginCheck.setSelected(true);
						this.registerCheck.setSelected(false);
					}
					else
					{
						JOptionPane.showMessageDialog(null, "注册失败，该用户名已经存在，请重新设置","警告",JOptionPane.WARNING_MESSAGE);
						this.userName.setText("");
						this.registerCheck.setSelected(true);
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
			else
			{
				String passwordMd5=null;
				String oldPassword=null;
				String userName=this.userName.getText();
				String inputPassword=this.password.getText();
				String sqlStr="select Password from UserInfo where UserName='"+userName+"'";
				ResultSet result=DBAccess.getInstance().selectInf(sqlStr);
				try {
					while(result.next())
					{
						oldPassword=result.getString("Password");
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				try {
					if(checkPassword(inputPassword,oldPassword))
					{
						this.userName.setText("");
						this.password.setText("");
						this.loginCheck.setSelected(true);
						this.setVisible(false);
						new ConfigureUI(this);
						//JOptionPane.showMessageDialog(null, "登录成功","信息",JOptionPane.INFORMATION_MESSAGE);
					}
					else
					{
						this.userName.setText("");
						this.password.setText("");
						this.loginCheck.setSelected(true);
						JOptionPane.showMessageDialog(null, "用户名或者密码错误，登录失败","警告",JOptionPane.WARNING_MESSAGE);
					}
				} catch (NoSuchAlgorithmException | UnsupportedEncodingException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
		}
		else if(e.getSource()==this.cancel)
		{
			System.exit(0);
		}
	}
}
