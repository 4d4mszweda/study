extern crate float_cmp;
extern crate piston_window;
extern crate rand;

use piston_window::*;

struct Colour {
    r: f32,
    g: f32,
    b: f32,
    a: f32,
}

impl Colour {
    fn to_rgba(&self) -> [f32; 4] {
        [self.r, self.g, self.b, self.a]
    }
}

//-----------------------------------------------------------------------------
// Direction to move.
#[derive(Copy, Clone)]
enum Direction {
    L,
    R,
}

//-----------------------------------------------------------------------------
// Facing enum for encoding way ant is pointing.
enum Facing {
    N,
    E,
    S,
    W,
}

//-----------------------------------------------------------------------------
// The Ant structure defining its position, movement rule, associated colours
// and iteration count.
struct Ant {
    pos_x: usize,
    pos_y: usize,
    rule: Vec<Direction>,
    colours: Vec<Colour>,
    facing: Facing,
    stalled: bool,
    iterations: u64,
}

impl Ant {
    fn new(x: usize, y: usize) -> Ant {
        Ant {
            pos_x: x,
            pos_y: y,
            rule: vec![Direction::R, Direction::L],
            colours: vec![Colour {
                r: 0.24677,
                g: 0.23577,
                b: 0.85639,
                a: 1.0,
            }, Colour {
                r: 0.94767,
                g: 0.75434,
                b: 0.46743,
                a: 1.0,
            }],
            facing: Facing::N,
            stalled: false,
            iterations: 0,
        }
    }
}

//-----------------------------------------------------------------------------
// The row structure defnies the current colour code for each cell 
// on a given row.
struct Row {
    cells: Vec<usize>,
}

impl Row {
    fn new(num_cells: usize, clr_idx: usize) -> Row {
        let mut r = Row { cells: Vec::new() };
        r.cells.resize(num_cells, clr_idx);
        r
    }
}

//-----------------------------------------------------------------------------
// The grid structure encoding the state of each cell as a numerical value
// between 0 and n - 1, where there are n colours, one for each move in
// a rule.
struct Grid {
    rows: Vec<Row>,
}

impl Grid {
    fn new(num_rows: usize, num_cols: usize, clr_idx: usize) -> Grid {
        let mut g = Grid {
            rows: Vec::with_capacity(num_rows),
        };
        while g.rows.len() != num_rows {
            g.rows.push(Row::new(num_cols, clr_idx));
        }
        g
    }
}

//-----------------------------------------------------------------------------
// FUNCTIONS
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
// Move ant coming from originally facing North.
fn move_from_north(ant_dir: Direction, dim: usize, ant: &mut Ant) {
    match ant_dir {
        Direction::L => {
            // Set new direction to face.
            ant.facing = Facing::W;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if 0 == ant.pos_x {
                ant.stalled = true;
            } else {
                ant.pos_x -= 1;
            }
        }
        Direction::R => {
            // Set new direction to face.
            ant.facing = Facing::E;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if dim - 1 == ant.pos_x {
                ant.stalled = true;
            } else {
                ant.pos_x += 1;
            }
        }
    }
}

//-----------------------------------------------------------------------------
// Move ant coming from originally facing East.
fn move_from_east(ant_dir: Direction, dim: usize, ant: &mut Ant) {
    match ant_dir {
        Direction::L => {
            // Set new direction to face.
            ant.facing = Facing::N;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if 0 == ant.pos_y {
                ant.stalled = true;
            } else {
                ant.pos_y -= 1;
            }
        }
        Direction::R => {
            // Set new direction to face.
            ant.facing = Facing::S;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if dim - 1 == ant.pos_y {
                ant.stalled = true;
            } else {
                ant.pos_y += 1;
            }
        }
    }
}

//-----------------------------------------------------------------------------
// Move ant coming from originally facing South.
fn move_from_south(ant_dir: Direction, dim: usize, ant: &mut Ant) {
    match ant_dir {
        Direction::L => {
            // Set new direction to face.
            ant.facing = Facing::E;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if dim - 1 == ant.pos_x {
                ant.stalled = true;
            } else {
                ant.pos_x += 1;
            }
        }
        Direction::R => {
            // Set new direction to face.
            ant.facing = Facing::W;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if 0 == ant.pos_x {
                ant.stalled = true;
            } else {
                ant.pos_x -= 1;
            }
        }
    }
}

