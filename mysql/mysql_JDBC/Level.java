package mysql_JDBC;

import java.util.ArrayList;

public class Level {
	private ArrayList<String> level1;
	private ArrayList<String> level2;
	private ArrayList<String> level3;
	private ArrayList<String> level4;
	private ArrayList<String> level5;
	private ArrayList<String> level6;
	private ArrayList<String> level7;
	private ArrayList<String> level8;
	private ArrayList<String> level9;
	public ArrayList<String> getLevel1() {
		if(this.level1 == null) {
			this.level1 = new ArrayList<>();
		}
		return level1;
	}
	public ArrayList<String> getLevel2() {
		if(this.level2 == null) {
			this.level2 = new ArrayList<>();
		}
		return level2;
	}
	public ArrayList<String> getLevel3() {
		if(this.level3 == null) {
			this.level3 = new ArrayList<>();
		}
		return level3;
	}
	public ArrayList<String> getLevel4() {
		if(this.level4 == null) {
			this.level4 = new ArrayList<>();
		}
		return level4;
	}
	public ArrayList<String> getLevel5() {
		if(this.level5 == null) {
			this.level5 = new ArrayList<>();
		}
		return level5;
	}
	public ArrayList<String> getLevel6() {
		if(this.level6 == null) {
			this.level6 = new ArrayList<>();
		}
		return level6;
	}
	public ArrayList<String> getLevel7() {
		if(this.level7 == null) {
			this.level7 = new ArrayList<>();
		}
		return level7;
	}
	public ArrayList<String> getLevel8() {
		if(this.level8 == null) {
			this.level8 = new ArrayList<>();
		}
		return level8;
	}
	public ArrayList<String> getLevel9() {
		if(this.level9 == null) {
			this.level9 = new ArrayList<>();
		}
		return level9;
	}
	public static void printLevel(ArrayList<String> input, int level) {
		int i = 0;
		while (i < input.size()) {
			System.out.println(input.get(i) + " at level " + String.valueOf(level));
			i++;
		}
	}
}
