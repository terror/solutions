use std::{cmp::min, io::stdin};

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn check(s: &String) -> bool {
  if s.chars().count() - 1 < 5 {
    return false;
  }

  let mut seen = vec![];
  for ch in s.chars() {
    if seen.contains(&ch) {
      return false;
    }
    seen.push(ch);
  }

  true
}

fn main() {
  let n = parse(read());

  let mut names = vec![];
  for _ in 0..n {
    let name = read();

    if !check(&name) {
      continue;
    }

    names.push(name);
  }

  if names.len() == 0 {
    println!("neibb!");
  } else {
    let mut mn = 20;
    for name in &names {
      mn = min(mn, name.len());
    }

    let mut rest = vec![];
    for name in &names {
      if name.len() == mn {
        rest.push(name);
      }
    }

    rest.sort();
    println!("{}", rest[rest.len() - 1]);
  }
}
