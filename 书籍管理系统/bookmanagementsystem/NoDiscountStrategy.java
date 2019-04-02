package bookmanagementsystem;

public class NoDiscountStrategy extends PricingStrategy 
{
	public double getSubTotal(SaleLineItem item)
	{
		return item.getProdSpec().getPrice()*item.getCopies();
	}
}
