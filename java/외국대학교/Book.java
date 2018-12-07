
class Book {

	int id;
	String author;
	String title;
	int noOfPages;
	boolean fiction;
	public Book(int id, String author, String title, int noOfPages, boolean fiction) {
		this.id = id;
		this.author = author;
		this.title = title;
		this.noOfPages = noOfPages;
		this.fiction = fiction;
	}
	@Override
	public String toString() {
		return "id:" + id + ", Title:" + title + ", Author:" + author +
				", No. of pages:" + noOfPages + ", Fiction:"
				+ fiction;
	}
	
	
}
