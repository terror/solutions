use std::io;

fn main() {
  let mut s = String::new();
  let mut ans = String::from("h");
  let mut cnt = 0;

  io::stdin().read_line(&mut s);

  for c in s.chars() {
    if c == 'e' {
      cnt += 1;
    }
  }

  for _ in 0..2 * cnt {
    ans += "e";
  }

  println!("{}", ans + "y");
}
