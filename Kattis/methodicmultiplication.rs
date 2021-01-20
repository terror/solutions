use std::{io, process};

fn main() {
    let mut x: String = String::new();
    let mut y: String = String::new();

    io::stdin().read_line(&mut x);
    io::stdin().read_line(&mut y);

    let cx: i32 = cnt(&x);
    let cy: i32 = cnt(&y);

    if cx * cy == 0 {
        println!("{}", 0);
    } else {
        let mut ans: String = String::from("S");

        for i in 0..((cx * cy) - 1) {
            ans += "(S";
        }

        ans += "(0";

        for i in 0..(cx * cy) {
            ans += ")";
        }

        println!("{}", ans);
    }
}

fn cnt(s: &String) -> i32 {
    let mut cnt: i32 = 0;
    for i in s.chars() {
        if i == 'S' {
            cnt += 1;
        }
    }
    cnt
}
