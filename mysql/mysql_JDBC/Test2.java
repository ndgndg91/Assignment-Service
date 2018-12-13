package mysql_JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Test2 {
	private static Scanner scn;
	private static Connection con;
	private static PreparedStatement psmt;
	private static ResultSet rset;
	
	public static void main(String args[]) {
		scn = new Scanner(System.in);
		problem_2();
		scn.close();
	}
	
	private static void problem_2() {
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
			String query = "SELECT COUNT(*) FROM EMPLOYEE WHERE Superssn = ?";
			psmt = con.prepareStatement(query);
			System.out.print("Enter a ssn: ");
			String ssn = scn.next(); // TEST CASE : 888665555, 453453453 , 999887777, 333445555
			psmt.setString(1, ssn);
			rset = psmt.executeQuery();
			int cnt = 0;
			while (rset.next()) {
				cnt = rset.getInt(1);
			}
			if (cnt > 0) {
				query = "SELECT lv1.ssn as lv1, lv2.ssn as lv2, lv3.ssn as lv3 , lv4.ssn as lv4, lv5.ssn as lv5, lv6.ssn as lv6, lv7.ssn as lv7, lv8.ssn as lv8, lv9.ssn as lv9"
						+ " FROM EMPLOYEE lv1 left join EMPLOYEE lv2" + " on lv2.Superssn = lv1.ssn"
						+ " left join EMPLOYEE lv3 " + " on lv3.Superssn = lv2.ssn" + " left join EMPLOYEE lv4"
						+ " on lv4.Superssn = lv3.ssn" + " left join EMPLOYEE lv5" + " on lv5.Superssn = lv4.ssn"
						+ " left join EMPLOYEE lv6" + " on lv6.Superssn = lv5.ssn" + " left join EMPLOYEE lv7"
						+ " on lv7.Superssn = lv6.ssn" + " left join EMPLOYEE lv8" + " on lv8.Superssn = lv7.ssn"
						+ " left join EMPLOYEE lv9" + " on lv9.Superssn = lv8.ssn" + " where lv1.ssn = ?";
				psmt = con.prepareStatement(query);
				psmt.setString(1, ssn);
				rset = psmt.executeQuery();
				while (rset.next()) {
					if (rset.getString(2) != null && rset.getString(1).length() > 0) {
						level1.add(rset.getString(2));
					}
					if (rset.getString(3) != null && rset.getString(1).length() > 0) {
						level2.add(rset.getString(3));
					}
					if (rset.getString(4) != null && rset.getString(1).length() > 0) {
						level3.add(rset.getString(4));
					}
					if (rset.getString(5) != null && rset.getString(1).length() > 0) {
						level4.add(rset.getString(5));
					}
					if (rset.getString(6) != null && rset.getString(1).length() > 0) {
						level5.add(rset.getString(6));
					}
					if (rset.getString(7) != null && rset.getString(1).length() > 0) {
						level6.add(rset.getString(7));
					}
					if (rset.getString(8) != null && rset.getString(1).length() > 0) {
						level7.add(rset.getString(8));
					}
					if (rset.getString(9) != null && rset.getString(1).length() > 0) {
						level8.add(rset.getString(9));
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
			} else {

			}
			System.out.println("END OF LIST");
			con.close();
		} catch (SQLException ex) {
			System.out.println("SQLException" + ex);
		} catch (Exception ex) {
			System.out.println("Exception:" + ex);
		}

	}
}
