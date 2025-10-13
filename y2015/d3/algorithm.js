const STARTING_POINT = (0,0);
const MOVEMENTS = { 
    '^': (0,1), 
    'v': (0,-1),
    '>': (1,0),
    '<': (-1,0)
};

export function getNumberHappyHouses(path) {
    let happyHousesCoordinates = new Set();
    happyHousesCoordinates.add(STARTING_POINT)
    

    return happyHousesCoordinates.size;
}