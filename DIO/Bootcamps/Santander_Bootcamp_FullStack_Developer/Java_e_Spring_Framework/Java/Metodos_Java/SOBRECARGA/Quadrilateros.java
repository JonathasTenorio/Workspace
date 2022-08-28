package SOBRECARGA;

public class Quadrilateros {
    
    public static void area(double lado) {
        System.out.println("Área do quadrilatero é " + lado *lado);
    }

    public static void area(double lado1, double lado2) {
        System.out.println("Área do quadrilatero é " + lado1 *lado2);
    }

    public static void area(double baseMaior, double baseMenor, double altura) {
        System.out.println("Área do quadrilatero é " + ((baseMaior+baseMenor)*altura)/2);
    }
}
