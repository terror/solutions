use std::io::stdin;

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn read_vec() -> Vec<i32> {
  let n = read();

  let mut ret = vec![];
  for item in n.split(" ") {
    ret.push(parse(item.to_owned()));
  }

  ret
}

fn main() {
  let mut winner = 0;
  let mut result = 0;

  for i in 0..5 {
    let line = read_vec();

    let points = line.iter().sum();
    if points > result {
      winner = i + 1;
      result = points;
    }
  }

  println!("{} {}", winner, result);
}
