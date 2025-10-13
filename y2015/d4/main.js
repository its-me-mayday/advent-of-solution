import { getHashAdventCoinPayload } from "./algorithm.js"

const testInput1 = "abcdef"; 
const testInput2 = "pqrstuv";
const testInput3 = "abcdef609043"; 

const inputPartOne = "ckczppom";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Santa, the payload of adventCoin hash is: ${getHashAdventCoinPayload(testInput1)}`);
console.log(`Santa, the hash of adventCoin is: ${getHashAdventCoinPayload(testInput2)}`);
console.log(`Santa, the payload of adventCoin hash is: ${getHashAdventCoinPayload(testInput3)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 ====");
console.log(`Santa, the hash of adventCoin is: ${getHashAdventCoinPayload(inputPartOne)}`);