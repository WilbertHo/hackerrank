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
  std::istream * input;
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
  int packets;
  while (*input >> packets) {
    cout << packets << endl;
  }

  // sort packets
  // sliding window, max()-min()
  return 0;
}
