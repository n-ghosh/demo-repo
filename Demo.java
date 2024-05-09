
public class Demo {
    public static void main(String[] args) {
        // String dash = "-"*2;
        String border = "\n" + "-------" + "\n";
        System.out.println(border + "hi world" + border);
        for (String string : args) {
            System.out.println("String: " + string);
        }
    }
}