package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.BevelBorder;

public class SimpleStrategyDialog extends JDialog implements ActionListener
{
	private String title;
	private int typeForBook;
	private int strategyType;
	private double discount;
	private StrategyUI mainWindow;
	int oldType;                                             //��Ҫ���ڱ༭���Ե�ʱ��
	//����ָʾ���������еĲ���(��ӻ��߱༭)��
	private boolean flag;
	//���dialog������,����Ա��������¼��ı���Ҳ��ͬ
	private JLabel titleLabel=new JLabel("�������ƣ� ");
	private JLabel typeLabel=new JLabel("�������ͣ� ");
	private JLabel typeForBookLabel=new JLabel("�����鼮�� ");
	private JLabel discountLabel=new JLabel("  �ۿ�      �� ");
	//����������
	//private JTextField isbnText=new JTextField(20);
	private JTextField titleText=new JTextField(20);
	private JTextField discountText=new JTextField(20);
	
	private JComboBox typeForBookBox = new JComboBox (new String[]{"�ǽ̲�������ͼ��","�̲���ͼ��",
			"��������ͼ��","������ͼ��","����"});
	private JComboBox strategyBox = new JComboBox (new String[]{"����ֵ�Ż�","�ٷֱ��ۿ�"});
	
	//private JPanel isbnPanel=new JPanel();
	private JPanel titlePanel=new JPanel();
	private JPanel typeForBookPanel=new JPanel();
	private JPanel typePanel=new JPanel();
	private JPanel discountPanel=new JPanel();
	private JPanel ButtonPanel=new JPanel();
	//OK and RESET
	private JButton okButton=new JButton("ȷ��");
	private JButton resetButton=new JButton("���");
	
	public SimpleStrategyDialog(StrategyUI mainWindow,boolean flag)
	{
		this(0,null,mainWindow,flag);
	}
	
