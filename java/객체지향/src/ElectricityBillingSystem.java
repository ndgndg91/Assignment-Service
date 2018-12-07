
/*
 * @author Dabin Kim
 * @file: ElectricityBillingSystem
 * @description: This class handles and do actual operations about the selected menu
 * @date: 2017.11.02
 * */

import java.util.InputMismatchException;
import java.util.Scanner;

public class ElectricityBillingSystem {

	private Customer[] custList;

	public enum Type {
		DUP, SEARCH
	}// checking type for user's name

	private int totCust = 0; // the number of customer which registered in the EBS system
	private Date date;
	private final int METERING_DAY; // 검침일
	private final int NOTICE_DAY; // 고지일
	private final int DUE_DAY; // 납기일
	private static int state; //

	// This object should be create at once
	ElectricityBillingSystem(Date date) {
		custList = new Customer[50];
		this.date = date;
		METERING_DAY = 1;
		NOTICE_DAY = 10;
		DUE_DAY = 25;

	}

	/*************************************************************
	 * Methods that are relative to 1.Customer registration 
	 ***********************************************************/

	public void registerCustomer() {
		Scanner input = new Scanner(System.in);
		String name;
		boolean isValid = false;

		do {
			System.out.print("Enter a new customer's name: ");
			name = input.nextLine();

			// Duplicated name check
			try {
				checkName(name, Type.DUP);
				isValid = true;
			} catch (IllegalArgumentException e) {
				System.out.println(e.getMessage());
			}
		} while (!isValid);

		// register the customer' name
		if (totCust != custList.length) {
			custList[totCust++] = new Customer(name);
			System.out.println(name + " is successfully registered.\n" + custList[totCust - 1]);

		} else {
			System.out.println("We can register a customer no more");
		}
	}

	public int checkName(String name, Type type) {
		int i;
		for (i = 0; i < totCust; i++) {
			if (custList[i].getName().equals(name)) {
				if (type == Type.DUP)
					throw new IllegalArgumentException("Duplicate name. Try this with another name");
				else
					return i;
			}
		}
		return i;
	}

	/*************************************************************
	 * Methods that are relative to 2. Select Customer 
	 ***********************************************************/

	public void selectCustomer() {
		int index = 0;
		boolean isValid = false;
		Scanner input = new Scanner(System.in);

		System.out.print("Enter a customer' name: ");
		String name = input.nextLine();

		if ((index = checkName(name, Type.SEARCH)) != totCust) {
			do {
				try {
					System.out.print("  1.Check bills\n  2.Charge bills\n  >> ");
					int menu = input.nextInt();
					checkBill(custList[index], menu);
					isValid = true;

				} catch (InputMismatchException e) {
					System.out.println("Invalid input type. Try again");
					input.nextLine();
				} catch (IllegalArgumentException e) {
					System.out.println(e.getMessage());
				}
			} while (!isValid);
		} else
			System.out.println("Cannot find the customer \"" + name + "\"\n");

	}

	public void checkBill(Customer cust, int menu) {
		int day;
		Scanner input = new Scanner(System.in);

		if (menu > 2)
			throw new IllegalArgumentException("Invalid menu. Try agin");

		while (true) {
			if (this.date.getDay() == this.METERING_DAY) // before informing the E-bills to customers
			{
				System.out.print("Enter the checking date1 (1-9): ");
				if ((day = input.nextInt()) > this.NOTICE_DAY) {
					System.out.println("Input value cannot be bigger than 9. Try again");
					continue;
				} else
					break;

			} else if (this.date.getDay() == this.NOTICE_DAY) { // after informing the E-bills to customers
				System.out.print("Enter the checking date (10-31): ");
				if ((day = input.nextInt()) < this.NOTICE_DAY) {
					System.out.println("Input value cannot be less than 10. Try again");
					continue;
				} else
					break;
			}
		}
		if (menu == 1)
			cust.showElecticityBill(day);
		else
			cust.chargeElectricityBill(day);
	}

	/*************************************************************
	 * Methods that are relative to 3. Meter reading 
	 ***********************************************************/

	public void readMeter() {
		// If previous state is METERING, then this process should be denied.
		if (date.getState() == Date.Type.METERING) {
			throw new IllegalArgumentException("\'4. Price notice\' should precede \'3. Meter reading\'\nTry again\n");
		}

		// Read meter information for this month about every registered customer
		readPowerUsageforAllCust();

		// Change date to 1st day of the next month
		this.date.setMonth(date.getMonth() + 1);
		this.date.setDay(METERING_DAY);

		System.out.println("[Today is: " + date + "]");
		System.out.println("Electric Power Corporation have read customer's metering data.\n");

		// Change system state to after metering
		date.setState(Date.Type.METERING);
	}

	public void readPowerUsageforAllCust() {
		for (int i = 0; i < totCust; i++) {
			custList[i].recordPowerUsage();
		}
	}

	/*************************************************************
	 * Methods that are relative to 4. Price notice 
	 ***********************************************************/

	public void noticePrice() {
		// If previous state is not NOTICE, then this process should be denied

		if (date.getState() == Date.Type.NOTICE) {
			throw new IllegalArgumentException("\'3. Meter reading\' should precede \'4. Price notice\'\nTry again\n");
		}

		// Change date to 1st day of the next month
		this.date.setDay(NOTICE_DAY);

		System.out.println("[Today is: " + date +"]");
		System.out.println("Electric Power Corporation have sent electricity bills to customers.\n");

		// Change system state to after metering
		date.setState(Date.Type.NOTICE);

		// Update the Electricity Bill
		sendElectricityBillToAllCust();
	}
	
	public void sendElectricityBillToAllCust()
	{
		for(int i=0; i<totCust; i++)
		{
			custList[i].receiveElectricityBill();
		}
		
	}

}
