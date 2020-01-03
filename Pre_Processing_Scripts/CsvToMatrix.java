import java.io.*;
import java.util.*;

public class CsvToMatrix
{
  public ArrayList<ArrayList<String>> getMatrix(String fileName) throws IOException
  {
    ArrayList<ArrayList<String>> matrix =  new ArrayList<ArrayList<String>>();
    String word = "";
    ArrayList<String> words;
    String line = null;
    try
    {
      FileReader reader=new FileReader(fileName);
      BufferedReader buffer=new BufferedReader(reader);
      while((line = buffer.readLine())!=null)
      {
        words = new ArrayList();;
        for(int i=0; i<line.length(); i++)
        {
          if(line.charAt(i)==',')
          {
            //System.out.println(word);
            words.add(word);
            word="";

          }
          else
            word=word+line.charAt(i);
        }
        matrix.add(words);

      }
      //System.out.println("ZRandom test"+Random.nextInt(20));
      buffer.close();
    }
    catch(FileNotFoundException ex)
    {
      System.out.println("Unable to open file");
    }
    catch(IOException ex) {
      System.out.println("Error reading file");
    }

    return matrix;
  }
}
