namespace AdventOfCode2020
{
  public interface IDay
  {
    int Day { get; }

    void LoadData(string filePath);

    int Part1();

    int Part2();
  }
}