package bookmanagementsystem;

public class PercentageStrategy extends PricingStrategy
{
	private double discountPercentage;
	//¹¹Ôìº¯Êý
	public PercentageStrategy()
	{
		this(0,"",0,0);
	}
	
	public PercentageStrategy(int isbnOfStrategy,String nameOfStrategy,
			int typeOfStrategy,double discountPercentage)
	{
		this.setIsbnOfStrategy(isbnOfStrategy);
		this.setNameOfStrategy(nameOfStrategy);
		this.setTypeOfStrategy(typeOfStrategy);
		this.discountPercentage=discountPercentage;
	}
	
	public double getDiscount()
	{
		return this.discountPercentage;
	}
	
	public double getSubTotal(SaleLineItem item)
	{
		return item.getCopies()*item.getProdSpec().getPrice()*(1-discountPercentage);
	}
}
