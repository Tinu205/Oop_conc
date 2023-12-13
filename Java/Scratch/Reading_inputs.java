//Must import java.util.scanner
import java.util.Scanner;
public class Reading_inputs{
  public static void main(String args[]){
    System.out.print("Enter a integer: ");
    
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    sc.close();

    System.out.println("You have entered: "+num);
    
  }
}
