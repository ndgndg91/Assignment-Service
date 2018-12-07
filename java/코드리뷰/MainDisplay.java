import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
 
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
 
public class MainDisplay implements ActionListener{
 
	JFrame iFrame;
	JPanel iPaneLbl, temp;
	JButton byPerson, byBook,  Borrow, Return, extProgram;
	JLabel iName;
	
	JTable bookTable, personTable;
	String category[] = {"책이름", "저자", "대출자"};
	String category2[] = {"회원이름", "나이", "대출책 갯수", "직업"};
	String category3[] = {"학생", "직장인",};
	
	DefaultTableModel model, model2;
	JScrollPane tbl_sp, tbl_sp2;
	Person[] libPerson;
	int countPerson;
	Book[] libBook;
	int countBook;	
	public MainDisplay(){		
		libPerson = new Person[100];
		libBook = new Book[100];		
		countPerson = countBook = 0;
		
		iFrame=new JFrame("Book Management Program");
		iFrame.setLayout(null);
		iFrame.setBounds(40, 40, 1270, 430);
		iFrame.setResizable(false);
 
		iPaneLbl=new JPanel(null);
		iPaneLbl.setBounds(10, 0, 530, 60);
		iPaneLbl.setBackground(Color.black);
		iName=new JLabel("Book Management Program");
		iName.setBounds(135, 5, 500, 50);
		iName.setForeground(Color.white);
		iName.setFont(new Font("Helvitica", Font.BOLD, 20));
		iPaneLbl.add(iName);
		iFrame.add(iPaneLbl);
 
		byPerson=new JButton("Manage by Person");
		byPerson.setBounds(140, 90, 250, 30);
		byPerson.addActionListener(this);
		iFrame.add(byPerson);
 
		byBook=new JButton("Manage by Book");
		byBook.setBounds(140, 140, 250, 30);
		byBook.addActionListener(this);
		iFrame.add(byBook);
 
	
 
		extProgram=new JButton("Exit the program");
		extProgram.setBounds(140, 240, 250, 30);
		extProgram.addActionListener(this);
		iFrame.add(extProgram);
		
		Borrow=new JButton("Borrow");
		Borrow.setBounds(140, 190, 120, 30);
		Borrow.addActionListener(this);
		iFrame.add(Borrow);
		
		Return=new JButton("Return");
		Return.setBounds(270, 190, 120, 30);
		Return.addActionListener(this);
		iFrame.add(Return);
		
		model = new DefaultTableModel(category,0); // model(table)에 카테고리(책이름, 저자, 대출자) 저장  
		bookTable = new JTable(model);				// 책테이블 에 JTable 모델 저장		
		tbl_sp = new JScrollPane(bookTable);		// 책테이블 에 스크롤바 만들기
		tbl_sp.setBounds(550, 0, 250, 400);			// tbl_sp 의 크기와 위치 설정
		iFrame.add(tbl_sp);							// iFrame 에 tbl_sp 생성
	
		model2 = new DefaultTableModel(category2, 0); // model2 ( 2번째 테이블 ) 에 카테고리 ( 회원이름, 나이 , 대출갯수, 직업 ) 저장
		personTable = new JTable(model2);			// 회원테이블에 model2 저장
		tbl_sp2 = new JScrollPane(personTable);		// 회원테이블에 스크롤바 생성
		tbl_sp2.setBounds(805, 0, 440, 400);		// 크기 설정(가로 위치, 세로 위치, 가로 길이, 세로 길이)
		iFrame.add(tbl_sp2);						// 테이블에 생성
		iFrame.setVisible(true);  					// 테이블 보임
	}
	private void load() {	// 연결
		try {
			FileInputStream fis = new FileInputStream("library.txt"); // 텍스트 파일 생성
			InputStreamReader isr = new InputStreamReader(fis, "MS949");
			BufferedReader br = new BufferedReader(isr);
			String temp;
			if(br.readLine().trim().equals("Book")){
				while(true){
					temp = br.readLine().trim();
					if(!temp.equals("Person")){
						libBook[countBook] = new Book();
						libBook[countBook].setName(temp);
						libBook[countBook].setAuth(br.readLine().trim());
						temp = br.readLine().trim();
						if(temp.equals("null"))
							libBook[countBook++].setPersonname(null);
						else
							libBook[countBook++].setPersonname(temp);
					}
					else{
						while(true){
						libPerson[countPerson] = new Person() {
						};
						libPerson[countPerson].setName(br.readLine().trim());
						libPerson[countPerson].setAge(Integer.parseInt(br.readLine().trim()));
						libPerson[countPerson].setAddress(br.readLine().trim());
						libPerson[countPerson].setStatus(br.readLine().trim());
						libPerson[countPerson++].setNumofbook(Integer.parseInt(br.readLine().trim()));
						}
					}
				}
			}
			br.close();
			isr.close();
			fis.close();
		} catch (Exception e) {
			refresh();
			return;
		}
		refresh();
	}
	public void actionPerformed(ActionEvent iEvent) {
		if(iEvent.getSource()==byPerson) {
			String name = JOptionPane.showInputDialog("이름을 입력하세요");
			int age = Integer.parseInt(JOptionPane.showInputDialog("나이를 입력하세요"));
			String address = JOptionPane.showInputDialog("주소를 입력하세요");
			int abc = JOptionPane.showOptionDialog(temp, "선택", "뮤", 0, 0, null, category3, 10);
			switch (abc) {
			case 0:
				libPerson[countPerson++] = new Student(name, age, address); // 학생
				refresh();
				break;
			case 1:
				libPerson[countPerson++] = new Faculty(name, age, address); // 직장인
				refresh();
				break;
		
			}
		}
		else if(iEvent.getSource()==byBook) {
			String name = JOptionPane.showInputDialog("책 제목을 입력하세요");
			String auth = JOptionPane.showInputDialog("저자를 입력하세요");			
			libBook[countBook++] = new Book(name, auth);
			refresh();
		}
	
		else if(iEvent.getSource()==Borrow){
			int book = bookTable.getSelectedRow();
			
			String bookname = (String) model.getValueAt(book, 0);
			
			if(model.getValueAt(book, 2) !=null){
				JOptionPane.showMessageDialog(temp, "먼저 \"" + bookname +"\"을 반납해 주세요");
				return;
			}
			
		}
		else if(iEvent.getSource()==Return){
			int book = bookTable.getSelectedRow();
			if(model.getValueAt(book, 2)==null){
				JOptionPane.showMessageDialog(temp, "이 책을 빌린사람이 아무도 없습니다");
			}
			else{
				String personname = (String) model.getValueAt(book, 2);
				Return(personname, (String) model.getValueAt(book, 0));
				refresh();
			}			
		}
		else
		{
			try {
				FileOutputStream fos = new FileOutputStream("library.txt");  // 프로그램 내의 텍스트파일 생성
				OutputStreamWriter osw = new OutputStreamWriter(fos, "MS949");
				BufferedWriter bw = new BufferedWriter(osw);
				bw.write("Book\r\n");
				for(int i=0; i<countBook; i++){
					bw.write(libBook[i].getName()+"\r\n");
					bw.write(libBook[i].getAuth()+"\r\n");
					bw.write(libBook[i].getPersonname()+"\r\n");
				}
				bw.write("Person\r\n");
				for(int i=0; i<countPerson; i++){
					bw.write(libPerson[i].getName()+"\r\n");
					bw.write(libPerson[i].getAge()+"\r\n");
					bw.write(libPerson[i].getAddress()+"\r\n");
					bw.write(libPerson[i].getStatus()+"\r\n");
					bw.write(libPerson[i].getNumofbook()+"\r\n");
				}
				bw.flush();
				osw.close();
				fos.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.exit(0);
		}
	}
	private void Return(String personname, String bookname) {
		for (int i = 0; i < countPerson; i++) {
			if(libPerson[i].getName().equals(personname)){
				libPerson[i].setNumofbook(libPerson[i].getNumofbook()-1);
				break;
			}
		}
		for (int i = 0; i < countBook; i++) {
			if(libBook[i].getName().equals(bookname)){
				libBook[i].setPersonname(null);
				return;
			}
		}
	}
	private void borrow(String bookname, String personname) {
		for(int i=0; i<countPerson; i++){
			if(libPerson[i].getName().equals(personname)){
				libPerson[i].setNumofbook(libPerson[i].getNumofbook()+1);
				break;
			}
		}
		for(int i=0; i<countBook; i++){
			if(libBook[i].getName().equals(bookname)){
				libBook[i].setPersonname(personname);
				break;
			}
		}		
		refresh();
	}
	private void refresh() {
		model = new DefaultTableModel(category, 0);
		for(int i=0; i<countBook; i++){
			model.addRow(libBook[i].getall());
		}
		model2 = new DefaultTableModel(category2, 0);
		for(int i=0; i<countPerson; i++){
			model2.addRow(libPerson[i].getall());
		}
		bookTable.setModel(model);
		personTable.setModel(model2);
		iFrame.invalidate();
	}
	public static void main(String[] args) {
		MainDisplay MDisMDis=new MainDisplay();
		MDisMDis.load();
	}
}