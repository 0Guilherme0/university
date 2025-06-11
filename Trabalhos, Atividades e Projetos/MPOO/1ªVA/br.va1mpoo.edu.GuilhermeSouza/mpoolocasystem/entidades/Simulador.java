package entidades;

import java.util.ArrayList;

import gui.Mensagem;

public class Simulador {
	public void simularAlugueis(int dias) {
		ArrayList<String> valores = new ArrayList<String>();
		
		for (Veiculo currentVeiculo : BaseDados.getVeiculos()) {
		    double total = currentVeiculo.getValorDiaria() * dias;   
		    String valor = String.valueOf(total);  
		    valor = currentVeiculo.modelo + " | Valor total: " + valor;
		    valores.add(valor);                                      
		}

		valores.add(0, "===Simulação de Alugueis por " + dias + " dias===");
		
		String mensagem = "";
		
		for(String strs: valores) {
			mensagem += strs + "\n";
		}
		
		Mensagem msg = new Mensagem();
		msg.exibirMensagem(mensagem);
		
	}
}
