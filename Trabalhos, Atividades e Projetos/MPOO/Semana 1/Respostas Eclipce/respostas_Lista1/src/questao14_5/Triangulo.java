package questao14_5;

public class Triangulo {
    public double l1, l2, l3;
    public double ang1, ang2, ang3;

    public Triangulo(double l1, double l2, double l3) {
        if (!Geometria.existeTriangulo(l1, l2, l3)) {
            throw new IllegalArgumentException("Triângulo não existe");
        }

        this.l1 = l1;
        this.l2 = l2;
        this.l3 = l3;

        this.ang1 = calcularAngulo(l1, l2, l3); 
        this.ang2 = calcularAngulo(l2, l1, l3); 
        this.ang3 = calcularAngulo(l3, l1, l2);
    }

    public double calcularAngulo(double ladoOposto, double lado1, double lado2) {
        double numerador = Math.pow(lado1, 2) + Math.pow(lado2, 2) - Math.pow(ladoOposto, 2);
        double denominador = 2 * lado1 * lado2;
        double cos = numerador / denominador;
        return Math.toDegrees(Math.acos(cos));
    }

    public String tipoTrianguloAng() {
        if (ang1 < 90 && ang2 < 90 && ang3 < 90) {
            return "Acutângulo";
        } else if (ang1 == 90 || ang2 == 90 || ang3 == 90) {
            return "Retângulo";
        } else if (ang1 > 90 || ang2 > 90 || ang3 > 90) {
            return "Obtusângulo";
        } else {
            return "Indeterminado";
        }
    }

    public String tipoTrianguloLado() {
        if (l1 == l2 && l2 == l3) {
            return "Equilátero";
        } else if (l1 == l2 || l1 == l3 || l2 == l3) {
            return "Isósceles";
        } else {
            return "Escaleno";
        }
    }
}
