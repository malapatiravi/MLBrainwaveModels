#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "extract.h"
#include "fileHelp.h"
#include "missingValues.h"

using namespace std;
std::string ExtractFile::loadFile(std::string path)
{
	std::string line;
	ifstream lFile;
	lFile.open(path.c_str());
	if(lFile.is_open())
	{
		while(getline(lFile,line))
		{
			//cout<<"\n This is here";
			//cout<<line<<'\n';
			fileData += line+"\n";
		}
		lFile.close();
	}
	else
		cout<<"\n Unable to open file";


return fileData;



}
bool ExtractFile::preProcessNS(std::string path)
{
	if(fileData.size()<2)
	{
		std::cout<<"\n The file data is not present";
	}
	else
	{
    int state=0;
    // int mainstate=0;
		std::string first="";
		std::string second="";
		std::string third="";
		int status=1;
		for(size_t it=0;it<fileData.length();it++)
		{
			//std::cout<<fileData[it];
			//if(state==1)
			if(fileData[it]==10||state==0)
			{
				if(state!=0)
				{
					if(second=="RawCount")
					{
						modFileData += "}\","+third;
					}
					else if(second=="Meditation")
					{
						modFileData += ","+third+","+first+"\n"+"\"{";
						status=2;
						//cout<<"\n In meditation";
					}
					else
					{
						if(status!=2)
						modFileData += ","+third;
						else
						{
							status=1;
							modFileData += third;
						}
					}
				}
				state=1;
				first="";
				second="";
				third="";
			}
			else if(state==1){

				if(fileData[it]==44)
				{
				 	state=2;
				}
				else
				{
					first += fileData[it];
				}
			}
			else if(state==2)
			{
				if(fileData[it]==44)
				{
					//cout<<"Second is :"<<second<<endl;
					state=3;
				}
				else
					second += fileData[it];
			}
			else if(state==3)
			{
				//modFileData += fileData[it];
				third += fileData[it];
			}
		}
		cout<<modFileData;
		ofstream myfile;
		myfile.open (fileName+".csv");
		myfile << modFileData;
		myfile.close();
		//cout<<mainStr;
	}
return true;
}

int main(int argc, char* argv[])
{
	ExtractFile file;
	std::vector<string> fileList=file.parseCommandLineArguments(argc, argv);
	//file.filName=
	for(size_t it=1;it<fileList.size();it++)
	{

		ExtractFile file1;
		file1.fileName = fileList[it];
 		file1.loadFile(fileList[it]);
		file1.preProcessNS(fileList[it]);
	}
	/*
	cout<<"\n starting the application";
	vector<string>	fileList;
	fileList.push_back("One_Acc.txt");
	fileList.push_back("One_Gyr.txt");
	fileList.push_back("Two_Acc.txt");
	fileList.push_back("Two_Gyr.txt");
	fileList.push_back("Three_Acc.txt");
	fileList.push_back("Three_Gyr.txt");
	fileList.push_back("Four_Acc.txt");
	fileList.push_back("Four_Gyr.txt");
//	fileList.push_back("Four_Acc.txt");
//	fileList.push_back("Four_Acc.txt");

//	fileList.push_back("Four_Acc.txt");
	for(size_t i=6;i<fileList.size();i++)
	{
		ExtractFile file1;
		file1.loadFile(fileList[i]);
		std::string fileData = file.loadFile(fileList[i]);
		missingValues* mv=new missingValues();
		bool status = mv->missingValue(fileData);
		if(status==false)
			cout<<" This file is having missing Values:"<<fileList[i];
		else
			cout<<" This file is perfect:  "<<fileList[i]<<"\n";
		fileData="";
	}	*/
	//cout<<fileData;

	//std::string str="This is that \n Hello";
	//cout<<str;
	/*for(int i=0;i<str.length();i++)
	{
		if(str[i]==10)
			cout<<"NewLine";
		else
			cout<<static_cast<int>(str[i])<<str[i];
	}*/


}
