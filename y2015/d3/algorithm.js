const coordinate = (x, y) => `${x}|${y}`;

const STARTING_POINT = coordinate(0,0);
const MOVEMENTS = { 
    '^': coordinate(0,1), 
    'v': coordinate(0,-1),
    '>': coordinate(1,0),
    '<': coordinate(-1,0)
};


function move(direction){
  return (MOVEMENTS[direction] ?? STARTING_POINT);
}

const fromCoordinate = (c) => {
  const [xs, ys] = c.split('|');
  return [Number(xs), Number(ys)];
};

const sumCoordinates = (c1, c2) => {
  const [x1, y1] = fromCoordinate(c1);
  const [x2, y2] = fromCoordinate(c2);
  return coordinate(x1 + x2, y1 + y2);
};

export function getNumberHappyHouses(path) {
    let happyHousesCoordinates = new Set();
    let currentCoordinate = STARTING_POINT;
    const pathLength = path.length;
    
    happyHousesCoordinates.add(currentCoordinate);
    
    for (let i=0; i<pathLength; i++) {
        let direction = path[i];
        let newCoordinate = move(direction);
        currentCoordinate = sumCoordinates(currentCoordinate, newCoordinate);
        happyHousesCoordinates.add(currentCoordinate)
    }

    return happyHousesCoordinates.size;
}