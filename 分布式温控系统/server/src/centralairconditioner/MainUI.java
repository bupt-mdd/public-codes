package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.util.ArrayList;
import java.util.Hashtable;

import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import centralairconditioner.ConfigureUI;

public class MainUI extends JFrame implements WindowListener,ActionListener
{
	private JFrame fatherWindow;
	private CentralConnectDemo serverDemo;
	
	private int workType;
	private int initialTemp;
	private int initialWind;  									 //0、1、2对应着风速的低、中、高
	private int lowTemp;
	private int highTemp;
	
	private JMenuItem openMonitor;
	private JMenuItem stopMonitor;
	private JMenuItem dayChart;
	private JMenuItem monthChart;
	private JMenuItem yearChart;
	private JMenuItem specifications;
	private JMenuItem charges;
	private JMenuItem aboutUs;
	
	private DefaultTableModel stateModel;
	private JTable stateTable;
	private JScrollPane contentpane;
    
	public Hashtable<String,ArrayList<Object>> roomIDIndes =new Hashtable<String,ArrayList<Object>>();//房间号，行索引、上一时刻温度、此次开机费用
	private CentralController controller = new CentralController();
	
	public MainUI(JFrame fatherWindow,int workType,int initialTemp,int initialWind,
			int lowTemp,int highTemp) {

		this.fatherWindow=fatherWindow;
		this.workType=workType;
		this.initialTemp=initialTemp;
		this.initialWind=initialWind;   				//0、1、2对应着风速的低、中、高
		this.lowTemp=lowTemp;
		this.highTemp=highTemp;
		
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 580, 220);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu mnNewMenu = new JMenu("\u76D1\u63A7\u72B6\u6001");
		menuBar.add(mnNewMenu);
		
		openMonitor = new JMenuItem("\u6253\u5F00\u76D1\u63A7");
		mnNewMenu.add(openMonitor);
		
		stopMonitor = new JMenuItem("\u5173\u95ED\u76D1\u63A7");
		mnNewMenu.add(stopMonitor);
		
		JMenu mnNewMenu_1 = new JMenu("\u62A5\u8868");
		menuBar.add(mnNewMenu_1);
		
		dayChart = new JMenuItem("\u65E5\u62A5\u8868");
		mnNewMenu_1.add(dayChart);
		
		monthChart = new JMenuItem("\u6708\u62A5\u8868");
		mnNewMenu_1.add(monthChart);
		
		yearChart = new JMenuItem("\u5E74\u62A5\u8868");
		mnNewMenu_1.add(yearChart);
		
		JMenu mnNewMenu_2 = new JMenu("详单&结账");
		menuBar.add(mnNewMenu_2);
		
	    specifications = new JMenuItem("详单");
		mnNewMenu_2.add(specifications);
		
		charges = new JMenuItem("结账");
		mnNewMenu_2.add(charges);
		
		JMenu mnNewMenu_3 = new JMenu("\u5173\u4E8E");
		menuBar.add(mnNewMenu_3);
		
		aboutUs = new JMenuItem("\u5173\u4E8E\u6211\u4EEC");
		mnNewMenu_3.add(aboutUs);
		
		this.setVisible(true);
		this.setResizable(false);
		
		//new一个服务器demo来监听处理客户端的请求
		serverDemo=new CentralConnectDemo(this,controller);
		getContentPane().setLayout(new BorderLayout(0, 0));
		
		stateTable = new JTable();
		stateTable.setEnabled(false);
		stateModel =new DefaultTableModel(new String[] { "房间号","开关机状态","目标温度","当前温度","目标风速","当前风速","运行状态","当前计费" }, 0);
		stateTable.setModel(stateModel);
		contentpane = new JScrollPane(stateTable);
		getContentPane().add(contentpane, BorderLayout.CENTER);
		
