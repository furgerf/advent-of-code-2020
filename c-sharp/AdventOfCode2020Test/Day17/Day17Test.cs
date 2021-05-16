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
    public void SamplePart1()
    {
      this.testee.LoadData(TestUtils.InputFilePath(this.testee.Day, "sample.txt"));

      this.testee.Part1().Should().Be(112);
    }

    [Fact]
    public void Part1()
    {
      this.testee.LoadData(TestUtils.InputFilePath(this.testee.Day, "input.txt"));

      this.testee.Part1().Should().Be(395);
    }

    [Fact]
    public void SamplePart2()
    {
      this.testee.LoadData(TestUtils.InputFilePath(this.testee.Day, "sample.txt"));

      this.testee.Part2().Should().Be(848);
    }

    [Fact]
    public void Part2()
    {
      this.testee.LoadData(TestUtils.InputFilePath(this.testee.Day, "input.txt"));

      this.testee.Part2().Should().Be(2296);
    }
  }
}