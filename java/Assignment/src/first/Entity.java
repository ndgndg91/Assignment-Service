package first;

public class Entity {
	private Position position;

	@Override
	public String toString() {
		return "("+this.position.getX()+","+ this.position.getY()+")";
	}

	public Position getPosition() {
		return position;
	}

	public void setPosition(Position position) {
		this.position = position;
	}
	
	
	
}
