package centralairconditioner;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.Map;

public class CentralConnectDemo {

	private MainUI mainWindow;
	private Hashtable readerTable;
	private Hashtable writerTable;
	
	private ArrayList roomIDList;
	private boolean running=true;                       //用于决定是否开始检测。
	private CentralController controller;
	
	public CentralConnectDemo(MainUI mainWindow,CentralController controller)
	{
		this.mainWindow=mainWindow;
		this.controller = controller;
		this.readerTable=new Hashtable();
		this.writerTable=new Hashtable();
		
		this.roomIDList=new ArrayList();	
		Thread mainThread=new Thread(new ServerListen());
		mainThread.start();
		Thread monitorThread=new Thread(new Monitor());
		monitorThread.start();
	}
	
	private class ServerListen implements Runnable{

		@Override
		public void run()
		{
			ServerSocket server = null;
			try 
			{
				server = new ServerSocket(6000);
			} 
			catch (IOException e1) 
			{
				//e1.printStackTrace();
			}
			System.out.println("开始监听");
			while(true)
			{
				try {
					Socket client=server.accept();
					PrintWriter write=new PrintWriter(client.getOutputStream());
					
					InputStreamReader streamReader=new InputStreamReader(client.getInputStream());
					BufferedReader reader=new BufferedReader(streamReader);
					String inf[]=reader.readLine().split(" ");
					if(inf[1].equals("1"))
					{
						if(roomIDList.contains(inf[0]))
						{
							write.println("NO");
							write.flush();
							write.close();
							reader.close();
							client.close();
						}
						else
						{
							roomIDList.add(inf[0]);
							String ackInf=mainWindow.getInitialInf();
							write.println("OK "+ackInf);
							write.flush();
							readerTable.put(inf[0], reader);
							writerTable.put(inf[0], write);
						}
					}
					else
					{
						write.println("OK");
						write.flush();
						Thread thread=new Thread(new DealWithReq(reader,write,inf[0]));
						thread.start();
					}
					
					System.out.println(client.getRemoteSocketAddress());
					System.out.println(roomIDList.get(0));
				} catch (Exception e) {
					//
				}
			}
		}	
	}
	
	public void startMonitor()
	{
		this.running=true;
	}
	
	public void stopMonitor()
	{
		this.running=false;
	}
	
	private synchronized void removeClient(String curRoomID)
	{
		if(roomIDList.contains(curRoomID))
		{
			roomIDList.remove(curRoomID);
			readerTable.remove(curRoomID);
			writerTable.remove(curRoomID);
			
		}
	}
	
	private String sendAndRecv(BufferedReader reader,PrintWriter writer,String request)throws Exception
	{
		String ack=null;
		writer.println(request);
		writer.flush();
		
		ack=reader.readLine();
		return ack;
	}
	
	private class DealWithReq implements Runnable
	{
		private BufferedReader reader;
		private PrintWriter write;
		private String curRoomID;
		
		public DealWithReq(BufferedReader reader,PrintWriter write,String curRoomID)
		{
			this.reader=reader;
			this.write=write;
			this.curRoomID=curRoomID;
		}
		
		@Override
		public void run() {
			// TODO Auto-generated method stub
			try
			{
				while(true)
				{
					try
					{
						String message=null;
						message=this.reader.readLine();
						
						String[] inf=message.split(" ");
						if(inf[0].equals("SD"))
						{
							this.write.println("OK");
							this.write.flush();
							try {
								this.reader.close();
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
							this.write.close();
							break;
						}
						else if(inf[0].equals("GIS"))      //get initial state
						{
							String ackInf=mainWindow.getInitialInf();
							this.write.println(ackInf);
							this.write.flush();
							//以上传输只是为了模拟而已。
							if(!controller.addOnOffTime(inf[1]))//统计开关次数
								System.out.println("write database error!");
						}
						else if(inf[0].equals("GC"))       //get charge
						{
							this.write.println(mainWindow.roomIDIndes.get(inf[1]).get(2));
							this.write.flush();
						}
						else if(inf[0].equals("AW"))       //adjust wind
						{
							this.write.println("OK");
							this.write.flush();
							if(!controller.addAdjustWind(inf[2]))//统计调风次数
								System.out.println("write database error!");
						}
						else if(inf[0].equals("AT"))       //adjust temp 格式:"AT 目标温度 当前温度 当前风速 房间号"
						{
							this.write.println("OK");
							this.write.flush();
							if(!controller.addAdjustTempTime(inf[4])) {//统计调温次数	
								System.out.println("write database error!");
							}
							else {
								Thread thread1 = new Thread(new RealTimeAdjustTemp(
										inf[4],Integer.parseInt(inf[2]),Integer.parseInt(inf[1]),Integer.parseInt(inf[3])));
								thread1.start();
							}
						}
					}
					catch(Exception e)
					{
						removeClient(curRoomID);
						break;
					}
				}
			}
			catch(Exception e)
			{
				removeClient(curRoomID);
				return;
			}
		}	
	}
	
