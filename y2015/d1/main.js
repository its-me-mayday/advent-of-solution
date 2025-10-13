const instructions = { '(': 1, ')': -1 };

function step(c){
  return (instructions[c] ?? 0);
}

function go_to_floor(path, floor) {
    let pathLength = path.length

    for (let i=0; i<pathLength; i++) {
        let instruction = path[i]
        floor += step(instruction)
    }

    return floor
}

const SOURCE_FLOOR = 0;
console.log("===== TEST INPUTS ====")
console.log(`Santa, is at floor: ${go_to_floor("(())", SOURCE_FLOOR)}`)
console.log(`Santa, is at floor: ${go_to_floor("(()(()(", SOURCE_FLOOR)}`)
console.log(`Santa, is at floor: ${go_to_floor("(())", SOURCE_FLOOR)}`)
console.log(`Santa, is at floor: ${go_to_floor("))(((((", SOURCE_FLOOR)}`)
console.log(`Santa, is at floor: ${go_to_floor("))(", SOURCE_FLOOR)}`)
console.log(`Santa, is at floor: ${go_to_floor(")())())", SOURCE_FLOOR)}`)