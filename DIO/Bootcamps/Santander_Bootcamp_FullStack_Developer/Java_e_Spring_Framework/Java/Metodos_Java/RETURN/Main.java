package RETURN;

public class Main {
    
    public static void main(String[] args) {

        System.out.println("Exercício de Retornos");

        double areaQuadrado = Quadrilateros.area(3);
        System.out.println(areaQuadrado);

        double areaRetangulo = Quadrilateros.area(5, 6);
        System.out.println(areaRetangulo);

        double areaTrapezio = Quadrilateros.area(7, 3, 5);
        System.out.println(areaTrapezio);



    }
}
