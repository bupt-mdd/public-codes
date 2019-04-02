package bookmanagementsystem;

public class BookSpecification 
{
	String isbn;
	String name;
	double price;
	int type;
	//int number;
	
	public BookSpecification(String isbn,String name,double price,int type)
	{
		this.isbn=isbn;
		this.name=name;
		this.price=price;
		this.type=type;
	}
	
	public BookSpecification()
	{
		this("","",0,0);
	}
	
	public double getPrice()
	{
		return this.price;
	}
	
	public String getName()
	{
		return this.name;
	}
	
	public String getIsbn()
	{
		return this.isbn;
	}
	
	public int getType()
	{
		return this.type;
	}
}
