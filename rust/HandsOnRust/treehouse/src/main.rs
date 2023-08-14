use std::io::stdin;

fn main() {
    println!("");
    println!("TreeOS(tm)::SecurityModule(1.1.18): ");
    println!("Enter name: ");

    // read user's name
    // NB: 'String' is Rust builtin type
    let mut your_name = String::new();
    stdin()
        .read_line(&mut your_name)
        .expect("Failed to read line");

    // print greeting
    println!("Hello, {:?}", your_name);
}
