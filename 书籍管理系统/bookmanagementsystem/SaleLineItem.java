package bookmanagementsystem;

public class SaleLineItem 
{
	private int copies;
	private ProductSpecification prodSpec;
	private PricingStrategy strategy;
	//构造函数
	public SaleLineItem()
	{
		this(0,null,null);
	}
	
	public SaleLineItem(int copies,ProductSpecification prodSpec,PricingStrategy strategy)
	{
		this.copies=copies;
		this.prodSpec=prodSpec;
		this.strategy=strategy;
	}
	
	public ProductSpecification getProdSpec()
	{
		return this.prodSpec;
	}
	
	public int getCopies()
	{
		return this.copies;
	}
	
	public void setCopies(int copies)
	{
		this.copies=copies;
	}
	
	public void setStrategy(PricingStrategy strategy)
	{
		this.strategy=strategy;
	}
	
	public double getSubTotal()
	{
		if(this.strategy==null)
		{
			return this.prodSpec.getPrice()*this.copies;
		}
		else
		{
			return this.strategy.getSubTotal(this);
		}
	}
	
	public String toString()
	{
		return("商品名：\t"+this.getProdSpec().getTitle()+
				"\t单价：\t"+this.getProdSpec().getPrice()+
				"\t数量：\t"+this.copies+"\n");
	}
}
