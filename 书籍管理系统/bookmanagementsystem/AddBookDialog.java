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
	//���dialog������,����Ա��������¼��ı���Ҳ��ͬ
	private JLabel isbnLabel=new JLabel("��� �� ");
	private JLabel titleLabel=new JLabel("���� �� ");
	private JLabel priceLabel=new JLabel("�۸� �� ");
	private JLabel typeLabel=new JLabel("���� �� ");
	
	private JComboBox typeOfBookBox = new JComboBox (new String[]{"�ǽ̲�������ͼ��","�̲���ͼ��",
			"��������ͼ��","������ͼ��","����"});
	//����������
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
		//�������������Ű����
		this.mainWindow=bookUI;
		this.typeOfBookBox.setPreferredSize(new Dimension(224,24));
		
		this.setTitle("¼���鱾��Ϣ");
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
			
		//������panel����dialog��
		this.setLayout(new FlowLayout());
		this.add(this.isbnPanel);
		this.add(this.titlePanel);
		this.add(this.typePanel);
		this.add(this.pricePanel);
		this.add(this.ButtonPanel);
		
		this.setSize(320,180);
		this.add(this.ButtonPanel);				
		
		this.setResizable(false);     //�̶���С
		this.setVisible(true);
			
		//���ü���
		this.okButton.addActionListener(this);
		this.resetButton.addActionListener(this);	
	} 
		
	public void actionPerformed(ActionEvent e)
	{
		if(e.getSource()==okButton)
		{	
			try
			{
				//��ȡ���ڵ�����
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
					JOptionPane.showMessageDialog(null, "���ʧ�ܣ��Ѿ����ڸ��鱾����Ϣ","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
				}
				this.mainWindow.updateList();
				
			}
			//���׳����쳣���д���
			catch(Exception  e1)
			{
				//��������Ϊ��ʱ�򣬻��׳��쳣���ֱ���д���
				if(isbn.equals(""))
				{
					JOptionPane.showMessageDialog(null, "�鱾��Ų���Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.isbnText.requestFocus();
				}
				else if(title.equals(""))
				{
					JOptionPane.showMessageDialog(null, "�鼮���Ʋ���Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.titleText.requestFocus();
				}
				else if(priceText.getText().equals(""))
				{
					JOptionPane.showMessageDialog(null, "�鼮�۸���Ϊ��","��Ϣ",JOptionPane.INFORMATION_MESSAGE);
					this.priceText.requestFocus();
				}
				else if(!priceText.getText().matches("^[-+]?(([0-9]+)([.]([0-9]+))?|([.]([0-9]+))?)$"))
				{   //������ת��Ϊ����ʱ��Ҳ���׳��쳣��������ʽ�ж�
					JOptionPane.showMessageDialog(null, "�鼮�۸����������","����",JOptionPane.WARNING_MESSAGE);
					this.priceText.setText("");
					this.priceText.requestFocus();
				}
			}
		}
		//��ո������ڵ�����
		else if(e.getSource()==resetButton)
		{
			this.isbnText.setText("");
			this.titleText.setText("");
			this.typeOfBookBox.setSelectedIndex(0);
			this.priceText.setText("");
		}
	}
}
