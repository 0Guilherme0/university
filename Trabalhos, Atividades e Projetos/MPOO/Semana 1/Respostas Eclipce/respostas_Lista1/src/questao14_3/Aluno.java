package questao14_3;

import java.lang.Math;

public class Aluno {
	private String name;
	private String matricula;
	private double nota1;
	private double nota2;
	private double nota3;
	
	public Aluno(String name, String matricula, double nota1, double nota2, double nota3) {
		this.name = name;
		this.matricula = matricula;
		this.nota1 = nota1;
		this.nota2 = nota2;
		this.nota3 = nota3;
	}
	
	public String cituacao() {
		double n1 = this.nota1, n2 = this.nota2, n3 = this.nota3;
		double maior = Math.max(n1, Math.max(n2, n3));
		double segundoMaior = (n1 != maior) ? Math.max(n1, Math.min(n2, n3)) : Math.max(n2, n3);
		double media = (maior+segundoMaior)/2;
		
		String resultado =
			(media > 7.0) ? "Aprovado":
			(media > 3.0) ? "Fazer prova final": "Reprovado";
			
		return resultado;
	}
}
