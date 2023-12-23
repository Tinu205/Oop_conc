//Declaration is by two steps <type> <name> = <value(optional)>
public class Variables{
  public static void main(String args[]){
    
    int num = 12;
    int num2 = 12;
    System.out.println("Sum of "+num+" and "+num2+" = " +(num+num2));
    long longint = 1000000L;
    System.out.println(longint);
    //Strings
    String mystring = "Hello java";
    String oterstring = "Bye java";
    System.out.println(mystring);
    System.out.print(oterstring);
    
    //String concatenation
    String newstring = mystring+oterstring;
    StringBuilder bc = new StringBuilder();
    bc.append("Or ");
    bc.append("this can be used ");
    bc.append("instead of plus concatenation");
    System.out.print("Plus concateted string :"+newstring+"\n");
    System.out.print(bc);
    
  }
}
