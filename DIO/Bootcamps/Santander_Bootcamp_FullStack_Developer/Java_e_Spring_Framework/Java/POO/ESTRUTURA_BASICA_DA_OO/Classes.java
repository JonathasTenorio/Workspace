package ESTRUTURA_BASICA_DA_OO;
// Atividade 1, criar a classe carro.
class carro{
    // Atividade 2, criar 3 atributos, sendo eles: Cor, Modelo e a Cpacidade do tanque.
    String cor;
    String modelo;
    int capacidadeTanque;


    // Atividade 3, construir um método e passar duas sobrecargas. Utilizar GET e SET se possível.

    // construtor aqui

    carro(String cor, String modelo, int capacidadeTanque) {
        this.cor = cor;
        this.modelo = modelo;
        this.capacidadeTanque = capacidadeTanque;
    }

    carro() {

    }


    void setCor(String cor){
        this.cor = cor;
    }

    String getCor() {
        return cor;
    }

    void setModelo(String modelo){
        this.modelo = modelo;
    }

    String getModelo(){
        return modelo;
    }

    void setCapacidadeTanque(int capacidadeTanque){
        this.capacidadeTanque = capacidadeTanque;
    }

    int getCapacidadeTanque(){
        return capacidadeTanque;
    }

    // metodo para realizar operações

    double totalValorTanque(double valorCombustivel){
        return capacidadeTanque * valorCombustivel;
    }

}