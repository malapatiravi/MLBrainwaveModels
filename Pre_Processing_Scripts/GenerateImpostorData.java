import java.io.*;
import java.util.*;
import java.io.File;

public class GenerateImpostorData
{
/*impostorList -- Number of impostors and their names
  deviceName -- modularity for which the data should be generated
  genuineUser -- genuine user for which the testing data should be generated
  activityId -- activity id the activity for which and from which the data should be referd.*/
  public boolean generateImpostorDataDevice(String activityId,
    String deviceName,
    String fileName,
    String train_or_test,
    ArrayList<String> impostorList,
    String genuineUser,
    int noOfFeatureLinesPerImpostor,
    int totalNoOfFeatureLines)
    {
      for(int i=0;i<impostorList.size();i++)
      {
        System.out.println("Received list: "+ impostorList.get(i));
        System.out.print(genuineUser);
      }
        String genuinePathPart1; //This is static and should be given by the programmer
                                 // Example is "/home/malz/workspace_mars/Java_Practice/src/User1"
                                // User1 is taken from genuineUser
        String genuinePathPart2; // This is assigned during run time
                                // /Training/ActivityId/deviceName/fileName
        String impostorPathPart1; //This is static and should be assigned during initialization
                                  //Example /home/malz/workspace_mars/Java_Practice/src/User2
        String impostorPathPart2; // This is assigned during runtime
                                  //Example /Training/ActivityId/deviceName/fileName
        //ArrayList<String> impPathList=new ArrayList();
        /*Initialization*/
        ArrayList<ArrayList<String>> genuineMatrix = null;
        ArrayList<ArrayList<ArrayList<String>>> impostorMatrixArray = new ArrayList<ArrayList<ArrayList<String>>>();

        genuinePathPart1 = "/home/malz/workspace_mars/Java_Practice/src/"+genuineUser;
        genuinePathPart2 = "/" + train_or_test + "/" + activityId + "/" + deviceName
                           +"/"+fileName;
        //System.out.println(genuinePathPart1+genuinePathPart2);
        //The below code gets the genuineMatrix from the given path
        try{
          genuineMatrix=getMatrix(genuinePathPart1+genuinePathPart2);
        }
        catch(FileNotFoundException ex) {
          System.out.println("Error reading file");
        }
        catch(IOException ex)
        {
          System.out.println("Unable to open file");
        }

        //The below code gets the impostor matrix arraylist from the given
        //impostor users in the impostorList
        for(int i=0;i<10;i++)
        System.out.print("====");
        for(String path:impostorList)
        {
          ArrayList<ArrayList<String>> impMatrix;
          try
          {
            //readFile("/home/malz/workspace_mars/Java_Practice/src/"+path+"/" +
            //train_or_test + "/" + activityId + "/" + deviceName+"/"+fileName);
           impMatrix=  getMatrix("/home/malz/workspace_mars/Java_Practice/src/"+path+"/" +
            train_or_test + "/" + activityId + "/" + deviceName+"/"+fileName);
            impostorMatrixArray.add(impMatrix);
          }
          catch(FileNotFoundException ex) {
            System.out.println("Error reading file");
          }
          catch(IOException ex)
          {
            System.out.println("Unable to open file");
          }
        }

        //Now we have genuineMatrix and impostorMatrixArray
        //Lets get the number of rows availabe with genuineMatrix
        int genuineRows = genuineMatrix.size();
        int noOfFeatureLinesPerImpostor1 = genuineRows/impostorList.size();
        ArrayList<ArrayList<String>> impostorData = new ArrayList<ArrayList<String>>();
        ArrayList<ArrayList<String>> tempImpostorData = new ArrayList<ArrayList<String>>();

        for(int i = 0;i < impostorMatrixArray.size();i++)
        {
          tempImpostorData=impostorMatrixArray.get(i);
          Random rg=new Random();
          ArrayList<Integer> track=new ArrayList<Integer>();
          ArrayList<Integer> impFeaList=new ArrayList<Integer>();
          impFeaList = getUniqueNumbers(tempImpostorData.size(),noOfFeatureLinesPerImpostor1);
          //impFeaList=getUniqueNumbers(tempImpostorData.size(),5);
          if(noOfFeatureLinesPerImpostor1<tempImpostorData.size())
          {
            for(int j=0;j<noOfFeatureLinesPerImpostor1;j++)
            {


              //if(noOfFeatureLinesPerImpostor1<=)
              /*int index = rg.nextInt(tempImpostorData.size());
              if(track.contains(index))
              {
                j--;
              }
              else
              {
                track.add(j);
                impostorData.add(tempImpostorData.get(index));
                System.out.println("Added");
              }*/
              //for(int y=0;y<impFeaList.size();y++)
              {
                impostorData.add(tempImpostorData.get(impFeaList.get(j)));
              }

            }

          }
          else
          {
            for(int j=0;j<tempImpostorData.size();j++)
            {
              {
                impostorData.add(tempImpostorData.get(impFeaList.get(j)));
              }

            }
          }

        }
        writeFile(genuinePathPart1+"/" + train_or_test + "/" + activityId + "/" + deviceName
                           +"/"+"impostorData.csv", impostorData);




        return true;
    }
    public ArrayList<Integer> getUniqueNumbers(Integer no, Integer reqNo)
    {
      ArrayList<Integer> mainList = new ArrayList<Integer>();
      ArrayList<Integer> randomList = new ArrayList<Integer>();
      System.out.println(no);
      System.out.println(reqNo);


      for(int i=0;i<no;i++)
      {
        mainList.add(i);
      }
      Collections.shuffle(mainList);
      if(reqNo>no)
      {
        for(int i=0;i<no;i++)
        {
          randomList.add(mainList.get(i));
        }
      }
      else
      {
        for(int i=0;i<reqNo;i++)
        {
          randomList.add(mainList.get(i));
        }
      }

      return randomList;
    }
  public void writeFile(String fileName, ArrayList<ArrayList<String>> matrix)
  {
    File fout = new File(fileName);
    String line="";
    try
    {
      FileOutputStream fos = new FileOutputStream(fout);
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
      for(int i=0;i<matrix.size();i++)
      {
        line="";
        ArrayList<String> row=new ArrayList<String>();
        row=matrix.get(i);
        for(int k=0;k<row.size();k++)
        {
          if(k==0)
          line=row.get(k);
          else
          line=line+","+row.get(k);
        }
        bw.write(line);
        bw.newLine();
        line="";
      }
      bw.close();

    }
    catch(FileNotFoundException ex)
    {
      System.out.println("Unable to open file");
    }
    catch(IOException ex)
    {
      System.out.println("Error reading file");
    }


  }
  public void readFile(String fileName)
  {
    String line=null;
    try
    {
      FileReader fileReader= new FileReader(fileName);
      BufferedReader breader = new BufferedReader(fileReader);
      while((line = breader.readLine()) != null)
      {
        for(int i=0;i<line.length();i++)
        {
          //String str=line.charAt[i];
          System.out.print(line.charAt(i));
        }
        System.out.print("\n");

      }
      breader.close();
    }


    catch(FileNotFoundException ex)
    {
      System.out.println("Unable to open file");
    }
    catch(IOException ex)
    {
      System.out.println("Error reading file");
    }
  }

  public void readFileRandom(String fileName, int n)
  {

  }

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
        words = new ArrayList();
        for(int i=0; i<line.length(); i++)
        {
          if(line.charAt(i)==',')
          {
            //System.out.println(word);
            words.add(word);
            word="";

          }
          else if(i==line.length()-1)
          {
            word=word+line.charAt(i);
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
