package first;


public class Dragon extends Entity {
	private Color color;
	
	public Dragon(Color color) {
		this.color = color;
	}
	
	
	public Color getColor() {
		return color;
	}


	public void setColor(Color color) {
		this.color = color;
	}


	@Override
	public String toString() {
		return super.toString();
	}
}
