package questao14_8;

public class ContaBancaria {
    private int numConta;
    private String nome;
    private double saldo;

    public ContaBancaria(int numero, String titular) {
        this.numConta = numero;
        this.nome = titular;
        this.saldo = 0.0;
    }

    public int getNumero() {
        return numConta;
    }

    public String getTitular() {
        return nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public boolean sacar(double valor) {
        if (valor > 0 && saldo >= valor) {
            saldo -= valor;
            return true;
        }
        return false;
    }
}
