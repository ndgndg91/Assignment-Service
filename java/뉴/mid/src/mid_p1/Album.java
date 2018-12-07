package mid_p1;


public class Album {
	private String albumName;
	private String singerName;
	private String issueDate;
	
	public Album(String albumName, String singerName, String issueDate) {
		this.albumName = albumName;
		this.singerName = singerName;
		this.issueDate = issueDate;
	}

	public String getAlbumName() {
		return albumName;
	}

	public String getSingerName() {
		return singerName;
	}

	public String getIssueDate() {
		return issueDate;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "¾Ù¹ü/"+getAlbumName()+"/"+getIssueDate()+"/"+getSingerName();
	}
}
