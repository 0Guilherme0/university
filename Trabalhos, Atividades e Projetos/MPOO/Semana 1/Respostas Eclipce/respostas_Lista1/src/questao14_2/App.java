package questao14_2;

public class App {
	public static void main(String[] args) {	
//		14.2
		Paciente paciente = new Paciente("Marcus", 32, 41.1);
		System.out.println(Hospital.classificarFebre(paciente.getTemperatura()));
		
	}
}
