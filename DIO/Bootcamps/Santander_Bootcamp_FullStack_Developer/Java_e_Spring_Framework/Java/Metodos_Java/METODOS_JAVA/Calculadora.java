package METODOS_JAVA;

public class Calculadora {
    
    public static void main(String[] args) {
    
    }

    public static void soma(double n1, double n2) {
        double resultado = n1 + n2;
        System.out.println("A soma de " + n1 + " mais " + n2 + " é " + resultado);
    }

    public static void sub(double n1, double n2) {
        double resultado = n1 - n2;
        System.out.println("A subtracao de " + n1 + " menos " + n2 + " é " + resultado);
    }

    
    public static void mult(double n1, double n2) {
        double resultado = n1 * n2;
        System.out.println("A multiplicação de " + n1 + " e " + n2 + " é " + resultado);
    }

    
    public static void div(double n1, double n2) {
        double resultado = n1 / n2;
        System.out.println("A divisão de " + n1 + " por " + n2 + " é " + resultado);
    }
    
}