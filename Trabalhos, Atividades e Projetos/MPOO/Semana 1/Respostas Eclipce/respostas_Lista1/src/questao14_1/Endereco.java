package questao14_1;

public class Endereco {
	private String rua;
	private int numCasa;
	private String cidade;
	private String bairro;
	private String cep;
	
	public Endereco(String rua, int numCasa, String cidade, String bairro, String cep) {
		this.rua = rua;
		this.numCasa = numCasa;
		this.cidade = cidade;
		this.bairro = bairro;
		this.cep = cep;	
	}

	@Override
	public String toString() {
		return "Endereco: " + rua + ", " + numCasa + ", " + cidade + ", " + bairro + ", "+ cep;
	}
}
