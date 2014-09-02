object GemStones {
  def main(args: Array[String]) {
    // drop the first line, which is the number of cases, which we don't need
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines.drop(1).toVector
    println(input.map(x => x.toSeq.toSet).foldLeft(input(0).toSeq.toSet)
    ((accum, elem) => accum & elem).size)
  }
}
