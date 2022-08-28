package DESAFIO_BANCO_EM_JAVA_DIO;

public class ContaPoupanca extends Conta{
    
    @Override
    public void imprimirExtrato() {
        System.out.println("=== Extrato Conta Poupança ===");
        super.imprimirInfosComuns();
        
    }

}
