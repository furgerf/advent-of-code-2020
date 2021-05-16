namespace AdventOfCode2020Test
{
  using System.IO;

  public static class TestUtils
  {
    public static string InputFilePath(int day, string fileName)
    {
      return Path.Join("..", "..", "..", $"Day{day}", fileName);
    }
  }
}