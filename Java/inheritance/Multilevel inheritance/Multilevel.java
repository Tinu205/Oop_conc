class vehicle{
  private String make,model;
  private int year;
  
  public void set_make(String make){
    this.make = make;
  }

  public void set_model(String model){
    this.model = model;
  }

  public void set_year(int year){
    this.year = year;
  }

  public void print_datas(){
    System.out.println("Make: "+this.make+"\n"+"Model: "+this.model+"\n"+"Year: "+this.year);
  }

  public void start(){
    System.out.println("The Vehicle is started");
  } 

  public void stop(){
    System.out.println("Turning off the engine");
  }

}

class car extends vehicle{
  private int numDoors;

  public void set_numDoors(int doors){
    this.numDoors = doors;
  }

  public void display_doors(){
    System.out.println("Number of doors: "+this.numDoors);
  }
  
  public void accelearte(){
    System.out.println("Accelerating. . .");
  }

  public void break_v(){
    System.out.println("Breaks applied !!");
  }
}

class sportscar extends car{
  private int topspeed;

  public void set_ts(int speed){
    this.topspeed = speed;
  }

  public void activateturbo(){
    System.out.println("Turbo activated achiving topspeed ! ! !");
  }
}

class Multilevel{

  public static void main(String args[]){

    printf("Runnting sportscar class ");
    sportscar_class();

    printf("!-------------------!");

    printf("Running car class");
    car_class();

    printf("!-------------------!");
    printf("Running vechile class");
    vehicle_class();

  }
  
  public static void printf(String cont){
    System.out.println("\n"+cont+"\n");
  }

  public static void sportscar_class(){
    sportscar nissan = new sportscar();
    nissan.start();                       
    nissan.accelearte();                
    nissan.activateturbo();
    nissan.break_v();
    nissan.stop();
  }

  public static void car_class(){
    car sedan = new car();
    sedan.start();
    sedan.accelearte();
    sedan.break_v();
    sedan.stop();
  }

  public static void vehicle_class(){
    vehicle tractor = new vehicle();
    tractor.start();
    tractor.stop();
  }
}
