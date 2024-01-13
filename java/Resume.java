import java.util.Scanner;
public class ResumeBuilder {
    public static void main(String[] args) {
        Scanner kel = new Scanner(System.in);
        System.out.print("Enter your full name: ");
        String name = kel.nextLine();
        System.out.print("Enter your Email Address: ");
        String email = kel.nextLine();
        System.out.print("Enter your phone number: ");
        String phone = kel.nextLine();
        System.out.print("Enter your address: ");
        String address = kel.nextLine();
        System.out.print("Enter your course: ");
        String course = kel.nextLine();
        System.out.print("Enter your dream job: ");
        String job = kel.nextLine();
        System.out.println("\n Resume");
        System.out.println("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _");
        System.out.println("Name    : " + name);
        System.out.println("Email   : " + email); 
        System.out.println("Phone   : " + phone);
        System.out.println("Address : " + address);
        System.out.println("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _");
        System.out.println("Course : " + course);
        System.out.println("Dream Job : " + job);   
    }
}
