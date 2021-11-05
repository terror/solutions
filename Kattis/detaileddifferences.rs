use std::io::stdin;

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn main() {
  let n = parse(read());

  for _ in 0..n {
    let a = read();
    let b = read();

    println!("{}", a);
    println!("{}", b);

    for i in 0..a.len() - 1 {
      if a.as_bytes()[i] != b.as_bytes()[i] {
        print!("*");
      } else {
        print!(".");
      }
    }

    println!();
  }
}
