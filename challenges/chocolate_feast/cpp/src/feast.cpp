#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::istream;
using std::ifstream;
using std::string;

int redeem_wrappers(int credit, int cost) {
  if (cost > credit) return 0;
  int wrappers = credit / cost;
  int leftover = credit % cost;
  return wrappers + redeem_wrappers(wrappers + leftover, cost);
}

int main(int argc, char* argv[]) {
  string mystr;
  istream * input;
  ifstream in_file;

  // Read from file if given, else STDIN
  if (argc == 2) {
    in_file.open(argv[1]);
    input = &in_file;
  } else {
    input = &cin;
  }

  int num_cases;
  *input >> num_cases;
  // Get rid of the remaining newline
  getline(*input, mystr);

  while (getline(*input, mystr)) {
    std::istringstream iss(mystr);
    int credit, price, wrapper_price;
    iss >> credit >> price >> wrapper_price;
    int wrappers = credit / price;
    wrappers += redeem_wrappers(wrappers, wrapper_price);
    cout << wrappers << endl;
  }

  return 0;
}
