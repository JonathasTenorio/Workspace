package UPCASTING;

public class RodarAplicacao {
    public static void main(String[] args) {
        // Criando objetos da classe do tipo funcionario.

        Funcionario funcionario = new Funcionario();

        //upcasting

        Funcionario gerente = new Gerente();
        Funcionario vendedor = new Vendedor();
        Funcionario faxineiro = new Faxineiro();

        // Downcasting

        //Gerente gerente = new Funcionario();
        Vendedor vendedor_ = (Vendedor) new Funcionario();
    }
}
