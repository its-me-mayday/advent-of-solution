import { readText } from "../_shared/readFile.js"
import { getNumberHappyHouses } from "./algorithm.js"

let sizeInput1 = await readText("inputs/part1.txt");
let sizeInput2 = await readText("inputs/part2.txt");

const testInput1 = ">"; 
const testInput2 = "^>v<";
const testInput3 = "^v^v^v^v^v";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Santa, houses that received at least one present are: ${getNumberHappyHouses(testInput1)}`);
console.log(`Santa, houses that received at least one present are: ${getNumberHappyHouses(testInput2)}`);
console.log(`Santa, houses that received at least one present are: ${getNumberHappyHouses(testInput3)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 (inputs/part1.txt) ====");
console.log(`Santa, houses that received at least one present are: ${getNumberHappyHouses(sizeInput1)}`);
