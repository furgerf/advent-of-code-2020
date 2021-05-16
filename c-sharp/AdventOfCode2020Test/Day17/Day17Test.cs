namespace AdventOfCode2020Test.Day17
{
  using AdventOfCode2020;
  using FluentAssertions;
  using Xunit;

  public class Day17Test
  {
    private readonly IDay testee;

    public Day17Test()
    {
      this.testee = new Day17(new FileReader());
    }

    [Fact]
    public void Sample()
    {
      this.testee.LoadData(TestUtils.InputFilePath(this.testee.Day, "sample.txt"));

      this.testee.Part1().Should().Be(112);
    }
  }
}