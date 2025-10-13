import { readText } from "../_shared/readFile.js"
import { total_square_feet_wrapping_paper } from "./algorithm.js"

let sizeInput1 = await readText("inputs/part1.txt");
let sizeInput2 = await readText("inputs/part2.txt");

const testInput1 = "2x3x4"; 
const testInput2 = "1x1x10";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Elves, the total square feet of wrapping paper is: ${total_square_feet_wrapping_paper(testInput1)}`);
console.log(`Elves, the total square feet of wrapping paper is: ${total_square_feet_wrapping_paper(testInput2)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 (inputs/part1.txt) ====");
console.log(`Elves, the total square feet of wrapping paper is: ${total_square_feet_wrapping_paper(sizeInput1)}`);

console.log("===== PART TWO - TEST INPUTS ====");
console.log("===== PART TWO - <TODO> ====");
console.log("===== PART ONE - TEST TASK INPUT 2 (inputs/part2.txt) ====");
console.log("===== <TODO> ====");