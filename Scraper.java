package Job_Search;

class Scraper {
    public static void main(String[] args) {
        System.out.println("\n\nHello, World from Scraper.java!\n\n");
        String[] lines = {
            " OOO    N   N  EEEEE  PPPP   I  EEEEE  CCCC  EEEEE",
            "O   O   NN  N  E      P   P  I  E     C      E",
            "O   O   N N N  EEEE   PPPP   I  EEEE  C      EEEE",
            "O   O   N  NN  E      P      I  E     C      E",
            " OOO    N   N  EEEEE  P      I  EEEEE  CCCC  EEEEE"
        };

        for (String line : lines) {
            System.out.println(line);

        }
    }
}