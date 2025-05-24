package app;

import entidades.Fruta;

public class Aplication {
	public static void main(String[] args) {
		Fruta[] frutas = {
	            new Fruta("Maçã", true, false, true),    
	            new Fruta("Banana", false, false, true),   
	            new Fruta("Abacate", true, true, false),  
	            new Fruta("Pêssego", true, true, false),   
	            new Fruta("Cereja", false, true, false),   
	            new Fruta("Pera", true, false, false),     
	            new Fruta("Uva", false, false, true)      
	        };  

     for (Fruta fruta : frutas) {
         System.out.println("=======================================");
         System.out.println("ANTES DE COMER:");
         System.out.println(fruta.status());

         boolean foiComida = fruta.comerFruta();

         System.out.println("\nDEPOIS DE COMER:");
         System.out.println(fruta.status());

         if (foiComida) {
             fruta = null;
             System.gc();
         }
         System.out.println("=======================================\n");
     }
 }
}


