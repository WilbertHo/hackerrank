import java.io.*;

public class Solution {

  /**
   * Return number of chocolates redeemed for a given number of wrappers.
   *
   * Wrappers / cost in wrappers == chocolates, each of which is another
   * wrapper. Any wrappers leftover are added to the new wrapper from the
   * eaten chocolate and those are redeemed for additional chocolates.
   */
  public int redeemWrappers(int cost, int wrappers, int chocolates) {
    if (cost > wrappers) return chocolates;
    int newWrappers = wrappers / cost;
    int remainingWrappers = wrappers % cost;
    return redeemWrappers(cost, newWrappers + remainingWrappers, chocolates + newWrappers);
  }

  public static void main(String[] args) {
    // read input
    BufferedReader br = null;

    try {
      br = new BufferedReader(args.length > 0 ?
          new FileReader(args[0]) : new InputStreamReader(System.in));

      // first line is the number of cases
      int numCases = Integer.parseInt(br.readLine());

      Solution s = new Solution();
      String line = null;
      while ((line = br.readLine()) != null) {
        String temp[] = line.split(" ");
        int dollars = Integer.parseInt(temp[0]);
        int costInDollars = Integer.parseInt(temp[1]);
        int costInWrappers = Integer.parseInt(temp[2]);

        int wrappers = dollars / costInDollars;
        int numChocolates = s.redeemWrappers(costInWrappers, wrappers, wrappers);
        System.out.println(numChocolates);
      }
    } catch (IOException e) {}
  }

}
