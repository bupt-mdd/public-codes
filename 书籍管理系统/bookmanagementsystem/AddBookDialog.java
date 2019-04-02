package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.BevelBorder;

public class AddBookDialog  extends JDialog implements ActionListener
{
	String isbn;
	String title;
	int type;
	double price;
	private BookUI mainWindow;
	//存放dialog的类型,两种员工的信心录入的表项也不同
	private JLabel isbnLabel=new JLabel("编号 ： ");
	private JLabel titleLabel=new JLabel("书名 ： ");
	private JLabel priceLabel=new JLabel("价格 ： ");
	private JLabel typeLabel=new JLabel("类型 ： ");
	
	private JComboBox typeOfBookBox = new JComboBox (new String[]{"非教材类计算机图书","教材类图书",
			"连环画类图书","养生类图书","其他"});
	//表项的输入框
	private JTextField isbnText=new JTextField(20);
	private JTextField titleText=new JTextField(20);
	private JTextField priceText=new JTextField(20);
	//private JTextField typeText=new JTextField(20);
		
	private JPanel isbnPanel=new JPanel();
	private JPanel titlePanel=new JPanel();
	private JPanel pricePanel=new JPanel();
	private JPanel typePanel=new JPanel();
	private JPanel ButtonPanel=new JPanel();
	//OK and RESET
	private JButton okButton=new JButton("ok");
	private JButton resetButton=new JButton("reset");
		
	public AddBookDialog(BookUI bookUI)
	{
		//将各部件进行排版组合
		this.mainWindow=bookUI;
		this.typeOfBookBox.setPreferredSize(new Dimension(224,24));
		
		this.setTitle("录入书本信息");
		this.setLocation(350, 350);
		this.isbnPanel.setLayout(new BorderLayout());
		this.isbnPanel.add("West",isbnLabel);
		this.isbnPanel.add("East",isbnText);
			
		this.titlePanel.setLayout(new BorderLayout());
		this.titlePanel.add("West",titleLabel);
		this.titlePanel.add("East",titleText);
			
		this.pricePanel.setLayout(new BorderLayout());
		this.pricePanel.add("West",priceLabel);
		this.pricePanel.add("East",priceText);
			
		this.typePanel.setLayout(new BorderLayout());
		this.typePanel.add("West",typeLabel);
		this.typePanel.add("East",typeOfBookBox);
			
		this.ButtonPanel.setLayout(new GridLayout(1,2,120,20));
		this.ButtonPanel.add("West",okButton);
		this.ButtonPanel.add("East",resetButton);
			
		//将各个panel加入dialog中
		this.setLayout(new FlowLayout());
		this.add(this.isbnPanel);
		this.add(this.titlePanel);
		this.add(this.typePanel);
		this.add(this.pricePanel);
		this.add(this.ButtonPanel);
		
		this.setSize(320,180);
		this.add(this.ButtonPanel);				
		
		this.setResizable(false);     //固定大小
		this.setVisible(true);
			
		//设置监听
		this.okButton.addActionListener(this);
		this.resetButton.addActionListener(this);	
	} 
		
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==okButton)
		{	
			try
			{
				//获取表内的内容
				this.isbn=this.isbnText.getText();
				this.title=this.titleText.getText();
				this.type=this.typeOfBookBox.getSelectedIndex();
				this.price=Double.parseDouble(this.priceText.getText());
				boolean ifSuc=Controller.getInstance().addBook(isbn, title, price, type);
				if(ifSuc==true)
				{
					this.dispose();
				}
				else
				{
					JOptionPane.showMessageDialog(null, "添加失败，已经存在该书本的信息","消息",JOptionPane.INFORMATION_MESSAGE);
				}
				this.mainWindow.updateList();
				
			}
			//对抛出的异常进行处理
			catch(Exception  e1)
			{
				//当各部件为空时候，会抛出异常，分别进行处理
				if(isbn.equals(""))
				{
					JOptionPane.showMessageDialog(null, "书本编号不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
					this.isbnText.requestFocus();
				}
				else if(title.equals(""))
				{
					JOptionPane.showMessageDialog(null, "书籍名称不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
					this.titleText.requestFocus();
				}
				else if(priceText.getText().equals(""))
				{
					JOptionPane.showMessageDialog(null, "书籍价格不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
					this.priceText.requestFocus();
				}
				else if(!priceText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{   //当不能转换为数字时，也会抛出异常，用正则式判断
					JOptionPane.showMessageDialog(null, "书籍价格必须是数字","警告",JOptionPane.WARNING_MESSAGE);
					this.priceText.setText("");
					this.priceText.requestFocus();
				}
			}
		}
		//清空各表项内的内容
		else if(e.getSource()==resetButton)
		{
			this.isbnText.setText("");
			this.titleText.setText("");
			this.typeOfBookBox.setSelectedIndex(0);
			this.priceText.setText("");
		}
	}
}
