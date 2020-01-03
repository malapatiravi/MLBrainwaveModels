import java.io.*;
import java.util.*;
import java.io.File;

class GenerateACCBasedOnNS
{
  public int getNumberOfRows(String path)
  {
    int size=0;
    CsvToMatrix csvtoMatrix=new CsvToMatrix();
    try
    {
      //System.out.println(csvtoMatrix.getMatrix(path).size());
      size=csvtoMatrix.getMatrix(path).size();
    }
    catch(FileNotFoundException ex)
    {
      System.out.println("Unable to open file in GenerateACCBasedOnNS");
    }
    catch(IOException ex) {
      System.out.println("Error reading file GenerateACCBasedOnNS");
    }

    return size;
  }
  public static void main(String[] args)
  {
    //Define the User lower limit
    int UserL=4;
    //define the user upper limit
    int UserU=5;
    //defind the root path for the user data
    String rootPath="/home/malz/workspace_mars/Java_Practice/src";
    //Generate the path for each user
    ArrayList<String> UserPath=new ArrayList<String>();
    for(int i=UserL;i<UserU;i++)
    {
      UserPath.add(rootPath+"/User"+i);
      System.out.println(rootPath+"/User"+i);
    }

    ArrayList<String> sessions=new ArrayList<String>();
    sessions.add("Training");
    //sessions.add("Testing");

    //System.out.println(UserPath.get(0));
    //Now read the list of Source folders
    //the code actually reads input from the Neurosky number of rows and store in the variable
    ArrayList<String> activities=new ArrayList<String>();
    activities.add("Activity_One");
    activities.add("Activity_Two");
    activities.add("Activity_Three");
    activities.add("Activity_Four");


    ArrayList<String> devices_Source=new ArrayList<String>();
    devices_Source.add("Neurosky");
    ArrayList<String> devices_destination=new ArrayList<String>();
    devices_destination.add("Accelerometer");
    devices_destination.add("Gyroscope");
    for(int i=0;i<UserPath.size();i++)
    {
      for(int it_ses=0;it_ses<sessions.size();it_ses++)
      {
        for(int k=0;k<activities.size();k++)
        {
          //System.out.println(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k));
          GenerateACCBasedOnNS gc=new GenerateACCBasedOnNS();
          int sourceSize=gc.getNumberOfRows(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Neurosky/Neurosky_Fea.csv");

          //System.out.println(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Accelerometer/Accelerometer.csv");
          //System.out.println(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Gyroscope/Gyroscope.csv");
          int destSizeACC = gc.getNumberOfRows(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Accelerometer/Accelerometer.csv");
          int destSizeGyr = gc.getNumberOfRows(UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Gyroscope/Gyroscope.csv");
          if(sourceSize>0 && destSizeACC >0)
            System.out.println("./fileHelp "+destSizeACC/sourceSize +" "+ UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Accelerometer/Accelerometer.csv");
          if(sourceSize>0 && destSizeGyr>0)
            System.out.println("./fileHelp "+destSizeGyr/sourceSize +" "+ UserPath.get(i)+"/"+sessions.get(it_ses)+"/"+activities.get(k)+"/Gyroscope/Gyroscope.csv");
        }
      }

    }

  }
}
