#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;

template<typename T>
shared_ptr<vector<vector<T>>> process_input(istream* is) {
  shared_ptr<vector<vector<T>>> input(new vector<vector<T>>);
  string buffer;
  while (getline(*is, buffer)) {
    istringstream iss(buffer);
    vector<T> current_line;
    T token;
    while (iss >> token) {
      current_line.push_back(token);
    }
    input->push_back(current_line);
  }

  // return the pointer (address)
  return input;
}

int main(int argc, char* argv[]) {
  istream* input;
  ifstream in_file;

  // Read from file if given, else STDIN
  if (argc == 2) {
    in_file.open(argv[1]);
    input = &in_file;
  } else {
    input = &cin;
  }

  // receive a pointer (address) from process_input
  const auto& v = process_input<int>(input);

  /*
  for (const auto line: *v) {
    for (const auto temp: line)
      cout << temp << " ";
    cout << endl;
  }
  */

  // first line gives the length of the road and number of cases
  const auto& road_len = v->begin()->begin();
  const auto& num_cases = (v->begin()->begin()) + 1;

  // second line describes width of the road
  const auto& road = v->begin() + 1;

  // rest are cases
  for (unsigned int i = 2; i < v->size(); ++i) {
    const unsigned int& entry = v->at(i).at(0);
    const unsigned int& _exit = v->at(i).at(1);

    // min_element compares [begin_iterator, end_iterator)
    // so add one to end_iterator to include final element
    const auto& min_width = min_element(road->begin() + entry, road->begin() + _exit + 1);
    cout << *min_width << endl;
  }

  return 0;
}
