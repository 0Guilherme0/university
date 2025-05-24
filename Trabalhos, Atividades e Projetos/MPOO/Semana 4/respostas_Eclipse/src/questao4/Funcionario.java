package questao4;

public class Funcionario {
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
	private double salario;
    private String matricula;
    private String senha = "123456"; //Deve ter pelo menos seis digitos

    public Funcionario(String nome, String cpf, String telefone, String email, double salario, String matricula) {
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.email = email;
        this.salario = salario;
        this.matricula = matricula;

    }

	@Override
	public String toString() {
		return "Funcionario [nome=" + nome + ", cpf=" + cpf + ", telefone=" + telefone + ", email=" + email
				+ ", salario=" + salario + ", matricula=" + matricula + "]";
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getCpf() {
		return cpf;
	}
	
	public String getTelefone() {
		return telefone;
	}
	
	public String getEmail() {
		return email;
	}
	
	public double getSalario() {
		return salario;
	}
	
	public String getMatricula() {
		return matricula;
	}
}

