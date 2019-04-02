package bookmanagementsystem;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;

public class BuyUI   extends JFrame implements WindowListener,ActionListener
{
	ArrayList<BookSpecification> books=null;
	
	private JFrame mainWindow;
	private DefaultTableModel bookModel = new DefaultTableModel(
            new String[] { "�鼮���", "�鼮����", "�鼮�۸�", "�鼮����" }, 0);
	String[] nameOfBookType=new String[]{"�ǽ̲�������ͼ��","�̲���ͼ��","��������ͼ��","������ͼ��","����"};
	private JTable bookTable = new JTable(bookModel);
    private JScrollPane pane = new JScrollPane(bookTable);
    
    private JPanel ButtonPanel=new JPanel();
	private JButton buyButton=new JButton("���빺�ﳵ");
	private JButton resetButton=new JButton("��չ��ﳵ");
	private JTextField isbnText=new JTextField(10);
	private JTextField countText=new JTextField(10);
	private JLabel infLabel=new JLabel("��Ʒ��ţ�");
	private JLabel countLabel=new JLabel("������");
	private ShoppingCarUI ShoppingCarUI=new ShoppingCarUI();
	public BuyUI(JFrame mianWindow)
	{
		this.mainWindow=mianWindow;
		this.books=Controller.getInstance().getBooks();
		
		this.setTitle("��Ʒѡ�����");
		add(pane, BorderLayout.CENTER);
	    this.ButtonPanel.setLayout(new FlowLayout());
	    this.ButtonPanel.add(infLabel);
	    this.ButtonPanel.add(isbnText);
	    this.ButtonPanel.add(countLabel);
	    this.ButtonPanel.add(countText);
	    this.ButtonPanel.add(buyButton);
		this.ButtonPanel.add(resetButton);
		add(ButtonPanel,BorderLayout.SOUTH);
		
		Controller.getInstance().getSale().registerObserver(ShoppingCarUI);
		
		//���ü���
		this.addWindowListener(this); 
		this.buyButton.addActionListener(this);
		this.resetButton.addActionListener(this);
		
		DefaultTableCellRenderer r =new DefaultTableCellRenderer();   
		r.setHorizontalAlignment(JLabel.CENTER);   
		bookTable.setDefaultRenderer(Object.class,r);
		
		while (bookModel.getRowCount() > 0) {
			bookModel.removeRow(0);
        }
		for (int i = 0; i < books.size(); i++) {
			bookModel.addRow(new Object[] { books.get(i).getIsbn(),books.get(i).getName(),books.get(i).getPrice(),nameOfBookType[books.get(i).getType()]});
        }
		
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	    setSize(600,350);
	    setLocation(200,150);
	    setVisible(true);
	}

	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==this.buyButton)
		{
			try
			{
				String isbn=this.isbnText.getText();
				int copies=Integer.parseInt(this.countText.getText());
				BookSpecification bookSpec=Controller.getInstance().findBook(isbn);
				if(bookSpec==null)
				{
					JOptionPane.showMessageDialog(null, "�����ڸ��鼮��������ѡ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.isbnText.setText("");
					this.countText.setText("");
					this.isbnText.requestFocus();
				}
				else
				{
					Controller.getInstance().addItems(copies, bookSpec.getIsbn(), bookSpec.getPrice(), bookSpec.getName(), bookSpec.getType());
					this.isbnText.setText("");
					this.countText.setText("");
					this.isbnText.requestFocus();
					Controller.getInstance().getSale().notifyObservers();
				}
			}
			//���׳����쳣���д���
			catch(Exception  e1)
			{
				if(this.isbnText.getText().equals(""))
				{
					JOptionPane.showMessageDialog(null, "������Ҫ������鼮���","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.isbnText.requestFocus();
				}
				else if(this.countText.getText().equals(""))
				{
					JOptionPane.showMessageDialog(null, "������鱾��������Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.countText.requestFocus();
				}
				else if(!countText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{
					JOptionPane.showMessageDialog(null, "������鱾��������Ϊ����","��Ϣ",JOptionPane.WARNING_MESSAGE);
					this.countText.setText("");
					this.countText.requestFocus();
				}
			}
		}
		else if(e.getSource()==this.resetButton)
		{
			Controller.getInstance().removeAllItem();
			Controller.getInstance().getSale().notifyObservers();
		}
	}
	
	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowClosed(WindowEvent e) {	
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
		Controller.getInstance().removeAllItem();
		this.ShoppingCarUI.dispose();
		mainWindow.setVisible(true);		
	}
}
