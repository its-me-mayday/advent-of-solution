import { getHashAdventCoin } from "./algorithm.js"

const testInput1 = "abcdef"; 
const testInput2 = "pqrstuv";

const inputPartOne = "ckczppom";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Santa, the hash of adventCoin is: ${getHashAdventCoin(testInput1)}`);
console.log(`Santa, the hash of adventCoin is: ${getHashAdventCoin(testInput2)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 ====");
console.log(`Santa, the hash of adventCoin is: ${getHashAdventCoin(inputPartOne)}`);