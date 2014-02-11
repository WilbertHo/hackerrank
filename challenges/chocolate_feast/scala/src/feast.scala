class Feast {

  def feast(credit: Int, cost: Int, total: Int): Int = {
    if (credit < cost) return total;
    total = total + (credit / cost);
    val leftover = (credit / cost) + (credit % cost);
    return feast(leftover, cost, total);
  }

}

object Main {

  def main(args: Array[String]) {
  }

}
