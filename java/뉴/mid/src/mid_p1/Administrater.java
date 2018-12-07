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
			System.out.println("1. ������ �Է�"); 
			System.out.println("2. ������ ����");
			System.out.println("3. ������ �˻�");
			System.out.println("4. �Ǹŷ� �Է�");
			System.out.println("5. ����");
			
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
		
		System.out.println("�Ǹŷ��� �Է��� ���ȣ�� �����ּ���: ");
		int number = scanner.nextInt();
		if(number>musics.size()){
			try {
				throw new IndexOutOfBoundsException();
			} catch (Exception e) {
				System.out.println("����: �Է� ����");
			}
		}else{
			System.out.println("�Ǹŷ�: ");
			int salesRate = scanner.nextInt();
			musics.get(number-1).setSalesRate(salesRate);
			System.out.println(musics.get(number-1).toString()); 
		}
			
		
	}
	
	public static void searchData(){
		 
		  System.out.println("�˻��Ͻ� �ؽ�Ʈ�� �Է��ϼ���:");
		  String text = scanner.nextLine();
		  if(text.isEmpty())
			try {
				throw new Exception();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				System.out.println("����: �Է°��� �����ϴ�.");
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
			System.out.println("���� : �Է»����� �����ϴ�. �����͸� ���� �Է��ϼ���.");
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

		System.out.println("1. ����");
		System.out.println("2. �ٹ�");
		System.out.println("3. ����");
		input = scanner.nextLine();

		switch (input) {
		case "1":
			System.out.println("�����̸�> ");
			String name = scanner.nextLine();
			System.out.println("�������> ");
			String birthdate = scanner.nextLine();
			System.out.println("�Ҽӻ�> ");
			String entertainment = scanner.nextLine();
			Singer singer = new Singer(name, birthdate, entertainment);
			singers.add(singer);
			System.out.println(singer.toString()+" ��ϵ�");
			break;
		case "2":
			System.out.println("�ٹ��̸�>");
			String albumName = scanner.nextLine();
			System.out.println("�����̸�>");
			String singerName = scanner.nextLine();
			System.out.println("�߸���>");
			String issueDate = scanner.nextLine();
			System.out.println();
			Album album = new Album(albumName, singerName, issueDate);
			albums.add(album);
			System.out.println(album.toString()+ " ��ϵ�");
			break;
		case "3":
			System.out.println("���>");
			String musicName = scanner.nextLine();
			System.out.println("�����̸�>");
			String singername = scanner.nextLine();
			System.out.println("�ٹ���>");
			String albumname = scanner.nextLine();
			System.out.println("�帣>");
			String jenre = scanner.nextLine();
			Music music = new Music(musicName, singername, albumname, jenre,0,0);
			musics.add(music);
			System.out.println(music.toString()+ " ��ϵ�");
			break;
		}
	}
}
