#include <iostream>
#include <fstream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::istream;
using std::ifstream;
using std::getline;

int main(int argc, char* argv[]) {
  string mystr;
  istream * input;
  ifstream in_file;

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
    cout << mystr << endl;
  }

  return 0;
}
