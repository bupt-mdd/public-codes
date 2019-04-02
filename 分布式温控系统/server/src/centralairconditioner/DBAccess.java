package centralairconditioner;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DBAccess 
{
	static DBAccess instance;                 	//存放单子实例
	
	private final String url="jdbc:sqlserver://localhost:1433; DatabaseName=DTCS";
	private final String userName="sa";
	private final String password="MDD95129";
	private Connection con=null;
	private Statement state=null;
	private ResultSet result=null;
	
	//加载驱动
	static 
	{
		try
		{
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		}
		catch(Exception ex)
		{
			System.out.println("数据库加载失败"+ex.getMessage());
		}
	}
	
	private DBAccess()
	{
		//
		creatConnection();
	}
	
	//链接数据库
	public boolean creatConnection()
	{
		try
		{
			this.con=DriverManager.getConnection(url,userName,password);
			this.con.setAutoCommit(true);
			System.out.println("连接成功");
			this.state=this.con.createStatement();
		}
		catch(SQLException e)
		{
			System.out.println(e.getMessage());
			System.out.println("creatConnectError!");
			this.con = null;
			this.state = null;
			return false;
		}
		return true;
	}
	//关闭连接
	public void closeConnect()
	{
		try
		{
			if(this.result!=null)
				this.result.close();
			if(this.state!=null)
				this.state.close();
			if(this.con!=null)
				this.con.close();
		}
		catch(SQLException e)
		{
			e.printStackTrace();
		}
	}
	
	public static synchronized DBAccess getInstance()
	{
		if(instance==null)
		{
			instance=new DBAccess();
		}
		return instance;
	}
	
	//执行sql语句
	public boolean exeSql(String sqlStr)
	{
		boolean temp = false;
		if(this.con == null) {
			temp = this.creatConnection();
			if(!temp)
				return false;
		}
		try
		{
			this.state.executeUpdate(sqlStr);
		}
		catch(SQLException e)
		{
			//e.printStackTrace();
			return false;
		}
		return true;
	}
	
	//查询并打印信息。
	public ResultSet selectInf(String sqlStr)
	{
		boolean temp = false;
		if(this.con == null) {
			temp = this.creatConnection();
			if(!temp)
				return null;
		}
		try 
		{
			this.result=this.state.executeQuery(sqlStr);
		} 
		catch (SQLException e) 
		{
			// TODO Auto-generated catch block
			// e.printStackTrace();
			this.result = null;
		}
		return result;
	}
}
