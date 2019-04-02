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
	private int initialWind;  									 //0��1��2��Ӧ�ŷ��ٵĵ͡��С���
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
    
	public Hashtable<String,ArrayList<Object>> roomIDIndes =new Hashtable<String,ArrayList<Object>>();//����ţ�����������һʱ���¶ȡ��˴ο�������
	private CentralController controller = new CentralController();
	
	public MainUI(JFrame fatherWindow,int workType,int initialTemp,int initialWind,
			int lowTemp,int highTemp) {

		this.fatherWindow=fatherWindow;
		this.workType=workType;
		this.initialTemp=initialTemp;
		this.initialWind=initialWind;   				//0��1��2��Ӧ�ŷ��ٵĵ͡��С���
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
		
		JMenu mnNewMenu_2 = new JMenu("�굥&����");
		menuBar.add(mnNewMenu_2);
		
	    specifications = new JMenuItem("�굥");
		mnNewMenu_2.add(specifications);
		
		charges = new JMenuItem("����");
		mnNewMenu_2.add(charges);
		
		JMenu mnNewMenu_3 = new JMenu("\u5173\u4E8E");
		menuBar.add(mnNewMenu_3);
		
		aboutUs = new JMenuItem("\u5173\u4E8E\u6211\u4EEC");
		mnNewMenu_3.add(aboutUs);
		
		this.setVisible(true);
		this.setResizable(false);
		
		//newһ��������demo����������ͻ��˵�����
		serverDemo=new CentralConnectDemo(this,controller);
		getContentPane().setLayout(new BorderLayout(0, 0));
		
		stateTable = new JTable();
		stateTable.setEnabled(false);
		stateModel =new DefaultTableModel(new String[] { "�����","���ػ�״̬","Ŀ���¶�","��ǰ�¶�","Ŀ�����","��ǰ����","����״̬","��ǰ�Ʒ�" }, 0);
		stateTable.setModel(stateModel);
		contentpane = new JScrollPane(stateTable);
		getContentPane().add(contentpane, BorderLayout.CENTER);
		
		//���ü���
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
		ackInf=this.workType+" "+this.initialTemp+" "+this.initialWind+" "+0d;           //�Ʒѳ�ʼΪ0
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
		String[] Str1={"�ػ�","����"};
		String[] Str2={"������","�ȴ���"};
		String[] windStr={"����","����","����"};
		
		if(this.roomIDIndes.containsKey(roomID))
		{
			int index=(int) this.roomIDIndes.get(roomID).get(0);
			Integer indexI = new Integer(index);
			Integer initialTempI = new Integer(initialTemp);
			//System.out.println("index "+index);
			if(inf[0].equals("0"))
			{
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(indexI);add(new Integer(100));add(new Double(0d));}});//��100������һʱ�̹ػ���
				this.stateModel.setValueAt(Str1[Integer.parseInt(inf[0])], index, 1);
				for(int i=2;i<=7;i++)                     //���ڴ�ʱ���ӿͻ��˻�ȡ��ֻ����5����������������״̬�ͼƷ�������յ�������
				{
					this.stateModel.setValueAt("", index, i);
				}
			}
			else
			{
				this.stateModel.setValueAt(Str1[Integer.parseInt(inf[0])], index, 1);         //���ػ�״̬
				this.stateModel.setValueAt(inf[1], index, 2);                                 //Ŀ���¶�
				this.stateModel.setValueAt(inf[2], index, 3);								  //��ǰ�¶�
				this.stateModel.setValueAt(windStr[Integer.parseInt(inf[3])], index, 4);		  //Ŀ�����
				this.stateModel.setValueAt(windStr[Integer.parseInt(inf[4])], index, 5);		  //��ǰ����

				//�˴����Դ�����յ���ȡ����״̬�ͼƷѵ���Ϣ����������
				this.stateModel.setValueAt(Str2[0], index, 6);   							  //����״̬
				int lastTemp = (int)this.roomIDIndes.get(roomID).get(1);
				if(lastTemp == 100){
					lastTemp = Integer.parseInt(inf[2]);
				}
				double countTem = (double)(this.roomIDIndes.get(roomID).get(2));
			    double newCount= countTem + countThisCharge(lastTemp,Integer.parseInt(inf[2]),
						Integer.parseInt(inf[4]),countTem);
				this.stateModel.setValueAt(newCount, index, 7);         			 //�Ʒ�
				
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(indexI);add(new Integer(inf[2]));
				         add(new Double(newCount));}});
			}
		}
		else
		{
			if(inf[0].equals("0"))
			{
				this.stateModel.addRow(new Object[]{roomID,"�ػ�"});
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(new Integer(stateModel.getRowCount()-1));
				add(new Integer(initialTemp));add(new Double(0d));}});
			}
			else
			{
				this.stateModel.addRow(new Object[]{roomID,Str1[Integer.parseInt(inf[0])],inf[1],inf[2],
						windStr[Integer.parseInt(inf[3])],windStr[Integer.parseInt(inf[4])],Str2[0],0d});
				//�ӿͻ��˻�ȡ��ֻ����5������,��������ֶ�Ϊ����״̬�ͼƷѣ��˴��Ȳ�������
				this.roomIDIndes.put(roomID,new ArrayList<Object>(){{add(new Integer(stateModel.getRowCount()-1));
				add(new Integer(initialTemp));add(new Double(0d));}});
			}
		}
		this.repaint();	
	}
	
	public double countThisCharge(int lastTemp,int curTemp,int windSpeed,double count){//����һ�ο��������ķ���
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
