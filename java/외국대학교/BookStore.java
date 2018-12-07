
public class BookStore {

	public static void main(String[] args) {
		Book[] books = new Book[10];
		books[0] = new Book(10,"The Red Sari","Javier Moro",102,false);
		books[1] = new Book(4,"Neither a Hake Nor a dove","Khurshid M Kasuari",350,true);
		books[2] = new Book(1,"Faces and Places Professor","Deepak Nayyar,",311,false);
		books[3] = new Book(6,"Indian Parliamentary Diplomacy","Meira Kumar",89,true);
		books[4] = new Book(5,"Farishta,","Kapil Isapuari",600,false);
		books[5] = new Book(3,"Super Economies","Raghav Bahal",201,true);
		books[6] = new Book(2,"China :Confucius in the Shadow","Poonam Surie,",199,false);
		books[7] = new Book(7,"My country My Life","L.K.Advani",143,false);
		books[8] = new Book(9,"Joseph Anton","Sulman Rushdie",454,true);
		books[9] = new Book(8,"A Political Biography","Andy Marino",411,false);
		
		

		int fiction_cnt = 0;
		int non_fiction_cnt =0;
		int page_more_200 = 0;
		int page_less_200 = 0;
		for( int i = 0 ; i<books.length; i++){
			System.out.println(books[i].toString());
			System.out.println();
			if(books[i].fiction == true)
				fiction_cnt +=1;
			else
				non_fiction_cnt +=1;
			if(books[i].noOfPages >= 200)
				page_more_200 += 1;
			if(books[i].noOfPages <= 200)
				page_less_200 += 1;
		}

		
		System.out.println(page_more_200+" books have number of pages more than 200.");
		System.out.println();
		System.out.println(page_less_200+" books have number of pages less than 200.");
		System.out.println();
		System.out.println(fiction_cnt + " books are fiction.");
		System.out.println();
		System.out.println(non_fiction_cnt + " books are not fiction.");
	}

}
