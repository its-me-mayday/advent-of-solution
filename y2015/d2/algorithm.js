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
    return {
            lxw: size.length * size.width,
            wxh: size.width * size.height,
            hxl: size.height * size.length
        }
}

function getAreaSmallestSide(area) { 
    return Math.min(area.hxl, area.lxw, area.wxh);
}

export function totalSquareFeetWrappingPaper(input) {
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

function getPerimeterData(size) {
    return {
            p1: 2*size.length + 2*size.width,
            p2: 2*size.width + 2*size.height,
            p3: 2*size.height + 2*size.length
        }
}

function getSmallestPerimeter(perimeter) {
    return Math.min(perimeter.p1, perimeter.p2, perimeter.p3)
}

export function totalFeetOfRibbon(input) {
    const sizes = manageMultipleLines(input)
    let total = 0;
    
    for (const sizeString of sizes) {
        const size = parseSize(sizeString);
        const perimeterData = getPerimeterData(size);
        const volume = size.length * size.width * size.height;
        const totalArea = volume + getSmallestPerimeter(perimeterData);

        total+=totalArea
    }

    return total;
}