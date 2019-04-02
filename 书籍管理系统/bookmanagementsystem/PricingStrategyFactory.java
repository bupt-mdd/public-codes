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
	
	//�ṩ������ʵ��
	public static synchronized PricingStrategyFactory getInstance()
	{
		if(instance==null)
		{
			instance=new PricingStrategyFactory();
		}
		return instance;
	}
	
	//����������ά�����������Է���
	HashMap<Integer,PricingStrategy> getStrategies()
	{
		return this.strategies;
	}
	
	//��Ӳ���
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
	
	//ɾ������
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
	
	//ͨ��������������Ҳ���
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
	
	//�༭����
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
	
	//�����Ӳ����ڵ��Ӳ��Է����仯ʱ���Ը��Ӳ��Խ�����Ӧ�ĸ���
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
