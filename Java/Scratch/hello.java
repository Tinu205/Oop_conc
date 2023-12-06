public class hello{
  public static void main(String args[]){
    System.out.println("Hello world");
    System.out.println(
      " Integer: " + 10  +
      " Double : " + 1.2 +
      " Boolean: " + true
    );
    //To print without new lines use System.out.print();
    System.out.print("Hello ");
    System.out.print("world");
    //Formatted strings is also supported in java

    System.out.printf("\n%.5f",1.234567890);
  }
}
