package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import java.util.*;

import javax.swing.*;
import javax.swing.border.*;
import javax.swing.event.*;

public class CompStrategyDialog extends JFrame implements ActionListener
{
	private int typeForBook;                                       //所对应的的书籍类型。
	private StrategyUI mainWindow;              // 父窗口。
	int oldType;                                                   //主要用于编辑策略的时候
	String title;												   //用于存放策略的name
	
	HashMap<Integer,PricingStrategy> strategies;//存放策略工厂的所有策略，便于进行界面呈现
	protected JList comStrategyList;
	
	private JLabel typeForBookLabel=new JLabel("适用书籍： ");
	private JComboBox typeForBookBox = new JComboBox (new String[]{"非教材类计算机图书","教材类图书",
			"连环画类图书","养生类图书","其他"});
	
	//用于指示接下来进行的操作(添加或者编辑)。
	private boolean flag;
	
	private JLabel titleLabel=new JLabel("策略名称： ");
	private JTextField titleText=new JTextField(17);
	//OK and RESET
	private JButton okButton=new JButton("确定");
	private JButton resetButton=new JButton("清空");
	
	private JPanel titlePanel=new JPanel();
	private JPanel typeForBookPanel=new JPanel();
	private JPanel ButtonPanel=new JPanel();
	InstallData[] options;
	
	public CompStrategyDialog(StrategyUI mainWindow,boolean flag) 
	{
		this(0,null,mainWindow,flag);
	}
	
	public CompStrategyDialog(int typeForBook,PricingStrategy strategy,StrategyUI mainWindow,boolean flag) 
	{	
		this.flag=flag;
		this.mainWindow=mainWindow;
		this.titlePanel.setLayout(new BorderLayout());
		this.titlePanel.add("West",titleLabel);
		this.titlePanel.add("East",titleText);
		
		this.typeForBookPanel.setLayout(new BorderLayout());
		this.typeForBookPanel.add("West",typeForBookLabel);
		this.typeForBookPanel.add("East",typeForBookBox);
		
		this.ButtonPanel.setLayout(new GridLayout());
		this.ButtonPanel.add(new JPanel());
		this.ButtonPanel.add("West",okButton);
		this.ButtonPanel.add("East",resetButton);
		this.ButtonPanel.add(new JPanel());
		getContentPane().setLayout(new FlowLayout());

		this.strategies=PricingStrategyFactory.getInstance().getStrategies();
		java.util.Iterator<Integer> keys=strategies.keySet().iterator();
		int i=0;
		while(keys.hasNext())
		{
			i++;
			keys.next();
		}
		if(strategy==null)               //添加策略界面
		{
			keys=strategies.keySet().iterator();
			options=new InstallData[i];
			int j=0;
			while(j<i)
			{
				int index=keys.next();
				options[j]=new InstallData(strategies.get(index).getIsbnOfStrategy(), strategies.get(index).getTypeOfStrategy(),index);
				j++;
			}
		}
		else                           //编辑策略界面
		{
			i--;
			keys=strategies.keySet().iterator();
			options=new InstallData[i];
			int j=0;
			while(j<i)
			{
				int index=keys.next();
				if(strategies.get(index).getIsbnOfStrategy()!=strategy.getIsbnOfStrategy())
				{
					options[j]=new InstallData(strategies.get(index).getIsbnOfStrategy(), strategies.get(index).getTypeOfStrategy(),index);
					j++;
				}
			}
			this.oldType=typeForBook;          //待编辑策略所对应的的书的类型
		}
		
		comStrategyList = new JList(options);
		CheckListCellRenderer renderer = new CheckListCellRenderer();
		comStrategyList.setCellRenderer(renderer);
		comStrategyList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		CheckListener lst = new CheckListener(this);
		comStrategyList.addMouseListener(lst);

		JScrollPane jsp = new JScrollPane();
		jsp.getViewport().add(comStrategyList);

		this.add(titlePanel);
		JPanel p = new JPanel();
		p.setLayout(new BorderLayout());
		p.add(jsp, BorderLayout.CENTER);
		p.add(typeForBookPanel, BorderLayout.SOUTH);
		p.setBorder(new TitledBorder(new EtchedBorder(), "Please   select   options: "));
		getContentPane().add(p);
		getContentPane().add(ButtonPanel);
		
		//设置监听
		this.okButton.addActionListener(this);
		this.resetButton.addActionListener(this);
		
		//设置待编辑策略之前已经包含的策略。
		if(strategy!=null)
		{
			ArrayList<PricingStrategy> strArray=((CompositeStrategy)strategy).getArraystr();
			ListModel model = comStrategyList.getModel();
			for(int i1=0;i1<strArray.size();i1++)
			{	
				for (int k = 0; k < model.getSize(); k++) {
					InstallData data = (InstallData) model.getElementAt(k);
					if(strArray.get(i1).getIsbnOfStrategy()==data.getIsbn())
					{
						data.setSelected(true);
					}
				}
			}
			
			this.titleText.setText(strategy.getNameOfStrategy());
			this.typeForBookBox.setSelectedIndex(oldType);
		}
		
		setSize(280, 300);
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setLocation(450,200);
		this.setResizable(false);     //固定大小
		this.setVisible(true);
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
		else if(e.getSource()==resetButton)
		{
			ListModel model = comStrategyList.getModel();
			for (int k = 0; k < model.getSize(); k++) {
				InstallData data = (InstallData) model.getElementAt(k);
				data.setSelected(false);
			}
			this.typeForBookBox.setSelectedIndex(0);
			this.titleText.setText("");
			comStrategyList.repaint();
		}
	}

