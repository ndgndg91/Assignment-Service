
/*
 * @author Dabin Kim
 * @file: Bill.java
 * @description: This class contains specific contents 
 *  related to the electricity bill calculation
 * @date: 2017.11.02
 * */

public class Bill {
	private int month; // ���� ��
	private int powerUsage; // �Һ����·�
	private int baseRate; // �⺻��� = �ܰ� ���� ��뷮 * �⺻���

	private double consumptionRate; // ���·���� Electricity consumption rate
	private double vatRate; //
	private double elecFund; // ���±�ݱ��

	private double totalRate; // ������ �հ�
	// private double overdueRate; // ��ü��

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

	// ������ = �⺻���
	public int getBaseRate() {
		if (this.powerUsage <= 200)
			return 910;
		else if ((201 < this.powerUsage) && (this.powerUsage < 400))
			return 1600;
		else
			return 7300;
	}

	// ������ += ���·���� (���̸�����)
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

	// ������ += �ΰ���
	public void calVat() {
		this.totalRate += Math.round((this.totalRate * 0.1));
	}

	public double getTotalRate() {
		return this.totalRate;

	}

	@Override
	public String toString() {
		return ("���»�뷮	: " + this.powerUsage + "kWh" + "\n�⺻���	: " + this.baseRate + "��" + "\n���·����	: "
				+ this.consumptionRate + "��" + "\n�������հ�	: " + (this.baseRate + this.consumptionRate) + "��"
				+ "\n�ΰ���ġ��	: " + this.vatRate + "��" + "\n���±�ݱ��	: " + this.elecFund + "��" + "\nû���ݾ�	: "
				+ this.totalRate + "��");
	}

}