	public SimpleStrategyDialog(int typeForBook,PricingStrategy strategy,StrategyUI mainWindow,boolean flag)
	{	
		this.flag=flag;
		this.mainWindow=mainWindow;
		this.typeForBookBox.setPreferredSize(new Dimension(224,22));//���������˵��ĳߴ�
		this.strategyBox.setPreferredSize(new Dimension(224,22));
		
		//�������������Ű����
		this.setTitle("¼���鱾��Ϣ");
		this.setLocation(350, 350);
			
		this.titlePanel.setLayout(new BorderLayout());
		this.titlePanel.add("West",titleLabel);
		this.titlePanel.add("East",titleText);
			
		this.typeForBookPanel.setLayout(new BorderLayout());
		this.typeForBookPanel.add("West",typeForBookLabel);
		this.typeForBookPanel.add("East",typeForBookBox);
			
		this.typePanel.setLayout(new BorderLayout());
		this.typePanel.add("West",typeLabel);
		this.typePanel.add("East",strategyBox);
			
		this.discountPanel.setLayout(new BorderLayout());
		this.discountPanel.add("West",discountLabel);
		this.discountPanel.add("East",discountText);
		
		this.ButtonPanel.setLayout(new GridLayout(1,2,120,20));
		this.ButtonPanel.add("West",okButton);
		this.ButtonPanel.add("East",resetButton);
		
		//������panel����dialog��
		this.setLayout(new FlowLayout());
		//this.add(this.isbnPanel);
		this.add(this.titlePanel);
		this.add(this.typePanel);
		this.add(this.discountPanel);
		this.add(this.typeForBookPanel);
		this.add(this.typePanel);
		this.add(this.ButtonPanel);
		
		this.setSize(320,180);
		this.add(this.ButtonPanel);				
		
		this.setResizable(false);     //�̶���С
		this.setVisible(true);
		//���ü���
		this.okButton.addActionListener(this);
		this.resetButton.addActionListener(this);	
		
		if(strategy!=null)
		{
			oldType=typeForBook;
			this.titleText.setText(strategy.getNameOfStrategy());
			this.strategyBox.setSelectedIndex(strategy.getTypeOfStrategy());
			this.typeForBookBox.setSelectedIndex(typeForBook);
			if(strategy instanceof PercentageStrategy )
			{
				PercentageStrategy temp=(PercentageStrategy)strategy;
				this.discountText.setText(String.valueOf(temp.getDiscount()*100));
			}
			else
			{
				FlatRateStrategy temp=(FlatRateStrategy)strategy;
				this.discountText.setText(String.valueOf(temp.getDiscount()));
			}
		}
	} 
		
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==okButton)
		{	
			if(flag==true)
			{
				editStrategy();
			}
			else
			{
				addStrategy();
			}
			
		}
		//��ո������ڵ�����
		else if(e.getSource()==resetButton)
		{
			this.titleText.setText("");
			this.strategyBox.setSelectedIndex(0);
			this.typeForBookBox.setSelectedIndex(0);
			this.discountText.setText("");
		}
	}
	
	private void addStrategy()
	{
		try
		{
			boolean ifInstance=true;
			this.title=this.titleText.getText();
			this.discount=Double.parseDouble(this.discountText.getText());
			this.typeForBook=this.typeForBookBox.getSelectedIndex();
			this.strategyType=this.strategyBox.getSelectedIndex();
			if(strategyType==1)
			{
				this.discount=this.discount/100;
			}
			int isbn=0;
			PricingStrategy newStrategy=null;
			if(strategyType==0)
			{
				newStrategy=(PricingStrategy)new FlatRateStrategy(
						isbn,this.title,this.strategyType,this.discount);
			}
			else
			{
				newStrategy=(PricingStrategy)new PercentageStrategy(
						isbn,this.title,this.strategyType,this.discount);
			}
			boolean flag=Controller.getInstance().addStrategy(typeForBook, newStrategy);
			if(flag==false)
			{
				JOptionPane.showMessageDialog(null, "�����鼮�Ѿ��ж�Ӧ�Ĳ��ԣ���ѡ���Ĳ���","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
			}
			this.mainWindow.updateList();
			this.dispose();
		}
		//���׳����쳣���д���
		catch(Exception  e1)
		{
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "�������Ʋ���Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else if(this.discountText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "�ۿ�/�Żݶ��Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else
			{   //������ת��Ϊ����ʱ��Ҳ���׳��쳣��������ʽ�ж�
				if(!this.discountText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{
					JOptionPane.showMessageDialog(null, "�ۿ�/�Żݶ����������","����",JOptionPane.WARNING_MESSAGE);
					this.discountText.setText("");
					this.discountText.requestFocus();
				}
			}
		}
	}
	
	private void editStrategy()
	{
		try
		{
			boolean ifInstance=true;
			this.title=this.titleText.getText();
			this.discount=Double.parseDouble(this.discountText.getText());
			this.typeForBook=this.typeForBookBox.getSelectedIndex();
			this.strategyType=this.strategyBox.getSelectedIndex();
			if(strategyType==1)
			{
				this.discount=this.discount/100;
			}
			int isbn=0;
			PricingStrategy editStrategy=null;
			if(strategyType==0)
			{
				editStrategy=(PricingStrategy)new FlatRateStrategy(
						isbn,this.title,this.strategyType,this.discount);
			}
			else
			{
				editStrategy=(PricingStrategy)new PercentageStrategy(
						isbn,this.title,this.strategyType,this.discount);
			}
			boolean flag=Controller.getInstance().editStrategy(oldType,typeForBook, editStrategy);
			if(flag==false)
			{
				JOptionPane.showMessageDialog(null, "�����鼮�Ѿ��ж�Ӧ�Ĳ��ԣ���ѡ����������鼮","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
			}
			else
			{
				this.dispose();
			}
			this.mainWindow.updateList();
		}
		//���׳����쳣���д���
		catch(Exception  e1)
		{
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "�������Ʋ���Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else if(this.discountText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "�ۿ�/�Żݶ��Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else
			{   //������ת��Ϊ����ʱ��Ҳ���׳��쳣��������ʽ�ж�
				if(!this.discountText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{
					JOptionPane.showMessageDialog(null, "�ۿ�/�Żݶ����������","����",JOptionPane.WARNING_MESSAGE);
					this.discountText.setText("");
					this.discountText.requestFocus();
				}
			}
		}
	}
}
