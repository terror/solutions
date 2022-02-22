use std::io::stdin;

fn main() {
  let mut x = String::new();
  let mut y = String::new();

  stdin().read_line(&mut x).unwrap();
  stdin().read_line(&mut y).unwrap();

  let cx = cnt(&x);
  let cy = cnt(&y);

  if cx * cy == 0 {
    println!("{}", 0);
  } else {
    let mut ans = String::from("S");

    for _ in 0..((cx * cy) - 1) {
      ans += "(S";
    }

    ans += "(0";

    for _ in 0..(cx * cy) {
      ans += ")";
    }

    println!("{}", ans);
  }
}

fn cnt(s: &String) -> i32 {
  let mut cnt: i32 = 0;
  for c in s.chars() {
    if c == 'S' {
      cnt += 1;
    }
  }
  cnt
}
