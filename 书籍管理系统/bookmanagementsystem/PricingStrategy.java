package bookmanagementsystem;

public abstract class PricingStrategy 
{
	private int isbnOfStrategy;
	private String nameOfStrategy;
	private int typeOfStrategy;
	
	public void setIsbnOfStrategy(int isbnOfStrategy)
	{
		this.isbnOfStrategy=isbnOfStrategy;
	}
	
	public void setNameOfStrategy(String nameOfStrategy)
	{
		this.nameOfStrategy=nameOfStrategy;
	}
	
	public void setTypeOfStrategy(int typeOfStrategy)
	{
		this.typeOfStrategy=typeOfStrategy;
	}
	/*
	public void setTypeOfBook(int typeOfBook)
	{
		this.typeOfBook=typeOfBook;
	}*/
	public int getIsbnOfStrategy()
	{
		return this.isbnOfStrategy;
	}
	
	public String getNameOfStrategy()
	{
		return this.nameOfStrategy;
	}
	
	public int getTypeOfStrategy()
	{
		return this.typeOfStrategy;
	}

	public abstract double getSubTotal(SaleLineItem item);
}
