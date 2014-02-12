import scala.annotation.tailrec

class Feast {

  @tailrec
  final def feast(credit: Int, cost: Int, total: Int): Int = {
    if (credit < cost) return total;
    return feast((credit / cost) + (credit % cost),
                  cost,
                  total + (credit / cost));
  }

}

object Main {

  def main(args: Array[String]) {
    // get input
    val input = if (args.length < 1) io.Source.stdin
                else io.Source.fromFile(args(0));
    val f = new Feast();

    for (line <- input.getLines()) {
      val Array(dollars, costDollar, costWrapper) =
        line.trim().split("""\s+""").map(x => x.toInt);
      val candies = dollars / costDollar;
      println(f.feast(candies, costWrapper, candies));
    }
  }

}
