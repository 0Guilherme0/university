package questao5;

public class App {
    public static void main(String[] args) {
    	BaseDados.createBase();
    	
    	for (Usuario usuario: BaseDados.getUsuarios()) {
    		System.out.println(usuario);
    	}
    }
}

