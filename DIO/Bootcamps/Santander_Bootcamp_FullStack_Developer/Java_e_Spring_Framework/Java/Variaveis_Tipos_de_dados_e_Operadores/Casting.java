public class Casting {
    public static void main(String[] args) {
        byte b1;
        short s1 = 1000;
        b1 = (byte) s1;

        System.out.println("Downcast");
        System.out.println(s1 + " " + b1);
        
        long l1;
        int i = 10;

        l1 = i;

        System.out.println("Upcast");
        System.out.println(l1 + " " + i);

        int i2;
        long l2  = 100000000000000L;
        
        i2 = (int)l2;
        
        System.out.println("Downcast");
        System.out.println(l2 + " " + i2);

        int i3;
        long l3 = 1000L;

        i3 = (int)l3;

        System.out.println("Downcast ");
        System.out.println(l3 + " " + i3);
    }
}
