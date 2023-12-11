#![warn(clippy::all, clippy::pedantic)]
/*
HoR ("Hands on Rust"), page 14
 */
fn main() { 
    // let MYLIST = [ "One", "Two", "Three" ];
    // for i in 0..3 {
    //     println!("{}", MYLIST[i]);
    // }

    // rev 1: replacing the name it doesn't like
    // let my_list = [ "One", "Two", "Three" ];
    // for i in 0..3 {
    //     println!("{}", my_list[i]);
    // }

    // rev 2: use iterator loop
    // let my_list = [ "One", "Two", "Three" ];
    // for s in &my_list {
    //     println!("{}", s);
    // }

    // rev 3: fix pedantic complaint about println() call
    let nums_los = [ "One", "Two", "Three" ];
    for s in &nums_los {
        println!("{s}");
    }
}
