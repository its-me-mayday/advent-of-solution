package d5;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    
    final static String[] inputTests = {
        "ugknbfddgicrmopn",
        "aaa",
        "jchzalrnumimnmhp",
        "haegwjzuvuyypxyu",
        "dvszwmarrgswjxmb",
    }; 
    
    final static String[] officialInputPaths = {
        "./inputs/part1.txt",
        "./inputs/part2.txt",
    }; 
    
    final static String inputPartOnePath = "./inputs/part1.txt";
    
    public static void main(String[]args) throws IOException{
        System.out.println("==== Doesn't He Have Intern-Elves For This? =====");
         
        final int inputTestsLen = inputTests.length;
        NiceString niceString = null;


        for(int i=0; i<inputTestsLen; i++) {
            niceString = new NiceString(inputTests[i]);
            System.out.println(niceString + " is Nice? " + niceString.isNiceString());
        }   
        
        System.out.println("==== PART ONE TEST - Doesn't He Have Intern-Elves For This? =====");
        final List<String> strings = FileUtils.readLines(Paths.get(officialInputPaths[0]));
        System.out.println("How many nice strings? " + countNiceStrings(strings));
        
        System.out.println("==== PART TWO TEST - Doesn't He Have Intern-Elves For This? =====");
        final List<String> nicestStrings = FileUtils.readLines(Paths.get(officialInputPaths[1]));
        System.out.println("How many nice strings? " + countNicestStrings(nicestStrings));
    }
    
    public static final int countNiceStrings(final List<String> strings){
        final int listSize = strings.size();
        int countNiceStrings = 0;
        NiceString niceString = null;

        for(int i=0; i< listSize; i++) {
            final String str = strings.get(i);
            niceString = new NiceString(str);
            if(niceString.isNiceString()) countNiceStrings++; 
        }
        return countNiceStrings;
    }
    
    public static final int countNicestStrings(final List<String> strings){
        final int listSize = strings.size();
        int countNicestStrings = 0;
        NiceString nicestString = null;

        for(int i=0; i< listSize; i++) {
            final String str = strings.get(i);
            nicestString = new NiceString(str);
            if(nicestString.isNicestString()) countNicestStrings++; 
        }
        return countNicestStrings;
    }
}