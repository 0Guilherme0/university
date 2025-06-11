package entidades;

import java.util.Calendar;

import util.TabelaPrecos;

public class Carro extends Veiculo {
	private int numeroProtas;
	private boolean isArCondicionado;
	


	public Carro(String marca, String modelo, int ano, String descricao, EquipamentoOpcional opcional, String plca,
			boolean isLocado, int numeroProtas, boolean isArCondicionado) {
		super(marca, modelo, ano, descricao, opcional, plca, isLocado);
		this.numeroProtas = numeroProtas;
		this.isArCondicionado = isArCondicionado;
		calcularValorDiaria();
	}
	

	public Carro(String marca, String modelo, int ano, EquipamentoOpcional opcional, String plca, boolean isLocado,
			int numeroProtas, boolean isArCondicionado) {
		super(marca, modelo, ano, opcional, plca, isLocado);
		this.numeroProtas = numeroProtas;
		this.isArCondicionado = isArCondicionado;
		calcularValorDiaria();
	}


	@Override
	public void calcularValorDiaria() {
		double valor = TabelaPrecos.VALOR_REF_CARRO;
		int anoAtual = Calendar.getInstance().get(Calendar.YEAR);
		
		if (anoAtual == this.ano) {
			valor = valor * 1.1;
		}
		
		this.setValorDiaria(valor);
	}


	@Override
	public String toString() {
		return "Dados do Veiculo: marca=" + marca + ", modelo=" + modelo + ", ano=" + ano + ", descricao=" + descricao
				+ ", opcional=" + opcional + ", plca=" + placa + ", isLocado=" + isLocado + ", valorDiaria="
				+ this.getValorDiaria() + ", numeroFrota=" + this.getNumeroFrota() 
				+ "[numeroProtas=" + numeroProtas + ", isArCondicionado=" + isArCondicionado;
	}




	
	

	
	
	
	
}
