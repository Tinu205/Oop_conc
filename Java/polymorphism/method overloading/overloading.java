class sum_of_args{
  public void sum(int a,int b){
    System.out.println("Sum = "+(a+b));
  }
  public void sum(int a, int b, int c){
    System.out.println("Sum = "+(a+b+c));
  }
}

public class overloading{
  public static void main(String args[]){
    sum_of_args two = new sum_of_args();
    System.out.println("Sum of two digits 1,5");
    two.sum(1,5);
    sum_of_args three = new sum_of_args();
    System.out.println("Sum of three digits 1,5,8");
    three.sum(1,5,8);
  }
}
