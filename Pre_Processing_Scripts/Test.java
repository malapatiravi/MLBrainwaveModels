
import java.lang.System;
import java.io.*;
import java.util.*;

public class Test {
	public static void main(String[] args)
	{
		ListOfFiles fun=new ListOfFiles("TestFolder");
		ArrayList<String> files=fun.getListOfFiles("TestFolder", true);
		for(String str:files)
		System.out.println(str);

		System.out.println("Hello");
		String fileName = "Test.java";
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
	catch(IOException ex) {
		System.out.println("Error reading file");
	}
	}

}
