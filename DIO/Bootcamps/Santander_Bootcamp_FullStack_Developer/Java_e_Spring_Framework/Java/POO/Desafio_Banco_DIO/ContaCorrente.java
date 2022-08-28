package DESAFIO_BANCO_EM_JAVA_DIO;

public class ContaCorrente extends Conta {

    @Override
    public void imprimirExtrato() {
        System.out.println("=== Extrato Conta Corrente ===");
        super.imprimirInfosComuns();
        
    }
   

}
