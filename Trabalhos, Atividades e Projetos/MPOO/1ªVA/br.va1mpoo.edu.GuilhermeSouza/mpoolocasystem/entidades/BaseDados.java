package entidades;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.concurrent.ConcurrentHashMap;

public class BaseDados {
	protected static ArrayList<Veiculo> veiculos;

	public void createBase() {
		veiculos = new ArrayList<Veiculo>();
		inicializarBase();

	}

	private void inicializarBase() {
		Carro c1 = new Carro(
				"Honda", "Civic", 2020, "Seguro 48h grátis",
				new EquipamentoOpcional(true, true, false), "ABC1234", false,
				4, true);
		addVeiculo(c1);


		Carro c2 = new Carro(
				"Honda", "HR-V", 2025, "Seguro 48h grátis",
				new EquipamentoOpcional(true, true, true), "XYZ1234", false,
				4, true);
		addVeiculo(c2);

		Moto m1 = new Moto(
				"Yamaha", "R15", 2024, null,
				new EquipamentoOpcional(false, true, true), "ZZZ0000", false,
				150);
		addVeiculo(m1);


		Moto m2 = new Moto(
				"Honda", "CB650R", 2025, null,
				new EquipamentoOpcional(false, true, true), "AAA1122", false,
				650);
		addVeiculo(m2);


		Moto m3 = new Moto(
				"Honda", "Hornet 500", 2022, null,
				new EquipamentoOpcional(false, true, true), "BBB9999", false,
				470);		
		addVeiculo(m3);
		
	}


	public Veiculo buscarVeiculo(String placa) {
		for (Veiculo currentVeiculo : veiculos) {
			if (currentVeiculo.getPlca().equalsIgnoreCase(placa)) {
				return currentVeiculo;
			}
		}
		return null;
	}

	public boolean isVeiculo(String placa) {
		if (buscarVeiculo(placa) != null) {
			return true;
		}
		return false;
	}

	public boolean isVeiculo(Veiculo veiculo) {
		if (buscarVeiculo(veiculo.getPlca())!=null) {
			return true;
		}
		return false;
	}

	public boolean addVeiculo(Veiculo veiculo) {
		if (buscarVeiculo(veiculo.placa) == null) {
			if (veiculos.add(veiculo)) {
				return true;
			}
		}

		return false;
	}

	public boolean removerVeiculo(Veiculo veiculo) {
		if (veiculos.remove(buscarVeiculo(veiculo.placa))){
			return true;
		}
		return false;

	}

	public ArrayList<Veiculo> listVeiculosDisponiveis(){
		ArrayList<Veiculo> currentVeiculos = new ArrayList<Veiculo>();
		for (Veiculo currentVeiculo : veiculos) {
			if (!currentVeiculo.isLocado) {
				currentVeiculos.add(currentVeiculo);
			}

		}
		return currentVeiculos;
	}

	public ArrayList<Carro> listCarrosDisponiveis(){
		ArrayList<Carro> carrosTemp = new ArrayList<Carro>();
		for (Veiculo currentVeiculo : veiculos) {
			if (currentVeiculo instanceof Carro) {
				if (!currentVeiculo.isLocado) {		
					carrosTemp.add((Carro) currentVeiculo);
				}
			}
		}
		return carrosTemp;
	}

	public ArrayList<Moto> listMotosDisponiveis(){
		ArrayList<Moto> motosTemp = new ArrayList<Moto>();
		for (Veiculo currentVeiculo : veiculos) {
			if (currentVeiculo instanceof Moto) {
				if (!currentVeiculo.isLocado) {
					motosTemp.add((Moto)currentVeiculo);
				}
			}
		}
		return motosTemp;
	}

	public static ArrayList<Veiculo> getVeiculos() {
		return veiculos;
	}

}

