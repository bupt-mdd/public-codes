package bookmanagementsystem;

import java.util.ArrayList;
import java.util.Scanner;

public class Controller 
{
	static Controller instance;                 	//存放单子实例
	private BookCatalogue bookCatelogue=null;		//存放书本目录
	private Sale sale=null;						//存放一个销售的数据
	
	//构造函数
	private Controller()
	{
		bookCatelogue=new BookCatalogue();
		sale=new Sale();
	}
	
	//获得该control的实例
	public static synchronized Controller getInstance()
	{
		if(instance==null)
		{
			instance=new Controller();
		}
		return instance;
	}
	
	//返回所有的书本信息
	public ArrayList<BookSpecification> getBooks()
	{
		return this.bookCatelogue.getBooks();
	}	
	
	//按照书本的isbn号找书
	public BookSpecification findBook(String isbn)
	{
		return this.bookCatelogue.findBook(isbn);
	}
	
	//添加一条书本信息
	boolean addBook(String isbn,String name,double price,int type)
	{
		return this.bookCatelogue.addBook(new BookSpecification(isbn,name,price,type));
	}
	
	//添加一个物品到sale中
	void addItems(int copies ,String isbn,double price,String title,int type)
	{
		this.sale.buyThing(copies, isbn, price, title, type);
	}
	
	//获取单次消费的信息
	public Sale getSale()
	{
		return this.sale;
	}
	
	//移除单词消费的所有商品，清空购物车
	void removeAllItem()
	{
		this.sale.getItems().clear();
	}
	
	//编辑策略
	boolean editStrategy(int oldType,int type,PricingStrategy editStrategy)
	{
		return PricingStrategyFactory.getInstance().editStrategy(oldType,type, editStrategy);
	}
	
	//添加策略
	boolean addStrategy(int type,PricingStrategy newStrategy)
	{
		return PricingStrategyFactory.getInstance().addStrategy(type, newStrategy);
	}
	
	//删除策略
	public PricingStrategy deleteStrategy(int type)
	{
		return PricingStrategyFactory.getInstance().deleteStrategy(type);
	}
}
