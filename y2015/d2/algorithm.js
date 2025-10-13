import { manage_multiple_lines } from "../_shared/readFile.js"

export function total_square_feet_wrapping_paper(input) {
    const sizes = manage_multiple_lines(input)
    let total = 0;
    
    for (const size of sizes) {
        console.log(size)
    }

    return total;
}