#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

template<typename T>
// vector<vector<T>>* process_input(istream* is) {
shared_ptr<vector<vector<T>>> process_input(istream* is) {
  // vector<vector<T>>* input = new vector<vector<T>>;
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

  for (auto line: *input) {
    for (auto temp: line) {
      cout << "hi ";
    }
    cout << endl;
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
  // vector<vector<int>>* v = process_input<int>(input);
  // const vector<vector<int>>& v = *process_input<int>(input);
  const auto& v = *process_input<int>(input);

  // first line gives the length of the road and number of cases
  // int road_len = *(v->begin()->begin());
  // int num_cases = *((v->begin()->begin())+1);
  const auto& road_len = v.begin()->begin();
  const auto& num_cases = (v.begin()->begin()) + 1;

  // second line describes width of the road
  // vector<int> road = *(v->begin()+1);
  const auto& road = v.begin() + 1;

  // rest are cases
  // for (vector<vector<int>>::iterator temp = v->begin() + 2; temp != v->end(); temp++) {
  for (auto temp = v.begin() + 2; temp != v.end(); temp++) {
    int min_width = 0;
    // for (vector<int>::iterator foo = temp->begin(); foo != temp->end(); foo++) {
    for (const auto& foo: *temp) {
      cout << foo << " ";
    }
    cout << endl;
  }

  return 0;
}
