// Interface 1
interface Mother {
    void eyeColor();
}

// Interface 2
interface Father {
    void hairColor();
}

// Class implementing both interfaces
class Child implements Mother, Father {
    @Override
    public void eyeColor() {
        System.out.println("The inherited eye color is green");
    }

    @Override
    public void hairColor() {
        System.out.println("The inherited hair color is black");
    }
}

// Main class
public class Multiple {
    public static void main(String args[]) {
        Child baby = new Child();
        baby.eyeColor();
        baby.hairColor();
    }
}

