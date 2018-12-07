package first;

public class Crate extends Entity{
	private Treasure treasure;

	public Crate(Treasure treasure) {
		this.treasure = treasure;
	}

	@Override
	public String toString() {
		return super.toString();
	}

	public Treasure getTreasure() {
		return treasure;
	}

	public void setTreasure(Treasure treasure) {
		this.treasure = treasure;
	}
	
	
	
	
	
}
