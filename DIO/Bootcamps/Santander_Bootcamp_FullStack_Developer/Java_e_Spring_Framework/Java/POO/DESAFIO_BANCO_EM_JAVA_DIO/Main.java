package DESAFIO_BANCO_EM_JAVA_DIO;

public class Main {
    public static void main(String[] args) {
        
        Conta cc = new ContaCorrente();
        Conta poupanca = new ContaPoupanca();

        cc.imprimirExtrato();
        poupanca.imprimirExtrato();
    }
}
