package questao14_5;

public class Geometria {
	 public static boolean existeTriangulo(double a, double b, double c) {
	        return (a + b > c) && (a + c > b) && (b + c > a);
	 }
	 
	 public static double calcArea(double l1, double l2, double l3) {
	        double semiPer = (l1 + l2 + l3) / 2.0;
	        return Math.sqrt(semiPer * (semiPer - l1) * (semiPer - l2) * (semiPer - l3));
	 }
  
}
