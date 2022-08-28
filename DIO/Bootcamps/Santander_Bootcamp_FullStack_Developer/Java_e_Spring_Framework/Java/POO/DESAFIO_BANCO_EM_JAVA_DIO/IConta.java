package DESAFIO_BANCO_EM_JAVA_DIO;

public interface IConta {

    void sacar(double valor);

    void depositar(double valor);
    
    void transferir(double valor, Conta contaDestino );
    
    void imprimirExtrato();

}