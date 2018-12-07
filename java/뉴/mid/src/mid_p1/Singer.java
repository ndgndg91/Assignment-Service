package mid_p1;
public class Singer {
	private String name;
	private String birthdate; 
	private String entertainment;
	private double income;
	
	public Singer(String name, String birthdate, String entertainment) {
		this.name = name;
		this.birthdate = birthdate;
		this.entertainment = entertainment;
	}

	public String getName() {
		return name;
	}

	public String getBirthdate() {
		return birthdate;
	}

	public String getEntertainment() {
		return entertainment;
	}
	
	public double calculate(){
		return income;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "°¡¼ö/"+getName()+"/"+getBirthdate()+"/"+getEntertainment();
	}
}
