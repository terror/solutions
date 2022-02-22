use std::{collections::HashMap, io::stdin};

fn parse(s: &str) -> i32 {
  s.parse::<i32>().unwrap()
}

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn main() {
  let vec: Vec<i32> = read().split_whitespace().map(|x| parse(x)).collect();

  let mut map = HashMap::new();

  for _ in 0..vec[0] {
    for item in read().split_whitespace() {
      *map.entry(item.to_string()).or_insert(0) += 1;
    }
  }

  let mut ans = vec![];
  for (k, v) in map.into_iter() {
    if v == vec[0] {
      ans.push(k);
    }
  }

  ans.sort();

  println!("{}", ans.len());
  for item in ans {
    println!("{}", item);
  }
}
