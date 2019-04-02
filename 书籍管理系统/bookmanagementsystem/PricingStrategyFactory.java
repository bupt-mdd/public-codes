package bookmanagementsystem;
import java.util.*;


public class PricingStrategyFactory 
{
	static PricingStrategyFactory instance; 
	int isbn;
	private HashMap<Integer,PricingStrategy> strategies=null;
	
	private PricingStrategyFactory()
	{
		isbn=0;
		strategies=new HashMap<Integer,PricingStrategy>();
	}
	
	//提供工厂的实例
	public static synchronized PricingStrategyFactory getInstance()
	{
		if(instance==null)
		{
			instance=new PricingStrategyFactory();
		}
		return instance;
	}
	
	//将工厂类中维护的所欲策略返回
	HashMap<Integer,PricingStrategy> getStrategies()
	{
		return this.strategies;
	}
	
	//添加策略
	public boolean addStrategy(int type,PricingStrategy newStrategy)
	{
		if(this.strategies.containsKey(type))
		{
			return false;
		}
		else
		{
			newStrategy.setIsbnOfStrategy(++isbn);
			this.strategies.put(type, newStrategy);
			return true;
		}
	}
	
	//删除策略
	public PricingStrategy deleteStrategy(int type)
	{
		int oldIsbn=strategies.get(type).getIsbnOfStrategy();
		PricingStrategy temp=null;
		java.util.Iterator<Integer> keys=strategies.keySet().iterator();
		int i=0;
		while(keys.hasNext())
		{
			i=keys.next();
			temp=strategies.get(i);
			if(temp.getTypeOfStrategy()==2)
			{
				ArrayList<PricingStrategy> strArray=((CompositeBestForCustomer)temp).getArraystr();
				for(int j=0;j<strArray.size();j++)
				{
					if(strArray.get(j).getIsbnOfStrategy()==oldIsbn)
					{
						strArray.remove(j);
					}
				}
			}
		}
		return this.strategies.remove(type);
	}
	
	//通过书的类型来查找策略
	public PricingStrategy getPricingStrategy(int booktype)
	{
		if(this.strategies.containsKey(booktype))
		{
			return this.strategies.get(booktype);
		}
		else
		{
			return null;
		}
		
	}
	
	//编辑策略
	public boolean editStrategy(int oldType,int type,PricingStrategy editStrategy)
	{
		int oldIsbn=this.strategies.get(oldType).getIsbnOfStrategy();
		if(oldType==type)
		{
			this.strategies.remove(oldType);
			editStrategy.setIsbnOfStrategy(oldIsbn);
			updateCompStr(oldIsbn,editStrategy);		
			this.strategies.put(type, editStrategy);
			return true;
		}
		else if(this.strategies.containsKey(type))
		{
			return false;
		}
		else
		{
			this.strategies.remove(oldType);
			editStrategy.setIsbnOfStrategy(oldIsbn);
			updateCompStr(oldIsbn,editStrategy);
			this.strategies.put(type, editStrategy);
			return true;
		}
	}
	
	//当复杂策略内的子策略发生变化时，对复杂策略进行相应的更新
	void updateCompStr(int oldIsbn,PricingStrategy editStrategy)
	{
		PricingStrategy temp=null;
		java.util.Iterator<Integer> keys=strategies.keySet().iterator();
		int i=0;
		while(keys.hasNext())
		{
			i=keys.next();
			temp=strategies.get(i);
			if(temp.getTypeOfStrategy()==2)
			{
				boolean flag=false;
				ArrayList<PricingStrategy> strArray=((CompositeBestForCustomer)temp).getArraystr();
				for(int j=0;j<strArray.size();j++)
				{
					if(strArray.get(j).getIsbnOfStrategy()==oldIsbn)
					{
						strArray.remove(j);
						flag=true;
					}
				}
				if(flag)
				{
					strArray.add(editStrategy);
				}
			}
		}
	}
}
