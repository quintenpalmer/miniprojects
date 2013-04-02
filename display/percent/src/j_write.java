import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class j_write{
	public static void main(String[] args){
		int num = 100;
		int wait = 50;
		try{
			BufferedReader in = new BufferedReader(new FileReader("../settings.txt"));
			num = Integer.parseInt(in.readLine());
			wait = Integer.parseInt(in.readLine());
			in.close();
		}
		catch(IOException e){
			System.out.println("Could not open file");
		}
		try{
			for(int i=0;i<=num;i++){
				System.out.print("\r"+Integer.toString(i)+"%");
					Thread.sleep(wait);
			}
		}
		catch(InterruptedException e){
			Thread.currentThread().interrupt();
		}
		System.out.print("\n");
	}
}
