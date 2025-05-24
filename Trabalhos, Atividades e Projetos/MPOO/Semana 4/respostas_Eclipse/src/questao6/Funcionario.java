package questao6;

import java.time.LocalDateTime;

public class Funcionario {
	private String nome;
	private String cpf;
	private String matricula;

	public Funcionario(String nome, String cpf, String matricula) {
		this.nome = nome;
		this.cpf = cpf;
		this.matricula = matricula;
	}

	public double darDesconto(Produto produto) {
		double desconto = produto.getPreco() * 0.1;
		desconto = desconto * produto.getQuantidade();
		return desconto;
	}

	public void registrarCompra(Produto produto, boolean hasDesconto) {
		LocalDateTime data =  LocalDateTime.now();
		if (hasDesconto) {
			double desconto = darDesconto(produto);
			double valorTotal = produto.getQuantidade() * produto.getPreco() - desconto;
			Compra compra = new Compra(produto, desconto, valorTotal, data);
			
			// base
			// mensagem
		} else {
			double valorTotal = produto.getQuantidade() * produto.getPreco();
			Compra compra = new Compra(produto, 0, valorTotal, data);
			// base
			// mensagem
		}
//		imprimirResumoCompra()
	}

}