	private class RealTimeAdjustTemp implements Runnable{
		
		private BufferedReader reader;
		private PrintWriter write;
		private String curRoomID;
		private int curTemp;
		private int aimTemp;
		private int curWindSpeed;
		private String startTime;
		private String endTime;
		private DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//时间格式
		
		public RealTimeAdjustTemp(String curRoomID,int curTemp,int aimTemp,int curWindSpeed)
		{
			this.reader=(BufferedReader)readerTable.get(curRoomID);
			this.write=(PrintWriter)writerTable.get(curRoomID);
			this.curRoomID=curRoomID;
			this.curTemp = curTemp;
			this.aimTemp = aimTemp;
			this.curWindSpeed = curWindSpeed;
			this.startTime = df.format(new Date());
			//System.out.println("st"+startTime);
		}
		
		@Override
		public void run() {
			// TODO Auto-generated method stub
			int changeTemp = Math.abs(this.aimTemp - this.curTemp);
			while(true){
				//System.out.println(changeTemp);
				try {
					switch(curWindSpeed){
					case 0:{
						Thread.sleep(3000);
						write.println("CT");
						write.flush();
						changeTemp--;
						break;
					}
					case 1:{
						Thread.sleep(2000);
						write.println("CT");
						write.flush();
						changeTemp--;
						break;
					}
					case 2:{
						Thread.sleep(1000);
						write.println("CT");
						write.flush();
						changeTemp--;
						break;
					}
					}
					if(changeTemp == 0){
						this.endTime = df.format(new Date());
						double count =  countATCharge(curTemp, aimTemp, curWindSpeed);
						if(!controller.adjustTem(curRoomID, startTime, endTime, curTemp, aimTemp, curWindSpeed, count))
							System.out.println("write database error!");
						if(!controller.addExpense(curRoomID,count))//记录报表中的费用
							System.out.println("write database error!");
						break;
					}
					
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
			}
		}
		
	}
	
	private double countATCharge(int curTemp,int aimTemp,int curWindSpeed){//计费函数 ,计算一次调温请求过程的费用:
		//高速风1度/分钟 、中速风1度/2分钟、低速风1度/3分钟，低速0.75功率/分钟,中速1功率/分钟，高速1.25功率/分钟 、1元/度
		double count = 0;
		int time = 0;
		time = (Math.abs(curTemp-aimTemp))*(3-curWindSpeed);
		switch(curWindSpeed){
		case 0:{
			count = time*0.75;
			break;
		}
		case 1:{
			count = time;
		}
		case 2:{
			count = time*1.25;
		}
		}
		return  count;
	}
	
	private class Monitor implements Runnable
	{
		BufferedReader reader;
		PrintWriter writer;
		String request=null;
		String roomID=null;
		
		@Override
		public void run() {
			// TODO Auto-generated method stub
			try
			{
				while(true)
				{
					try {
						Thread.sleep(200);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					if(running)
					{
						try{
							for(Iterator entity=readerTable.entrySet().iterator();entity.hasNext();)
							{
								Map.Entry one=(Map.Entry)entity.next();
								request="GS";             //get state
								roomID=(String)one.getKey();
								reader=(BufferedReader)readerTable.get(roomID);
								writer=(PrintWriter)writerTable.get(roomID);
								String ackInf=sendAndRecv(reader,writer,request);
								mainWindow.updateAllRommState(roomID,ackInf);					//刷新显示个房间的状态
							}
						}
						catch(Exception e)
						{
							removeClient(roomID);
							mainWindow.removeClientInTable();
							//e.printStackTrace();
						}
					}
				}
			}
			catch(Exception e)
			{
				removeClient(roomID);
				mainWindow.removeClientInTable();
				//e.printStackTrace();
			}	
		}
		
		
	}
}
