import java.io.*;
import java.util.*;
import java.io.File;

public class ListOfFolders
{
  public ArrayList<String> getListOfFolders(String path, boolean status_path)
  {
    private String path_main;
    ListOfFolders(String path_input)
    {
      path_main=path_input;
    }
    public ArrayList<String> getListOfFolders(String path1, boolean status_path)
    {
      ArrayList<String> files = new ArrayList<String>();
      File path = new File(path1);

      for( File fileEntry:path.listFiles())
      {
        //File file = new File(fileEntry);
        if(fileEntry.isDirectory())
        //System.out.println(fileEntry.getName());
        //System.out.println(" "+fileEntry);
        files.add(fileEntry.getName());
      }
      files.trimToSize();
      return files;
  }
}
