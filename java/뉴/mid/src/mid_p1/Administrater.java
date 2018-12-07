package mid_p1;

import java.util.ArrayList;
import java.util.Scanner;

public class Administrater {
	static Scanner scanner = new Scanner(System.in);
	static ArrayList<Singer> singers = new ArrayList<>();
	static ArrayList<Album> albums = new ArrayList<>();
	static ArrayList<Music> musics = new ArrayList<>();
	
	public static void main(String[] args) {
		init();
	}
	
	public static void init(){
		String input;
		while(true){
			System.out.println("1. 데이터 입력"); 
			System.out.println("2. 데이터 삭제");
			System.out.println("3. 데이터 검색");
			System.out.println("4. 판매량 입력");
			System.out.println("5. 종료");
			
			input = scanner.nextLine();
			if(!input.equals("5")){
				switch (input) {
				case "1":
					inputData();
					break; 
				case "2":
					removeData();
					break;
				case "3":
					searchData();
					break;
				case "4":
					setMusicSaleInfo();
					break;
				}
			}else if(input.equals(""))
				break;

		}
	}
	
	public static void setMusicSaleInfo(){
		for (int i = 0; i < musics.size(); i++) {
			System.out.println(musics.get(i).toString()); 
		}
		
		System.out.println("판매량을 입력할 곡번호를 적어주세요: ");
		int number = scanner.nextInt();
		if(number>musics.size()){
			try {
				throw new IndexOutOfBoundsException();
			} catch (Exception e) {
				System.out.println("오류: 입력 오류");
			}
		}else{
			System.out.println("판매량: ");
			int salesRate = scanner.nextInt();
			musics.get(number-1).setSalesRate(salesRate);
			System.out.println(musics.get(number-1).toString()); 
		}
			
		
	}
	
	public static void searchData(){
		 
		  System.out.println("검색하실 텍스트를 입력하세요:");
		  String text = scanner.nextLine();
		  if(text.isEmpty())
			try {
				throw new Exception();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				System.out.println("오류: 입력값이 없습니다.");
			}
		  for (int i = 0; i < singers.size(); i++) {
			if(text.equals(singers.get(i).getName())||text.equals(singers.get(i).getEntertainment()))
				System.out.println(singers.get(i).toString());
		  }
		  
		  for (int i = 0; i < albums.size(); i++) {
			if(text.equals(albums.get(i).getAlbumName())||text.equals(albums.get(i).getSingerName()))
				System.out.println(albums.get(i).toString());
		  }
		  for (int i = 0; i < musics.size(); i++) {
			if(text.equals(musics.get(i).albumName)||text.equals(musics.get(i).jenre)||
					text.equals(musics.get(i).musicName)||text.equals(musics.get(i).singer)){
				System.out.println(musics.get(i).toString()); 
			}
		  }
	}
	
	public static void removeData() {
		if (singers.size() == 0 && albums.size() == 0 && musics.size() == 0) {
			System.out.println("오류 : 입력사항이 없습니다. 데이터를 먼저 입력하세요.");
			return;
		} 
			int counter = 1;
			int singerC = 0;
			for (int i = 0; i < singers.size(); i++) {
				System.out.println(counter + "." + singers.get(i).toString());
				counter++;
				singerC++;
			}

			int albumC = 0;
			for (int i = 0; i < albums.size(); i++) {
				System.out.println(counter + "." + albums.get(i).toString());
				counter++;
				albumC++;
			}
			int musicC = 0;
			for (int i = 0; i < musics.size(); i++) {
				System.out.println(counter + "." + musics.get(i).toString());
				counter++;
				musicC++;
			}
			int input = scanner.nextInt();
			if(input<=0){
				throw new IndexOutOfBoundsException();
			}
			if (input <= singerC)
			singers.remove(input - 1);
		else if (input > singerC && input <= singerC + albumC)
			albums.remove(input - (singerC) - 1);
		else
			musics.remove(input - (singerC + albumC) - 1);

		counter = 1;
		for (int i = 0; i < singers.size(); i++) {
			System.out.println(counter + "." + singers.get(i).toString());
			counter++;

		}

		for (int i = 0; i < albums.size(); i++) {
			System.out.println(counter + "." + singers.get(i).toString());
			counter++;

		}

		for (int i = 0; i < musics.size(); i++) {
			System.out.println(counter + "." + singers.get(i).toString());
			counter++;

		}

	}

	public static void inputData(){
		
		String input = "";

		System.out.println("1. 가수");
		System.out.println("2. 앨범");
		System.out.println("3. 음악");
		input = scanner.nextLine();

		switch (input) {
		case "1":
			System.out.println("가수이름> ");
			String name = scanner.nextLine();
			System.out.println("생년월일> ");
			String birthdate = scanner.nextLine();
			System.out.println("소속사> ");
			String entertainment = scanner.nextLine();
			Singer singer = new Singer(name, birthdate, entertainment);
			singers.add(singer);
			System.out.println(singer.toString()+" 등록됨");
			break;
		case "2":
			System.out.println("앨범이름>");
			String albumName = scanner.nextLine();
			System.out.println("가수이름>");
			String singerName = scanner.nextLine();
			System.out.println("발매일>");
			String issueDate = scanner.nextLine();
			System.out.println();
			Album album = new Album(albumName, singerName, issueDate);
			albums.add(album);
			System.out.println(album.toString()+ " 등록됨");
			break;
		case "3":
			System.out.println("곡명>");
			String musicName = scanner.nextLine();
			System.out.println("가수이름>");
			String singername = scanner.nextLine();
			System.out.println("앨범명>");
			String albumname = scanner.nextLine();
			System.out.println("장르>");
			String jenre = scanner.nextLine();
			Music music = new Music(musicName, singername, albumname, jenre,0,0);
			musics.add(music);
			System.out.println(music.toString()+ " 등록됨");
			break;
		}
	}
}
