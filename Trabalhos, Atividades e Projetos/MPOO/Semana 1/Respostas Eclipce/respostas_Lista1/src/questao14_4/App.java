package questao14_4;

public class App {
	public static void main(String[] args) {
		Circulo circulo = new Circulo(2);
		System.out.println(Geometria.calcArea(circulo.raio));
		System.out.println(Geometria.calcPerimetro(circulo.raio));
	}
}
