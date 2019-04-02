package bookmanagementsystem;

public class CompositeBestForCustomer extends CompositeStrategy 
{
	public CompositeBestForCustomer(int isbnOfStrategy,String nameOfStrategy,int typeOfStrategy)
	{
		this.setIsbnOfStrategy(isbnOfStrategy);
		this.setNameOfStrategy(nameOfStrategy);
		this.setTypeOfStrategy(typeOfStrategy);
	}

	public double getSubTotal(SaleLineItem item) {
		double minSubPrice=Double.POSITIVE_INFINITY;
		double subPrice=0;
		if(this.strategies.size()==0)
		{
			return item.getProdSpec().getPrice()*item.getCopies();
		}
		for(int i=0;i<this.strategies.size();i++)
		{
			subPrice=this.strategies.get(i).getSubTotal(item);
			if(minSubPrice>subPrice)
			{
				minSubPrice=subPrice;
			}
		}
		return minSubPrice;
	}
}
