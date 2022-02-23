#include <bits/stdc++.h>

using namespace std;

struct Position {
  int x;
  int y;

  Position() {
    this->x = 0;
    this->y = 0;
  }

  Position(int x, int y) {
    this->x = x;
    this->y = y;
  }

  void update(Position movement) {
    this->x += movement.x;
    this->y += movement.y;
  }

  bool operator== (const Position &o) {
    return this->x == o.x && this->y == o.y;
  }
};

struct Robot {
  Position pos;
  Position target;
  int curr;
  vector<Position> ins;

  Robot(Position pos, Position target) {
    this->pos = pos;
    this->target = target;
    this->curr = 0;
    this->ins.push_back(Position(0, 1));
    this->ins.push_back(Position(1, 0));
    this->ins.push_back(Position(0, -1));
    this->ins.push_back(Position(-1, 0));
  }

  void load(string ins) {
    if (ins == "Right")
      this->curr = ++curr % this->ins.size();
    else if (ins == "Left")
      this->curr = --curr % this->ins.size();
    else
      this->move();
  }

  void move() {
    this->pos.update(this->ins[curr]);
  }

  bool at_target() {
    return this->pos == this->target;
  }
};

int main() {
  int x, y;
  cin >> x >> y;

  vector<string> instructions;
  int N; cin >> N;
  while (N--) {
    string ins; cin >> ins;
    instructions.push_back(ins);
  }

  vector<string> tmp;
  tmp.push_back("Right");
  tmp.push_back("Left");
  tmp.push_back("Forward");

  for (int i = 0; i < instructions.size(); ++i) {
    for (int j = 0; j < tmp.size(); ++j) {
      Robot robot = Robot(Position(), Position(x, y));
      for (int k = 0; k < instructions.size(); ++k) {
        if (k == i) {
          robot.load(tmp[j]);
          continue;
        }
        robot.load(instructions[k]);
      }
      if (robot.at_target()) {
        cout << i + 1 << " " << tmp[j] << "\n";
        return 0;
      }
    }
  }
}
