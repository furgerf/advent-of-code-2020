namespace AdventOfCode2020
{
  using System.Collections.Generic;
  using System.IO;

  public class FileReader : IFileReader
  {
    public IEnumerable<string> ReadFile(string filePath)
    {
      var lines = new List<string>();
      using var reader = new StreamReader(filePath);
      string line;
      while ((line = reader.ReadLine()) != null)
      {
        lines.Add(line);
      }

      return lines;
    }
  }
}