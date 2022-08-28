package ESTRUTURA_BASICA_DA_OO;

public class RodarAplicacao {
    public static void main(String[] args) {

        carro carro1 =  new carro();

        carro1.setCor("Azul");
        carro1.setModelo("Mouza");
        carro1.setCapacidadeTanque(50);

        System.out.println(carro1.getCor());
        System.out.println(carro1.getModelo());
        System.out.println(carro1.getCapacidadeTanque());
        System.out.println(carro1.totalValorTanque(6.39));

        carro carro2 = new carro("Cinza", "Mercedez", 66);
        
        System.out.println(carro2.getCor());
        System.out.println(carro2.getModelo());
        System.out.println(carro2.getCapacidadeTanque());
        System.out.println(carro2.totalValorTanque(6.46));
    }
}
