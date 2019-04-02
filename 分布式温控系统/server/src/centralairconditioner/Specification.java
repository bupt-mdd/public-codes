package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.sql.*;
import java.text.DateFormat;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTable;

public class Specification extends JFrame implements WindowListener{
	
	private MainUI fatherWin;
	
    private CentralController controller;
	private JScrollPane contentPane;
    private JTable table;
    private DefaultTableModel tableModel;
	
	public Specification(MainUI fatherWin,CentralController controller) {
		
		this.fatherWin=fatherWin;
		
		setTitle("详单");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 546, 364);
		getContentPane().setLayout(new BorderLayout(0, 0));
		this.controller = controller;
		this.setVisible(true);
		
		table = new JTable();
		table.setEnabled(false);
		tableModel = new DefaultTableModel(new String[]{"房间号","起始时间","终止时间","起始温度","目标温度","当前风速","费用"},0);
	    table.setModel(tableModel);
		contentPane = new JScrollPane(table);
		getContentPane().add(contentPane,BorderLayout.CENTER);
		this.addWindowListener(this);
		this.fatherWin.setEnabled(false);
		if(!controller.showSpecification(this))
			JOptionPane.showMessageDialog(this, "数据获取失败","警告",JOptionPane.WARNING_MESSAGE);
		
	}
	public void insertData(String roomNum,String startTime,String endTime,int curTem,int AimTem,String curWindSpeed,double expense){
	
		this.tableModel.addRow(new Object[]{roomNum,startTime,endTime,curTem,AimTem,curWindSpeed,expense});
	}
	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowClosing(WindowEvent e) {
		// TODO Auto-generated method stub
		this.fatherWin.setEnabled(true);
		this.fatherWin.requestFocus();
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
