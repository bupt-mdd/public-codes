package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.GridLayout;
import javax.swing.SwingConstants;
import java.awt.Font;
import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JSpinner;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SpinnerNumberModel;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

import centralairconditioner.MainUI;

public class ConfigureUI extends JFrame implements WindowListener,ActionListener{
	
	private JFrame fatherWindow;
	
	private JPanel contentPane;
	private JComboBox workTypeComb;
	private JComboBox initialWindComb;
	private JSpinner initialTemSpinner;
	private JSpinner lowTemSpinner;
	private JSpinner highTemSpinner;

	JButton okBtn = new JButton("\u786E\u5B9A");
	JButton cancelBtn = new JButton("\u53D6\u6D88");
	
	/**
	 * Create the frame.
	 */
	public static void main(String[] args) {
		new ConfigureUI(null);
	}
	
	public ConfigureUI(JFrame fatherWindow) 
	{
		this.fatherWindow=fatherWindow;
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 380, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(new GridLayout(7, 0, 0, 0));
		
		JPanel panel_1 = new JPanel();
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("\u4E2D\u592E\u7A7A\u8C03\u914D\u7F6E\u9762\u677F");
		lblNewLabel.setBounds(93, 5, 168, 24);
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setForeground(Color.BLUE);
		lblNewLabel.setFont(new Font("宋体", Font.BOLD, 20));
		panel_1.add(lblNewLabel);
		
		JPanel panel_2 = new JPanel();
		contentPane.add(panel_2);
		panel_2.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("\u5DE5\u4F5C\u6A21\u5F0F\uFF1A");
		lblNewLabel_1.setBounds(68, 8, 76, 15);
		panel_2.add(lblNewLabel_1);
		
		workTypeComb = new JComboBox();
		workTypeComb.setBounds(194, 5, 88, 21);
		workTypeComb.setModel(new DefaultComboBoxModel(new String[] {"\u5236\u51B7\u6A21\u5F0F", "\u5236\u70ED\u6A21\u5F0F"}));
		workTypeComb.setMaximumRowCount(2);
		panel_2.add(workTypeComb);
		
		JPanel panel_3 = new JPanel();
		contentPane.add(panel_3);
		panel_3.setLayout(null);
		
		JLabel lblNewLabel_2 = new JLabel("\u9ED8\u8BA4\u98CE\u901F\uFF1A                  ");
		lblNewLabel_2.setBounds(71, 8, 168, 15);
		panel_3.add(lblNewLabel_2);
		
		initialWindComb = new JComboBox();
		initialWindComb.setBounds(195, 5, 87, 21);
		initialWindComb.setToolTipText("");
		initialWindComb.setMaximumRowCount(3);
		initialWindComb.setModel(new DefaultComboBoxModel(new String[] {"\u4F4E", "\u4E2D", "\u9AD8"}));
		panel_3.add(initialWindComb);
		
		JPanel panel_4 = new JPanel();
		contentPane.add(panel_4);
		panel_4.setLayout(null);
		
		JLabel lblNewLabel_3 = new JLabel("\u9ED8\u8BA4\u6E29\u5EA6\uFF1A                   ");
		lblNewLabel_3.setBounds(70, 8, 174, 15);
		panel_4.add(lblNewLabel_3);
		
		initialTemSpinner = new JSpinner();
		initialTemSpinner.setEnabled(false);
		initialTemSpinner.setBounds(193, 5, 89, 22);
		initialTemSpinner.setModel(new SpinnerNumberModel(25, 18, 30, 1));
		panel_4.add(initialTemSpinner);
		
		JPanel panel_5 = new JPanel();
		contentPane.add(panel_5);
		panel_5.setLayout(null);
		
		JLabel lblNewLabel_4 = new JLabel("\u6700\u4F4E\u6E29\u5EA6\uFF1A                   ");
		lblNewLabel_4.setBounds(70, 8, 174, 15);
		panel_5.add(lblNewLabel_4);
		
		lowTemSpinner = new JSpinner();
		lowTemSpinner.setBounds(193, 5, 91, 22);
		lowTemSpinner.setModel(new SpinnerNumberModel(18, 18, 30, 1));
		panel_5.add(lowTemSpinner);
		
		JPanel panel_6 = new JPanel();
		contentPane.add(panel_6);
		panel_6.setLayout(null);
		
		JLabel lblNewLabel_5 = new JLabel("\u6700\u9AD8\u6E29\u5EA6\uFF1A                   ");
		lblNewLabel_5.setBounds(70, 8, 174, 15);
		panel_6.add(lblNewLabel_5);
		
		highTemSpinner = new JSpinner();
		highTemSpinner.setBounds(194, 5, 90, 22);
		highTemSpinner.setModel(new SpinnerNumberModel(25, 18, 30, 1));
		panel_6.add(highTemSpinner);
		
		JPanel panel = new JPanel();
		contentPane.add(panel);
		
		panel.setLayout(null);
		okBtn.setBounds(67, 5, 76, 23);
		panel.add(okBtn);
		
		cancelBtn.setBounds(210, 5, 76, 23);
		cancelBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		panel.add(cancelBtn);
		this.setResizable(false);
		this.setVisible(true);
		
		//设置监听
		this.addWindowListener(this);
		this.okBtn.addActionListener(this);
		this.cancelBtn.addActionListener(this);
		this.workTypeComb.addActionListener(this);
	}
	
	/**
	 * Action performed.
	 */
	
	public void actionPerformed(ActionEvent e)
	  {
		int workType=this.workTypeComb.getSelectedIndex();
		int initialTemp=(Integer)this.initialTemSpinner.getValue();
		int initialWind=(Integer)this.initialWindComb.getSelectedIndex();   //0、1、2对应着风速的低、中、高
		int lowTemp=(Integer)(this.lowTemSpinner.getValue());
		int highTemp=(Integer)(this.highTemSpinner.getValue());
		
		if (e.getSource() == okBtn)
	    {
			new MainUI(this,workType,initialTemp,initialWind,lowTemp,highTemp);
			this.setVisible(false);
	    }
		else if(e.getSource()==this.workTypeComb)
		{
			if(this.workTypeComb.getSelectedIndex()==0)
			{
				Integer low=(Integer)this.initialTemSpinner.getValue()-7;
				this.lowTemSpinner.setValue(low);
				this.highTemSpinner.setValue(this.initialTemSpinner.getValue());
			}
			else 
			{
				Integer high=(Integer)this.initialTemSpinner.getValue()+5;
				this.lowTemSpinner.setValue(this.initialTemSpinner.getValue());
				this.highTemSpinner.setValue(high);
			}
		}
		else if (e.getSource() == cancelBtn)
	    {
			//this.fatherWindow.setVisible(true);
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
		//this.fatherWindow.setVisible(true);
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
