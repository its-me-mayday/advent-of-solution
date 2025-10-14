package d5;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    
    public static void main(String[]args) throws IOException{
        System.out.println("==== Doesn't He Have Intern-Elves For This? =====");
        
        final String inputTest1 = "ugknbfddgicrmopn";
        final String inputTest2 = "aaa";
        final String inputTest3 = "jchzalrnumimnmhp";
        final String inputTest4 = "haegwjzuvuyypxyu";
        final String inputTest5 = "dvszwmarrgswjxmb";
        
        final String inputPartOnePath = "./inputs/part1.txt";
        
        NiceString niceString = new NiceString(inputTest1); 
        System.out.println("is Nice? " + niceString.isNiceString());
        
        niceString = new NiceString(inputTest2); 
        System.out.println("is Nice? " + niceString.isNiceString());
        
        niceString = new NiceString(inputTest3); 
        System.out.println("is Nice? " + niceString.isNiceString());
        
        niceString = new NiceString(inputTest4); 
        System.out.println("is Nice? " + niceString.isNiceString());
        
        niceString = new NiceString(inputTest5); 
        System.out.println("is Nice? " + niceString.isNiceString());
        
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