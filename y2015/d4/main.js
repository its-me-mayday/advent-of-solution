import { getHashAdventCoinPayload, getHashAdventCoinPayloadSixZeros } from "./algorithm.js"

const testInput1 = "abcdef"; 
const testInput2 = "pqrstuv";
const testInput3 = "abcdef609043"; 

const officialInput = "ckczppom";

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Santa, the payload of adventCoin hash with at least 5 zeros is: ${getHashAdventCoinPayload(testInput1)}`);
console.log(`Santa, the payload of adventCoin hash with at least 5 zeros is: ${getHashAdventCoinPayload(testInput2)}`);
console.log(`Santa, the payload of adventCoin hash with at least 5 zeros is: ${getHashAdventCoinPayload(testInput3)}`);
console.log("===== PART ONE - TEST TASK INPUT 1 ====");
console.log(`Santa, the payload of adventCoin hash with at least 5 zeros is: ${getHashAdventCoinPayload(officialInput)}`);

console.log("===== PART TWO - TEST INPUTS ====");
console.log(`Santa, the payload of adventCoin hash with at least 6 zeros is: ${getHashAdventCoinPayloadSixZeros(testInput1)}`);
console.log(`Santa, the payload of adventCoin hash with at least 6 zeros is: ${getHashAdventCoinPayloadSixZeros(testInput2)}`);
console.log("===== PART TWO - TEST TASK INPUT 2 ====");
console.log(`Santa, the payload of adventCoin hash with at least 6 zeros is: ${getHashAdventCoinPayloadSixZeros(officialInput)}`);