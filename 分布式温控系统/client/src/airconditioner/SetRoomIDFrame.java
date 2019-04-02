package airconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JDialog;
import java.awt.Font;
import java.awt.Color;
import java.awt.SystemColor;

public class SetRoomIDFrame extends JFrame implements ActionListener
{
	private JPanel contentPane;
	private JPasswordField password;
	private JTextField adminName;
	private JTextField roomIDText;
	
	private JButton btnOk;

	private String roomID;
	Socket linkPort=null;
	BufferedReader reader=null;
	PrintWriter writer=null;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		new SetRoomIDFrame();
	}

	/**
	 * Create the frame.
	 */
	public SetRoomIDFrame() 
	{
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 320, 300);
		
		contentPane = new JPanel();
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(34, 60, 241, 103);
		panel.setBorder(BorderFactory.createTitledBorder( "鉴权认证区"));
		contentPane.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("\u7528\u6237\u540D\uFF1A");
		lblNewLabel.setBounds(21, 25, 54, 15);
		panel.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u5BC6\u7801\uFF1A");
		lblNewLabel_1.setBounds(21, 60, 54, 15);
		panel.add(lblNewLabel_1);
		
		password = new JPasswordField();
		password.setBounds(85, 57, 135, 21);
		panel.add(password);
		
		adminName = new JTextField();
		adminName.setBounds(85, 22, 135, 21);
		panel.add(adminName);
		adminName.setColumns(10);
		
		JLabel lblNewLabel_2 = new JLabel("\u623F\u95F4\u53F7\uFF1A");
		lblNewLabel_2.setBounds(54, 179, 54, 15);
		contentPane.add(lblNewLabel_2);
		
		roomIDText = new JTextField();
		roomIDText.setBounds(118, 176, 134, 21);
		contentPane.add(roomIDText);
		roomIDText.setColumns(10);
		
		btnOk = new JButton("ok");
		btnOk.setBounds(182, 217, 93, 23);
		contentPane.add(btnOk);
		
		JLabel label = new JLabel("\u623F\u95F4\u7A7A\u8C03\u914D\u7F6E\u5B89\u88C5\u754C\u9762");
		label.setForeground(SystemColor.textHighlight);
		label.setFont(new Font("宋体", Font.BOLD, 16));
		label.setBounds(63, 10, 174, 28);
		contentPane.add(label);
		
		setVisible(true);
		
		this.btnOk.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==this.btnOk)
		{
			String name=this.adminName.getText();
			String pass=this.password.getText();
			roomID=this.roomIDText.getText();
			if(name.equals(""))
			{
				JOptionPane.showMessageDialog(this, "用户名不能为空","警告",JOptionPane.WARNING_MESSAGE);
				this.adminName.requestFocus();
			}
			else if(pass.equals(""))
			{
				JOptionPane.showMessageDialog(this, "用户密码不能为空","警告",JOptionPane.WARNING_MESSAGE);
				this.password.requestFocus();
			}
			else if(roomID.equals(""))
			{
				JOptionPane.showMessageDialog(this, "房间号不能为空","警告",JOptionPane.WARNING_MESSAGE);
				this.roomIDText.requestFocus();
			}
			else if(name.equals("root")&&pass.equals("root"))
			{	
				try 
				{
					linkPort=new Socket("127.0.0.1",6000);
					InputStreamReader streamReader=new InputStreamReader(linkPort.getInputStream());
					reader=new BufferedReader(streamReader);
					writer=new PrintWriter(linkPort.getOutputStream());
					
					writer.println(this.roomID+" 1");    //把房间号和链路标识发给服务器
					writer.flush();
					String[] inf=reader.readLine().split(" ");
					if(inf[0].equals("NO"))
					{
						this.reader.close();
						this.writer.close();
						this.linkPort.close();
						JOptionPane.showMessageDialog(this, "此房间号已经被设置，请选择其他房间号","警告",JOptionPane.WARNING_MESSAGE);
						this.roomIDText.setText("");
						this.roomIDText.requestFocus();
					}
					else
					{
						int worktype=Integer.parseInt(inf[1]);
						int desttemp=Integer.parseInt(inf[2]);
						//System.out.println(worktype);
						new RoomOpePanel(worktype,desttemp,roomID,this,reader,writer,linkPort);
						this.setVisible(false);
					}
				} 
				catch (Exception e1) 
				{
					JOptionPane.showMessageDialog(this, "无法连接中央空调，请联系管理员","警告",JOptionPane.WARNING_MESSAGE);
					//error
				}
			}
			else
			{
				JOptionPane.showMessageDialog(this, "用户名或密码错误，无权设置房间号","警告",JOptionPane.WARNING_MESSAGE);
				this.adminName.setText("");
				this.password.setText("");
				this.adminName.requestFocus();
			}
		}
	}
}
