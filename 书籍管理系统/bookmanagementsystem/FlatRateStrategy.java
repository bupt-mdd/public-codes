package bookmanagementsystem;

public class FlatRateStrategy extends PricingStrategy
{
	private double discountPerBook;
	//¹¹Ôìº¯Êý
	public FlatRateStrategy()
	{
		this(0,"",0,0);
	}
	
	public FlatRateStrategy(int isbnOfStrategy,String nameOfStrategy,
			int typeOfStrategy,double discountPerBook)
	{
		this.setIsbnOfStrategy(isbnOfStrategy);
		this.setNameOfStrategy(nameOfStrategy);
		this.setTypeOfStrategy(typeOfStrategy);
		this.discountPerBook=discountPerBook;
	}
	
	public double getDiscount()
	{
		return this.discountPerBook;
	}
	
	public double getSubTotal(SaleLineItem item)
	{
		return item.getCopies()*(item.getProdSpec().getPrice()-discountPerBook);
	}
}
