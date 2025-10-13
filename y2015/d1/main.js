function step_to(c, floor){
    if (c == '(')
        return floor+1
    else if (c == ')')
        return floor-1
    else
        return floor
}

function go_to_floor(path, floor) {
    let pathLength = path.length

    for (let i=0; i<pathLength; i++) {
        let instruction = path[i]
        floor = step_to(instruction, floor)
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