/*This code will copy files from android folder to the ML folder structure.
This supports the below devices as per the latest EEG data collection App*/
//Sample Input will be as follows
// Android folder
//Android file names for devices Accelerometer, Gyroscope, Neurosky and Rotational vector
// Output folder
import java.io.*;
import java.util.*;
import java.io.File;
import java.util.HashMap;
import java.util.Iterator;

public class CopyFilesTraining
{

  private HashMap<String, String> sourceDict=new HashMap<String, String>();
  private HashMap<String, String> destDict=new HashMap<String, String>();

  public void initDict()
  {
    sourceDict.put("One_Acc.txt", "Accelerometer");
    sourceDict.put("One_Gyr.txt", "Gyroscope");
    sourceDict.put("One_NS.txt", "Neurosky");
    sourceDict.put("One_RoV.txt", "RotationalVec");
    sourceDict.put("Two_Acc.txt", "Accelerometer");
    sourceDict.put("Two_Gyr.txt", "Gyroscope");
    sourceDict.put("Two_NS.txt", "Neurosky");
    sourceDict.put("Two_RoV.txt", "RotationalVec");
    sourceDict.put("One","Activity_One");
    sourceDict.put("Two", "Activity_Two");
    sourceDict.put("Three","Activity_Three");
    sourceDict.put("Four","Activity_Four");

    Iterator it = sourceDict.entrySet().iterator();
    while(it.hasNext())
    {
      Map.Entry pair= (Map.Entry)it.next();
      System.out.println(pair.getKey()+" = "+pair.getValue());
    //  it.remove();
    }

  }




  public void getListOfAndroidMachineLearning(String androidUser,String machineLearningFolder, boolean test_or_train)
  {

    HashMap<String, HashMap<String, String>> source = new HashMap<String, HashMap<String, String>>();
    HashMap<String, HashMap<String, String>> destination = new HashMap<String, HashMap<String, String>>();

    ArrayList<String> mlTrainingActivities=new ArrayList<String>();
    mlTrainingActivities.add("Activity_One");
    mlTrainingActivities.add("Activity_Two");
    mlTrainingActivities.add("Activity_Three");
    mlTrainingActivities.add("Activity_Four");

    ArrayList<String> mlDevices=new ArrayList<String>();
    mlDevices.add("Accelerometer");
    mlDevices.add("Gyroscope");
    mlDevices.add("Neurosky");
    mlDevices.add("RotationalVec");

    ArrayList<String> androidActivities = new ArrayList<String>();
    ArrayList<String> ListFiles=new ArrayList<String>();

    androidActivities.add("One");
    androidActivities.add("Two");
    androidActivities.add("Three");
    androidActivities.add("Four");

    ListFiles.add("One_Acc.txt");
    ListFiles.add("One_Gyr.txt");
    ListFiles.add("One_NS.txt");
    ListFiles.add("One_RoV.txt");

    //ArrayList<String> ListFolders;

    ListOfFiles files=new ListOfFiles("Test");

    ArrayList<String> listFolders = new ArrayList<String>();
    listFolders=files.getListOfFolders(androidUser, true);
    if(test_or_train==true)
    {
      System.out.println("Testing");
      machineLearningFolder=machineLearningFolder+"/Testing";
    }
    else if(test_or_train==false)
    {
      System.out.println("Training");
      machineLearningFolder=machineLearningFolder+"/Training";
    }

  /*  for(int i=0;i<mlTrainingActivities.size();i++)
    {
      File f=new File(machineLearningFolder+"/"+mlTrainingActivities.get(i));
      //System.out.println("Creating"+machineLearningFolder+"/"+mlTrainingActivities.get(i));
      boolean a_s=f.mkdirs();
      System.out.println(f);
      for(int k=0;k<mlDevices.size();k++)
      {
        File f1=new File(machineLearningFolder+"/"+mlTrainingActivities.get(i)+"/"+
        mlDevices.get(k));
        boolean b_s=f1.mkdirs();
        System.out.println(f1.getPath());
      }

    }
*/

    for(int i=0;i<listFolders.size();i++)
    {
      //System.out.println(listFolders.get(i));
      File f1=new File(listFolders.get(i));
      String activity=f1.getName();
      HashMap<String,String> actHash=new HashMap<String, String>();
      //get the destination activity folder

      ArrayList<String> list= new ArrayList<String>();
      list=files.getListOfFiles1(listFolders.get(i), true);
      for(int k=0;k<list.size();k++)
      {
        File tempF=new File(list.get(k));
        actHash.put(activity,tempF.getPath());
        //System.out.println(tempF.getPath());

      //  System.out.println(machineLearningFolder+"/"+sourceDict.get(activity)+"/"
      //  +sourceDict.get(tempF.getName())+"/"+sourceDict.get(tempF.getName())+".csv");

        fileCopier(tempF.getPath(),machineLearningFolder+"/"+sourceDict.get(activity)+"/"
        +sourceDict.get(tempF.getName())+"/"+sourceDict.get(tempF.getName())+".csv");
      }

    }
    //CopySourceDest(source,destination);
  }
public void fileCopier(String sourcePath, String destinationPath)
{
  System.out.println(sourcePath);
  System.out.println(destinationPath);
  System.out.println("==============================================");
  FileReader fr=null;
  FileWriter fw=null;
  try
  {
    fr=new FileReader(sourcePath);
    fw=new FileWriter(destinationPath);

          int c=fr.read();
          while(c!=-1)
          {
            fw.write(c);
            c=fr.read();
          }

  }
  catch(IOException e)
  {
          System.out.println(e);
  }
  finally
  {
    if (fr != null)
    {
      try{
          fr.close();
      }
      catch(IOException e){

      }

    }
    if (fw != null)
    {
      try{
          fw.close();
      }
      catch(IOException e)
      {

      }
    }
  }
}
/*public void CopySourceDest(HashMap<String, HashMap<String, String>> source, HashMap<String, HashMap<String, String>> destination )
{

//  System.out.println(source.get("One"));
//  System.out.println(source.get("Two"));
//  System.out.println(source.get("Three"));
//  System.out.println(source.get("Four"));


}*/

}
