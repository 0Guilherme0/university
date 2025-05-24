package app;

import pacoteB.Usuario;

public class Main {
	public static void main(String[] args) {
		Usuario usuario = new Usuario("Alberto", "093984");
		pacoteA.Usuario.showMessage(usuario.login);
	}

}
