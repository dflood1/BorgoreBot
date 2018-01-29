import java.io.File
import scala.io.Source
import java.io.PrintWriter

val length = 2

val dirPath = "/home/eherbert/Misc/BorgoreBot/data/"
val pw = new PrintWriter(dirPath + "encoded_" + length + "words.txt")

(new File(dirPath))
.listFiles
.toArray
.map{f =>
    Source.fromFile(f)
    .getLines
    .toArray
    .flatMap(x => if(x.trim.isEmpty) Array("NEWLINE") else x.trim.split(" "))
    .sliding(length)
    .toArray
    .filter(_.length==length)
    .map(_.mkString("BREAK") + "\n")
}.flatten
.foreach{l =>
    pw.write(l)
}

pw.close()
