package mid_p1;
public class Music {
	String musicName;
	String singer;
	String albumName;
	String jenre;
	double price;
	int salesRate;
	
	public Music(String musicName, String singer, String albumName, String jenre, double price, int salesRate) {
		this.musicName = musicName;
		this.singer = singer;
		this.albumName = albumName;
		this.jenre = jenre;
		this.price = price;
		this.salesRate = salesRate;
	}

	public String getMusicName() {
		return musicName;
	}

	public String getSinger() {
		return singer;
	}

	public String getAlbumName() {
		return albumName;
	}

	public String getJenre() {
		return jenre;
	}
	
	
	
	public double getPrice() {
		return price;
	}

	public double getSalesRate() {
		return salesRate;
	}

	
	public void setSalesRate(int salesRate) {
		this.salesRate = salesRate;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "À½¾Ç/"+getMusicName()+"/"+getSinger()+"/"+getAlbumName()+"/"+getJenre()+"/"+getPrice()+"/"+getSalesRate();
	}
	
}
