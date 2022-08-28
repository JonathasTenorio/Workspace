public class Operadores_aritmeticos {
    public static void main(String[] args) {
    
        System.out.println("PreFixado");
        preFix();
        
        System.out.println("Aritimetico");
        artimetico();

        
        System.out.println("Atribuicao");
        atribuicao();

    }
    private static void preFix() {
        int k = 10;
        int i = ++k;
        int j = k--;

        int x = k;
        System.out.println("i " + i);
        System.out.println("j " + j);
        System.out.println("k " + x);
    }

    private static void artimetico() {
        int a = 10;
        int b = 20;
        int c = 30;
        int d = 40;
        int e = 50;

        int r1 = a+b;
        int r2 = c-a;
        int r3 = d*b;
        int r4 = e/a;
        int r5 = c%b;

        System.out.println("a+b " + r1);
        System.out.println("c-a " + r2);
        System.out.println("d*b " + r3);
        System.out.println("e/a " + r4);
        System.out.println("c%b " + r5);
    }

    private static void atribuicao() {
        int i = 500;
        float f = 15f;
        short s = 30;
        long l = 3400L;
        double d = 3490d;

        
        System.out.println("d " + d);
        
        i += 5;
        s -= 3;
        d /= 2.7;
        l *= 3;

        
        System.out.println("i " + i);
        System.out.println("s " + s);
        System.out.println("d " + d);
        System.out.println("l " + l);
        System.out.println("f " + f);
    }


}
