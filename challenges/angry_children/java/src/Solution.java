import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Solution {
  public static void main(String[] args) {
    BufferedReader br = null;
    int inputSize = 0;
    int windowSize = 0;
    List<Integer> input = null;

    try {
      // read the input
      br = new BufferedReader(args.length > 0 ?
          new FileReader(args[0]) :
          new InputStreamReader(System.in));
      // process input
      inputSize = Integer.parseInt(br.readLine());
      windowSize = Integer.parseInt(br.readLine());
      input = new ArrayList<Integer>();
      int i = 0;
      String line = null;
      while ((line = br.readLine()) != null) {
        input.add(Integer.parseInt(line));
      }
    } catch (IOException e) {}

    // sort the array
    Collections.sort(input);

    // sliding window
    int minUnfairness = input.get(inputSize - 1) - input.get(0);
    if (windowSize == 1) {
      minUnfairness = input.get(0);
    } else {
      for (int start = 0, end = windowSize - 1; end < input.size(); ++start, ++end) {
        int diff = input.get(end) - input.get(start);
        minUnfairness = Math.min(minUnfairness, diff);
        if (minUnfairness == 1) break;
      }
    }

    System.out.println(minUnfairness);
  }
}
