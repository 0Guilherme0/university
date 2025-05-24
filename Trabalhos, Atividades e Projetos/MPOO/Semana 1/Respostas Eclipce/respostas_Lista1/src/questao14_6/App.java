package questao14_6;

public class App {
	public static void main(String[] args) {
		Retangulo retangulo1 = new Retangulo(15, 5);
		Retangulo retangulo2 = new Retangulo(10, 8);
		System.out.println(Geometria.calcArea(retangulo1.comprimento, retangulo1.altura));
		System.out.println(Geometria.clacPerimetro(retangulo1.comprimento, retangulo1.altura));
		System.out.println(Geometria.calcArea(retangulo2.comprimento, retangulo2.altura));
		System.out.println(Geometria.clacPerimetro(retangulo2.comprimento, retangulo2.altura));
		
	}
}
