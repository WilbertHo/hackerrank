import scala.annotation.tailrec

object AngryChildren {

  @tailrec
  def findMin(cases: Seq[Int], winSize: Int=0, minSoFar: Int=0): Int = {
    // base case
    if (cases.size < winSize) return minSoFar

    val unfairness = cases(winSize - 1) - cases(0)
    return findMin(cases.slice(1, cases.size), winSize, if (unfairness < minSoFar) unfairness else minSoFar)
  }

  def main(args: Array[String]) {
    // Get input.  Drop the first item, which is number of cases.
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines.drop(1).toVector.map(_.toInt)

    // Window size is the next item
    val winSize = input(0)
    val cases = input.drop(1).sorted

    println(findMin(cases, winSize, cases.max))
  }
}
