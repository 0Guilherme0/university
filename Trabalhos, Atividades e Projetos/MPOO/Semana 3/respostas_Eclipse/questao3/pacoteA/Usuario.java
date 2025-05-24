package pacoteA;

import javax.swing.JOptionPane;

public class Usuario {
	public static final String MENSAGEM_BENVINDO = "Seja ben-vindo ";
	
	public static void showMessage(String nome) {
		System.out.println(MENSAGEM_BENVINDO + nome);
	}

}
