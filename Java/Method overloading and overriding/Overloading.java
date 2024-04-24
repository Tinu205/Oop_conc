class Area{
  public double area(double radius){
    return 3.14*radius*radius;
  }
  public int area(int length, int width){
    return length*width;
  }
  public int area(int side){
    return side*side;
  }
}

class Overloading{
  public static void main(String args[]){
    Area calc = new Area();

    double circle = calc.area(5.67);
    System.out.println("The area of circle is : "+circle);

    double square = calc.area(4);
    System.out.println("The are of the square is: "+square);
  }
}
