#ifndef STRINGTOVECTOR_H
#def STRINGTOVECTOR_H

#include <string>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;
class StringToVector
{
public:
  void setFileData(std::string fileData_);
  std::string getFileData();
  std::vector<std::vector<double>> getMatrix(char delim_);
private:
  std::string fileData;
  std::vector<std::vector<double>> listOfVec;
  
};
#endif