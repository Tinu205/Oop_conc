import java.util.Scanner;

class Single_inheri{
  public static void main(String args[]){
   mustang old = new mustang();
    old.set_model();
    old.get_model();
    old.start();
    old.honk();
    old.stop();
  }
}

class Car{

  public void start(){
    System.out.println("The car is started");
  }

  public void stop(){
    System.out.println("Breaks applied . . . Car turened off");
  }

  public void honk(){
    System.out.println("beep boop ! ! ! ");
  }
}

class mustang extends Car{
  private String model;
  //getter
  public void set_model(){
    System.out.println("Enter the model of your car: ");
    Scanner sc = new Scanner(System.in);
    this.model = sc.nextLine();
    
  }

  //setter 
  public void get_model(){
    System.out.println("The model of your car is: "+this.model);
  }

}
