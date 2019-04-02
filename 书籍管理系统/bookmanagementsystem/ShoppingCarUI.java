package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.HashMap;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;

public class ShoppingCarUI   extends JDialog implements ActionListener,Observer
{

	private DefaultTableModel bookModel = new DefaultTableModel(
            new String[] { "�鼮����", "����","����" }, 0);
	private JTable bookTable = new JTable(bookModel);
    private JScrollPane pane = new JScrollPane(bookTable);
	
	private JPanel ButtonPanel=new JPanel();
	private JLabel infLabel=new JLabel("�ܼ�Ϊ��");
	private JLabel totalPticeLabel=new JLabel("");
    
	public ShoppingCarUI()
	{
		this.setTitle("������Ʒ��Ϣ����");
		
		add(pane, BorderLayout.CENTER);
	    this.ButtonPanel.setLayout(new GridLayout());
	    this.ButtonPanel.add(infLabel);
	    this.ButtonPanel.add(totalPticeLabel);
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
	    this.ButtonPanel.add(new JPanel());
		add(ButtonPanel,BorderLayout.SOUTH);
		
		//���ü���
		
		DefaultTableCellRenderer r =new DefaultTableCellRenderer();   
		r.setHorizontalAlignment(JLabel.CENTER);   
		bookTable.setDefaultRenderer(Object.class,r);
		setDefaultCloseOperation(0);
		setSize(500,350);
	    setLocation(800,150);
	    setVisible(true);
	    
	}
	
	//�Լ����¼����д���
	
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}

	public void update(Sale sale) 
	{
		ArrayList<SaleLineItem> items=sale.getItems();
		while (bookModel.getRowCount() > 0) {
			bookModel.removeRow(0);
        }
		for (int i = 0; i < items.size(); i++) {
			bookModel.addRow(new Object[] { items.get(i).getProdSpec().getTitle(),items.get(i).getCopies(),items.get(i).getProdSpec().getPrice()});
        }
		this.totalPticeLabel.setText(String.valueOf(sale.getTotal()));
	}
}
