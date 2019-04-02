package bookmanagementsystem;

import java.util.ArrayList;

public abstract class CompositeStrategy extends PricingStrategy
{
	public ArrayList<PricingStrategy> strategies=new ArrayList<PricingStrategy>();
	
	public ArrayList<PricingStrategy>getArraystr()
	{
		return this.strategies;
	}
	
	public void add(PricingStrategy NewStrategy)
	{
		this.strategies.add(NewStrategy);
	}
}
