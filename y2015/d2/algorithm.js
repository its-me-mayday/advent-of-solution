import { get } from "http";
import { manageMultipleLines } from "../_shared/readFile.js"

function parseSize(str) {
    const size = str.split('x');

    return {
        length: size[0],
        width: size[1],
        height: size[2]
    }
}

function getAreaData(size) {
return    {
            lxw: size.length * size.width,
            wxh: size.width * size.height,
            hxl: size.height * size.length
        }
}

function getAreaSmallestSide(area) { 
    return Math.min(area.hxl, area.lxw, area.wxh);
}

export function total_square_feet_wrapping_paper(input) {
    const sizes = manageMultipleLines(input)
    let total = 0;
    
    for (const sizeString of sizes) {
        const size = parseSize(sizeString);
        const areaData = getAreaData(size);
        const totalArea = (2*areaData.lxw + 2*areaData.wxh + 2*areaData.hxl) + getAreaSmallestSide(areaData);

        total+=totalArea
    }

    return total;
}