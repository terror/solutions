use std::io;

fn main() {
  let mut s = String::new();

  std::io::stdin().read_line(&mut s).unwrap();

  let v = s
    .split_whitespace()
    .map(|x| x.parse::<i32>())
    .collect::<Result<Vec<i32>, _>>()
    .unwrap();

  println!("{}", v[0] * v[1] * v[2]);
}
