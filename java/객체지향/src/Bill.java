
/*
 * @author Dabin Kim
 * @file: Bill.java
 * @description: This class contains specific contents 
 *  related to the electricity bill calculation
 * @date: 2017.11.02
 * */

public class Bill {
	private int month; // 고지 월
	private int powerUsage; // 소비전력량
	private int baseRate; // 기본요금 = 단계 전력 사용량 * 기본요금

	private double consumptionRate; // 전력량요금 Electricity consumption rate
	private double vatRate; //
	private double elecFund; // 전력기반기금

	private double totalRate; // 전기요금 합계
	// private double overdueRate; // 연체료

	Bill(int month, int powerUsage) {
		this.month = month;
		this.powerUsage = powerUsage;
		this.baseRate = getBaseRate();
		this.consumptionRate = calConsumptionRate();

		this.totalRate = Math.floor(this.baseRate + this.consumptionRate);
		this.vatRate = Math.round(this.totalRate * 0.1);
		this.elecFund = Math.floor((this.totalRate * 0.037) / 10) * 10;

		this.totalRate = Math.floor((this.totalRate + this.vatRate + this.elecFund) / 10) * 10;
	}

	public int getMonth() {
		return month;
	}

	public void setMonth(int month) {
		this.month = month;
	}

	// 전기요금 = 기본요금
	public int getBaseRate() {
		if (this.powerUsage <= 200)
			return 910;
		else if ((201 < this.powerUsage) && (this.powerUsage < 400))
			return 1600;
		else
			return 7300;
	}

	// 전기요금 += 전력량요금 (원미만절사)
	public double calConsumptionRate() {
		double rate;

		if (this.powerUsage > 400)
			rate = ((200 * 93.3) + (200 * 187.9) + ((this.powerUsage - 400) * 280.5));
		else if (this.powerUsage > 200)
			rate = ((200 * 93.3) + ((this.powerUsage - 200) * 187.9));
		else
			rate = ((200 - this.powerUsage) * 93.3);

		return (Math.floor(rate));
	}

	// 전기요금 += 부가세
	public void calVat() {
		this.totalRate += Math.round((this.totalRate * 0.1));
	}

	public double getTotalRate() {
		return this.totalRate;

	}

	@Override
	public String toString() {
		return ("전력사용량	: " + this.powerUsage + "kWh" + "\n기본요금	: " + this.baseRate + "원" + "\n전력량요금	: "
				+ this.consumptionRate + "원" + "\n전기요금합계	: " + (this.baseRate + this.consumptionRate) + "원"
				+ "\n부가가치세	: " + this.vatRate + "원" + "\n전력기반기금	: " + this.elecFund + "원" + "\n청구금액	: "
				+ this.totalRate + "원");
	}

}
