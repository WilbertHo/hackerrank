object AngryChildren {
  def main(args: Array[String]) {
    // get input. if no args passed, then take stdin, else read the
    // passed arg as a filename
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines.map(x => x.toInt).toList

    println(input.sorted)

    val winSize = input(1)
    println(input.slice(2, input.size).sorted.sliding(winSize).map{ case List(a, b, c) => c - a }.min)
  }
}
