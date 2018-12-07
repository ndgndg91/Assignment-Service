package first;

public class Driver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Arena arena = new Arena(10, 10);
		Crate crateCoins = new Crate(Treasure.COINS);
		Crate crateFood = new Crate(Treasure.FOOD);
		Crate crateRags = new Crate(Treasure.RAGS);
		Crate crateStatue = new Crate(Treasure.STATUE);
		Crate crateWood = new Crate(Treasure.WOOD);
		Dragon dragonGold = new Dragon(Color.GOLD);
		Dragon dragonRed = new Dragon(Color.RED);
		Hero kelly = new Hero("Kelly");
		Hero pat = new Hero("Pat");
		
		arena.batchEntity(dragonGold, 6, 6);
		arena.batchEntity(crateWood, 1, 1);
		arena.batchEntity(crateFood, 5, 5);
		arena.batchEntity(crateRags, 2, 6);
		arena.batchEntity(crateStatue, 3, 3);
		arena.batchEntity(crateCoins, 1,1);
		arena.batchEntity(pat, 8, 2);
		arena.batchEntity(kelly, 8,2);
		arena.batchEntity(dragonRed, 4, 4);
		
		arena.countEntity("before");
		System.out.println();
		pat.move(arena,4,4);
		pat.move(arena, 5, 5);
		pat.move(arena, 3, 4);
		pat.move(arena, 6, 6);
		pat.move(arena, 3, 4);
		pat.move(arena, 2, 6);
		
		pat.reportHero();
		
		arena.countEntity("after");

	}

}
