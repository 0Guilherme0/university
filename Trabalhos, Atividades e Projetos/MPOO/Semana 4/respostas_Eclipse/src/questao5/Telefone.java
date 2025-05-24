package questao5;

public class Telefone {
    private int ddi;
    private int ddd;
    private int numero;

    public Telefone(int ddi, int ddd, int numero) {
        this.ddi = ddi;
        this.ddd = ddd;
        this.numero = numero;
    }

    public int getDdi() { return ddi; }


	public int getDdd() { return ddd; }

    public int getNumero() { return numero; }
    
    @Override
    public String toString() {
    	return "Telefone [ddi=" + ddi + ", ddd=" + ddd + ", numero=" + numero + "]";
    }
}


