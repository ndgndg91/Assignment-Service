package first;

public class Arena {
	private Entity[][] dimension;

	public Arena(int x, int y) {
		this.dimension = new Entity[x][y];
	}
	
	public void move(Hero hero, int x, int y) {
		this.dimension[hero.getPosition().getX()][hero.getPosition().getY()] = null;
		if(this.dimension[x][y] instanceof Crate) {
			Crate temp = (Crate) this.dimension[x][y];
			this.dimension[x][y] = hero;
			hero.setPosition(new Position(x, y));
			if(temp.getTreasure() == Treasure.COINS) {
				hero.takeTreasure(Treasure.COINS);
				System.out.println(hero.getName()+" crushed the crate into bits and"
						+ "found "+temp.getTreasure());
			} else if (temp.getTreasure() == Treasure.FOOD) {
				hero.takeTreasure(Treasure.FOOD);
				System.out.println(hero.getName()+" crushed the crate into bits and"
						+ "found "+temp.getTreasure());
			} else if (temp.getTreasure() == Treasure.RAGS) {
				hero.takeTreasure(Treasure.RAGS);
				System.out.println(hero.getName()+" crushed the crate into bits and"
						+ "found "+temp.getTreasure());
			} else if (temp.getTreasure() == Treasure.STATUE) {
				hero.takeTreasure(Treasure.STATUE);
				System.out.println(hero.getName()+" crushed the crate into bits and"
						+ "found "+temp.getTreasure());
			} else if (temp.getTreasure() == Treasure.WOOD) {
				hero.takeTreasure(Treasure.WOOD);
				System.out.println(hero.getName()+" crushed the crate into bits and"
						+ "found "+temp.getTreasure());
			}
			
		} else if(this.dimension[x][y] instanceof Dragon) {
			Dragon temp = (Dragon) this.dimension[x][y];
			this.dimension[x][y] = hero;
			hero.setPosition(new Position(x, y));
			if(temp.getColor() == Color.GOLD) {
				hero.takeTreasure(Treasure.COINS);
				System.out.println(hero.getName()+" bravely defeated the Golden dragon"
						+ " and came away with gold conins as a prize.");
			} else {
				System.out.println(hero.getName()+" bravely defeated the "
						+ temp.getColor()+" dragon.");
			}
		} else {
			this.dimension[x][y] = hero;
			hero.setPosition(new Position(x, y));
		}
		System.out.println(hero.getName()+" moved to "+hero.toString());
	}

	public void batchEntity(Entity entity, int x, int y) {
		if (this.dimension.length <= x) {
			System.out.println("unvalid x");
			return;
		} else {
			if (this.dimension[x].length <= y) {
				System.out.println("unvalid y");
				return;
			} else {
				if (this.dimension[x][y] == null) {
					entity.setPosition(new Position(x, y));
					this.dimension[x][y] = entity;
					printSuccess(entity);
				} else if(this.dimension[x][y] instanceof Hero && entity instanceof Hero){
					Hero temp = (Hero) entity;
					System.out.println("Could not add '"+temp.getName()+" standing at ("+x+","+y+")' "
							+ "because there is already a hero in the arena.");
				} else {
					printFail(entity, this.dimension[x][y]);
				}
			}
		}

	}
	private void printFail(Entity entityAdd, Entity entityAlready) {
		if (entityAdd instanceof Crate) {
			Crate temp = (Crate) entityAdd;
			System.out.println("Could not add 'Crate with "+temp.getTreasure()+" at "+
			entityAlready.toString()+"' because another entity is already there");
		} else if (entityAdd instanceof Dragon) {
			Dragon temp = (Dragon) entityAdd;
			System.out.println("Could not add 'The "+temp.getColor()+" dragon breathing fire at "+
			entityAlready.toString()+"' because another entity is already there");
		}
	}

	private void printSuccess(Entity entity) {
		if (entity instanceof Crate) {
			Crate temp = (Crate) entity;
			System.out.println("Successfully added 'Crate with " + temp.getTreasure() + " at " + temp.toString()
					+ "' to the game arena");
		} else if (entity instanceof Dragon) {
			Dragon temp = (Dragon) entity;
			System.out.println("Successfully added 'The "+temp.getColor()+" dragon breathing fire at "+ temp.toString()
			+"' to the game arena");
		} else if (entity instanceof Hero) {
			Hero temp = (Hero) entity;
			System.out.println("Successfully added 'Hero named "+temp.getName()+" at "+temp.toString()
			+"' to the game arena");
		}
	}
	
	public void countEntity(String beforeOrAfter) {
		System.out.println();
		int totalEntity = 0;
		int totalDragon = 0;
		int totalWoodCrate = 0;
		int totalStatueCrate = 0;
		int totalFoodCrate = 0;
		int totalCoinsCrate = 0;
		int totalRagCrate = 0;
		for(int i = 0 ; i < this.dimension.length; i++) {
			for(int j = 0; j< this.dimension[i].length; j++) {
				if(this.dimension[i][j] != null ) {
					totalEntity += 1;
				}
				if(this.dimension[i][j] instanceof Dragon) {
					totalDragon += 1;
				}
				if(this.dimension[i][j] instanceof Crate) {
					Crate temp = (Crate) this.dimension[i][j];
					if(temp.getTreasure() == Treasure.COINS) {
						totalCoinsCrate += 1;
					}else if(temp.getTreasure() == Treasure.FOOD) {
						totalFoodCrate += 1;
					}else if(temp.getTreasure() == Treasure.WOOD) {
						totalWoodCrate += 1;
					}else if(temp.getTreasure() == Treasure.RAGS) {
						totalRagCrate += 1;
					}else if(temp.getTreasure() == Treasure.STATUE) {
						totalStatueCrate +=1;
					}
				}
			}
		}
		System.out.println("--- Arena Status "+beforeOrAfter+" Moving the Hero ---");
		System.out.println("There are "+totalEntity+" entitis.");
		System.out.println("There are "+totalDragon+" dragons.");
		System.out.println("There are "+totalWoodCrate+" wood treasures.");
		System.out.println("There are "+totalStatueCrate+" statue treasures.");
		System.out.println("There are "+totalFoodCrate+" food treasures.");
		System.out.println("There are "+totalCoinsCrate+" coins treasures.");
		System.out.println("There are "+totalRagCrate+" rag treasures.");
	}

}
