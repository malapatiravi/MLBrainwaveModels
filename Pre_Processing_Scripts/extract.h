
#include <iostream>
#include <fstream>
#include <vector>
#include "fileHelp.h"

using namespace std;

class ExtractFile
{
	public:
	std::string loadFile(std::string path);
	bool preProcessNS(std::string writePath);
	
	//private:
	std::string fileData;
	std::string modFileData;
	std::string fileName;
	std::vector<string> parseCommandLineArguments(int argc, char* argv[])
{
	std::vector<string> fileVec;
	for(int i=0;i<argc;i++)
	{
		cout<<argv[i]<<endl;
		fileVec.push_back(argv[i]);
	}
	return fileVec;	
}
	
};


