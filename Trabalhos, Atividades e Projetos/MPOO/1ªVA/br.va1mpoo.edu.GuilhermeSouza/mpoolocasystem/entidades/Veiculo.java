package entidades;

public abstract class Veiculo {
	public String marca;
	public String modelo;
	public int ano;
	public String descricao;
	public EquipamentoOpcional opcional;
	String placa;
	protected boolean isLocado;
	private double valorDiaria;
	private int numeroFrota;
	private static int numeroProximo = 0;
	
	public Veiculo(String marca, String modelo, int ano, String descricao, EquipamentoOpcional opcional, String plca,
			boolean isLocado) {
		this.marca = marca;
		this.modelo = modelo;
		this.ano = ano;
		this.descricao = descricao;
		this.opcional = opcional;
		this.placa = plca;
		this.isLocado = isLocado;
		numeroFrota = numeroProximo;
		numeroProximo += 1;
	}

	public Veiculo(String marca, String modelo, int ano, EquipamentoOpcional opcional, String plca, boolean isLocado) {
		this.marca = marca;
		this.modelo = modelo;
		this.ano = ano;
		this.opcional = opcional;
		this.placa = plca;
		this.isLocado = isLocado;
	}
	
	
	public abstract void calcularValorDiaria();
	
	public int getNumeroFrota() {
		return numeroFrota;
	}

	public double getValorDiaria() {
		return valorDiaria;
	}
	
	public void setValorDiaria(double valorDiaria) {
		this.valorDiaria = valorDiaria;
	}
	
	public String getPlca() {
		return placa;
	}
	
	public void setOpcional(EquipamentoOpcional opcional) {
		this.opcional = opcional;
	}

	public void setLocado(boolean isLocado) {
		this.isLocado = isLocado;
	}
	
	
	
	
}
