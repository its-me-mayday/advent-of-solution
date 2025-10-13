package d5;

import java.util.HashSet;
import java.util.Set;

class Main{
    private static final int MIN_VOWELS = 3;
    private static final String VOWELS = "aeiouAEIOU";
    private static final Set<String> proibitedStrings = Set.of("ab", "cd", "pq", "xy");
    
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
        return checkProibitedStrings(str) &&
            checkVowels(str) &&
            checkTwiceLetterInARow(str);
    }
    
    private static final boolean checkProibitedStrings(final String str) {
        if(str == null) return false;
        return proibitedStrings.stream().noneMatch(str::contains);
    }
    
    private static final boolean checkVowels(final String str) {
        final int strLenght = str.length();
        int countVowels = 0;
        
        for(int i=0; i<strLenght;i++) {
            char ch = str.charAt(i);
            if (VOWELS.indexOf(ch) >= 0 && ++countVowels >= MIN_VOWELS) {
            return true; 
        }
        }

        return countVowels >= MIN_VOWELS;
    }
     
    private static final boolean checkTwiceLetterInARow(final String str) {
        return true;
    }
}