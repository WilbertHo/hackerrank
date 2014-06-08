#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

template<typename T>
vector<vector<T>>* process_input(istream* is) {
  vector<vector<T>>* input = new vector<vector<T>>;
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
  return input;
}

int main(int argc, char* argv[]) {
  istream * input;
  ifstream in_file;

  // Read from file if given, else STDIN
  if (argc == 2) {
    in_file.open(argv[1]);
    input = &in_file;
  } else {
    input = &cin;
  }
  auto v = process_input<int>(input);

  // first line gives the length of the road and number of cases
  int road_len, num_cases;
  auto first_line = v->begin();

  // second line describes width of the road

  // rest are cases
  for (vector<vector<int>>::iterator temp = v->begin() + 2; temp != v->end(); temp++) {
    for (vector<int>::iterator foo = temp->begin(); foo != temp->end(); foo++) {
      cout << *foo << " ";
    }
    cout << endl;
  }

  return 0;
}
