package d5;

class Main{
    private static final int MIN_VOWELS = 3;
    
    public static void main(String[]args){
        System.out.println("==== Doesn't He Have Intern-Elves For This? =====");
        
        final String inputTest1 = "ugknbfddgicrmopn";
        final String inputTest2 = "aaa";
        final String inputTest3 = "jchzalrnumimnmhp";
        final String inputTest4 = "haegwjzuvuyypxyu";
        final String inputTest5 = "dvszwmarrgswjxmb";
        
        System.out.println(isNiceString(inputTest1));
        System.out.println(isNiceString(inputTest2));
        System.out.println(isNiceString(inputTest3));
        System.out.println(isNiceString(inputTest4));
        System.out.println(isNiceString(inputTest5));
    }
    
    private static final boolean isNiceString(final String str) {
        return checkProibitedLetters(str) &&
            checkVowels(str) &&
            checkTwiceLetterInARow(str);
    }
    
    private static final boolean checkProibitedLetters(final String str) {
        return true;
    }
    
    private static final boolean checkVowels(final String str) {
        final int strLenght = str.length();
        int countVowels = 0;
        
        for(int i=0; i<strLenght;i++) {
            char ch = str.charAt(i);
            if(isVowel(ch)) countVowels += 1;
        }

        return countVowels >= MIN_VOWELS;
    }
    
    private static boolean isVowel(final char ch) {
        return ch == 'a' ||
            ch == 'e' ||
            ch == 'i' ||
            ch == 'o' ||
            ch == 'u';
    }
    
    private static final boolean checkTwiceLetterInARow(final String str) {
        return true;
    }
}