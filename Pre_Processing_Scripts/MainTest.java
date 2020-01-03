import java.io.*;
import java.util.*;
import java.io.File;

public class MainTest
{
  public static void main(String[] args)
  {
      GenerateImpostorData gp = new GenerateImpostorData();
      ArrayList<String> impostors= new ArrayList();
      String genuinePath="";
      //impostors.add("User2");
      //impostors.add("User3");
      ArrayList<ArrayList<String>> matrix=null;
      ListOfFiles files=new ListOfFiles("Test");
      ArrayList<String> listFiles = new ArrayList<String>();
      listFiles=files.getListOfFiles("/home/malz/workspace_mars/Java_Practice/src", true);
      for(int i=0;i<listFiles.size();i++)
      {
        impostors.clear();
        for(int k=0;k<listFiles.size();k++)
        {

          //impostors.removeAll(impostors);
          if(listFiles.get(k)!=listFiles.get(i))
          {
            System.out.println("Adding Sub "+listFiles.get(k));
            impostors.add(listFiles.get(k));
          }

          else
          {
            System.out.println("Main"+listFiles.get(k));
            genuinePath=listFiles.get(k);
          }

        }
        gp.generateImpostorDataDevice("Activity_One", "Accelerometer", "One_Acc.txt.csv",
        "Training",impostors,genuinePath,20,5);
      }
    /*  ArrayList<ArrayList<ArrayList<String>>> three=new ArrayList<ArrayList<ArrayList<String>>>();
      ArrayList<ArrayList<String>> second=new ArrayList<ArrayList<String>>();
      for(int i=0;i<5;i++)
      {

        for(int k=0;k<5;k++)
        {
          ArrayList<String> first=new ArrayList<String>();
          for(int j=0;j<5;j++)
          {
            first.add("one");
          }
          second.add(first);
        }
        three.add(second);
      } */



  /*    CsvToMatrix ctom=new CsvToMatrix();
      try{
          matrix=gp.getMatrix("/home/malz/workspace_mars/Java_Practice/src/User1/Testing/Activity_One/Accelerometer/One_Acc.txt.csv");
      }
      catch(FileNotFoundException ex) {
        System.out.println("Error reading file");
      }
      catch(IOException ex)
      {
        System.out.println("Unable to open file");
      }
      for(ArrayList<String> words:matrix)
      {
        for(String word: words)
        {
          System.out.print(word+",");
        }
        //System.out.print("\n");
      }
      int size=matrix.size();
      Random rg=new Random();
      for(int i=0;i<20;i++)
      {
        //System.out.println("The total number of rows in the file is: "+matrix.size());
        //System.out.println("Random Numer is:"+rg.nextInt(size));
        int randomNumber=rg.nextInt(size);
        ArrayList<String> row=matrix.get(randomNumber);
        for(String str:row)
        {
          System.out.print(str);
        }
        System.out.println("\n");
      }
      gp.writeFile("writetest.csv", matrix); */
  }
}
