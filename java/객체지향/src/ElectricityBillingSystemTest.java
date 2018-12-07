/*
 * @author Dabin Kim
 * @file: ElectricityBillingSystem
 * @description: This class only shows Menu and handles the input value exception. 
 *  Each of specific function will be handled in ElectricityBillingSystem.java.
 * @date: 2017.11.02
 * */
import java.util.*;

public class ElectricityBillingSystemTest {

	private static Date date; // save current system date
	private static ElectricityBillingSystem ebs;

	public static void main(String[] args) {
		int menu = 0;
		Scanner input = new Scanner(System.in);

		// initialization of this program
		initProgram();

		// Select menu
		do {
			try {
				System.out.println("[" + date + "]");
				System.out.println("메뉴를 선택하세요: ");
				System.out.print(
						"1. 고객등록\n2. 고객선택\n3. 검침\n4. 고지\n5. 종료 \n>> ");
				menu = input.nextInt();
				processMenu(menu);

			} catch (InputMismatchException e) {
				System.out.println("Invalid input type. Try again");
				input.nextLine();
			} catch (IllegalArgumentException e) {
				System.out.println(e.getMessage());
			}
		} while (menu != 5);
	}

	public static void initProgram() {
		date = new Date();
		ebs = new ElectricityBillingSystem(date);
		date.setState(Date.Type.NOTICE);

		System.out.println("Welcome to the Electricity Billing System.===================");
		//System.out.println("[현재날짜: " + date + "]");

	}

	public static void processMenu(int menu) {

		switch (menu) {
		case 1:
			ebs.registerCustomer();
			break;
		case 2:
			ebs.selectCustomer();
			break;
		case 3:
			ebs.readMeter();
			break;
		case 4:
			ebs.noticePrice();
			break;
		case 5:
			System.out.println("Bye~");
			break;
		default:
			throw new IllegalArgumentException("Invalid Menu. Try again.\n");

		}

	}

}
