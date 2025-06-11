package entidades;

public class EquipamentoOpcional {
	private boolean som;
	private boolean alarme;
	private boolean bloqueador;
	
	public EquipamentoOpcional(boolean som, boolean alarme, boolean bloqueador) {
		super();
		this.som = som;
		this.alarme = alarme;
		this.bloqueador = bloqueador;
	}

	@Override
	public String toString() {
		return "Opcionais: [som=" + som + ", alarme=" + alarme + ", bloqueador=" + bloqueador + "]";
	}
	
	
}
