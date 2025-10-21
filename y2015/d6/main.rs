use std::env;
use std::fs::{File, create_dir_all};
use std::io::{BufRead, BufReader, BufWriter, Write};

fn write_grid_to_file(grid: &[Vec<Coordinate>], path: &str) -> std::io::Result<()> {
    let file = File::create(path)?;
    let mut w = BufWriter::new(file);

    for row in grid.iter() {
        for c in row.iter() {
            writeln!(w, "(x: {}, y: {}, lit: {})", c.x, c.y, c.lit)?;
        }
    }

    w.flush()?;
    Ok(())
}

#[derive(Clone, Copy)]
struct Coordinate {
    lit: bool,
    x: i16,
    y: i16
}

fn count_lit(grid: &[Vec<Coordinate>]) -> usize {
    grid.iter()
        .flatten()
        .filter(|c| c.lit)
        .count()
}

fn new_coordinate(x: i16, y: i16) -> Coordinate {
    Coordinate { lit: false, x, y }
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

fn transform_in_coordinate(c_str: &str) -> Coordinate {
    let mut it = c_str.split(',');
    let xs = it.next().expect("missing x");
    let ys = it.next().expect("missing y");
    let x: i16 = xs.trim().parse().expect("bad x");
    let y: i16 = ys.trim().parse().expect("bad y");
    new_coordinate(x, y)
}

fn in_rect(c: &Coordinate, a: Coordinate, b: Coordinate) -> bool {
    let (x0, x1) = if a.x <= b.x { (a.x, b.x) } else { (b.x, a.x) };
    let (y0, y1) = if a.y <= b.y { (a.y, b.y) } else { (b.y, a.y) };
    c.x >= x0 && c.x <= x1 && c.y >= y0 && c.y <= y1
}
fn recognize_cmd(instruction: &str, grid: &mut Vec<Vec<Coordinate>>) {
    let mut it = instruction.split_whitespace();

    match it.next() {
        Some("turn") => {
            let on_or_off = it.next().unwrap_or_default(); 
            let c1_str = it.next().unwrap_or_default();    
            let _through = it.next();                     
            let c2_str = it.next().unwrap_or_default();    

            let c1 = transform_in_coordinate(c1_str);
            let c2 = transform_in_coordinate(c2_str);

            for row in grid.iter_mut() {
                for c in row.iter_mut() {
                    if in_rect(c, c1, c2) {
                        c.lit = on_or_off == "on";
                    }
                }
            }
        }
        Some("toggle") => {
            let c1_str = it.next().unwrap_or_default();
            let _through = it.next();
            let c2_str = it.next().unwrap_or_default();

            let c1 = transform_in_coordinate(c1_str);
            let c2 = transform_in_coordinate(c2_str);

            for row in grid.iter_mut() {
                for c in row.iter_mut() {
                    if in_rect(c, c1, c2) {
                        c.lit = !c.lit;
                    }
                }
            }
        }
        _ => eprintln!("Unrecognized instruction: {instruction}"),
    }
}

fn process_instructions<R: BufRead>(reader: R, grid: &mut Vec<Vec<Coordinate>>) -> std::io::Result<()> {
    for (idx, line) in reader.lines().enumerate() {
        let line = line?;
        let l = line.trim();
        if l.is_empty() || l.starts_with('#') {
            continue;
        }
        recognize_cmd(l, grid);
        println!("[{}] {} -> lights ON = {}", idx + 1, l, count_lit(&grid));
    }
    Ok(())
}

fn main() {
    let mut grid = init_grid();

    println!("==== PART ONE, d6: Probably a Fire Hazard ====");
    
    let instruction_1 = "turn on 0,0 through 999,999";
    let instruction_2 = "turn off 499,499 through 500,500";
    let instruction_3 = "toggle 0,0 through 999,0";
    
    println!("==== ;;preavious-test(1);; d6: Probably a Fire Hazard, $cmd: '{instruction_1}' ====");
    recognize_cmd(instruction_1, &mut grid);
    write_grid_to_file(&grid, "out/grid-intermediate-turn-on.txt").expect("failed to write grid");
    println!("==== ;;preavious-test(2);; d6: Probably a Fire Hazard, $cmd: '{instruction_2}' ====");
    recognize_cmd(instruction_2, &mut grid);
    write_grid_to_file(&grid, "out/grid-intermediate-turn-off.txt").expect("failed to write grid");
    println!("==== ;;preavious-test(3);; d6: Probably a Fire Hazard, $cmd: '{instruction_3}' ====");
    recognize_cmd(instruction_3, &mut grid);
    write_grid_to_file(&grid, "out/grid-preavious-test-1.txt").expect("failed to write grid"); 
    println!("lit_count: {}", count_lit(&grid)); 
    
    grid = init_grid(); 
    let path = env::args().nth(1).unwrap_or_else(|| "inputs/part1.txt".to_string());
    println!("Reading instructions from: {}", path);
    let file = File::open(&path).expect("cannot open instructions file");
    let reader = BufReader::new(file);
    process_instructions(reader, &mut grid).expect("failed processing instructions");
    println!("==== ;;input;; d6: Probably a Fire Hazard ====");
    write_grid_to_file(&grid, "out/grid-part-1.txt").expect("failed to write grid");
    println!("lit_count: {}", count_lit(&grid)); 

    println!("==== END PART ONE: d6: Probably a Fire Hazard ====");
}