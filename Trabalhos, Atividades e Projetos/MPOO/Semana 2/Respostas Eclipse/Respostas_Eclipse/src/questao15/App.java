package questao15;

public class App {
	public static void main(String[] args) {
		Usuario usuario1 = new Usuario("maria", "mariamaria", "16672884076");
		Usuario usuario2 = new Usuario("jose", "JoSe", null);
		Usuario usuario3 = new Usuario("joao", "JoAo123", "12345678900");
		
		System.out.println(usuario1.cpf);
		System.out.println(usuario2.cpf);
		System.out.println(usuario3.cpf);
		
	}
}
