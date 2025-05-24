package entidades;

public class Fruta {
    public String nome;
    public boolean temCasca;
    public boolean temCaroco;
    public boolean podeSerComidaDiretamente;
    public boolean foiComida;

    public Fruta(String nome, boolean temCasca, boolean temCaroco, boolean podeSerComidaDiretamente) {
        this.nome = nome;
        this.temCasca = temCasca;
        this.temCaroco = temCaroco;
        this.podeSerComidaDiretamente = podeSerComidaDiretamente;
        this.foiComida = false;
    }

    public boolean retirarCaroco() {
        if (temCaroco) {
            temCaroco = false;
            System.out.println("Caroço retirado de " + nome + ".");
            return true;
        }
        return false;
    }

    public boolean retirarCasca() {
        if (temCasca) {
            temCasca = false;
            System.out.println("Casca retirada de " + nome + ".");
            return true;
        }
        return false;
    }

    public boolean comerFruta() {
        if (podeSerComidaDiretamente) {
            foiComida = true;
            System.out.println(nome + " comida diretamente.");
            return true;
        } else {
            retirarCaroco();
            retirarCasca();

            if (!temCasca && !temCaroco) {
                foiComida = true;
                System.out.println(nome + " comida após retirar casca e/ou caroço.");
                return true;
            } else {
            	System.out.println("Não consigo comer a fruta. ");
            	return false;
            }
        }
    }

    public String status() {
        return "Fruta: " + nome +
               "\nTem casca: " + (temCasca ? "Sim" : "Não") +
               "\nTem caroço: " + (temCaroco ? "Sim" : "Não") +
               "\nPode ser comida diretamente: " + (podeSerComidaDiretamente ? "Sim" : "Não") +
               "\nFoi comida: " + (foiComida ? "Sim" : "Não");
    }

}
