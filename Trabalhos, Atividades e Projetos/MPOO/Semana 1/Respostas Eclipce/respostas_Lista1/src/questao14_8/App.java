package questao14_8;

public class App {
	public class Main {
	    public static void main(String[] args) {
	        Banco banco = new Banco();

	        ContaBancaria conta1 = new ContaBancaria(1001, "Alice");
	        banco.adicionarConta(conta1);

	        banco.depositar(1001, 500);
	        System.out.println("Saldo: " + banco.buscarConta(1001).getSaldo());

	        boolean saque = banco.sacar(1001, 200);
	        System.out.println("Saldo após saque: " + banco.buscarConta(1001).getSaldo());

	    }
	}
}
