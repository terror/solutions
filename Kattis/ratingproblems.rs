use std::io::stdin;

fn main() {
  let mut line = String::new();
  stdin().read_line(&mut line).unwrap();

  let v = line
    .split_whitespace()
    .map(|x| x.parse::<f32>())
    .collect::<Result<Vec<f32>, _>>()
    .unwrap();

  let mut s = 0.0;
  for _ in 0..v[1] as i32 {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    s += input.trim().parse::<f32>().unwrap();
  }

  println!(
    "{} {}",
    (-3.0 * (v[0] - v[1]) + s) / v[0],
    (3.0 * (v[0] - v[1]) + s) / v[0]
  );
}
