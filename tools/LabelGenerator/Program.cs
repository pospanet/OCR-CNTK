using System;
using System.Linq;
using System.IO;

namespace LabelGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            string directoryPath = args.Where(arg => arg.ToLower().StartsWith("dir:")).First().Replace("dir:",string.Empty);
            string label = args.Where(arg => arg.ToLower().StartsWith("label:")).First().Split(':')[1];

            DirectoryInfo directoryInfo = new DirectoryInfo(directoryPath);

            foreach (FileInfo fileInfo in directoryInfo.EnumerateFiles("*.tsv"))
            {
                string labels = File.ReadAllLines(fileInfo.FullName).Where(line => !string.IsNullOrWhiteSpace(line)).Select(line => label).Aggregate((current, next) => current + Environment.NewLine + next);
                using (StreamWriter streamWriter = File.CreateText(Path.Combine(directoryInfo.FullName, string.Concat(Path.GetFileNameWithoutExtension(fileInfo.FullName), ".labels.tsv"))))
                {
                    streamWriter.Write(labels);
                }
            }
        }
    }
}