import { readText } from "./utils.js"
import { totalSquareFeetWrappingPaper, totalFeetOfRibbon } from "./algorithm.js"

let sizeInput1 = await readText("inputs/part1.txt");
let sizeInput2 = await readText("inputs/part2.txt");

const testInput1 = "2x3x4"; 
const testInput2 = "1x1x10";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Elves, the total square feet of wrapping paper is: ${totalSquareFeetWrappingPaper(testInput1)}`);
console.log(`Elves, the total square feet of wrapping paper is: ${totalSquareFeetWrappingPaper(testInput2)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 (inputs/part1.txt) ====");
console.log(`Elves, the total square feet of wrapping paper is: ${totalSquareFeetWrappingPaper(sizeInput1)}`);

console.log("===== PART TWO - TEST INPUTS ====");
console.log(`Elves, the total feet of ribbon is: ${totalFeetOfRibbon(testInput1)}`);
console.log(`Elves, the total feet of ribbon is: ${totalFeetOfRibbon(testInput2)}`);
console.log("===== PART TWO - TEST TASK INPUT 2 (inputs/part2.txt) ====");
console.log(`Elves, the total square feet of wrapping paper is: ${totalFeetOfRibbon(sizeInput2)}`);