package questao14_5;

public class App {
	public static void main(String[] args) {
		Triangulo triangulo1 = new Triangulo(5, 5, 5);
		Triangulo triangulo2 = new Triangulo(3, 4, 5);
		Triangulo triangulo3 = new Triangulo(4, 5, 7);
//		Triangulo triangulo4 = new Triangulo(24, 5, 7);
		System.out.println(Geometria.calcArea(triangulo1.l1, triangulo1.l2, triangulo1.l3));
		System.out.println(Geometria.calcArea(triangulo2.l1, triangulo2.l2, triangulo2.l3));
		System.out.println(Geometria.calcArea(triangulo3.l1, triangulo3.l2, triangulo3.l3));
		System.out.println(triangulo1.tipoTrianguloAng());
		System.out.println(triangulo2.tipoTrianguloAng());
		System.out.println(triangulo3.tipoTrianguloAng());
		System.out.println(triangulo1.tipoTrianguloLado());
		System.out.println(triangulo2.tipoTrianguloLado());
		System.out.println(triangulo3.tipoTrianguloLado());
			
	}
}
