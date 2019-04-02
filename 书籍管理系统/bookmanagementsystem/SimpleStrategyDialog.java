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
	int oldType;                                             //主要用于编辑策略的时候
	//用于指示接下来进行的操作(添加或者编辑)。
	private boolean flag;
	//存放dialog的类型,两种员工的信心录入的表项也不同
	private JLabel titleLabel=new JLabel("策略名称： ");
	private JLabel typeLabel=new JLabel("策略类型： ");
	private JLabel typeForBookLabel=new JLabel("适用书籍： ");
	private JLabel discountLabel=new JLabel("  折扣      ： ");
	//表项的输入框
	//private JTextField isbnText=new JTextField(20);
	private JTextField titleText=new JTextField(20);
	private JTextField discountText=new JTextField(20);
	
	private JComboBox typeForBookBox = new JComboBox (new String[]{"非教材类计算机图书","教材类图书",
			"连环画类图书","养生类图书","其他"});
	private JComboBox strategyBox = new JComboBox (new String[]{"绝对值优惠","百分比折扣"});
	
	//private JPanel isbnPanel=new JPanel();
	private JPanel titlePanel=new JPanel();
	private JPanel typeForBookPanel=new JPanel();
	private JPanel typePanel=new JPanel();
	private JPanel discountPanel=new JPanel();
	private JPanel ButtonPanel=new JPanel();
	//OK and RESET
	private JButton okButton=new JButton("确定");
	private JButton resetButton=new JButton("清空");
	
	public SimpleStrategyDialog(StrategyUI mainWindow,boolean flag)
	{
		this(0,null,mainWindow,flag);
	}
	
	public SimpleStrategyDialog(int typeForBook,PricingStrategy strategy,StrategyUI mainWindow,boolean flag)
	{	
		this.flag=flag;
		this.mainWindow=mainWindow;
		this.typeForBookBox.setPreferredSize(new Dimension(224,22));//设置下拉菜单的尺寸
		this.strategyBox.setPreferredSize(new Dimension(224,22));
		
		//将各部件进行排版组合
		this.setTitle("录入书本信息");
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
		
		//将各个panel加入dialog中
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
		
		this.setResizable(false);     //固定大小
		this.setVisible(true);
		//设置监听
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
		//清空各表项内的内容
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
				JOptionPane.showMessageDialog(null, "该类书籍已经有对应的策略，请选择别的操作","消息",JOptionPane.INFORMATION_MESSAGE);
			}
			this.mainWindow.updateList();
			this.dispose();
		}
		//对抛出的异常进行处理
		catch(Exception  e1)
		{
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "策略名称不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else if(this.discountText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "折扣/优惠额不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else
			{   //当不能转换为数字时，也会抛出异常，用正则式判断
				if(!this.discountText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{
					JOptionPane.showMessageDialog(null, "折扣/优惠额必须是数字","警告",JOptionPane.WARNING_MESSAGE);
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
				JOptionPane.showMessageDialog(null, "该类书籍已经有对应的策略，请选择其他类的书籍","消息",JOptionPane.INFORMATION_MESSAGE);
			}
			else
			{
				this.dispose();
			}
			this.mainWindow.updateList();
		}
		//对抛出的异常进行处理
		catch(Exception  e1)
		{
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "策略名称不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else if(this.discountText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "折扣/优惠额不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
			}
			else
			{   //当不能转换为数字时，也会抛出异常，用正则式判断
				if(!this.discountText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{
					JOptionPane.showMessageDialog(null, "折扣/优惠额必须是数字","警告",JOptionPane.WARNING_MESSAGE);
					this.discountText.setText("");
					this.discountText.requestFocus();
				}
			}
		}
	}
}
