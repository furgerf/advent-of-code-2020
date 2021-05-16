namespace AdventOfCode2020
{
  using System.Collections.Generic;
  using System.Linq;

  public class Day17 : IDay
  {
    private const int CycleCount = 6;

    private readonly IFileReader loader;

    // x: row, y: column
    private readonly HashSet<Cell> activeCells = new HashSet<Cell>();

    public Day17(IFileReader loader)
    {
      this.loader = loader;
    }

    public int Day => 17;

    public void LoadData(string filePath)
    {
      const char activeCell = '#';
      var lines = this.loader.ReadFile(filePath).ToArray();

      for (var i = 0; i < lines.Length; i++)
      {
        for (var j = 0; j < lines[i].Length; j++)
        {
          var cell = lines[i][j];
          if (cell == activeCell)
          {
            this.activeCells.Add(new Cell(i, j, 0, 0));
          }
        }
      }
    }

    public int Part1()
    {
      RunCycles(false);

      return this.activeCells.Count;
    }

    public int Part2()
    {
      RunCycles(true);

      return this.activeCells.Count;
    }

    private void RunCycles(bool fourthDimension)
    {
      for (var cycle = 0; cycle < CycleCount; cycle++)
      {
        var x = this.activeCells.Select(cell => cell.X).ToArray();
        var y = this.activeCells.Select(cell => cell.Y).ToArray();
        var z = this.activeCells.Select(cell => cell.Z).ToArray();
        var w = this.activeCells.Select(cell => cell.W).ToArray();

        var spawnedCells = new List<Cell>();
        var diedCells = new HashSet<Cell>();

        void UpdateCell(Cell cell)
        {
          var isActive = this.activeCells.Contains(cell);
          var neighborCount = GetNumberOfNeighbors(cell);
          if (isActive && neighborCount != 2 && neighborCount != 3)
          {
            diedCells.Add(cell);
          }

          if (!isActive && neighborCount == 3)
          {
            spawnedCells.Add(cell);
          }
        }

        var indexes3d = Enumerable.Range(x.Min() - 1, x.Max() + 3 - x.Min())
          .SelectMany(x => Enumerable.Range(y.Min() - 1, y.Max() + 3 - y.Min()).Select(y => (x, y)))
          .SelectMany(xy => Enumerable.Range(z.Min() - 1, z.Max() + 3 - z.Min()).Select(z => (xy.x, xy.y, z)));
        var indexes4d = indexes3d
          .SelectMany(xyz =>
            Enumerable.Range(w.Min() - 1, w.Max() + 3 - w.Min()).Select(w => (xyz.x, xyz.y, xyz.z, w)));
        if (fourthDimension)
        {
          foreach (var cell in indexes4d.Select(xyzw => new Cell(xyzw.x, xyzw.y, xyzw.z, xyzw.w)))
          {
            UpdateCell(cell);
          }
        }
        else
        {
          foreach (var cell in indexes3d.Select(xyz => new Cell(xyz.x, xyz.y, xyz.z, 0)))
          {
            UpdateCell(cell);
          }
        }

        foreach (var spawnedCell in spawnedCells)
        {
          this.activeCells.Add(spawnedCell);
        }

        this.activeCells.RemoveWhere(cell => diedCells.Contains(cell));
      }
    }

    private int GetNumberOfNeighbors(Cell cell)
    {
      var neighborCount = 0;
      for (var i = cell.X - 1; i <= cell.X + 1; i++)
      {
        for (var j = cell.Y - 1; j <= cell.Y + 1; j++)
        {
          for (var k = cell.Z - 1; k <= cell.Z + 1; k++)
          {
            for (var l = cell.W - 1; l <= cell.W + 1; l++)
            {
              var currentCell = new Cell(i, j, k, l);
              if (!currentCell.Equals(cell) && this.activeCells.Contains(currentCell))
              {
                neighborCount++;
              }
            }
          }
        }
      }

      return neighborCount;
    }

    private readonly struct Cell
    {
      public Cell(int x, int y, int z, int w)
      {
        X = x;
        Y = y;
        Z = z;
        W = w;
      }

      public int X { get; }
      public int Y { get; }
      public int Z { get; }
      public int W { get; }

      public override string ToString()
      {
        return $"{X}/{Y}/{Z}/{W}";
      }
    }
  }
}