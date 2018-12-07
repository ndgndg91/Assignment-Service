import java.sql.SQLException;
import java.util.Scanner;

public class HanArtMain {
	static Scanner sc = null;

	public static void main(String[] args) {

		HanArtDBOperate con = new HanArtDBOperate();
		main(con);
	}

	static void main(HanArtDBOperate con) {
		sc = new Scanner(System.in);
		while (true) {
			print();
			String choice = sc.nextLine();
			if (choice.equals("1")) {
				System.out.print("고객의 이름을 입력하세요 : ");
				String e_name = sc.nextLine();
				con.SqlRun(e_name);
			} else if (choice.equals("2")) {
				System.out.print("년도를 입력하세요 (YYYY) :");
				String y_date = sc.nextLine();
				System.out.print("월을 입력하세요 (MM) : ");
				String m_date = sc.nextLine();
				if(m_date.length()==1){
					m_date = "0"+m_date;
				}
				int month = Integer.parseInt(m_date);
				if(month > 12 | month < 1){
					System.out.println("달은 01~12월 까지 입력이 가능합니다. 처음으로 돌아갑니다.");
					System.out.println();
					continue;
				}
				con.SqlRun2(y_date, m_date);
			} else if (choice.equals("3")) {
				System.out.println("프로그램을 종료합니다.");
				try {
					con.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
				break;
			} else {
				System.out.println("1, 2, 3번 만 입력하세요.");
				System.out.println();
			}
		}
	}

	static void print() {
		System.out.println("1. 특정한 고객의 주문에 포함된 제품 내역");
		System.out.println("2. 이달의 영업사원별 목표매출액과 매출액합계");
		System.out.println("3. 종료");
		System.out.print(">>>>");
	}

}