
public class Students {
	private	String courseName;
	private	int numberOfStudents;
	private	int[] points;
	private	char[] grades;
	private	char[] randomGrades;
	public Students(String courseName, int numberOfStudents) {
		this.courseName = courseName;
		this.numberOfStudents = numberOfStudents;
		this.grades = new char[numberOfStudents];
	}
	
	public void generatePoints(){
		this.points = new int[this.numberOfStudents];
		for ( int i =0; i<this.numberOfStudents; i++){
			this.points[i] = (int)(Math.random()*50) + 50;
		}
	}
	
	public void calculateGrades(){
		for( int i =0; i<this.numberOfStudents; i++){
			if (points[i] >=90)
				grades[i] = 'A';
			else if(points[i] >= 80 & points[i] <90)
				grades[i] = 'B';
			else if(points[i] >= 70 & points[i] <80)
				grades[i] = 'C';
			else if(points[i] >= 60 & points[i] <70)
				grades[i] = 'D';
			else if(points[i] >= 50 & points[i] <60)
				grades[i] = 'E';
			else if( points[i] < 50)
				grades[i] = 'F';
		}
//		displayGrades();
	}
	
	private void displayGrades(){
		System.out.println(this.courseName);
		for(int i = 0; i<this.numberOfStudents; i++){
			System.out.println("Student no.\t"+i+": Grade is\t"+this.grades[i]);
		}
	}
	
	public void generateRandomGrades(){
		this.randomGrades = new char[this.numberOfStudents];
		for(int i =0 ; i<this.numberOfStudents; i++){
			int random = (int)(Math.random() * 5) + 1;
			if(random == 1)
				randomGrades[i] = 'A';
			else if (random == 2)
				randomGrades[i] = 'B';
			else if (random == 3)
				randomGrades[i] = 'C';
			else if (random == 4)
				randomGrades[i] = 'D';
			else if (random == 5)
				randomGrades[i] = 'E';
			else if (random == 6)
				randomGrades[i] = 'F';
		}
	}
	
	public void displayGradesDetails(){
		String c = "correct";
		String nc = "not correct";
		int cnt = 0;
		for(int i =0; i<this.numberOfStudents; i++){
			if(grades[i] == randomGrades[i]){
			System.out.println("Student no.\t"+i+": Grade is\t"+this.grades[i]
					+" which is "+ c);
			}
			else{
				System.out.println("Student no.\t"+i+": Grade is\t"+this.grades[i]
						+" which is "+ nc);
				cnt += 1;
			}

		}
		System.out.println("Total "+ cnt+" students are wrongly graded");
	}
	
	public static void main(String[] args){
		Students is147=new Students("Introduction to Java Programming",24);
		is147.generatePoints();
		is147.calculateGrades();
		is147.generateRandomGrades();
		is147.displayGradesDetails();
	}
}
