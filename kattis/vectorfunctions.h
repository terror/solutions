#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void backwards(std::vector<int> &vec);
vector<int> everyOther(const std::vector<int> &vec);
int smallest(const std::vector<int> &vec);
int sum(const std::vector<int> &vec);
int veryOdd(const std::vector<int> &vec);

int main() {
  vector<int> test = {1, 2, 5, 3, 2, 5};
  vector<int> expected = {5, 2, 3, 5, 2, 1};
  backwards(test);
  if (test != expected) {
    std::cerr << "backwards() was incorrect" << std::endl;
    exit(1);
  }

  test = {1, 2, 5, 3, 2, 5};
  expected = {1, 5, 2};
  vector<int> got = everyOther(test);
  if (got != expected) {
    std::cerr << "everyOther() was incorrect" << std::endl;
    exit(1);
  }

  test = {1, 2, 5, 3, 2, 5};
  int ans = smallest(test);
  if (ans != 1) {
    std::cerr << "smallest() was incorrect" << std::endl;
    exit(1);
  }

  test = {1, 2, 5, 3, 2, 5};
  ans = sum(test);
  if (ans != 1 + 2 + 5 + 3 + 2 + 5) {
    std::cerr << "sum() was incorrect" << std::endl;
    exit(1);
  }

  test = {1, 2, 5, 3, 2, 5};
  ans = veryOdd(test);
  if (ans != 2) {
    std::cerr << "veryOdd() was incorrect" << std::endl;
    exit(1);
  }

  std::cerr << "OK!" << std::endl;
}
