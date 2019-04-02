package airconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JSpinner;
import javax.swing.JTree;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.SpinnerListModel;
import javax.swing.SpinnerNumberModel;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.BorderFactory;
import javax.swing.DefaultComboBoxModel;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.IOException;
import java.net.Socket;
import java.io.*;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.awt.event.ActionEvent;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;
import com.jgoodies.forms.layout.FormSpecs;


public class RoomOpePanel extends JFrame implements ActionListener
{
	private JFrame mainWindow;
	private int workType;                          //存储中央空调工作模式
	private String roomID;
	private JButton btnOnOff;
	private JPanel contentPane;
	private JSpinner temSpinner;
	private JComboBox windComboBox;
	private JButton adjustTemp;
	private JButton adjustWind;
	private JLabel roomIDLabel;
	private JLabel curTemLabel;
	private JLabel curWindLabel;
	private JLabel curMoneyLabel;
	
	private Socket linkPort1;
	private BufferedReader reader1;
	private PrintWriter writer1;
	private Socket linkPort2;
	private BufferedReader reader2;
	private PrintWriter writer2;
	
	private int onAndDown=0;
	private int destTemp=0;
	private int destWind=0;
	private int curTemp=25;
	private int curWind=0;
	private double consumeMoney=0;
	
	private boolean isGetCharge=false;			//用于标识，是否获取计费。
	private boolean autoChangeTemp=true;
	
