package d5;

import java.util.Set;

public class NiceString { 
    private final int MIN_VOWELS = 3;
    private final String VOWELS = "aeiouAEIOU";
    private final Set<String> proibitedStrings = Set.of("ab", "cd", "pq", "xy");

    private final String str;

    public NiceString(final String str) {
        this.str = str;
    } 
    
    public boolean isNicestString() {
        return hasRepeatedPair(this.str) &&
            hasRepeatingLetterWithGap(this.str);
    }

    private boolean hasRepeatedPair(final String str){
        return true;
    }
    private boolean hasRepeatingLetterWithGap(final String str){
        return true;
    }

    public boolean isNiceString() {
        return checkProibitedStrings(this.str) &&
            checkVowels(this.str) &&
            checkTwiceLetterInARow(this.str);
    }
    
    private boolean checkProibitedStrings(final String str) {
        if(str == null) return false;
        return proibitedStrings.stream().noneMatch(str::contains);
    }
    
    private boolean checkVowels(final String str) {
        final int strLenght = str.length();
        int countVowels = 0;
        
        for(int i=0; i<strLenght;i++) {
            final char ch = str.charAt(i);
            if (VOWELS.indexOf(ch) >= 0 && ++countVowels >= MIN_VOWELS) return true; 
        }

        return (countVowels >= MIN_VOWELS);
    }
     
    private boolean checkTwiceLetterInARow(final String str) {
        final int strLenght = str.length();
        
        for(int i=1; i<strLenght;i++) {
            final char chPreavious = str.charAt(i-1);
            final char chCurrent   = str.charAt(i);
            if(chPreavious == chCurrent) return true; 
        }
        return false;
    }
    
    @Override
    public String toString() {
        return this.str;
    }
}
