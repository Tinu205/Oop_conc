import java.util.Scanner;

class person{
  private String  name;
  private int age;
  
  //setter method to set variable
  public void set_name(String name){
    this.name = name;
  }

  public void set_age(int age){
    this.age = age;
  }
  
  //getter method to get the variable
  public void get_name(){
    System.out.println("Name : "+ this.name);
  }

  public void get_age(){
    System.out.println("Age  :"+ this.age);
  }
}

public class encapsulation{
  public static void main(String args[]){
    person ps  = new person();
    ps.set_name("Gojo");
    ps.set_age(18);
    ps.get_name();
    ps.get_age();
  }
}
