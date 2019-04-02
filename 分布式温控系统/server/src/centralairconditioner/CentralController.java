package centralairconditioner;

import java.sql.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JOptionPane;
import javax.swing.JTable;

public class CentralController {

    private String[] windSpeed= {"低速","中速","高速 "};
	public boolean showSpecification(Specification spe)  {
		// TODO Auto-generated method stub
		ResultSet rst = null; 
		String sqlStr = "select * from AirConditionerInfo order by StartTime, RoomNum";
		rst = DBAccess.getInstance().selectInf(sqlStr);
		if(rst == null)
			return false;
		try {
			while(rst.next()){
				spe.insertData( rst.getString(1), rst.getString(2), 
						rst.getString(3), rst.getInt(4), rst.getInt(5), 
						     windSpeed[rst.getInt(6)], rst.getDouble(7));
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			return false;
		}
		return true;
	}
	
	public boolean adjustTem(String roomNum,String startTime,String endTime,int curTemp, 
		int aimTemp, int curWind,double charge) {//将调温过程写入数据库
		// TODO Auto-generated method stub
		ResultSet rst = null;
		String sqlStr = "insert into AirConditionerInfo values('"+roomNum+"','"+startTime+
				"','"+endTime+"',"+curTemp+","+aimTemp+","+curWind+","+charge+")";
		return DBAccess.getInstance().exeSql(sqlStr);
	}
	
	public boolean showDayChart(Chart chart,String date) {
		// TODO Auto-generated method stub
		ResultSet rst = null; 
		String sqlStr = "select * from Chart where Dates = '"+date+"'";
		rst = DBAccess.getInstance().selectInf(sqlStr);
		if(rst == null)
			return false;
		try {
			while(rst.next()){
				chart.insertData( rst.getString(1), rst.getDouble(3), 
						rst.getInt(4), rst.getInt(5), rst.getInt(6), 
						      rst.getInt(7));
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			return false;
		}
		return true;
	}
	
	public boolean showMonthChart(Chart chart, String year, int month) {
		// TODO Auto-generated method stub
		ResultSet rst = null; 
		String sqlStr = "select * from Chart where DATEDIFF(MONTH,Dates,'"+year+"-"+month+"-01')=0";
		rst = DBAccess.getInstance().selectInf(sqlStr);
		if(rst == null)
			return false;
		try {
			while(rst.next()){
				chart.insertData( rst.getString(1), rst.getDouble(3), 
						rst.getInt(4), rst.getInt(5), rst.getInt(6), 
						      rst.getInt(7));
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			return false;
		}
		return true;
	}
	
	public boolean showYearChart(Chart chart, String year) {
		// TODO Auto-generated method stub
		ResultSet rst = null; 
		String sqlStr = "select * from Chart where DATEDIFF(YEAR,Dates,'"+year+"-01-01')=0";
		rst = DBAccess.getInstance().selectInf(sqlStr);
		if(rst == null)
			return false;
		try {
			while(rst.next()){
				chart.insertData( rst.getString(1), rst.getDouble(3), 
						rst.getInt(4), rst.getInt(5), rst.getInt(6), 
						      rst.getInt(7));
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			return false;
		}
		return true;
	}
	
	public boolean addOnOffTime(String roomNum) {
		// TODO Auto-generated method stub
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");//时间格式
		String nowTime = df.format(new Date());
		ResultSet rst = null;
		String sqlStr = "if not exists(select * from Chart where RoomNum = '"+roomNum+"'and Dates = '"+
		          nowTime+"')insert into Chart values('"+roomNum+"','"+nowTime+"',0,0,0,0,0) update "
		          		+ "Chart set OnOffTime = OnOffTime +1 where RoomNum = '"+roomNum+"'and Dates = '"+nowTime+"'";
		return DBAccess.getInstance().exeSql(sqlStr);
	}
	
	public boolean addAdjustWind(String roomNum) {
		// TODO Auto-generated method stub
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");//时间格式
		String nowTime = df.format(new Date());
		ResultSet rst = null;
		String sqlStr = "if not exists(select * from Chart where RoomNum = '"+roomNum+"'and Dates = '"+
		          nowTime+"')insert into Chart values('"+roomNum+"','"+nowTime+"',0,0,0,0,0) update "
		          		+ "Chart set AdjustWindTime = AdjustWindTime +1 where RoomNum = '"+roomNum+"'and"
		          				+ " Dates = '"+nowTime+"'update Chart set DispatchTime = DispatchTime +1 "
		          						+ "where RoomNum = '"+roomNum+"'and Dates = '"+nowTime+"'";
		return DBAccess.getInstance().exeSql(sqlStr);
	}
	
	public boolean addAdjustTempTime(String roomNum) {
		// TODO Auto-generated method stub
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");//时间格式
		String nowTime = df.format(new Date());
		ResultSet rst = null;
		String sqlStr = "if not exists(select * from Chart where RoomNum = '"+roomNum+"'and Dates = '"+
		          nowTime+"')insert into Chart values('"+roomNum+"','"+nowTime+"',0,0,0,0,0) update "
		          		+ "Chart set AdjustTempTime = AdjustTempTime +1 where RoomNum = '"+roomNum+"'and "
		          				+ "Dates = '"+nowTime+"'update Chart set DispatchTime = DispatchTime +1 "
		          						+ "where RoomNum = '"+roomNum+"'and Dates = '"+nowTime+"'";
		return DBAccess.getInstance().exeSql(sqlStr);
	}
	
	public boolean addExpense(String roomNum, double count) {
		// TODO Auto-generated method stub
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");//时间格式
		String nowTime = df.format(new Date());
		ResultSet rst = null;
		String sqlStr = "if not exists(select * from Chart where RoomNum = '"+roomNum+"'and Dates = '"+
		          nowTime+"')insert into Chart values('"+roomNum+"','"+nowTime+"',0,0,0,0,0) update "
		          		+ "Chart set Expense = Expense +"+count+"where RoomNum = '"+roomNum+"'and Dates = '"+nowTime+"'";
		return DBAccess.getInstance().exeSql(sqlStr);
	}
	
	public Double countExpense(String start, String end, String roomNum) {
		// TODO Auto-generated method stub
		ResultSet rst = null;
		Double count = null;
		String sqlStr = "select count(Expense) from AirConditionerInfo where RoomNum = '"+roomNum+"'and StartTime > '"+start+
				"'and EndTime < '"+end+ "'";
		rst = DBAccess.getInstance().selectInf(sqlStr);
		if(rst == null)
			return null;
		try {
			while(rst.next()){count = rst.getDouble(1);}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
		return count;
	}
	

}
