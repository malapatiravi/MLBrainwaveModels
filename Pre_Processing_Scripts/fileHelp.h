
#ifndef FILEHELP_H
#define FILEHELP_H

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;
class fileHelp
{
	public:
		
		void setFileData(std::string fileData_);
		std::string getFileData();
		std::vector<std::vector<double>> getMatrix(char delim_);
		std::string loadFile(std::string path);
		std::vector<std::string> parseCommandLineArguments(int argc, char* argv[]);
		std::vector<std::string> getListOfFiles(std::string path);
		std::vector<std::string> getListOfFolders(std::string path);
		std::vector<std::string> getListOfFilesAndFolders(std::string path);
		bool closeFile();
		std::vector<std::vector<double>*> loadFileAsMatrix(std::string path, char delim_);
		size_t getNumberOfCol(std::string testLine, char delim_);
		std::vector<double>* createVecObject();
		std::vector<std::vector<double>> getFeaturesAcc(std::vector<std::vector<double>> matrix_, int windowSize_);
		std::vector<double> getMeanVec(std::vector<std::vector<double>*> &matrix_, int windowSize_);
		std::vector<double> getMeanVecSingle(std::vector<double> singleLine, int windowSize_);
		std::vector<double> getPercentileVec(std::vector<double> vecInput, double Percentages[], int ArrSize);
		double GetStdDev(std::vector<double> v);
		double GetMean(std::vector<double> v);
		double GetSquareSum(std::vector<double> v);
		double GetSum(std::vector<double> v);
		double GetMagnitude(double a, double b, double c);
		std::string NumberToString (double Number);
		std::string fileData;
		std::vector<std::vector<double>*> vecMatrix;
		std::vector<std::vector<double>*> featureVec;
		std::string fileName;
};

#endif