	public RoomOpePanel(int workType,int destTemp,String roomID,JFrame mainWindow,BufferedReader reader,PrintWriter writer,Socket linkPort) 
	{
		this.workType=workType;
		this.destTemp=destTemp;
		this.roomID=roomID;
		this.mainWindow=mainWindow;
		this.linkPort1=linkPort;
		this.reader1=reader;
		this.writer1=writer;
		
		setTitle("\u623F\u95F4\u7A7A\u8C03");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		setResizable(false);
		contentPane = new JPanel();
		contentPane.setToolTipText("");
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		adjustTemp = new JButton("\u8C03\u6E29");
		adjustTemp.setEnabled(false);
		adjustTemp.setBounds(218, 238, 93, 23);
		contentPane.add(adjustTemp);
		
		adjustWind = new JButton("\u8C03\u98CE");
		adjustWind.setEnabled(false);
		adjustWind.setBounds(321, 238, 93, 23);
		contentPane.add(adjustWind);
		
		JPanel panel = new JPanel();
		panel.setBounds(10, 10, 414, 70);
		panel.setBorder(BorderFactory.createTitledBorder( "配置启动"));
		contentPane.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel_5 = new JLabel("\u623F\u95F4\u53F7\uFF1A");
		lblNewLabel_5.setBounds(20, 26, 57, 15);
		panel.add(lblNewLabel_5);
		
		JLabel lblNewLabel_4 = new JLabel(" \u5F00\u5173");
		lblNewLabel_4.setBounds(262, 26, 30, 15);
		panel.add(lblNewLabel_4);
		
		btnOnOff = new JButton("ON");
		btnOnOff.setBounds(313, 22, 57, 23);
		panel.add(btnOnOff);
		
		roomIDLabel = new JLabel("");
		roomIDLabel.setBounds(87, 26, 54, 15);
		panel.add(roomIDLabel);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBounds(10, 90, 411, 123);
		panel_1.setBorder(BorderFactory.createTitledBorder( "状态显示、调节区"));
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("\u5F53\u524D\u98CE\u901F      :");
		lblNewLabel_1.setBounds(10, 57, 92, 15);
		panel_1.add(lblNewLabel_1);
		
		JLabel lblNewLabel = new JLabel("\u5F53\u524D\u6E29\u5EA6      :");
		lblNewLabel.setBounds(10, 22, 92, 15);
		panel_1.add(lblNewLabel);
		
		JLabel label_1 = new JLabel("\u2103");
		label_1.setBounds(176, 22, 23, 15);
		panel_1.add(label_1);
		
		JLabel lblNewLabel_2 = new JLabel("\u76EE\u6807\u6E29\u5EA6");
		lblNewLabel_2.setBounds(231, 22, 54, 15);
		panel_1.add(lblNewLabel_2);
		
		temSpinner = new JSpinner();
		temSpinner.setBounds(295, 19, 76, 22);
		panel_1.add(temSpinner);
		temSpinner.setEnabled(false);
		temSpinner.setModel(new SpinnerNumberModel(new Integer(25), null, null, new Integer(1)));
		
		JLabel lblNewLabel_3 = new JLabel("\u76EE\u6807\u98CE\u901F");
		lblNewLabel_3.setBounds(231, 57, 54, 15);
		panel_1.add(lblNewLabel_3);
		
		windComboBox = new JComboBox();
		windComboBox.setBounds(295, 54, 76, 21);
		panel_1.add(windComboBox);
		windComboBox.setEnabled(false);
		windComboBox.setModel(new DefaultComboBoxModel(new String[] {"\u4F4E", "\u4E2D", "\u9AD8"}));
		
		JLabel label_4 = new JLabel("\u2103");
		label_4.setBounds(381, 22, 31, 15);
		panel_1.add(label_4);
		
		JLabel label = new JLabel("\u672C\u6B21\u6D88\u8D39\u91D1\u989D  :");
		label.setBounds(10, 92, 92, 15);
		panel_1.add(label);
		
		JLabel label_3 = new JLabel("\u5143");
		label_3.setBounds(176, 92, 44, 15);
		panel_1.add(label_3);
		
		curTemLabel = new JLabel("");
		curTemLabel.setBounds(112, 22, 54, 15);
		panel_1.add(curTemLabel);
		
		curWindLabel = new JLabel("");
		curWindLabel.setBounds(112, 57, 54, 15);
		panel_1.add(curWindLabel);
		
		curMoneyLabel = new JLabel("");
		curMoneyLabel.setBounds(112, 92, 54, 15);
		panel_1.add(curMoneyLabel);
		
		this.roomIDLabel.setText(roomID);
		this.setVisible(true);
		//设置监听
		
		Thread thread1=new Thread(new TellState());                   //向中央空调汇报状态
		thread1.start();
		Thread thread2=new Thread(new feelCurTemp());				  //按照固定的算法，降低房间温度等。
		thread2.start();
		Thread thread3=new Thread(new getCharge());				  //按照固定的算法，降低房间温度等。
		thread3.start();
		
		this.btnOnOff.addActionListener(this);
		this.adjustTemp.addActionListener(this);
		this.adjustWind.addActionListener(this);
		
	}
	
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		try
		{
			if(e.getSource()==this.btnOnOff)
			{
				if(this.btnOnOff.getText().equals("ON"))
				{
					openConnect();
					getInitialState();
					this.isGetCharge=true;     //表示开机后，开始获取计费
					
					onAndDown=1;
					this.adjustTemp.setEnabled(true);
					this.adjustWind.setEnabled(true);
					this.windComboBox.setEnabled(true);
					this.temSpinner.setEnabled(true);
					this.btnOnOff.setText("OFF");
					
					this.adjustTemp.doClick(); 		//马上做一次调风调温操作
					this.adjustWind.doClick();
					
				}
				else
				{
					this.isGetCharge=false;			//表示关机后，停止获取计费。
					closeConnect();
					onAndDown=0;
					this.adjustTemp.setEnabled(false);
					this.adjustWind.setEnabled(false);
					this.windComboBox.setEnabled(false);
					this.temSpinner.setEnabled(false);
					this.btnOnOff.setText("ON");
					
				}
			}
			else if(e.getSource()==this.adjustWind)
			{
				String request="AW "+this.windComboBox.getSelectedIndex()+" "+this.roomID;
				String ack=sendAndRecv(request);
				String[] wind2={"低速","中速","高速"};
				if(ack.equals("OK"))
				{
					this.curWindLabel.setText(wind2[this.windComboBox.getSelectedIndex()]);
					this.destWind=this.windComboBox.getSelectedIndex();    //将当前目标风速保存起来
					this.curWind=this.destWind;
				}
			}
			else if(e.getSource()==this.adjustTemp)
			{
				//此处可以把当前温度和风速也发过去，便于进行计费的计算
				String request="AT "+this.temSpinner.getValue()+" "+this.curTemp+" "+this.curWind+" "+this.roomID;	
				String ack=sendAndRecv(request);
				if(ack.equals("OK"))
				{
					this.destTemp=(Integer)this.temSpinner.getValue();      //将当前的目标温度保存起来
				}
			}
		}
		catch(Exception e1)
		{
			JOptionPane.showMessageDialog(this, "与中央空调连接中断，请联系管理员","警告",JOptionPane.WARNING_MESSAGE);
		}
	}
	
	private synchronized String sendAndRecv(String request)throws Exception
	{
		String ack=null;
		this.writer2.println(request);
		this.writer2.flush();
		
		ack=this.reader2.readLine();
		return ack;
	}
	
	private void getInitialState()throws Exception
	{
		String conf=this.sendAndRecv("GIS "+this.roomID);    //get initial state(工作方式+ 目标温度+ 目标风速+ 计费)
		String[] confInf=conf.split(" ");
		this.workType=Integer.parseInt(confInf[0]);
		this.destTemp=Integer.parseInt(confInf[1]);
		this.destWind=Integer.parseInt(confInf[2]);
		this.consumeMoney=Double.parseDouble(confInf[3]);
		this.curWind=this.destWind;	
		
		this.temSpinner.getModel().setValue(this.destTemp);
		this.windComboBox.setSelectedIndex(this.destWind);
		String[] wind2={"低速","中速","高速"};
		this.curWindLabel.setText(wind2[this.curWind]);
		this.curTemLabel.setText(((Integer)this.curTemp).toString());
		this.curMoneyLabel.setText(((Double)this.consumeMoney).toString());
	}
	
	private void openConnect()throws Exception
	{
		this.linkPort2=new Socket("127.0.0.1",6000);
		InputStreamReader streamReader2=new InputStreamReader(this.linkPort2.getInputStream());
		this.reader2=new BufferedReader(streamReader2);
		
		this.writer2=new PrintWriter(this.linkPort2.getOutputStream());
		this.writer2.println(this.roomID+" 2");
		this.writer2.flush();
		this.reader2.readLine();
	}
	
	private void closeConnect()throws Exception
	{
		sendAndRecv("SD "+roomID);          //shutdown
	}
	
	public class TellState implements Runnable
	{
		@Override
		public void run() {
			// TODO Auto-generated method stub
			String message;
			try {
				while(true)
				{
					message=reader1.readLine();
					String[] inf=message.split(" "); 
					if(inf[0].equals("GS"))           //get state
					{
						//将相应的信息按照约定的格式组织好后，发送给客户端。
						if(onAndDown==1)
						{
							//格式为：开关机状态+ 目标温度+ 目标风速 +当前温度 +当前风速+当前计费+房间号
							message=onAndDown+" "+destTemp+" "+curTemp+" "+destWind+" "+curWind+" "+consumeMoney+" "+roomID;   
							writer1.println(message);
							writer1.flush();
						}
						else
						{
							message="0";
							writer1.println(message);
							writer1.flush();
						}
					}
					else if(inf[0].equals("SD"))      //shut down
					{
						writer1.println(roomID);
						writer1.flush();
						reader2.close();
						writer2.close();
						linkPort2.close();
						adjustTemp.setEnabled(false);
						adjustWind.setEnabled(false);
						windComboBox.setEnabled(false);
						temSpinner.setEnabled(false);
						btnOnOff.setText("ON");
					}
					else if(inf[0].equals("CT")){
						if(curTemp < destTemp)
						    curTemp++;
						else if(curTemp > destTemp)
							curTemp--;
						curTemLabel.setText(String.valueOf(curTemp));
						if(curTemp == destTemp)
						{
							autoChangeTemp=true;
						}
						//System.out.println(curTemp);
					}
				}
			} catch (Exception e) {
				JOptionPane.showMessageDialog(null, "与中央空调连接中断，请联系管理员","警告",JOptionPane.WARNING_MESSAGE);
			}
		}
	}
	
	public class getCharge implements Runnable
	{

		@Override
		public void run() {
			// TODO Auto-generated method stub
			try{
				while(true)
				{
					Thread.sleep(500);
					if(isGetCharge)
					{
						String request="GC "+roomID;
						String charge=sendAndRecv(request);
						curMoneyLabel.setText(charge);
						consumeMoney=Double.parseDouble(charge);
					}
				}
			}
			catch(Exception e)
			{
				JOptionPane.showMessageDialog(null, "与中央空调连接中断，请联系管理员","警告",JOptionPane.WARNING_MESSAGE);
			}
		}
		
	}
	
	public class feelCurTemp implements Runnable
	{

		@Override
		public void run() {
			// TODO Auto-generated method stub	
			try {
				while(true)
				{
					Thread.sleep(3000);
					if(autoChangeTemp)
					{
						if(workType==0)				//制冷模式下
						{
							curTemp++;
							curTemLabel.setText(String.valueOf(curTemp));
							if((curTemp-destTemp)>=5)
							{
								if(btnOnOff.getText().equals("OFF"))
								{
									String request="AT "+temSpinner.getValue()+" "+curTemp+" "+curWind+" "+roomID;	
									String ack=sendAndRecv(request);
									if(ack.equals("OK"))
									{
										destTemp=(Integer)temSpinner.getValue();      //将当前的目标温度保存起来
										autoChangeTemp=false;
									}
								}
								if((curTemp-destTemp)>=10)			//当温度变化大于10时，表示与室温一致，房间空调温度不在变化
								{
									autoChangeTemp=false;
								}
							}
						}
						else						//制热模式下
						{
							curTemp--;
							curTemLabel.setText(String.valueOf(curTemp));
							if((destTemp-curTemp)>=5)
							{
								if(btnOnOff.getText().equals("OFF"))
								{
									String request="AT "+temSpinner.getValue()+" "+curTemp+" "+curWind+" "+roomID;	
									String ack=sendAndRecv(request);
									if(ack.equals("OK"))
									{
										destTemp=(Integer)temSpinner.getValue();      //将当前的目标温度保存起来
										autoChangeTemp=false;
									}
								}
								if((destTemp-curTemp)>=10)			//当温度变化大于10时，表示与室温一致，房间空调温度不在变化
								{
									autoChangeTemp=false;
								}
							}

						}
					}
				}
				
			} catch (Exception e) {
				JOptionPane.showMessageDialog(null, "与中央空调连接中断，请联系管理员","警告",JOptionPane.WARNING_MESSAGE);
			}
		}	
	}
}
