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

fn main() {
    let mut grid: Vec<Vec<Coordinate>> = Vec::new();
    
    println!("==== PART ONE, d6: Probably a Fire Hazard ====");
    let mut c = new_coordinate(0,0);
    println!("x: {}, y: {}, lit: {}", c.x, c.y, c.lit);
    c.lit = true;
    println!("x: {}, y: {}, lit: {}", c.x, c.y, c.lit);
    
    let mut v = Vec::new();
    v.push(c);
    grid.push(v);
    
    for vec in &grid {
        for x in vec { 
            println!("{}",x.lit);
        }
    }

    println!("==== END PART ONE: d6: Probably a Fire Hazard ====");
}