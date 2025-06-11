package questao4;

import java.time.LocalDate;

public class Data {
	private int dia;
	private int mes;
	private int ano;


	public Data() {
		LocalDate data = LocalDate.now();
		this.ano = data.getYear();
		this.mes = data.getMonthValue();
		this.dia = data.getDayOfMonth();
	}

	public Data(int dia, int mes, int ano) {
		this.dia = dia;
		this.mes = mes;
		this.ano = ano;
	}

	public Data(String data) {
		String[] partes = data.split("/");
		this.dia = Integer.parseInt(partes[0]);
		this.mes = Integer.parseInt(partes[1]);
		this.ano = Integer.parseInt(partes[2]);
	}

	public String formatoPadraoBR() {
		return String.format("%02d/%02d/%04d", dia, mes, ano);
	}


	public static void main(String[] args) {
		Data d1 = new Data(); 
		Data d2 = new Data(4, 6, 2025);
		Data d3 = new Data("04/06/2025");

		System.out.println(d2.formatoPadraoBR());
		System.out.println(d3.formatoPadraoBR());
		System.out.println(d1.formatoPadraoBR());
	}
}