	//添加策略
	private void addStrategy() 
	{
		try
		{
			this.title=this.titleText.getText();
			this.typeForBook=this.typeForBookBox.getSelectedIndex();
			boolean selected=false;
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "策略名称不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
				return;
			}
			ListModel model = comStrategyList.getModel();
			for (int k = 0; k < model.getSize(); k++) {
				InstallData data = (InstallData) model.getElementAt(k);
				if(data.isSelected())
				{
					selected=true;
				}
			}
			if(selected)
			{
				int isbn=0;
				//创建相应的组合类；（newStrategy）
				CompositeBestForCustomer newStrategy=new CompositeBestForCustomer(isbn,this.title,2);

				//通过检查checkbox来添加简单策略到组合策略中
				model = comStrategyList.getModel();
				for (int k = 0; k < model.getSize(); k++) {
					InstallData data = (InstallData) model.getElementAt(k);
					if(data.isSelected())
					{
						int type=data.getTypeOfBook();
						newStrategy.add(PricingStrategyFactory.getInstance().getPricingStrategy(type));
					}
				}
				
				boolean flag=Controller.getInstance().addStrategy(typeForBook, newStrategy);
				if(flag==false)
				{
					JOptionPane.showMessageDialog(null, "该类书籍已经有对应的策略，请选择别的操作","消息",JOptionPane.INFORMATION_MESSAGE);
				}
				this.mainWindow.updateList();
				this.dispose();
			}
			else
			{
				JOptionPane.showMessageDialog(null, "请选择子策略","消息",JOptionPane.INFORMATION_MESSAGE);
			}
		}
		//对抛出的异常进行处理
		catch(Exception  e1){
		}	
	}

	//编辑策略
	private void editStrategy() 
	{
		try
		{
			this.title=this.titleText.getText();
			this.typeForBook=this.typeForBookBox.getSelectedIndex();
			boolean selected=false;
			if(titleText.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "策略名称不能为空","消息",JOptionPane.INFORMATION_MESSAGE);
				this.titleText.requestFocus();
				return;
			}
			ListModel model = comStrategyList.getModel();
			for (int k = 0; k < model.getSize(); k++) {
				InstallData data = (InstallData) model.getElementAt(k);
				if(data.isSelected())
				{
					selected=true;
				}
			}
			if(selected)
			{
				int isbn=0;
				//创建相应的组合类；（newStrategy）
				CompositeBestForCustomer newStrategy=new CompositeBestForCustomer(isbn,this.title,2);
				
				//通过检查checkbox来添加简单策略到组合策略中
				model = comStrategyList.getModel();
				for (int k = 0; k < model.getSize(); k++) {
					InstallData data = (InstallData) model.getElementAt(k);
					if(data.isSelected())
					{
						int type=data.getTypeOfBook();
						newStrategy.add(PricingStrategyFactory.getInstance().getPricingStrategy(type));
					}
				}
				
				boolean flag=Controller.getInstance().editStrategy(oldType,typeForBook, newStrategy);
				if(flag==false)
				{
					JOptionPane.showMessageDialog(null, "该类书籍已经有对应的策略，请选择别的操作","消息",JOptionPane.INFORMATION_MESSAGE);
				}
				this.mainWindow.updateList();
				this.dispose();
			}
			else
			{
				JOptionPane.showMessageDialog(null, "请选择子策略","消息",JOptionPane.INFORMATION_MESSAGE);
			}	
		}
		//对抛出的异常进行处理
		catch(Exception  e1){
		}
	}
}

