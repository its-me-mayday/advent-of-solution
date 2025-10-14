package d5;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    
    final static String[] inputTestsPartOne = {
        "ugknbfddgicrmopn",
        "aaa",
        "jchzalrnumimnmhp",
        "haegwjzuvuyypxyu",
        "dvszwmarrgswjxmb",
    }; 
    
    final static String[] inputTestsPartTwo = {
        "qjhvhtzxzqqjkmpb",
        "xxyxx",
        "uurcxstgmygtbstg",
        "ieodomkazucvgmuy",
    }; 
    
    final static String[] officialInputPaths = {
        "./inputs/part1.txt",
        "./inputs/part2.txt",
    }; 
     
    public static void main(String[]args) throws IOException {
        final int inputTestsPartOneLen = inputTestsPartOne.length;
        final int inputTestsPartTwoLen = inputTestsPartTwo.length;
        NiceString niceString, nicestString = null;
        
        System.out.println("==== Doesn't He Have Intern-Elves For This? =====");
        System.out.println("==== Preavious Tests - Part One - Doesn't He Have Intern-Elves For This? =====");

        for(int i=0; i<inputTestsPartOneLen; i++) {
            niceString = new NiceString(inputTestsPartOne[i]);
            System.out.println(niceString + " is Nice? " + niceString.isNiceString());
        }   
        
        System.out.println("==== PART ONE TEST - Doesn't He Have Intern-Elves For This? =====");
        System.out.println("How many nice strings? " + countNiceStrings());
        System.out.println("==== PART ONE TEST - Terminate =====");
        
        System.out.println("==== Preavious Tests - Part Two - Doesn't He Have Intern-Elves For This? =====");

        for(int i=0; i<inputTestsPartTwoLen; i++) {
            nicestString = new NiceString(inputTestsPartTwo[i]);
            System.out.println(nicestString + " is Nicest? " + nicestString.isNicestString());
        }   
        
        System.out.println("==== PART TWO TEST - Doesn't He Have Intern-Elves For This? =====");
        System.out.println("How many nicest strings? " + countNicestStrings());
        System.out.println("==== PART TWO TEST - Terminate =====");
    }
     
    public static final int countNiceStrings() throws IOException {
        final List<String> strings = FileUtils.readLines(Paths.get(officialInputPaths[0]));
        final int listSize = strings.size();

        int countNiceStrings = 0;
        NiceString niceString = null;
        boolean isNice = false;

        for(int i=0; i< listSize; i++) {
            final String str = strings.get(i);
            niceString = new NiceString(str);
            isNice = niceString.isNiceString();
            //System.out.println(i + "| " + niceString + " is Nice? " + isNice);
            if(isNice) countNiceStrings++; 
        }
        return countNiceStrings;
    }
    
    public static final int countNicestStrings() throws IOException{
        final List<String> strings = FileUtils.readLines(Paths.get(officialInputPaths[1]));
        final int listSize = strings.size();

        int countNicestStrings = 0;
        NiceString nicestString = null;
        boolean isNicest = false;

        for(int i=0; i< listSize; i++) {
            final String str = strings.get(i);
            nicestString = new NiceString(str);
            System.out.println(i + "| " + nicestString);
            isNicest = nicestString.isNicestString();
            //System.out.println(i + "| " + nicestString + " is Nicest? " + isNicest);
            if(isNicest) countNicestStrings++;
        }
        return countNicestStrings;
    }
}