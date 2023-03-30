package Enum.Esercizi;
public class EsercizioMedia {
    public static void main(String args[]){
        int numeri[] = {9, 8, 4, 2, 7, 5, 8, 10};
        int somma = 0;
        double media;
         for (int i = 0; i < numeri.length; i++) {
            somma += numeri[i];
        }
        media = (double) somma / numeri.length;
        System.out.println("La media dei numeri nell'array è: " + media);
        }
}


