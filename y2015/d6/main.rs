#[derive(Clone, Copy)]
struct Coordinate {
    lit: bool,
    x: i16,
    y: i16
}

fn new_coordinate(x: i16, y: i16) -> Coordinate {
    Coordinate { lit: false, x, y }
}

fn _print_grid(grid:&[Vec<Coordinate>]) {
        for row in grid.iter() {
        for c in row.iter() { 
            println!("(x: {}, y: {}, lit: {})", c.x, c.y, c.lit);
        }
    }
}

fn init_grid() -> Vec<Vec<Coordinate>> {
    let mut grid: Vec<Vec<Coordinate>> = Vec::new();

    for i in 0..1000 {
        let mut v = Vec::new();
        
        for j in 0..1000 {
            v.push(new_coordinate(i,j));
        }
        grid.push(v);
    }

    return grid;
}

fn recognize_cmd(instruction: &str, grid: &mut Vec<Vec<Coordinate>>) {
    let mut iter = instruction.split_whitespace();
    println!("{:?}", iter.next());

    if instruction.starts_with("turn on") {
        for row in grid.iter_mut() {
            for c in row.iter_mut() {
                c.lit = true;
            }
        }
    }
    else if instruction.starts_with("turn off") {
        for row in grid.iter_mut() {
            for c in row.iter_mut() {
                c.lit = false;
            }
        }
    }
    else if instruction.starts_with("toggle") {
        for row in grid.iter_mut() {
            for c in row.iter_mut() {
                c.lit = !c.lit;
            }
        }
    }
}

fn main() {
    let mut grid = init_grid();

    println!("==== PART ONE, d6: Probably a Fire Hazard ====");
    
    let instruction_1 = "turn on 0,0 through 999,999";
    let instruction_2 = "toggle 0,0 through 999,0";
    let instruction_3 = "turn off 499,499 through 500,500";
    
    println!("==== ;;preavious-test(1);; d6: Probably a Fire Hazard, $cmd: '{instruction_1}' ====");
    recognize_cmd(instruction_1, &mut grid);
    println!("==== ;;preavious-test(2);; d6: Probably a Fire Hazard, $cmd: '{instruction_2}' ====");
    recognize_cmd(instruction_2, &mut grid);
    println!("==== ;;preavious-test(3);; d6: Probably a Fire Hazard, $cmd: '{instruction_3}' ====");
    recognize_cmd(instruction_3, &mut grid);
     
    grid = init_grid(); 

    println!("==== ;;input;; d6: Probably a Fire Hazard ====");
    println!("==== END PART ONE: d6: Probably a Fire Hazard ====");
}