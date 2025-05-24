package questao14_8;

import java.util.HashMap;

public class Banco {
    private HashMap<Integer, ContaBancaria> contas = new HashMap<>();

    public void adicionarConta(ContaBancaria conta) {
        contas.put(conta.getNumero(), conta);
    }

    public boolean depositar(int numeroConta, double valor) {
        ContaBancaria conta = contas.get(numeroConta);
        if (conta != null) {
            conta.depositar(valor);
            return true;
        }
        return false;
    }

    public boolean sacar(int numeroConta, double valor) {
        ContaBancaria conta = contas.get(numeroConta);
        if (conta != null) {
            return conta.sacar(valor);
        }
        return false;
    }

    public ContaBancaria buscarConta(int numeroConta) {
        return contas.get(numeroConta);
    }
}
