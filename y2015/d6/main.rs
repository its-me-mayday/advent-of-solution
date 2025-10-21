struct Coordinate {
    lit: bool,
    x: i16,
    y: i16
}

fn new_coordinate(x: i16, y: i16) -> Coordinate {
    Coordinate {
        lit: false,
        x: x,
        y: y
    }
}

fn print_grid(grid: Vec<Vec<Coordinate>>) {
        for vec in &grid {
        for c in vec { 
            println!("x: {}, y: {}, lit: {}", c.x, c.y, c.lit);
        }
    }
}

fn init_grid() -> Vec<Vec<Coordinate>> {
    let mut grid: Vec<Vec<Coordinate>> = Vec::new();

    for i in 0..100 {
        let mut v = Vec::new();
        
        for j in 0..100 {
            v.push(new_coordinate(i,j));
        }
        grid.push(v);
    }

    return grid;
}

fn main() {
    println!("==== PART ONE, d6: Probably a Fire Hazard ====");
    let grid = init_grid();
    print_grid(grid);
    println!("==== END PART ONE: d6: Probably a Fire Hazard ====");
}