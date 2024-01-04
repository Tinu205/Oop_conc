abstract class shape{
  abstract void draw();
}
class circle extends shape{
  public void draw(){
    System.out.println("Drawing a circle");
  }
}

public class abs{
  public static void main(String args[]){
    circle circ = new circle();
    circ.draw();
  }
}
