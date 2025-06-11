package entidades;

import java.util.Calendar;

import util.TabelaPrecos;

public class Moto extends Veiculo {
	private int cilindradas;

	
	public Moto(String marca, String modelo, int ano, String descricao, EquipamentoOpcional opcional, String plca,
			boolean isLocado, int cilindradas) {
		super(marca, modelo, ano, descricao, opcional, plca, isLocado);
		this.cilindradas = cilindradas;
		calcularValorDiaria();
	}

	
	public Moto(String marca, String modelo, int ano, EquipamentoOpcional opcional, String plca, boolean isLocado,
			int cilindradas) {
		super(marca, modelo, ano, opcional, plca, isLocado);
		this.cilindradas = cilindradas;
		calcularValorDiaria();
	}

	@Override
	public void calcularValorDiaria() {
		double valor = TabelaPrecos.VALOR_REF_MOTO;
		int anoAtual = Calendar.getInstance().get(Calendar.YEAR);
		
		if (anoAtual == this.ano) {
			valor += valor * 1.1;
		}
		
		this.setValorDiaria(valor);
	}

	@Override
	public String toString() {
		return "Dados do Veiculo: marca=" + marca + ", modelo=" + modelo + ", ano=" + ano + ", descricao=" + descricao
				+ ", opcional=" + opcional + ", plca=" + placa + ", isLocado=" + isLocado + ", valorDiaria=" + this.getValorDiaria() 
				+ ", numeroFrota=" + this.getNumeroFrota() + cilindradas;
	}

	
	
	
	
	
}
