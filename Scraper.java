package Job_Search;

class Scraper {
    public static void main(String[] args) {
          // ANSI color codes
        final String BLUE = "\u001B[34m";
        final String WHITE = "\u001B[37m";
        final String RESET = "\u001B[0m";

        // Banner with colors
        String banner = BLUE + """
                 ___   _  _  _____     ___  ___  ___  ___  ___ 
                | _ \\ | \\| ||_   _|   | _ \\| __|| __|| __|| _ \\
                |  _/ | .` |  | |     |  _/| _| | _| | _| |   /
                |_|   |_|\\_|  |_|     |_|  |___||_|  |___||_|_\\
                """ + RESET + WHITE + """
                      .-''''-.
                     / _  _  \\
                     |(@)(@)|
                     \\  __  /
                      '-..-'
                      Pirate Mode Engaged ☠️
                """ + RESET;

        System.out.println(banner);
    }
}