package questao6;

import java.util.ArrayList;

public abstract class  BaseDados {
	private static ArrayList<Compra> compras;
	private static ArrayList<Venda> vendas;
	
	public void createBase() {
		compras = new ArrayList<Compra>();
		vendas = new ArrayList<Venda>();
	}
	
	public Compra buscarCompra(Compra compra) {
		for (Compra currentCompra: compras) {
			if (compra.equals(currentCompra)) {
				return compra;
			}
		}
		return null;
	}
	
	public Compra buscarCompra(int id) {
		for (Compra currentCompra: compras) {
			if (id == currentCompra.getId()) {
				return currentCompra;
			}
		}
		return null;
	}
	
	public boolean adicionarCompra() {
		
	}
	
	
}
