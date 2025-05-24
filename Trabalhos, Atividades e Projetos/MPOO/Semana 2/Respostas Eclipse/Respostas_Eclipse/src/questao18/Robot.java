package questao18;

public class Robot {
	public static final String DEFAULT_DIRECTION = "n";
	public String name;
	public String direction;
	public Vetor position;
	
	public Robot(String name) {
		this.name = name;
		this.direction = DEFAULT_DIRECTION;
		this.position = new Vetor(); 
		
	}
		
	public void oneStep() {
	    switch (this.direction.toLowerCase()) {
	        case "n": this.position.incrementY(); break;
	        case "s": this.position.decrementY(); break;
	        case "l": this.position.incrementX(); break;
	        case "o": this.position.decrementX(); break;
	        default: System.out.println("Posição inválida");
	    }
	}

	public void multipleSteps(int steps) {
		for (int i = 0; i < steps; i++) {
			oneStep();
		}
	}
	
	public void transport(int x, int y) {
		this.position.update(x, y);
	}
	
	public void changeDirection(String direction) {
		if (direction.equalsIgnoreCase("n") || direction.equalsIgnoreCase("s")
			|| direction.equalsIgnoreCase("l") || direction.equalsIgnoreCase("o")) {
			this.direction = direction;
			
		} else System.out.println("Direção inválida");
	}
	
	public String status() {
	    return "Posição: " + this.position.toString() + " | Direção: " + this.direction;
	}

	
	public void defautPosition() {
		this.position.update(0, 0);
		this.direction = DEFAULT_DIRECTION;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
