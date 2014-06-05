#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

template<typename T>
vector<vector<T>>* process_input() {
  vector<vector<T>> foo = new vector<vector<T>>;
  return foo;
}

int main(int argc, char* argv[]) {
  string buffer;
  istream * input;
  ifstream in_file;
  istringstream iss;

  vector<vector<int>> in_vec;

  // Read from file if given, else STDIN
  if (argc == 2) {
    in_file.open(argv[1]);
    input = &in_file;
  } else {
    input = &cin;
  }

  // first line gives the length of the road and number of cases
  getline(*input, buffer);
  iss.str(buffer);
  int length, num_cases;
  iss >> length >> num_cases;

  // second line describes width of the road
  getline(*input, buffer);
  iss.str(string());
  iss.clear();
  iss.str(buffer);
  vector<int> road;
  int temp;
  while (iss >> temp) {
    road.push_back(temp);
  }

  while (getline(*input, buffer)) {
    iss.str(buffer);
    // int credit, price, wrapper_price;
    // iss >> credit >> price >> wrapper_price;
    // int wrappers = credit / price;
    // wrappers += redeem_wrappers(wrappers, wrapper_price);
    // cout << wrappers << endl;
  }

  return 0;
}
