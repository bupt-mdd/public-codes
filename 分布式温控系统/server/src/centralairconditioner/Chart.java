package centralairconditioner;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class Chart extends JFrame implements WindowListener{

	private JFrame fatherWin;
	
	private JTable table;
	private DefaultTableModel tableModel;
	private JScrollPane contentPane;
	private JTextField timeTextField;

	private DateFormat df = new SimpleDateFormat("yyyy.MM.dd");
	
	public Chart(JFrame fatherWin,CentralController controller,String date) {
		
		this.fatherWin=fatherWin;
		
		setTitle("\u62A5\u8868");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		this.setVisible(true);
		String date1 = date;
		table = new JTable();
		table.setEnabled(false);
		tableModel = new DefaultTableModel(new String[]{"房间号","消耗费用","开关次数","调温次数","调风次数","被调度次数"},0);
	    getContentPane().setLayout(null);
	    table.setModel(tableModel);
		contentPane = new JScrollPane(table);
		contentPane.setBounds(0, 34, 434, 227);
		getContentPane().add(contentPane);
		
		JLabel label = new JLabel("\u65F6\u95F4\u6BB5");
		label.setBounds(10, 9, 43, 15);
		getContentPane().add(label);
		
		timeTextField = new JTextField();
		timeTextField.setEditable(false);
		timeTextField.setBounds(63, 6, 209, 21);
		getContentPane().add(timeTextField);
		timeTextField.setColumns(10);
		timeTextField.setText(date1);
		this.addWindowListener(this);
		this.fatherWin.setVisible(false);
		if(!controller.showDayChart(this,date1)){
			JOptionPane.showMessageDialog(this, "数据获取失败","警告",JOptionPane.WARNING_MESSAGE);
		}	
	}
	
	public Chart(JFrame fatherWin,CentralController controller,String year,int month) {
		
		this.fatherWin=fatherWin;
		
		setTitle("\u62A5\u8868");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		this.setVisible(true);
		
		table = new JTable();
		table.setEnabled(false);
		tableModel = new DefaultTableModel(new String[]{"房间号","消耗费用","开关次数","调温次数","调风次数","被调度次数"},0);
	    getContentPane().setLayout(null);
	    table.setModel(tableModel);
		contentPane = new JScrollPane(table);
		contentPane.setBounds(0, 34, 434, 227);
		getContentPane().add(contentPane);
		
		JLabel label = new JLabel("\u65F6\u95F4\u6BB5");
		label.setBounds(10, 9, 43, 15);
		getContentPane().add(label);
		
		timeTextField = new JTextField();
		timeTextField.setEditable(false);
		timeTextField.setBounds(63, 6, 209, 21);
		getContentPane().add(timeTextField);
		timeTextField.setColumns(10);
		String date = year+"年"+month+"月";
		timeTextField.setText(date);
		this.addWindowListener(this);
		this.fatherWin.setVisible(false);
		if(!controller.showMonthChart(this,year,month)){
			JOptionPane.showMessageDialog(this, "数据获取失败","警告",JOptionPane.WARNING_MESSAGE);
		}		
	}
	
	public Chart(JFrame fatherWin,CentralController controller,String year,String year1) {
		
		this.fatherWin=fatherWin;
		
		setTitle("\u62A5\u8868");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		this.setVisible(true);
		
		table = new JTable();
		table.setEnabled(false);
		tableModel = new DefaultTableModel(new String[]{"房间号","消耗费用","开关次数","调温次数","调风次数","被调度次数"},0);
	    getContentPane().setLayout(null);
	    table.setModel(tableModel);
		contentPane = new JScrollPane(table);
		contentPane.setBounds(0, 34, 434, 227);
		getContentPane().add(contentPane);
		
		JLabel label = new JLabel("\u65F6\u95F4\u6BB5");
		label.setBounds(10, 9, 43, 15);
		getContentPane().add(label);
		
		timeTextField = new JTextField();
		timeTextField.setEditable(false);
		timeTextField.setBounds(63, 6, 209, 21);
		getContentPane().add(timeTextField);
		timeTextField.setColumns(10);
		String date = year+"年";
		timeTextField.setText(date);
		this.addWindowListener(this);
		this.fatherWin.setVisible(false);	
		if(!controller.showYearChart(this,year)) {
			JOptionPane.showMessageDialog(this, "数据获取失败","警告",JOptionPane.WARNING_MESSAGE);
		}
			
	}
	
	public void insertData(String roomNum,double expense,int onOffTime,int AdjTem,int AdjWind,int dispatch){
		this.tableModel.addRow(new Object[]{roomNum,expense,onOffTime,AdjTem,AdjWind,dispatch});
	}

	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosing(WindowEvent e) {
		// TODO Auto-generated method stub
		this.fatherWin.setVisible(true);
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
