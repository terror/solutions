use std::io::stdin;

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn main() {
  let n = parse(read());

  // A, A, A, A
  //    A, A, A
  // 3

  // A, D, B, B, C, A
  //    A, D, B, B, C
  // 1

  let mut grades = vec![];
  for _ in 0..n {
    grades.push(read());
  }

  let mut ans = 0;
  for (i, v) in grades.iter().enumerate() {
    if i == grades.len() - 1 {
      break;
    }
    if grades[i + 1] == *v {
      ans += 1
    }
  }

  println!("{}", ans);
}
