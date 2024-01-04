package interfaces;

interface make_sound {
    void noise();
}
class cat implements make_sound{
    public void noise(){
        System.out.println("Meow");
    }
}   

public class inter{
    public static void main(String args[]){
        cat kitty = new cat();
        kitty.noise();
    }
}