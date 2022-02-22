use std::io::stdin;

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn main() {
  let mut n = String::new();
  stdin().read_line(&mut n).unwrap();

  let mut v = vec![];
  for _ in 0..parse(n) {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    v.push(parse(input));
  }

  v.sort();
  v.reverse();

  let mut ans = 0;
  for (i, v) in v.iter().enumerate() {
    if (i + 1) % 3 == 0 {
      continue;
    }
    ans += v;
  }
  println!("{}", ans);
}
