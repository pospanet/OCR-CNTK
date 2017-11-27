using System;
using System.IO;
using System.Text;

namespace CharacterReplacer
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (string fileName in Directory.GetFiles(args[0], "*.labels.tsv"))
            {
                string workingFileName = string.Concat(fileName, ".working");
                Encoding fileEncoding = Encoding.GetEncoding(1250);
                using (StreamReader fileReader = new StreamReader(File.OpenRead(fileName), fileEncoding))
                using (StreamWriter fileWriter = File.CreateText(workingFileName))
                {
                    while (!fileReader.EndOfStream)
                    {
                        fileWriter.WriteLine(NormalizeNationalCharacters(fileReader.ReadLine()));
                    }
                }
                string backupFileName = string.Concat(fileName, ".original");
                File.Replace(workingFileName, fileName, backupFileName);
                File.Delete(backupFileName);
            }
        }
        
        private static string NormalizeNationalCharacters(string character)
        {
            switch (character)
            {
                case "Á":
                    return "Aapex";
                case "c":
                    return "Ccaron";
                case "d":
                    return "Dcaron";
                case "É":
                    return "Eapex";
                case "e":
                    return "Ecaron";
                case "Í":
                    return "Iapex";
                case "n":
                    return "Ncaron";
                case "Ó":
                    return "Oapex";
                case "r":
                    return "Rcaron";
                case "Š":
                    return "Scaron";
                case "t":
                    return "Tcaron";
                case "Ú":
                    return "Uapex";
                case "u":
                    return "Ucaron";
                case "Ý":
                    return "Yapex";
                case "Ž":
                    return "Zcaron";
                default:
                    return character;
            }
        }
    }
}
