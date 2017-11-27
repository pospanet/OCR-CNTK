using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LabelCovarageCalculator
{
    class Program
    {
        static readonly string[]  Labels = {"Aapex","Ccaron","Dcaron","Eapex","Ecaron","Iapex","Ncaron",
            "Oapex","Rcaron","Scaron","Tcaron","Uapex","Ucaron","Yapex","Zcaron",
            "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I",
            "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            ".",",","-","_","@","/","#","&","\"" };
        static void Main(string[] args)
        {
            string directoryPath = args.Where(arg => arg.ToLower().StartsWith("dir:")).First().Replace("dir:", string.Empty);
            string fileName = args.Where(arg => arg.ToLower().StartsWith("file:")).First().Replace("file:", string.Empty);
            DirectoryInfo directoryInfo = new DirectoryInfo(directoryPath);
            Dictionary<string, int> counter = Labels.ToDictionary(i => i, i => 0);
            CalculateLabelCoverage(directoryInfo, counter);
            using (StreamWriter streamWriter = File.CreateText(fileName))
            {
                string content = counter.Select(keyValue => string.Concat(keyValue.Key, ":\t", keyValue.Value)).Aggregate((current, next) => current + Environment.NewLine + next);
                streamWriter.Write(content);
            }
        }

        private static void CalculateLabelCoverage(DirectoryInfo directory, Dictionary<string, int> counter)
        {
            foreach (FileInfo fileInfo in directory.EnumerateFiles("*.bboxes.labels.tsv"))
            {
                Encoding fileEncoding = Encoding.GetEncoding(1250);
                using (StreamReader fileReader = new StreamReader(fileInfo.OpenRead(), fileEncoding))
                {
                    while (!fileReader.EndOfStream)
                    {
                        string key = fileReader.ReadLine().Trim();
                        if (counter.ContainsKey(key))
                        {
                            counter[key]++;
                        }
                        else if(!key.Equals("UNDEFINED"))
                        {
                        }
                    }
                }
            }
        }
    }
}
