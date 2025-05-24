package questao5;

import java.util.ArrayList;

public class Usuario {
    private String nome;
    private String cpf;
    private String email;
    private String senha;
    private ArrayList<Telefone> telefones = new ArrayList<Telefone>();
    private Endereco endereco;

    public Usuario(String nome, String cpf, String email, String senha, Telefone telefone, Endereco endereco ) {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        this.senha = senha;
        this.telefones.add(telefone);
        this.endereco = endereco;
    }
    

	public Endereco getEndereco() {
		return endereco;
	}


	public String getNome() {
		return nome;
	}

	public String getCpf() {
		return cpf;
	}

	public String getSenha() {
		return senha;
	}
	
	public ArrayList<Telefone> getTelefone() {
		return telefones;
	}

	public String getEmail() {
		return email;
	}


	@Override
	public String toString() {
		return "Usuario [nome=" + nome + ", cpf=" + cpf + ", email=" + email + ", senha=" + senha + ", telefones="
				+ telefones + ", endereco=" + endereco + "]";
	}

	


}
