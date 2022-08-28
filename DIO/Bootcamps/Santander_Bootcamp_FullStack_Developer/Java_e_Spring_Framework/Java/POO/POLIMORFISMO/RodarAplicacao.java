package POLIMORFISMO;

public class RodarAplicacao {
    public static void main(String[] args) {
        ClasseMae[] classes = new ClasseMae[]{new ClasseFilha1(), new ClasseFilha2(), new ClasseMae()};
        
        //Exemplo que pode gerar Polimorfismo
        
        for (ClasseMae classe: classes){
            classe.metodo1();
        }

        System.out.println(" ");

        for (ClasseMae classe: classes){
            classe.metodo2();
        }
        
        System.out.println(" ");


        //Exemplo de sobrescrita
        ClasseFilha2 classeFilha2 = new ClasseFilha2();
        classeFilha2.metodo2();

    }

    
}
