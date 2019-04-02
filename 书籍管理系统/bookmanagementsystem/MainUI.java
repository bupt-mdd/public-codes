package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.*;
import javax.swing.border.BevelBorder;

public class MainUI extends JFrame implements ActionListener
{
	private JLabel operateLabel=new JLabel("请选择相应的操作： ");
	
	private JButton bookButton=new JButton("书本信息维护");
	private JButton strategyButton=new JButton("策略信息维护");
	private JButton buyButton=new JButton("购买书籍界面");
	
	private JPanel titlePanel=new JPanel();
	private JPanel bookPanel=new JPanel();
	private JPanel strategyPanel=new JPanel();
	private JPanel buyPanel=new JPanel();
	
	public MainUI()
	{
		this.setTitle("书籍购买系统");
		this.setLocation(350, 350);
		this.setLayout(new GridLayout(4,1));
		this.setSize(320,200);
		
		this.titlePanel.add(new JPanel());
		this.titlePanel.add(this.operateLabel);
		this.titlePanel.add(new JPanel());
		
		this.bookPanel.add(new JPanel());
		this.bookPanel.add(this.bookButton);
		this.bookPanel.add(new JPanel());
		
		this.strategyPanel.add(new JPanel());
		this.strategyPanel.add(this.strategyButton);
		this.strategyPanel.add(new JPanel());
		
		this.buyPanel.add(new JPanel());
		this.buyPanel.add(this.buyButton);
		this.buyPanel.add(new JPanel());
		
		this.add(this.titlePanel);	
		this.add(this.bookPanel);	
		this.add(this.strategyPanel);	
		this.add(this.buyPanel);	
		
		this.setResizable(false);     //固定大小
		this.setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	
		//设置监听
		this.bookButton.addActionListener(this);
		this.strategyButton.addActionListener(this);
		this.buyButton.addActionListener(this);	
	}
	
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==bookButton)
		{
			this.setVisible(false);
			new BookUI(this);
			//this.setVisible(true);
		}
		else if(e.getSource()==strategyButton)
		{
			this.setVisible(false);
			new StrategyUI(this);
			//this.setVisible(true);
		}
		else if(e.getSource()==buyButton)
		{
			this.setVisible(false);
			new BuyUI(this);
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub	
		MainUI input=new MainUI();
	}

}