//-----------------------------------------------------------------------------
// Move ant coming from originally facing West.
fn move_from_west(ant_dir: Direction, dim: usize, ant: &mut Ant) {
    match ant_dir {
        Direction::L => {
            // Set new direction to face.
            ant.facing = Facing::S;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if dim - 1 == ant.pos_y {
                ant.stalled = true;
            } else {
                ant.pos_y += 1;
            }
        }
        Direction::R => {
            // Set new direction to face.
            ant.facing = Facing::N;

            // Move ant in correct direction. Checking for
            // hitting boundary, in which case we mark ant
            // as stalled.
            if 0 == ant.pos_y {
                ant.stalled = true;
            } else {
                ant.pos_y -= 1;
            }
        }
    }
}

//-----------------------------------------------------------------------------
// Compute new position of ant updating grif colours as we move ant.
fn compute_ant_position(ant: &mut Ant, grid: &mut Grid) {
    // Has ant stalled?
    if ant.stalled {
        return;
    }

    // Grab the current colour index for the ant's current position.
    let mut cell_clr_idx = grid.rows[ant.pos_y].cells[ant.pos_x];

    if usize::max_value() == cell_clr_idx {
        cell_clr_idx = 0;
    }

    // Grab direction we need to turn.
    let ant_dir = ant.rule[cell_clr_idx];

    // Increment cell colour index.
    cell_clr_idx += 1;

    if ant.colours.len() == cell_clr_idx {
        cell_clr_idx = 0;
    }

    grid.rows[ant.pos_y].cells[ant.pos_x] = cell_clr_idx;

    // Grab the grid dimension.
    let dim = grid.rows.len();

    // Move ant in correctdirection based on way it is currently facing.
    match ant.facing {
        Facing::N => move_from_north(ant_dir, dim, ant),
        Facing::E => move_from_east(ant_dir, dim, ant),
        Facing::S => move_from_south(ant_dir, dim, ant),
        Facing::W => move_from_west(ant_dir, dim, ant),
    }

    // Increment the iteration count.
    if u64::max_value() == ant.iterations {
        ant.stalled = true;
    } else {
        ant.iterations += 1;
    }
}

// *  MAIN FUNCTION
fn main() {
    let fps: u64 = 50;
    let moves_per_tick: i32 = 20;
    let grid_size: u32 = 100;
    let square_size: f64 = 5.0;

    // Centre the starting point in the square grid.
    let start_point: usize = (grid_size as f64 / 2.0) as usize;

    // Initialise ant's position.
    let mut ant = Ant::new(start_point, start_point);

    // Grid size in pixels will be multiplication of grid_size in squares
    // by square_size in pixels.
    let dim: u32 = grid_size * (square_size as u32);

    // Initialise Grid.
    let mut grid = Grid::new(grid_size as usize, grid_size as usize, usize::max_value());
    // Create our 2D render window.
    let mut window: PistonWindow = WindowSettings::new("Langton's Ant", [dim, dim])
        .exit_on_esc(true)
        .build()
        .unwrap();

    // Tweak event loop timings.
    let mut evs = window.get_event_settings();
    evs.set_ups(fps);
    evs.set_max_fps(fps);
    window.set_event_settings(evs);

    // Process the events and start drawing.
    let ant_ref: &mut Ant = &mut ant;
    let grid_ref: &mut Grid = &mut grid;

    while let Some(e) = window.next() {
        window.draw_2d(&e, |c, g, _device| {
            clear([1.0; 4], g);
            for _ in 0..moves_per_tick {
                compute_ant_position(ant_ref, grid_ref);
            }
            let mut x: u32 = 0;
            for row in &mut grid_ref.rows {
                let mut y: u32 = 0;
                for cell in &mut row.cells {
                    let xr = x as f64 * square_size;
                    let yr = y as f64 * square_size;
                    if *cell != usize::max_value() {
                        rectangle(
                            ant_ref.colours[*cell].to_rgba(),
                            [xr, yr, square_size, square_size],
                            c.transform,
                            g,
                        );
                    }
                    y += 1;
                }
                x += 1;
            }
        });

        let mut title = String::from("");
        title.push_str(ant_ref.iterations.to_string().as_str());
        window.set_title(title);
    }
}