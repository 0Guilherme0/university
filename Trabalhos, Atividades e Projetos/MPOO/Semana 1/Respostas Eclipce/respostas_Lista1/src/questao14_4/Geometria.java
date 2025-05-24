package questao14_4;

import java.lang.Math;

public class Geometria {
	public static String calcArea(double raio) {
		double area = Math.PI * (raio * raio);
		String areaString =  String.format("%.2f", area);
		return areaString + "m^2";
		
	}
	
	public static String calcPerimetro(double raio) {
		double perimetro = 2 * Math.PI * raio;
		String perimetroString =  String.format("%.2f", perimetro);
		return  perimetroString + "m";
		
	}
}
