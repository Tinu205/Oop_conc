class Animal {
    void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Dog extends Animal {
    // Overrides the makeSound method in the superclass
    void makeSound() {
        System.out.println("Woof! Woof!");
    }
}

class Cat extends Animal {
    // Overrides the makeSound method in the superclass
    void makeSound() {
        System.out.println("Meow!");
    }
}

public class overriding {
    public static void main(String[] args) {
        Animal dog = new Dog();
        Animal cat = new Cat();

        // Calls the makeSound method in Dog class (runtime polymorphism)
        dog.makeSound();

        // Calls the makeSound method in Cat class (runtime polymorphism)
        cat.makeSound();
    }
}
