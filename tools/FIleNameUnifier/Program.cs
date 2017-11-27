using System;
using System.IO;
using System.Linq;

namespace FIleNameUnifier
{
    class Program
    {
        static void Main(string[] args)
        {
            string directoryPath = args.Where(arg => arg.ToLower().StartsWith("dir:")).First().Replace("dir:", string.Empty);

            DirectoryInfo directoryInfo = new DirectoryInfo(directoryPath);

            MoveAndRenameAllFIles(directoryInfo, directoryInfo);

        }

        private static void MoveAndRenameAllFIles(DirectoryInfo fromDir, DirectoryInfo toDir)
        {
            foreach (DirectoryInfo subDir in fromDir.EnumerateDirectories())
            {
                MoveAndRenameAllFIles(subDir, toDir);
            }
            foreach (FileInfo fileInfo in fromDir.EnumerateFiles("*.*"))
            {
                fileInfo.MoveTo(Path.Combine(toDir.FullName, string.Concat(Path.GetRandomFileName(), fileInfo.Extension)));
            }
        }
    }
}