class CheckListCellRenderer extends JCheckBox implements ListCellRenderer 
{
	protected static Border m_noFocusBorder = new EmptyBorder(0, 0, 0, 0);

	public CheckListCellRenderer() {
		super();
		setOpaque(true);
		setBorder(m_noFocusBorder);
	}

	public Component getListCellRendererComponent(JList list, Object value, int index, boolean isSelected,
			boolean cellHasFocus) {
		setText(value.toString());

		setBackground(isSelected ? list.getSelectionBackground() : list.getBackground());
		setForeground(isSelected ? list.getSelectionForeground() : list.getForeground());

		InstallData data = (InstallData) value;
		setSelected(data.isSelected());

		setFont(list.getFont());
		setBorder((cellHasFocus) ? UIManager.getBorder("List.focusCellHighlightBorder ") : m_noFocusBorder);

		return this;
	}
}

class CheckListener implements MouseListener 
{
	protected CompStrategyDialog m_parent;
	protected JList comStrategyList;

	public CheckListener(CompStrategyDialog parent) {
		m_parent = parent;
		comStrategyList = parent.comStrategyList;
	}

	public void mouseClicked(MouseEvent e) {
		if (e.getX() < 20)
			doCheck();
	}

	public void mousePressed(MouseEvent e) {
	}

	public void mouseReleased(MouseEvent e) {
	}

	public void mouseEntered(MouseEvent e) {
	}

	public void mouseExited(MouseEvent e) {
	}

	public void keyTyped(KeyEvent e) {
	}

	public void keyReleased(KeyEvent e) {
	}
	protected void doCheck() 
	{
		int index = comStrategyList.getSelectedIndex();
		if (index < 0)
			return;
		InstallData data = (InstallData) comStrategyList.getModel().getElementAt(index);
		data.invertSelected();
		comStrategyList.repaint();
	}
}

class InstallData 
{
	protected int isbn;
	protected int m_type;
	protected boolean m_selected;
	private int type;

	public InstallData(int isbn, int size,int type) {
		this.isbn = isbn;
		m_type = size;
		m_selected = false;
		this.type=type;
	}
	
	public int getTypeOfBook()
	{
		return this.type;
	}
	
	public int getIsbn() {
		return isbn;
	}

	public int getSize() {
		return m_type;
	}

	public void setSelected(boolean selected) {
		m_selected = selected;
	}

	public void invertSelected() {
		m_selected = !m_selected;
	}

	public boolean isSelected() {
		return m_selected;
	}

	public String toString() {
		return "策略编号："+isbn + "     策略类型：" + m_type + "  ";
	}

}