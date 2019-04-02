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
	            new String[] { "书本编号", "书籍名", "书籍价格", "书籍类型" }, 0);
		private JTable bookTable = new JTable(bookModel);
        private JScrollPane pane = new JScrollPane(bookTable);
        
        private JPanel ButtonPanel=new JPanel();
		private JButton addBookButton=new JButton("添加书籍");
        
		public BookUI(JFrame mainWindow)
		{
			this.mainWindow=mainWindow;
			this.setTitle("书籍信息维护系统");
			
			add(pane, BorderLayout.CENTER);
		    this.ButtonPanel.setLayout(new GridLayout());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
		    this.ButtonPanel.add(new JPanel());
			this.ButtonPanel.add(addBookButton);
			add(ButtonPanel,BorderLayout.SOUTH);
			
			//设置监听
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
		
		//对监听事件进行处理
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
			String[] nameOfType=new String[]{"非教材类计算机图书","教材类图书","连环画类图书","养生类图书","其他"};
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
