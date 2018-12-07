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
				System.out.print("���� �̸��� �Է��ϼ��� : ");
				String e_name = sc.nextLine();
				con.SqlRun(e_name);
			} else if (choice.equals("2")) {
				System.out.print("�⵵�� �Է��ϼ��� (YYYY) :");
				String y_date = sc.nextLine();
				System.out.print("���� �Է��ϼ��� (MM) : ");
				String m_date = sc.nextLine();
				if(m_date.length()==1){
					m_date = "0"+m_date;
				}
				int month = Integer.parseInt(m_date);
				if(month > 12 | month < 1){
					System.out.println("���� 01~12�� ���� �Է��� �����մϴ�. ó������ ���ư��ϴ�.");
					System.out.println();
					continue;
				}
				con.SqlRun2(y_date, m_date);
			} else if (choice.equals("3")) {
				System.out.println("���α׷��� �����մϴ�.");
				try {
					con.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
				break;
			} else {
				System.out.println("1, 2, 3�� �� �Է��ϼ���.");
				System.out.println();
			}
		}
	}

	static void print() {
		System.out.println("1. Ư���� ���� �ֹ��� ���Ե� ��ǰ ����");
		System.out.println("2. �̴��� ��������� ��ǥ����װ� ������հ�");
		System.out.println("3. ����");
		System.out.print(">>>>");
	}

}