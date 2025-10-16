package Job_Search;

class Scraper {
    public static void main(String[] args) {
          // ANSI color codes
        final String BLUE = "\u001B[34m";
        final String WHITE = "\u001B[37m";
        final String RESET = "\u001B[0m";

        // Banner with colors
        String banner = BLUE + """
                
 OOO    N   N  EEEEE  PPPP   I  EEEEE  CCCC  EEEEE
O   O   NN  N  E      P   P  I  E     C      E
O   O   N N N  EEEE   PPPP   I  EEEE  C      EEEE
O   O   N  NN  E      P      I  E     C      E
 OOO    N   N  EEEEE  P      I  EEEEE  CCCC  EEEEE
                """ + RESET + WHITE + """
                      .-''''-.
                     / _  _  \\
                     |(@)(@)|
                     \\  __  /
                      '-..-'
                      Pirate Mode Engaged ☠️
                """ + RESET;

        System.out.println(banner);
        System.out.println();
    
        //APP Description
        System.out.println(WHITE + "This app helps you explore job opportunities." + RESET);
        System.out.println(BLUE + "- " + WHITE + "Scrapes or loads postings from selected sources" + RESET);
        System.out.println(BLUE + "- " + WHITE + "Lets you filter by role, location, and keywords" + RESET);
        System.out.println(BLUE + "- " + WHITE + "Preps clean summaries you can compare quickly" + RESET);
        System.out.println();
        System.out.println(WHITE + "Tip: Keep your repo private and add your instructor as a collaborator." + RESET);
    }
}