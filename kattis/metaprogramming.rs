use std::{
  collections::HashMap,
  io::{prelude::*, stdin},
};

fn parse(s: String) -> i32 {
  s.trim().parse::<i32>().unwrap()
}

fn main() {
  let mut vars = HashMap::new();

  for line in stdin().lock().lines() {
    let input = line.unwrap();
    let query: Vec<&str> = input.split(" ").collect();

    match query[0] {
      "define" => {
        vars.insert(query[2].to_string(), parse(query[1].to_string()));
      }
      "eval" => {
        if !vars.contains_key(query[1]) || !vars.contains_key(query[3]) {
          println!("undefined");
        } else {
          match query[2] {
            "<" => println!("{}", vars.get(query[1]) < vars.get(query[3])),
            ">" => println!("{}", vars.get(query[1]) > vars.get(query[3])),
            "=" => println!("{}", vars.get(query[1]) == vars.get(query[3])),
            _ => panic!(),
          };
        }
      }
      _ => panic!(),
    }
  }
}
