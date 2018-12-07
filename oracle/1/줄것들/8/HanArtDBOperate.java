import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class HanArtDBOperate {
	Connection con;
	boolean bResult = false;
	PreparedStatement pstmt = null;

	public HanArtDBOperate() {
		String url = "jdbc:oracle:thin:@����Ŭ�����ּ�:��Ʈ/SID.�۷ι�DB�̸�";
		String userid = "�����̸�";
		String pwd = "������й�ȣ";

		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("driver�� �����ϴ��� üũ �Ϸ�");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
			System.out.println("Driver load failure");
		}
		try {
			System.out.println("before database connection");
			con = DriverManager.getConnection(url, userid, pwd);
		} catch (SQLException e) {
			e.printStackTrace();
			System.out.println("Database Connection Failure");
		}
	}

	public void SqlRun(String e_name) {
		String query = "select o.o_no ,o.o_date ,o.ship_address ,o.o_cnt,"
				+ "o.o_total,o.c_no ,o.e_no,p.p_no,p.p_name ,p.o_price ," + "p.c_price,p.cnt "
				+ "from orders o, product p " + "where o.p_no = p.P_NO and "
				+ "o.c_no = (select c_no from customer where c_name=?)";
		try {
			pstmt = con.prepareStatement(query);
			pstmt.setString(1, e_name);

			ResultSet rs = pstmt.executeQuery();
			System.out.println(" �ֹ���ȣ\t�ֹ���¥\t����ּ�\t�ֹ�����\t�ֹ��Ѿ�\t����ȣ\t���������ȣ\t" + "��ǰ��ȣ\t��ǰ�̸�\t��ǰ����\t�Һ��ڰ���\t��ǰ���");
			while (rs.next()) {
				System.out.print(rs.getInt(1));
				System.out.print("\t" + rs.getString(2).substring(0, 10));
				System.out.print("\t" + rs.getString(3));
				System.out.print("\t" + rs.getInt(4));
				System.out.print("\t" + rs.getInt(5));
				System.out.print("\t" + rs.getInt(6));
				System.out.print("\t" + rs.getInt(7));
				System.out.print("\t" + rs.getInt(8));
				System.out.print("\t" + rs.getString(9));
				System.out.print("\t" + rs.getInt(10));
				System.out.print("\t" + rs.getInt(11));
				System.out.print("\t" + rs.getInt(12));
				System.out.println();
			}
			System.out.println();
			// con.close();
		} catch (SQLException e) {
			e.printStackTrace();
			System.out.println("sql execution failure");
		}
	}

	public void SqlRun2(String year, String month) {

		String date = year + "/" + month + "/";
		String query = "select e.e_name ,sum(nvl(o_total,0)),se.GOAL_SALES " + "from orders o, sales_emp se, emp e "
				+ "where o.e_no(+)=e.E_NO and e.e_no = se.e_no and e.e_type ='����' and " + "O_DATE between ? and ? "
				+ "group by e.e_name,se.GOAL_SALES " + "order by sum(nvl(o_total,0)) desc";
		try {
			if (month.equals("01") | month.equals("03") | month.equals("05") | month.equals("07") 
					| month.equals("08") | month.equals("10") | month.equals("12")) {
				pstmt = con.prepareStatement(query);
				pstmt.setString(1, date + "01");
				pstmt.setString(2, date + "31");
			} else if (month.equals("04") | month.equals("06") | month.equals("09") | month.equals("11")) {
				pstmt = con.prepareStatement(query);
				pstmt.setString(1, date + "01");
				pstmt.setString(2, date + "30");
			}else if(month.equals("02")){
				pstmt = con.prepareStatement(query);
				pstmt.setString(1, date + "01");
				pstmt.setString(2, date + "28");
			}
			int real_sum = 0;
			int goal_sum = 0;
			ResultSet rs = pstmt.executeQuery();
			System.out.println("  \t�����̸�\t������հ� \t\t��ǥ�����");
			while (rs.next()) {
				System.out.print("\t" + rs.getString(1));
				System.out.print("\t" + rs.getInt(2));
				real_sum += rs.getInt(2);
				goal_sum += rs.getInt(3);
				System.out.print("\t\t" + rs.getInt(3));
				System.out.println();
			}
			System.out.println("\t\t " + real_sum + "\t" + goal_sum);
			System.out.println();
			// con.close();
		} catch (SQLException e) {
			e.printStackTrace();
			System.out.println("sql execution failure");
		}
	}

	public void close() throws SQLException {
		con.close();
	}
}
