import { manageMultipleLines } from "../_shared/readFile.js"

function parseSize(str) {
    const size = str.split('x');

    return {
        length: size[0],
        width: size[1],
        height: size[2]
    }
}

export function total_square_feet_wrapping_paper(input) {
    const sizes = manageMultipleLines(input)
    let total = 0;
    
    for (const sizeString of sizes) {
        const size = parseSize(sizeString);
        console.log(size)
    }

    return total;
}