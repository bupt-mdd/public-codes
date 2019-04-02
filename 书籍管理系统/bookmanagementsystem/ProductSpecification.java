package bookmanagementsystem;

public class ProductSpecification 
{
	private String isbn;
	private double price;
	private String title;
	private int type;
	//¹¹Ôìº¯Êý
	public ProductSpecification()
	{
		this("",0,"",0);
	}
	
	public ProductSpecification(String isbn,double price,String title,int type)
	{
		this.isbn=isbn;
		this.price=price;
		this.title=title;
		this.type=type;
	}
	
	public String getIsbn()
	{
		return this.isbn;
	}
	
	public String getTitle()
	{
		return this.title;
	}
	
	public int getTpye()
	{
		return this.type;
	}
	
	public double getPrice()
	{
		return price;
	}
}
