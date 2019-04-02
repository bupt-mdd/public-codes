package bookmanagementsystem;

import java.util.ArrayList;

public class BookCatalogue 
{
	private ArrayList<BookSpecification> books=new ArrayList<BookSpecification>();
	
	public BookSpecification findBook(String isbn)
	{
		for(int i=0;i<books.size();i++)
		{
			if(books.get(i).getIsbn().equals(isbn))
			{
				return books.get(i);
			}
		}
		return null;
	}
	
	public ArrayList<BookSpecification> getBooks()
	{
		return this.books;
	}
	
	public boolean addBook(BookSpecification newBook)
	{
		for(int i=0;i<books.size();i++)
		{
			if(books.get(i).getIsbn().equals(newBook.getIsbn()))
			{
				return false;
			}
		}
		return books.add(newBook);
	}
}
