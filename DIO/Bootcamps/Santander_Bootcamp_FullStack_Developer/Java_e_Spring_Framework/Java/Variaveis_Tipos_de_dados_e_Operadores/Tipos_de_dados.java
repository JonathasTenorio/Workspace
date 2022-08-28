public class Tipos_de_dados {

    /**
     Criando variáveis de todos os tipos de dados primitivos e string.
     */
    public static void main(String[] args){
        byte b1 = 10;
        byte b2 = 20;

        short s1 = 20000;
        //short s2 = 40000; ultrapassou o limite que o short permite.

        //int i1 = -10000000000000; ultrapassou o limite inferior que o int permite.
        int i2 = 28500;


        long l1 = 10000000000000000L;
        long l2 = 204000058030123208L;
    
        //float f1 = 4.5; tipos floats precisam terminar cm F no final do numero
        float f2 = 10.68f;

        double d1 = 85.69;
        double d2 = 99.84d;

        char c1 = 'W';
        //char c2 = 'Tw'; só armazena um caracterer.
        char c3 =  '\u0057';

        String st1 = "Fulano";
        String st2 = "Cicrano";
        
        boolean bol1 = true;
        boolean bol2 = false;

        System.out.println(b1);
        System.out.println(b2);
        System.out.println(s1);
        System.out.println(i2);
        System.out.println(l1);
        System.out.println(l2);
        System.out.println(f2);
        System.out.println(d1);
        System.out.println(d2);
        System.out.println(c1);
        System.out.println(c3);
        System.out.println(st1);
        System.out.println(st2);
        System.out.println(bol1);
        System.out.println(bol2);
    }

}
