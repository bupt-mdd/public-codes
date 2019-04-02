package bookmanagementsystem;

public class SaleLineItem 
{
	private int copies;
	private ProductSpecification prodSpec;
	private PricingStrategy strategy;
	//���캯��
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
		return("��Ʒ����\t"+this.getProdSpec().getTitle()+
				"\t���ۣ�\t"+this.getProdSpec().getPrice()+
				"\t������\t"+this.copies+"\n");
	}
}