		//设置监听
		this.addWindowListener(this);
		this.openMonitor.addActionListener(this);
		this.stopMonitor.addActionListener(this);
		this.aboutUs.addActionListener(this);
		this.dayChart.addActionListener(this);
		this.monthChart.addActionListener(this);
		this.yearChart.addActionListener(this);
		this.specifications.addActionListener(this);
		this.charges.addActionListener(this);
	}
	
	public String getInitialInf()
	{
		String ackInf;
		ackInf=this.workType+" "+this.initialTemp+" "+this.initialWind+" "+0d;           //计费初始为0
		return ackInf;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==this.openMonitor)
		{
			this.serverDemo.startMonitor();
		}
		else if(e.getSource()==this.stopMonitor)
		{
			this.serverDemo.stopMonitor();
		}
		else if(e.getSource()==this.aboutUs)
		{
			new CopyRight(this);
		}
		else if(e.getSource()==this.dayChart)
		{
			new selectDate(this,this.controller);
		}
		else if(e.getSource()==this.monthChart)
		{
			new selectMonth(this,this.controller);
		}
		else if(e.getSource()==this.yearChart)
		{
			new selectYear(this,this.controller);
		}
		else if(e.getSource()==this.specifications )
		{
		    new Specification(this,this.controller);
		}
		else if(e.getSource() == this.charges)
		{
			new selectChargeTime(this,this.controller);
		}
	}
	
	public void updateAllRommState(String roomID,String StateStr)
	{
		String[] inf=StateStr.split(" ");
		String[] Str1={"关机","开机"};
		String[] Str2={"服务中","等待中"};
		String[] windStr={"低速","中速","高速"};
		
		if(this.roomIDIndes.containsKey(roomID))
		{
			int index=(int) this.roomIDIndes.get(roomID).get(0);
			Integer indexI = new Integer(index);
			Integer initialTempI = new Integer(initialTemp);
			//System.out.println("index "+index);
			if(inf[0].equals("0"))
			{
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(indexI);add(new Integer(100));add(new Double(0d));}});//用100代表上一时刻关机了
				this.stateModel.setValueAt(Str1[Integer.parseInt(inf[0])], index, 1);
				for(int i=2;i<=7;i++)                     //由于此时，从客户端获取的只有这5个参数，至于运行状态和计费有中央空调决定。
				{
					this.stateModel.setValueAt("", index, i);
				}
			}
			else
			{
				this.stateModel.setValueAt(Str1[Integer.parseInt(inf[0])], index, 1);         //开关机状态
				this.stateModel.setValueAt(inf[1], index, 2);                                 //目标温度
				this.stateModel.setValueAt(inf[2], index, 3);								  //当前温度
				this.stateModel.setValueAt(windStr[Integer.parseInt(inf[3])], index, 4);		  //目标风速
				this.stateModel.setValueAt(windStr[Integer.parseInt(inf[4])], index, 5);		  //当前风速

				//此处可以从中央空调获取运行状态和计费的信息，进行设置
				this.stateModel.setValueAt(Str2[0], index, 6);   							  //运行状态
				int lastTemp = (int)this.roomIDIndes.get(roomID).get(1);
				if(lastTemp == 100){
					lastTemp = Integer.parseInt(inf[2]);
				}
				double countTem = (double)(this.roomIDIndes.get(roomID).get(2));
			    double newCount= countTem + countThisCharge(lastTemp,Integer.parseInt(inf[2]),
						Integer.parseInt(inf[4]),countTem);
				this.stateModel.setValueAt(newCount, index, 7);         			 //计费
				
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(indexI);add(new Integer(inf[2]));
				         add(new Double(newCount));}});
			}
		}
		else
		{
			if(inf[0].equals("0"))
			{
				this.stateModel.addRow(new Object[]{roomID,"关机"});
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(new Integer(stateModel.getRowCount()-1));
				add(new Integer(initialTemp));add(new Double(0d));}});
			}
			else
			{
				this.stateModel.addRow(new Object[]{roomID,Str1[Integer.parseInt(inf[0])],inf[1],inf[2],
						windStr[Integer.parseInt(inf[3])],windStr[Integer.parseInt(inf[4])],Str2[0],0d});
				//从客户端获取的只有这5个参数,最后两个字段为运行状态和计费，此处先不做处理
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(new Integer(stateModel.getRowCount()-1));
				add(new Integer(initialTemp));add(new Double(0d));}});
			}
		}
		this.repaint();	
	}
	
	public double countThisCharge(int lastTemp,int curTemp,int windSpeed,double count){//计算一次开机产生的费用
		int time = 0;
		time = (Math.abs(lastTemp-curTemp))*(3-windSpeed);
		switch(windSpeed){
		case 0:{
			count = time*0.75;
			break;
		}
		case 1:{
			count = time;
		}
		case 2:{
			count = time*1.25;
		}
		}
		return  count;
	}
	
	public void removeClientInTable()
	{
		int count=this.stateModel.getRowCount();
		for(int i=0;i<count;i++)
		{
			this.stateModel.removeRow(0);
		}
		this.roomIDIndes.clear();
		this.repaint();	
	}
	
	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosing(WindowEvent e) {
		// TODO Auto-generated method stub
		this.fatherWindow.setVisible(true);
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
