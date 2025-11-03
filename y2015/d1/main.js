import { readText } from "./utils.js"

const INSTRUCTIONS = { '(': 1, ')': -1 };
const SOURCE_FLOOR = 0;
const START_POSITION = 1;

function step(c){
  return (INSTRUCTIONS[c] ?? 0);
}

function hasEncounterBasement(basement, floor) {
  return (!basement && isBasement(floor));
}

function isBasement(floor) {
  return (floor == -1) ?? false;
}

function go_to_floor(path) {
    let basementEncountered = false;
    let first_basement_position = -1;
    let floor = SOURCE_FLOOR;
    let pathLength = path.length;
    let position = START_POSITION;

    for (let i=0; i<pathLength; i++) {
        let instruction = path[i];
        floor += step(instruction);
        if (hasEncounterBasement(basementEncountered, floor)) {
          basementEncountered = true;
          first_basement_position = position;
        }
        else position++;
    }
    
    return {floor: floor, first_basement_position: first_basement_position}
}

let pathi1 = await readText("./inputs/input_p1.txt");
let pathi2 = await readText("./inputs/input_p2.txt");

console.log("===== PART ONE - TEST INPUTS ====");
console.log(`Santa, is at floor: ${go_to_floor("(())").floor}`);
console.log(`Santa, is at floor: ${go_to_floor("(()(()(").floor}`);
console.log(`Santa, is at floor: ${go_to_floor("(())").floor}`);
console.log(`Santa, is at floor: ${go_to_floor("))(((((").floor}`);
console.log(`Santa, is at floor: ${go_to_floor("))(").floor}`);
console.log(`Santa, is at floor: ${go_to_floor(")())())").floor}`);
console.log("===== PART ONE - TEST TASK INPUT 1 (input_p1.txt) ====");
console.log(`Santa, is at floor: ${go_to_floor(pathi1).floor}`);

console.log("===== PART TWO - TEST INPUTS ====");
console.log("== PART TWO - TEST 1 ==");
console.log(`Santa, is at floor: ${go_to_floor(")").floor}`);
console.log(`Santa, the first time that you enter in basement (floor=-1) is at position: ${go_to_floor(")").first_basement_position}`);
console.log("== PART TWO - TEST 2 ==");
console.log(`Santa, is at floor: ${go_to_floor("()())").floor}`);
console.log(`Santa, the first time that you enter in basement (floor=-1) is at position: ${go_to_floor("()())").first_basement_position}`);
console.log("== PART TWO - TEST 3 ==");
console.log(`Santa, is at floor: ${go_to_floor("(())").floor}`);
console.log(`Santa, the first time that you enter in basement (floor=-1) is at position: ${go_to_floor("(())").first_basement_position}`);
console.log("===== PART TWO - TEST TASK INPUT 2 (input_p2.txt) ====");
console.log(`Santa, is at floor: ${go_to_floor(pathi2).floor}`);
console.log(`Santa, the first time that you enter in basement (floor=-1) is at position: ${go_to_floor(pathi2).first_basement_position}`);