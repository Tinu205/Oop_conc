class Arrays{
  public static void main(String args[]){
    String[] nsa = new String[5];
    int[] nia = new int[4];
    nsa[0] = "Batman";
    nia[0] = 100;
    for(int i = 0;i<5;i++){
      System.out.println("value of nsa @"+i+"="+nsa[i]);
    }
    //Other way to declare array
    int[] y = {100,200,300,400,500};
    String[] str = {"Batman","Superman","Captain America","Black panther"};
    //System.out.println(y);
    //System.out.println(str);
    for(int i = 0;i<5;i++){
      System.out.println(y[i]);
    }
    for(int i=0; i<4; i++){
      System.out.println(str[i]);
    }
  }
}
