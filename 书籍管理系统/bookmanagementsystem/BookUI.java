package bookmanagementsystem;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;

public class BookUI  extends JFrame implements WindowListener,ActionListener
{		
		private JFrame mainWindow;
		private DefaultTableModel bookModel = new DefaultTableModel(
	            new String[] { "�鱾���", "�鼮��", "�鼮�۸�", "�鼮����" }, 0);
		private JTable bookTable = new JTable(bookModel);
        private JScrollPane pane = new JScrollPane(bookTable);
        
        private JPanel ButtonPanel=new JPanel();
		private JButton addBookButton=new JButton("����鼮");
        
		public BookUI(JFrame mainWindow)
		{
			this.mainWindow=mainWindow;
			this.setTitle("�鼮��Ϣά��ϵͳ");
			
			add(pane, BorderLayout.CENTER);
		    this.ButtonPanel.setLayout(new GridLayout());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
			this.ButtonPanel.add(addBookButton);
			add(ButtonPanel,BorderLayout.SOUTH);
			
			//���ü���
			this.addBookButton.addActionListener(this);
			this.addWindowListener(this); 
			
			updateList();
			
			DefaultTableCellRenderer r =new   DefaultTableCellRenderer();   
			r.setHorizontalAlignment(JLabel.CENTER);   
			bookTable.setDefaultRenderer(Object.class,r);
			setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		    setSize(500,350);
		    setLocation(250,150);
	        setLocationRelativeTo(null);
		    setVisible(true);
		    
		}
		
		//�Լ����¼����д���
		public void actionPerformed(ActionEvent e)
		{
			if(e.getSource()==this.addBookButton)
			{
				AddBookDialog addBookUI=new AddBookDialog(this);
			}
		}
		
		
		public void updateList()
		{
			ArrayList<BookSpecification> books=Controller.getInstance().getBooks();
			
			while (bookModel.getRowCount() > 0) {
				bookModel.removeRow(0);
            }
			String[] nameOfType=new String[]{"�ǽ̲�������ͼ��","�̲���ͼ��","��������ͼ��","������ͼ��","����"};
			for (int i = 0; i < books.size(); i++) {
				bookModel.addRow(new Object[] { books.get(i).getIsbn(),books.get(i).getName(),books.get(i).getPrice(),nameOfType[books.get(i).getType()]});
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

		@Override
		public void windowClosing(WindowEvent e) {
			// TODO Auto-generated method stub
			mainWindow.setVisible(true);
				
		}
}
