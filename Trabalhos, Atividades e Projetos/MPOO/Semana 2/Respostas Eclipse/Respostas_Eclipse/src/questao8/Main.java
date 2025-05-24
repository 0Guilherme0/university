package questao8;

public class Main {
    public static void main(String[] args) {
    	int soma = 0;
    	
    	if (args.length <= 0) {
    		System.out.println("Sem parametros para serem utilizados. ");
    		return;
    	}
    	
    	for (String s:args) {
    		int value = Integer.valueOf(s);
    		soma += value;
    	}
    	System.out.println("A soma dos valores dos parametros é: " + soma);
    	
    }
}
