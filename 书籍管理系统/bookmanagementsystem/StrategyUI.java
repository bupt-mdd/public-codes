package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.HashMap;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;
import javax.swing.text.html.HTMLDocument.Iterator;

public class StrategyUI   extends JFrame implements WindowListener,ActionListener
{
	private JFrame mainWindow;
	private DefaultTableModel strategyModel = new DefaultTableModel(
            new String[] { "���Ա��", "��������", "��������", "�����鼮" }, 0);
	private JTable strategyTable = new JTable(strategyModel);
    private JScrollPane pane = new JScrollPane(strategyTable);
    
    private JMenuBar bar = new JMenuBar();
    private JMenu strategyMenu=new JMenu("���");
	
	private JMenuItem addSimpleStripe=new JMenuItem("�򵥲���");
	private JMenuItem addCompositionStripe=new JMenuItem("���Ӳ���");	
	
	private JPanel ButtonPanel=new JPanel();
	private JButton deleteStrategyButton=new JButton("ɾ������");
	private JButton editStrategyButton=new JButton("�༭����");
    
	public StrategyUI(JFrame mainWindow)
	{
		this.mainWindow=mainWindow;
		this.setTitle("������Ϣά��ϵͳ");
		
		this.strategyMenu.add(addSimpleStripe);
		this.strategyMenu.add(addCompositionStripe);
		
		this.bar.add(strategyMenu);
		this.setJMenuBar(bar);
		add(pane, BorderLayout.CENTER);
	    this.ButtonPanel.setLayout(new GridLayout());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
		this.ButtonPanel.add(deleteStrategyButton);
		this.ButtonPanel.add(editStrategyButton);
		add(ButtonPanel,BorderLayout.SOUTH);
		
		//���ü���
		this.deleteStrategyButton.addActionListener(this);
		this.editStrategyButton.addActionListener(this);
		this.addSimpleStripe.addActionListener(this);
		this.addCompositionStripe.addActionListener(this);
		this.addWindowListener(this); 
		
		updateList();
		
		DefaultTableCellRenderer r =new DefaultTableCellRenderer();   
		r.setHorizontalAlignment(JLabel.CENTER);   
		strategyTable.setDefaultRenderer(Object.class,r);
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	    setSize(500,350);
	    setLocation(250,150);
        setLocationRelativeTo(null);
	    setVisible(true);
	    
	}
	
	//�Լ����¼����д���
	public void actionPerformed(ActionEvent e)
	{
		boolean flag=false;
		if(e.getSource()==this.deleteStrategyButton)
		{
			int indexStrategy=this.strategyTable.getSelectedRow();
			if(indexStrategy==-1)
			{
				JOptionPane.showMessageDialog(null, "��ǰ��û��ѡ�в��ԣ�����ɾ������ѡ����Ӧ�Ĳ�����","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
			}
			else
			{
				String indexName=strategyTable.getValueAt(indexStrategy, 3).toString();
				String key=mapKey(indexName);
				Controller.getInstance().deleteStrategy(Integer.parseInt(key));
				JOptionPane.showMessageDialog(null, "ɾ���ɹ�","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
			}
			this.updateList();
		}
		else if(e.getSource()==this.editStrategyButton)
		{
			flag=true;
			int indexStrategy=this.strategyTable.getSelectedRow();
			if(indexStrategy==-1)
			{
				JOptionPane.showMessageDialog(null, "��ǰ��û��ѡ�в��ԣ����ɱ༭����ѡ����Ӧ�Ĳ�����","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
			}
			else
			{
				if(strategyTable.getValueAt(indexStrategy, 2).toString().equals("��ϲ���"))
				{
					String indexName=strategyTable.getValueAt(indexStrategy, 3).toString();
					String key=mapKey(indexName);
					PricingStrategy editStrategy=PricingStrategyFactory.getInstance().getPricingStrategy(Integer.parseInt(key));
					CompStrategyDialog addStrategyUI=new CompStrategyDialog(Integer.parseInt(key),editStrategy,this,flag);
				}
				else
				{
					String indexName=strategyTable.getValueAt(indexStrategy, 3).toString();
					String key=mapKey(indexName);
					PricingStrategy editStrategy=PricingStrategyFactory.getInstance().getPricingStrategy(Integer.parseInt(key));
					SimpleStrategyDialog editStrategyUI=new SimpleStrategyDialog(Integer.parseInt(key),editStrategy,this,flag);
				}
			}	
		}
		else if(e.getSource()==this.addSimpleStripe)
		{
			flag=false;
			SimpleStrategyDialog addStrategyUI=new SimpleStrategyDialog(this,flag);
		}
		else if(e.getSource()==this.addCompositionStripe)
		{
			//��ϲ���
			flag=false;
			CompStrategyDialog addStrategyUI=new CompStrategyDialog(this,flag);
		}
	}
	
	String mapKey(String key)
	{
		if(key.equals("�ǽ̲�������ͼ��"))
		{
			key="0";
		}
		else if(key.equals("�̲���ͼ��"))
		{
			key="1";
		}
		else if(key.equals("��������ͼ��"))
		{
			key="2";
		}
		else if(key.equals("������ͼ��"))
		{
			key="3";
		}
		else
		{
			key="4";
		}
		return key;
	}
	
	public void updateList()
	{
		String[] nameOfBookType=new String[]{"�ǽ̲�������ͼ��","�̲���ͼ��","��������ͼ��","������ͼ��","����"};
		String[] nameOfStrategy=new String[]{"����ֵ�Ż�","�ٷֱ��ۿ�","��ϲ���"};
		
		HashMap<Integer,PricingStrategy> strategies=PricingStrategyFactory.getInstance().getStrategies();
		while (strategyModel.getRowCount() > 0) {
			strategyModel.removeRow(0);
        }
		
		PricingStrategy temp=null;
		java.util.Iterator<Integer> keys=strategies.keySet().iterator();
		int i=0;
		while(keys.hasNext())
		{
			i=keys.next();
			temp=strategies.get(i);
			strategyModel.addRow(new Object[] { temp.getIsbnOfStrategy(),temp.getNameOfStrategy(),nameOfStrategy[temp.getTypeOfStrategy()],nameOfBookType[i]});
		}
	}
	
	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosed(WindowEvent e) {
		//mainWindow.setVisible(true);	
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

	//@Override
	public void windowClosing(WindowEvent e) {
		mainWindow.setVisible(true);
	}
}
