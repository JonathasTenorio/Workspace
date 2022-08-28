package METODOS_JAVA;

public class CalcJava {

    public static void main(String[] args) {
        

        System.out.println("Somas");
        Calculadora.soma(3, 6);
        Calculadora.soma(31, 22);
        Calculadora.soma(312, 603);
        Calculadora.soma(6785, 123);
        Calculadora.soma(123.1, 123.231);

        System.out.println("Subtrações");
        Calculadora.sub(3, 6);
        Calculadora.sub(31, 22);
        Calculadora.sub(312, 603);
        Calculadora.sub(6785, 123);
        Calculadora.sub(123.1, 123.231);

        System.out.println("Multiplicações");
        Calculadora.mult(3, 6);
        Calculadora.mult(31, 22);
        Calculadora.mult(312, 603);
        Calculadora.mult(6785, 123);
        Calculadora.mult(123.1, 123.231);

        System.out.println("Divisões");
        Calculadora.div(3, 6);
        Calculadora.div(31, 22);
        Calculadora.div(312, 603);
        Calculadora.div(6785, 123);
        Calculadora.div(123.1, 123.231);


    }
}