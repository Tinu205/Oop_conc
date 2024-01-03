class Employee {
    private String name, jobDisc;
    public int empID;

    public void setName(String name) {
        this.name = name;
    }

    public void setJobDisc(String disc) {
        this.jobDisc = disc;
    }

    public void setEmpID(int id) {
        this.empID = id;
    }

    public void displayInfo() {
        System.out.println("Name: " + this.name + "\n" + "Job Description: " + this.jobDisc + "\n" + "Employee ID: " + this.empID);
    }
}

class Manager extends Employee {
    // Specific attributes or behaviors for the Manager class can be added here
}

class Developer extends Employee {
    // Specific attributes or behaviors for the Developer class can be added here
}

class Salesperson extends Employee {
    // Specific attributes or behaviors for the Salesperson class can be added here
}

class Hierarchical {
    public static void main(String args[]) {
        System.out.println("Calling Manager class:");
        managerClass();
    }

    public static void managerClass() {
        Manager mano = new Manager();
        mano.setName("Mano");
        mano.setEmpID(01);
        mano.setJobDisc("Managing the employees");
        mano.displayInfo();
    }
}

