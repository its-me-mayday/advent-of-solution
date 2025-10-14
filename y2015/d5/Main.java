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
        "dvszwmarrgswjxmb"
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
        
        final List<String> strings = FileUtils.readLines(Paths.get(inputPartOnePath));
        System.out.println("How many nice strings? " + countNiceStrings(strings));
    }
    
    private static final int countNiceStrings(final List<String> strings){
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
}