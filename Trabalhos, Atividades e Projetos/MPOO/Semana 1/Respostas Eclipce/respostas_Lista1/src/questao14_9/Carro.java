package questao14_9;

public class Carro {
	public String marca;
	public String modelo;
	public int velAtual;
	
	public Carro(String marca, String modelo, int velAtual) {
		this.marca = marca;
		this.modelo = modelo;
		this.velAtual = velAtual;
	}
	
	public void acelerar() {
		this.velAtual += 1;
		System.out.println(this.velAtual);
	}
	public void freiar() {
		this.velAtual -= 1;
		System.out.println(this.velAtual);
	}
	
	public void acelerarAte(int ate) {
	    if (this.velAtual < ate) {
	        while (this.velAtual < ate) {
	            acelerar();
	        }
	    } else {
	        freiarAte(ate);
	    }
	}

	public void freiarAte(int ate) {
	    if (this.velAtual > ate) {
	        while (this.velAtual > ate) {
	            freiar();
	        }
	    } else {
	        acelerarAte(ate);
	    }
	}

	
	
}
