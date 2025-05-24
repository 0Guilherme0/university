package questao14_2;

public class Hospital {
	public static String classificarFebre(double temperatura) {
		if (temperatura > 41.0) {
			return "Hipertermia";
		} else if (temperatura > 39.6 && temperatura < 41.0) {
			return "Febre alta";
		} else if (temperatura > 37.6 && temperatura < 39.5) {
			return "Febre";
		} else if (temperatura > 36 && temperatura < 37.5) {
			return "Normal";
		} else if (temperatura < 35 ) {
			return "Hiportermia";
		} else return null;
	}
}
