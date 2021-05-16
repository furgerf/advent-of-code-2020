namespace AdventOfCode2020
{
  using System.Collections.Generic;

  public interface IFileReader
  {
    IEnumerable<string> ReadFile(string filePath);
  }
}