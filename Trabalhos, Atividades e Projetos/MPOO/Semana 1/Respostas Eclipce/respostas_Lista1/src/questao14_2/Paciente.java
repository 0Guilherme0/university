package questao14_2;

public class Paciente {
	private String nome;
	private int idade;
	private double temperatura;
	
	public Paciente(String nome, int idade, double temperatura) {
		this.nome = nome;
		this.idade = idade;
		this.temperatura = temperatura;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}

	public double getTemperatura() {
		return temperatura;
	}

	public void setTemperatura(double temperatura) {
		this.temperatura = temperatura;
	}
	
}
