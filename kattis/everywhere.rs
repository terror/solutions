use std::{collections::HashSet, io::stdin};

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn main() {
  for _ in 0 .. parse(read()) {
    let n = parse(read());

    let mut i = 0;
    let mut set = HashSet::new();
    while i < n {
      set.insert(read());
      i += 1;
    }

    println!("{}", set.len());
  }
}
