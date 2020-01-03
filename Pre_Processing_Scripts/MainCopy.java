
public class MainCopy
{
  public static void main(String[] args)
  {
    CopyFilesTraining cp=new CopyFilesTraining();
    cp.initDict();

    String androidUser="/media/malz/01D0E9654C2905F0/MyBooks_Materials/Research_work/NDSS/RajeshDataSession/rajesh origi/";
    //String androidFolder="Training";
    String machineLearningFolder="/home/malz/workspace_mars/Java_Practice/src/User4/Training";
    for(int i=5;i<6;i++)
    {
      machineLearningFolder="/home/malz/workspace_mars/Java_Practice/src/"+"User"+i;
      // false is Training and true=Testing
      boolean test_or_train=false;
      cp.getListOfAndroidMachineLearning(androidUser, machineLearningFolder, test_or_train);

    }

  }
}
