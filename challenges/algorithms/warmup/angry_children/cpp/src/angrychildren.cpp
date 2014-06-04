#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>
#include <sstream>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(int argc, char* argv[]) {
  string input_buffer;
  // pointer to input stream
  std::istream* input;
  // input file stream
  std::ifstream in_file;

  // read from file if given, else STDIN
  if (argc == 2) {
    in_file.open(argv[1]);
    input = &in_file;
  } else {
    input = &cin;
  }

  // number of cases
  int num_cases;
  *input >> num_cases;
  // discard remaining newline
  getline(*input, input_buffer);

  // aka number of children
  int window_size;
  *input >> window_size;
  // discard remaining newline
  getline(*input, input_buffer);

  // read N packets
  int packets[num_cases];
  for (int i = 0; i < num_cases; ++i) {
    *input >> packets[i];
  }

  // sort packets
  std::sort(packets, packets + num_cases);

  // set the initial unfairness value to maximum unfairness
  int min_unfairness = packets[num_cases - 1] - packets[0];
  // sliding window, to find min unfairness
  for (int start = 0, end = window_size - 1; end < num_cases; ++start, ++end) {
    int window_min = packets[end] - packets[start];
    if (window_min < min_unfairness) {
      min_unfairness = window_min;
    }
  }

  cout << min_unfairness << endl;

  return 0;
}
