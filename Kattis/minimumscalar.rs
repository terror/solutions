use std::io::stdin;

fn read() -> String {
  let mut s = String::new();
  stdin().read_line(&mut s).unwrap();
  s
}

fn read_vec() -> Vec<i64> {
  let n = read();

  let mut ret = vec![];
  for item in n.split(" ") {
    ret.push(parse(item.to_owned()));
  }

  ret
}

fn parse(s: String) -> i64 {
  s.trim().parse::<i64>().unwrap()
}

fn main() {
  let n = parse(read());

  for i in 0..n {
    let k = parse(read());

    let mut a = read_vec();
    let mut b = read_vec();

    a.sort();
    b.sort_by(|a, b| b.cmp(a));

    let mut ans = 0;
    for j in 0..k {
      ans += a[j as usize] * b[j as usize];
    }

    println!("Case #{}: {}", i + 1, ans);
  }
}
