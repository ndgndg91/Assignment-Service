
/*
 * @author Dabin Kim
 * @file: Customer.java
 * @description: This class models a customer. A customer object manages array of bills 
 *  which store monthly electricity bill information to check and pay a custmer's payment. *    
 * @date: 2017.11.02
 * */

import java.util.Scanner;
import java.util.Random;

public class Customer {

	private String name;
	private String type;
	private Date registrationDate;
	private Date currentDate;
	private Bill[] bill; // Store a customer's uncharged bill info.
	private int powerUsage; // metering data
	private int currentMonth = 0; // this index indicates that the latest month
	private int firstUnpaidMonth = 1; // this index indicates that the last paid month

	Customer(String name) {
		this.name = name;
		this.type = "residential";
		this.registrationDate = getDate();
		this.currentDate = getDate();
		this.bill = new Bill[12];
	}

	public Date getDate() {
		Date date = new Date();
		return date;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public Date getRegistrationDate() {
		return registrationDate;
	}

	public void setRegistrationDate(Date registrationDate) {
		this.registrationDate = registrationDate;
	}

	/*******************************************************************************
	 * When "Meter reading" is selected, this method is called. This method randomly
	 * generate every customer's powerUsage
	 *******************************************************************************/
	public void recordPowerUsage() {
		Random rand = new Random();
		this.powerUsage = (rand.nextInt(100) + 1) * 10;

		// test by dabin
		// this.powerUsage = 340;

		System.out.println("Customer " + name + "'s" + currentDate.getMonth() + " PowerUsage is " + powerUsage);

	}

	/********************************************************************************
	 * When "Price notice" is selected, this method is called. This method create a
	 * Bill object per month by using customer's powerUsage value
	 ********************************************************************************/
	public void receiveElectricityBill() {
		// Bill object for this month with full-filled Bill information
		bill[++currentMonth] = new Bill(currentDate.getMonth() - 1, powerUsage);
	}

	/********************************************************************************
	 * When a customer select "Check bills", this method is called. It shows the
	 * latest Bill information with unpaid electricity bills
	 ********************************************************************************/
	public void showElecticityBill(int checkDay) {

		double totalUnpaidRate;
		double lastMonthRate;
		double overdueRate = 0.0;
		double totalCharge;
		String line = "\n====================================\n";

		if (firstUnpaidMonth > currentMonth)
			System.out.println("조회하실 금액이 없습니다.");
		else {
			// 미납액 계산 (미납액은, 전전달까지의 미납액만 포함) 당월 고지에 해당하는 전달의 미납은 포함하지 않음
			totalUnpaidRate = getTotalUnpaidRate(checkDay);

			// 당월고지에 계산. 연체되었을 경우 연체료 필요
			lastMonthRate = bill[currentMonth].getTotalRate();

			if (checkDay > 25)
				overdueRate = Math.floor((lastMonthRate * 0.015 * ((checkDay - 25) / (double) 31)));

			totalCharge = totalUnpaidRate + lastMonthRate + overdueRate;

			if (totalCharge > 0) {
				System.out.println(line + this.name + " 고객님의 " + (currentDate.getMonth() - 1) + "월 전기요금 조회" + line
						+ bill[currentMonth] + "\n미납액	: " + totalUnpaidRate + "\n당월 연체료	: " + overdueRate + line);
			} else
				System.out.println("조회하실 금액이 없습니다.");
		}
	}

	/********************************************************************************
	 * When a customer select "Charge bills", this method is called. It moves the
	 * lastPaid index to the current index. This is because this application does
	 * not allow installments
	 ********************************************************************************/
	public void chargeElectricityBill(int checkDay) {

		double totalUnpaidRate;
		double lastMonthRate;
		double overdueRate = 0.0;
		double totalCharge;
		String line = "\n====================================\n";

		if (firstUnpaidMonth > currentMonth)
			System.out.println("납부하실 금액이 없습니다.");
		else {

			// 미납액 계산 (미납액은, 전전달까지의 미납액만 포함) 당월 고지에 해당하는 전달의 미납은 포함하지 않음
			totalUnpaidRate = getTotalUnpaidRate(checkDay);

			// 당월고지에 계산. 연체되었을 경우 연체료 필요
			lastMonthRate = bill[currentMonth].getTotalRate();

			if (checkDay > 25)
				overdueRate = Math.floor((lastMonthRate * 0.015 * ((checkDay - 25) / (double) 31)));

			totalCharge = totalUnpaidRate + lastMonthRate + overdueRate;

			if (totalCharge > 0) {
				System.out.println(line + this.name + " 고객님의 " + (currentDate.getMonth() - 1) + "월 전기요금 조회" + line
						+ bill[currentMonth] + "\n미납액	: " + totalUnpaidRate + "\n당월 연체료	: " + overdueRate + line);
			} else
				System.out.println(line + "납부하실 금액이 없습니다." + line);

			// move last paid index to the current
			firstUnpaidMonth = currentMonth + 1; // firstUnpaidMonth should be (currentMonth+1)
		}
	}

	public double getTotalUnpaidRate(int checkDay) {
		double unpaidRate = 0.0;
		double overdueRate = 0.0;

		for (int i = firstUnpaidMonth; i <= (currentMonth - 1); i++) {
			unpaidRate += bill[i].getTotalRate();

			// calculate overdue rate
			double overdue = 5 + checkDay + ((currentMonth - 1) - i) * 31;
			overdueRate = unpaidRate * 0.015 * (overdue / 31);
			System.out.println(i + "월분 미납 (연체일: " + overdue + ")]");
		}

		return unpaidRate;
	}

	public String toString() {
		String line = "\n====================================\n";
		return (line + "Customer: " + this.getName() + "\nType    : " + this.getType() + "\nRegistration date : "
				+ this.getRegistrationDate() + "\nMeter reading date  : " + "1st of the month"
				+ "\nPrice notice date : " + "10th of the month" + "\nDue date          : " + "25th of the month"
				+ line);
	}

}
