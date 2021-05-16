namespace AdventOfCode2020
{
  public class Day17 : IDay
  {
    private readonly IFileReader loader;

    public Day17(IFileReader loader)
    {
      this.loader = loader;
    }

    public int Day => 17;

    public void LoadData(string filePath)
    {
      var lines = this.loader.ReadFile(filePath);

      // TODO parse
    }

    public int Part1()
    {
      throw new System.NotImplementedException();
    }

    public int Part2()
    {
      throw new System.NotImplementedException();
    }
  }
}