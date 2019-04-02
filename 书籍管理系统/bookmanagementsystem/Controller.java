package bookmanagementsystem;

import java.util.ArrayList;
import java.util.Scanner;

public class Controller 
{
	static Controller instance;                 	//��ŵ���ʵ��
	private BookCatalogue bookCatelogue=null;		//����鱾Ŀ¼
	private Sale sale=null;						//���һ�����۵�����
	
	//���캯��
	private Controller()
	{
		bookCatelogue=new BookCatalogue();
		sale=new Sale();
	}
	
	//��ø�control��ʵ��
	public static synchronized Controller getInstance()
	{
		if(instance==null)
		{
			instance=new Controller();
		}
		return instance;
	}
	
	//�������е��鱾��Ϣ
	public ArrayList<BookSpecification> getBooks()
	{
		return this.bookCatelogue.getBooks();
	}	
	
	//�����鱾��isbn������
	public BookSpecification findBook(String isbn)
	{
		return this.bookCatelogue.findBook(isbn);
	}
	
	//���һ���鱾��Ϣ
	boolean addBook(String isbn,String name,double price,int type)
	{
		return this.bookCatelogue.addBook(new BookSpecification(isbn,name,price,type));
	}
	
	//���һ����Ʒ��sale��
	void addItems(int copies ,String isbn,double price,String title,int type)
	{
		this.sale.buyThing(copies, isbn, price, title, type);
	}
	
	//��ȡ�������ѵ���Ϣ
	public Sale getSale()
	{
		return this.sale;
	}
	
	//�Ƴ��������ѵ�������Ʒ����չ��ﳵ
	void removeAllItem()
	{
		this.sale.getItems().clear();
	}
	
	//�༭����
	boolean editStrategy(int oldType,int type,PricingStrategy editStrategy)
	{
		return PricingStrategyFactory.getInstance().editStrategy(oldType,type, editStrategy);
	}
	
	//��Ӳ���
	boolean addStrategy(int type,PricingStrategy newStrategy)
	{
		return PricingStrategyFactory.getInstance().addStrategy(type, newStrategy);
	}
	
	//ɾ������
	public PricingStrategy deleteStrategy(int type)
	{
		return PricingStrategyFactory.getInstance().deleteStrategy(type);
	}
}
