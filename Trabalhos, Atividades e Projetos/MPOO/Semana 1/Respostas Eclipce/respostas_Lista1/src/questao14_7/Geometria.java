package questao14_7;

import java.lang.Math;

public class Geometria {
	public static String calcAreaCircle(double raio) {
		double area = Math.PI * (raio * raio);
		String areaString =  String.format("%.2f", area);
		return areaString + "m^2";
	}
	
	public static String calcPerimetroCircle(double raio) {
		double perimetro = 2 * Math.PI * raio;
		String perimetroString =  String.format("%.2f", perimetro);
		return  perimetroString + "m";
	}
	
	 public static boolean existeTriangulo(double a, double b, double c) {
	        return (a + b > c) && (a + c > b) && (b + c > a);
	 }
	 
	 public static double calcArea(double l1, double l2, double l3) {
	        double semiPer = (l1 + l2 + l3) / 2.0;
	        return Math.sqrt(semiPer * (semiPer - l1) * (semiPer - l2) * (semiPer - l3));
	 }

	public static double calcAreaRetangulo(double comprimento, double altura){
		return comprimento * altura;
	}
	
	public static double clacPerimetroRetangulo(double comprimento, double altura) {	
		return (comprimento * 2) + (altura * 2);
	}
	
}
