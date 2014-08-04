object AngryChildren {
  def main(args: Array[String]) {
    // get input
    val input = if (args.length < 1) io.Source.stdin
                else io.Source.fromFile(args(0));
    println(input.getLines.toList)
  }
}
