package d5;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main{
    private static final int MIN_VOWELS = 3;
    private static final String VOWELS = "aeiouAEIOU";
    private static final Set<String> proibitedStrings = Set.of("ab", "cd", "pq", "xy");
    
    public static void main(String[]args) throws IOException{
        System.out.println("==== Doesn't He Have Intern-Elves For This? =====");
        
        final String inputTest1 = "ugknbfddgicrmopn";
        final String inputTest2 = "aaa";
        final String inputTest3 = "jchzalrnumimnmhp";
        final String inputTest4 = "haegwjzuvuyypxyu";
        final String inputTest5 = "dvszwmarrgswjxmb";
        
        final String inputPartOnePath = "./inputs/part1.txt";
        
        System.out.println("is Nice? " + isNiceString(inputTest1));
        System.out.println("is Nice? " + isNiceString(inputTest2));
        System.out.println("is Nice? " + isNiceString(inputTest3));
        System.out.println("is Nice? " + isNiceString(inputTest4));
        System.out.println("is Nice? " + isNiceString(inputTest5));
        
        final List<String> strings = FileUtils.readLines(Paths.get(inputPartOnePath));
        System.out.println("How many nice strings? " + countNiceStrings(strings));
    }
    
    private static final int countNiceStrings(final List<String> strings){
        final int listSize = strings.size();
        int countNiceStrings = 0;

        for(int i=0; i< listSize; i++) {
            final String str = strings.get(i);
            if(isNiceString(str)) countNiceStrings++; 
        }
        return countNiceStrings;
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
            final char ch = str.charAt(i);
            if (VOWELS.indexOf(ch) >= 0 && ++countVowels >= MIN_VOWELS) return true; 
        }

        return (countVowels >= MIN_VOWELS);
    }
     
    private static final boolean checkTwiceLetterInARow(final String str) {
        final int strLenght = str.length();
        
        for(int i=1; i<strLenght;i++) {
            final char chPreavious = str.charAt(i-1);
            final char chCurrent   = str.charAt(i);
            if(chPreavious == chCurrent) return true; 
        }
        return false;
    }
}