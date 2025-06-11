package app;

import entidades.BaseDados;
import entidades.Carro;
import entidades.EquipamentoOpcional;
import entidades.Moto;
import entidades.Simulador;

public class app {
	public static void main(String[] args) {
		BaseDados base = new BaseDados();
		base.createBase();
		
		Carro c1 = new Carro(
				"Honda", "Civic", 2020, "Seguro 48h grátis",
				new EquipamentoOpcional(true, true, false), "ABC1234", false,
				4, true);
		base.addVeiculo(c1);


		Carro c2 = new Carro(
				"Honda", "HR-V", 2025, "Seguro 48h grátis",
				new EquipamentoOpcional(true, true, true), "XYZ1234", false,
				4, true);
		base.addVeiculo(c2);

		base.addVeiculo(new Moto(
				"Yamaha", "R15", 2024, null,
				new EquipamentoOpcional(false, true, true), "ZZZ0000", false,
				150));


		base.addVeiculo(new Moto(
				"Honda", "CB650R", 2025, null,
				new EquipamentoOpcional(false, true, true), "AAA1122", false,
				650));
		
		base.addVeiculo(new Moto(
				"Honda", "Hornet 500", 2022, null,
				new EquipamentoOpcional(false, true, true), "BBB9999", false,
				470));

		
		Simulador simulador = new Simulador();
		simulador.simularAlugueis(10);
		
		base.buscarVeiculo(c2.getPlca()).setOpcional(null);
		base.buscarVeiculo(c2.getPlca()).setLocado(false);
		base.buscarVeiculo(c2.getPlca()).descricao = null;
		
		base.removerVeiculo(base.buscarVeiculo("BBB9999"));
		
		simulador.simularAlugueis(10);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}
}
