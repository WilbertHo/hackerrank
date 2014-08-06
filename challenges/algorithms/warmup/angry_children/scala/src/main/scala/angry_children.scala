object AngryChildren {
  def main(args: Array[String]) {
    // Get input.  Drop the first item, which is number of cases.
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines.drop(1).toVector.map(_.toInt)

    // Window size is the next item
    val winSize = input(0)

    var minUnfairness = input.max
    val cases = input.drop(1).sorted

    // Scala's sliding method's iterator is too slow.
    // input.drop(1).sorted.sliding(winSize).map(x => if (x(winSize - 1) - x(0) < minUnfairness) minUnfairness = x(winSize-1) - x(0))
    for (begin <- 0 until cases.size - winSize) {
      val left = cases(begin)
      val right = cases(begin + winSize - 1)
      if (right - left < minUnfairness) {
        minUnfairness = right - left
      }
    }

    println(minUnfairness)
  }
}
