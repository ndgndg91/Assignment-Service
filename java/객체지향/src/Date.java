
public class Date {
	private static int year = 2017;
	private static int month = 1;
	private static int day = 10;
	
	public enum Type {
		METERING, NOTICE
	}// checking the system state
	
	private static Type state; // Read meter or notice price
	
	public int getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	public int getMonth() {
		return month;
	}
	public void setMonth(int month) {
		this.month = month;
	}
	public int getDay() {
		return day;
	}
	public void setDay(int day) {
		this.day = day;
	}
	
	public static Type getState() {
		return state;
	}
	public void setState(Type state) {
		this.state = state;
	}
	
	
	@Override
	public String toString()
	{
		return String.format("%d. %d. %d", getYear(), getMonth(), getDay());
	}
	

}
