import scala.annotation.tailrec

object Solution {

  // def processLine(lines: Iterator[String]): Array[Int] = {
  //   return lines.next().split("""\s+""").map(x => x.toInt);
  // }

  def processLine(lines: Iterator[String]): List[Int] = {
    return lines.next().split("""\s+""").map(x => x.toInt).toList;
  }

  def main(args: Array[String]) {
    // get input
    val input = if (args.length < 1) io.Source.stdin
                else io.Source.fromFile(args(0));
    val lines = input.getLines();

    val List(road_length, num_cases) = processLine(lines);
    val road = processLine(lines);

    while (lines.hasNext) {
      val List(entry, exit) = processLine(lines);
      val min = road.slice(entry, exit + 1).min;
      println(min);
    }
  }

}
