package mysql_JDBC;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Test {
	private static Scanner scn;
	private static Connection con;

	public static void main(String args[]) {
		scn = new Scanner(System.in);
		problem_1();
		scn.close();
	}


	private static void problem_1() {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://db.hufs.ac.kr:3306/s201403658DB", "s201403658",
					"01064895758");
			Level levels = new Level();
			ArrayList<String> level1 = levels.getLevel1();
			ArrayList<String> level2 = levels.getLevel2();
			ArrayList<String> level3 = levels.getLevel3();
			ArrayList<String> level4 = levels.getLevel4();
			ArrayList<String> level5 = levels.getLevel5();
			ArrayList<String> level6 = levels.getLevel6();
			ArrayList<String> level7 = levels.getLevel7();
			ArrayList<String> level8 = levels.getLevel8();
			System.out.println("DB Connection");
			System.out.println("DB : s201403658DB");
			System.out.println("userid : s201403658");
			CallableStatement c = con.prepareCall("{call findBySSN(?)}");
			System.out.print("Enter a ssn: ");
			String ssn = scn.next(); // TEST CASE : 888665555, 453453453 , 999887777, 333445555
			c.setString(1, ssn);
			ResultSet r = c.executeQuery();
			while (r.next()) {
				if (r.getString(2) != null && r.getString(1).length() > 0) {
					level1.add(r.getString(2));
				}
				if (r.getString(3) != null && r.getString(1).length() > 0) {
					level2.add(r.getString(3));
				}
				if (r.getString(4) != null && r.getString(1).length() > 0) {
					level3.add(r.getString(4));
				}
				if (r.getString(5) != null && r.getString(1).length() > 0) {
					level4.add(r.getString(5));
				}
				if (r.getString(6) != null && r.getString(1).length() > 0) {
					level5.add(r.getString(6));
				}
				if (r.getString(7) != null && r.getString(1).length() > 0) {
					level6.add(r.getString(7));
				}
				if (r.getString(8) != null && r.getString(1).length() > 0) {
					level7.add(r.getString(8));
				}
				if (r.getString(9) != null && r.getString(1).length() > 0) {
					level8.add(r.getString(9));
				}
			}

			level1 = new ArrayList<String>(new HashSet<String>(level1));
			level2 = new ArrayList<String>(new HashSet<String>(level2));
			level3 = new ArrayList<String>(new HashSet<String>(level3));
			level4 = new ArrayList<String>(new HashSet<String>(level4));
			level5 = new ArrayList<String>(new HashSet<String>(level5));
			level6 = new ArrayList<String>(new HashSet<String>(level6));
			level7 = new ArrayList<String>(new HashSet<String>(level7));
			level8 = new ArrayList<String>(new HashSet<String>(level8));
			Level.printLevel(level1, 1);
			Level.printLevel(level2, 2);
			Level.printLevel(level3, 3);
			Level.printLevel(level4, 4);
			Level.printLevel(level5, 5);
			Level.printLevel(level6, 6);
			Level.printLevel(level7, 7);
			Level.printLevel(level8, 8);
			System.out.println("END OF LIST");
			con.close();
		} catch (SQLException ex) {
			System.out.println("SQLException" + ex);
		} catch (Exception ex) {
			System.out.println("Exception:" + ex);
		}
	}

}
