package first;

import java.util.ArrayList;
import java.util.List;

public class Hero extends Entity {
	private String name;
	private List<Treasure> list;
	public Hero(String name) {
		this.name = name;
		this.list = new ArrayList<>();
	}
	
	public void move(Arena arena,int x, int y) {
		arena.move(this,x,y);
	}
	public void takeTreasure(Treasure treasure) {
		this.list.add(treasure);
	}
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<Treasure> getList() {
		return list;
	}

	public void setList(List<Treasure> list) {
		this.list = list;
	}

	@Override
	public String toString() {
		return super.toString();
	}
	
	public void reportHero() {
		System.out.println("--- Hero Report for"+this.getName()+" ---");
		System.out.println("position : "+this.toString());
		System.out.println("Treasures : ");
		for(Treasure tr : list) {
			System.out.println("\t"+tr);
		}
	}
}
