package bookmanagementsystem;
import java.util.*;

public class Sale implements Subject 
{
	private ArrayList<Observer> observers=new ArrayList<Observer>();
	private ArrayList<SaleLineItem> items=null;
	private double totalMoney;
	
	public Sale()
	{
		items=new ArrayList<SaleLineItem>();
		totalMoney=0;
	}
	
	public ArrayList<SaleLineItem> getItems()
	{
		return this.items;
	}
	
	public void buyThing(int copies ,String isbn,double price,String title,int type)
	{
		boolean flag=false;
		ProductSpecification prodSpec =new ProductSpecification(isbn,price,title,type);
		PricingStrategy strategy=PricingStrategyFactory.getInstance().getPricingStrategy(type);
		for(int i=0;i<items.size();i++)
		{
			if(items.get(i).getProdSpec().getIsbn().equals(isbn))
			{
				flag=true;
				items.get(i).setCopies(items.get(i).getCopies()+copies);
			}
		}
		if(flag==false)
		{
			items.add(new SaleLineItem(copies,prodSpec,strategy));
		}		
	}
	//计算出所有商品的总价格
	public double getTotal()
	{
		totalMoney=0;
		for(int i=0;i<items.size();i++)
		{
			totalMoney+=items.get(i).getSubTotal();
		}
		return totalMoney;
	}
	
	public void printInf()
	{
		for(int i=0;i<items.size();i++)
		{
			System.out.print(items.get(i).toString());
		}
		System.out.print("打折后的总价格为："+this.getTotal());
	}

	public void notifyObservers()
	{
		for(int i=0;i<this.observers.size();i++)
		{
			this.observers.get(i).update(Controller.getInstance().getSale());
		}
	}
	
	public void removeObserver(Observer observer) 
	{	
		this.observers.remove(observer);
	}

	public void registerObserver(Observer observer) 
	{
		this.observers.add(observer);
	}
}
