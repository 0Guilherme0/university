package questao6;

import java.sql.Date;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class Compra {
	private static int idcount = 0;
	private int id;
	private LocalDateTime date;
	private static ArrayList<Produto> produtos; 
	private double desconto;
	private double valorTotal;

	public Compra(Produto produto, double desconto, double valorTotal, LocalDateTime date) {
		this.desconto = desconto;
		this.valorTotal = valorTotal;
		this.date = date;
		idcount++;
		this.id = idcount;
		produtos = new ArrayList<Produto>();
		produtos.add(produto);
	}
	
	public Compra(int id, double desconto, double valorTotal) {
		this.id = id;
		this.desconto = desconto;
		this.valorTotal = valorTotal;
	}


	public static void addProduto(Produto produto) {
		produtos.add(produto);
	}

	@Override
	public String toString() {
		return "Compra [id=" + id + ", desconto=" + desconto + ", valorTotal=" + valorTotal + "]";
	}

	public int getId() {
		return id;
	}

	public static ArrayList<Produto> getProdutos() {
		return produtos;
	}

	public double getDesconto() {
		return desconto;
	}

	public double getValorTotal() {
		return valorTotal;
	}
	
	
	
}
