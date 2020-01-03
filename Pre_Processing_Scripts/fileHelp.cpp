#include <iostream>
#include <vector>
#include <fstream>
#include <istream>
#include "fileHelp.h"
#include <math.h>
#include <algorithm>
using namespace std;
std::string fileHelp::loadFile(std::string path)
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
std::vector<double> fileHelp::getPercentileVec(std::vector<double> vecInput, double Percentages[], int ArrSize)
{
	std::sort(vecInput.begin(), vecInput.end());
	std::vector<double> ReturnValue;
	for (int i = 0; i < ArrSize; i++)
	{
		if ((Percentages[i]>100) || Percentages[i] < 0) ReturnValue.push_back(-1.0);
		else ReturnValue.push_back(vecInput[(Percentages[i]*1.0*vecInput.size()*1.0)/100.0]);
	}
	return ReturnValue;

}
double fileHelp::GetMean(std::vector<double> v)
{
	double sum = std::accumulate(v.begin(), v.end(), 0.0);
	return sum*1.0/(v.size()*1.0);
}
double fileHelp::GetMagnitude(double a, double b, double c)
{
	cout<<"MAgnitude:"<<a<<b<<c;
	return (pow((pow(a,2)+pow(b,2)+pow(c,2)), 0.5));
}

double fileHelp::GetStdDev(std::vector<double> v)
{
	double mean = GetMean(v);
	std::vector<double> diff(v.size());
	std::transform(v.begin(), v.end(), diff.begin(), std::bind2nd(std::minus<double>(), mean));
	double sq_sum = std::inner_product(diff.begin(), diff.end(), diff.begin(), 0.0);
	double stdev = std::sqrt(sq_sum / v.size());
	return stdev;
}
double fileHelp::GetSquareSum(std::vector<double> v)
{
	double mean = GetMean(v);
	std::vector<double> diff(v.size());
	std::transform(v.begin(), v.end(), diff.begin(), std::bind2nd(std::minus<double>(), mean));
	double sq_sum = std::inner_product(diff.begin(), diff.end(), diff.begin(), 0.0);
	return sq_sum;
}
double fileHelp::GetSum(std::vector<double> v)
{
	double sum = std::accumulate(v.begin(), v.end(), 0.0);
	return sum;
}
std::string fileHelp::NumberToString (double Number)
{
		std::ostringstream ss;
		ss << std::fixed << Number;
		return ss.str();
}
std::vector<double> fileHelp::getMeanVec(std::vector<std::vector<double>*> &VecMatrix, int windowSize_)
{
	double Percentiles[] 							= {10.0,25.0,50.0,75.0,90.0};
	int window=0;
	//double mean=0;
	//int count;
	std::vector<double> meanVec;
	std::vector<double> tempVecX;
	std::vector<double> tempVecY;
	std::vector<double> tempVecZ;
	std::vector<double> tempVecM;
	double XMean;
	double YMean;
	double ZMean;
	double MMean;
	double XStdDev;
	double YStdDev;
	double ZStdDev;
	double MStdDev;
	double XPercentile10;
	double XPercentile25;
	double XPercentile50;
	double XPercentile75;
	double XPercentile90;
	double YPercentile10;
	double YPercentile25;
	double YPercentile50;
	double YPercentile75;
	double YPercentile90;
	double ZPercentile10;
	double ZPercentile25;
	double ZPercentile50;
	double ZPercentile75;
	double ZPercentile90;
	double MPercentile10;
	double MPercentile25;
	double MPercentile50;
	double MPercentile75;
	double MPercentile90;
	std::vector<double> XpercentileVec;
	std::vector<double> YpercentileVec;
	std::vector<double> ZpercentileVec;
	std::vector<double> MpercentileVec;
	int count=0;
	//for(size_t i=1;i<vecMatrix.size();i++)

	{
		//if(i==1||i==2||i==3||i==8)
		{
			for(size_t it=0;it<(*vecMatrix[1]).size();it++)
			{
				window++;
				tempVecX.push_back((*vecMatrix[0])[it]);
				tempVecY.push_back((*vecMatrix[1])[it]);
				tempVecZ.push_back((*vecMatrix[2])[it]);
				tempVecM.push_back((*vecMatrix[6])[it]);

				if(window == windowSize_ || it==(*vecMatrix[1]).size()-1)
				{
					if(window==windowSize_)
					{
						count++;
						window=0;
						cout<<"\n First Vector is"<<count;
						//The below is mean
						XMean=GetMean(tempVecX);
						YMean=GetMean(tempVecY);
						ZMean=GetMean(tempVecZ);
						MMean=GetMean(tempVecM);
						//The below is std deviation
						XStdDev=GetStdDev(tempVecX);
						YStdDev=GetStdDev(tempVecY);
						ZStdDev=GetStdDev(tempVecZ);
						MStdDev=GetStdDev(tempVecM);

						//The below is X percentiles
						XpercentileVec = getPercentileVec(tempVecX,Percentiles,5);
						YpercentileVec = getPercentileVec(tempVecY,Percentiles,5);
						ZpercentileVec = getPercentileVec(tempVecZ,Percentiles,5);
						MpercentileVec = getPercentileVec(tempVecM,Percentiles,5);

						XPercentile10 = XpercentileVec[0];
						XPercentile25 = XpercentileVec[1];
						XPercentile50 = XpercentileVec[2];
						XPercentile75 = XpercentileVec[3];
						XPercentile90 = XpercentileVec[4];

						YPercentile10 = YpercentileVec[0];
						YPercentile25 = YpercentileVec[1];
						YPercentile50 = YpercentileVec[2];
						YPercentile75 = YpercentileVec[3];
						YPercentile90 = YpercentileVec[4];

						ZPercentile10 = ZpercentileVec[0];
						ZPercentile25 = ZpercentileVec[1];
						ZPercentile50 = ZpercentileVec[2];
						ZPercentile75 = ZpercentileVec[3];
						ZPercentile90 = ZpercentileVec[4];

						MPercentile10 = MpercentileVec[0];
						MPercentile25 = MpercentileVec[1];
						MPercentile50 = MpercentileVec[2];
						MPercentile75 = MpercentileVec[3];
						MPercentile90 = MpercentileVec[4];
					}
					tempVecX.clear();
					tempVecY.clear();
					tempVecZ.clear();
					tempVecM.clear();
					XpercentileVec.clear();
					YpercentileVec.clear();
					ZpercentileVec.clear();
					MpercentileVec.clear();
					featureVec.push_back(createVecObject());
					(*featureVec[count-1]).push_back(XMean);
					(*featureVec[count-1]).push_back(YMean);
					(*featureVec[count-1]).push_back(ZMean);
					(*featureVec[count-1]).push_back(MMean);

					(*featureVec[count-1]).push_back(XStdDev);
					(*featureVec[count-1]).push_back(YStdDev);
					(*featureVec[count-1]).push_back(ZStdDev);
					(*featureVec[count-1]).push_back(MStdDev);

					(*featureVec[count-1]).push_back(XPercentile10);
					(*featureVec[count-1]).push_back(XPercentile25);
					(*featureVec[count-1]).push_back(XPercentile50);
					(*featureVec[count-1]).push_back(XPercentile75);
					(*featureVec[count-1]).push_back(XPercentile90);

					(*featureVec[count-1]).push_back(YPercentile10);
					(*featureVec[count-1]).push_back(YPercentile25);
					(*featureVec[count-1]).push_back(YPercentile50);
					(*featureVec[count-1]).push_back(YPercentile75);
					(*featureVec[count-1]).push_back(YPercentile90);

					(*featureVec[count-1]).push_back(ZPercentile10);
					(*featureVec[count-1]).push_back(ZPercentile25);
					(*featureVec[count-1]).push_back(ZPercentile50);
					(*featureVec[count-1]).push_back(ZPercentile75);
					(*featureVec[count-1]).push_back(ZPercentile90);

					(*featureVec[count-1]).push_back(MPercentile10);
					(*featureVec[count-1]).push_back(MPercentile25);
					(*featureVec[count-1]).push_back(MPercentile50);
					(*featureVec[count-1]).push_back(MPercentile75);
					(*featureVec[count-1]).push_back(MPercentile90);




				}

			}
			//
		}

	}
	std::string mainStr="";
	for(size_t it=0; it<featureVec.size();it++)
	{
		for(size_t t=0; t<(*featureVec[it]).size(); t++)
		{
			//cout<<(*featureVec[it])[t]<<",";
			if(t!=(*featureVec[it]).size()-1)
				mainStr += NumberToString((*featureVec[it])[t])+",";
			else
				mainStr += NumberToString((*featureVec[it])[t])+"\n";
		}
		//cout<<endl;
		//mainStr += "\n";
	}
	 ofstream myfile;
	 myfile.open (fileName+".csv");
	 myfile << mainStr;
	 myfile.close();
	cout<<mainStr;
	//The below is the junk code.
	/*
	for(size_t i=1;i<vecMatrix.size();i++)
	{
		if(i==1||i==2||i==3||i==8)
		{
			cout<<"Doing it for : "<<i;
			for(size_t it=0;it<(*vecMatrix[i]).size();it++)
			{
				mean = mean + (*vecMatrix[i])[it];
				window++;
				if(window == windowSize_ || it==(*vecMatrix[i]).size()-1)
				{
					if(window==windowSize_)
					{
						mean = mean/windowSize_;
						window=0;
						meanVec.push_back(mean);
						//cout<<"pushing back:"<<mean;
						mean=0;
					}
					else if(it == (*vecMatrix[i]).size()-1)
					{
						mean= mean/window;
						window=0;
						meanVec.push_back(mean);
						mean=0;
					}
				}
		//cout<<(*VecMatrix[0])[it]<<","<<(*VecMatrix[1])[it]<<","<<(*VecMatrix[2])[it]<<","<<(*VecMatrix[3])[it]<<endl;
			}

			featureVec.push_back(createVecObject());
			int x;
			if(i==8)
			{
				x=3;
			}
			else x=i-1;

			for(size_t k=0;k<meanVec.size();k++)
			{
				(*featureVec[x]).push_back(meanVec[k]);
				cout<<meanVec[k]<<endl;
			}
			meanVec.clear();
		}
	}
		cout<<"\n";
		cout<<"\n ==============================================================================================================================="; */
	/*for(size_t i=0;i<meanVec.size();i++)
	{
		cout<<meanVec[i]<<endl;
	}*/

	/*the below code prints the X, y, X and magnitude values usinf the feature vector created newly*/
	/*for(size_t it=0; it<featureVec.size();it++)
	{
		for(size_t t=0; t<(*featureVec[it]).size(); t++)
		{
			cout<<(*featureVec[it])[t]<<endl;

		}
	}*/



	/*for(size_t i=0;i<singleLine.size();i++)
	{
		mean = mean + singleLine[i];
		window++;
		if(window == windowSize_-1 || i==singleLine.size()-1)
		{
			if(window==windowSize_)
			{
				mean = mean/windowSize_;
				window=0;
				meanVec.push_back(mean);
				mean=0;
			}
			else if(i == singleLine.size()-1)
			{
				mean= mean/window;
				window=0;
				meanVec.push_back(mean);
				mean=0;
			}
		}
	}*/

	return meanVec;
}
/*std::string fileHelp::NumberToString (double Number)
{
	std::ostringstream ss;
	ss << std::fixed << Number;
	return ss.str();
}*/
std::vector<double> fileHelp::getMeanVecSingle(std::vector<double> singleLine, int windowSize_)
{
	//int window=0;
	//double mean=0;int count;
	std::vector<double> meanVec;
	//cout<<"\n size is : "<<singleLine.size()<<"First is"<<singleLine[0];
	cout<<singleLine[1];
	for(size_t i=0;i<singleLine.size();i++)
	{
		cout<<singleLine[i]<<endl;
	}
	return meanVec;
}
std::vector<std::vector<double>> getFeaturesAcc(std::vector<std::vector<double>> matrix_, int windowSize_)
{
	//cout<<(*matrix_[0])[0];
	return matrix_;
}
std::vector<std::string> fileHelp::parseCommandLineArguments(int argc, char* argv[])
{
	std::vector<string> fileVec;
	for(int i=0;i<argc;i++)
	{
		cout<<argv[i]<<endl;
		fileVec.push_back(argv[i]);
	}
	return fileVec;
}
std::vector<double>* fileHelp::createVecObject()
{
	return new vector<double>;
}

void fileHelp::setFileData(std::string fileData_)
{
	fileData=fileData_;
	fileData_.clear();
    return;
}

std::vector<std::vector<double>*> fileHelp::loadFileAsMatrix(std::string path, char delim_)
{
	//std::vector<std::vector<double>*> vecMatrix;
std::cout<<"Inside the load Matrix";
	std::string testLine;
	ifstream iFile;
    iFile.open(path.c_str());
	//size_t x;
/*	if(iFile.good())
	{
		//std::string testLine;
		getline(iFile,testLine);
		x = getNumberOfCol(testLine, delim_);
		//size_t x = getNumberOfCol(line, delim_);
		cout<<"\n The number of columns are: "<<x;

	}*/

	std::vector<double> *mag=createVecObject();
	for(size_t i=0;i<6;i++)
	{
		vecMatrix.push_back(createVecObject());
	}
	vecMatrix.push_back(mag);
	cout<<"Mag is inserted";
  if(iFile.is_open())
	{
		//getline(iFile,testLine);
		//cout<<testLine;
		while(getline(iFile, testLine))
		{
			//cout<<"TestLine is :"<<testLine;
			std::string str="";
			std::vector<std::string> vecLine;
			for(size_t i=0;i<testLine.length();i++)
			{

				if(testLine[i]==delim_ || testLine[i]==10 || i==testLine.length()-1)
				{
					if(i==testLine.length()-1)
					{
						str += testLine[i];
						vecLine.push_back(str);
						//cout<<"\n Pushing back: "<<str;
						str="";
					}
					else
					{
						vecLine.push_back(str);
						//cout<<"\n Pushing back: "<<str;
						str="";
					}
				}
				else
				{
					str += testLine[i];
				}
			}
			for(size_t it=0;it<vecLine.size();it++)
			{

				(*vecMatrix[it]).push_back(std::stod(vecLine[it]));
			}

		}
		/*The below code calculates the magnitude of the X, Y an dX values. */
		for(size_t it=0;it<(*vecMatrix[0]).size();it++)
		{
			mag->push_back(GetMagnitude((*vecMatrix[0])[it],(*vecMatrix[1])[it],(*vecMatrix[2])[it]));
			//mag->push_back(sqrt(((*vecMatrix[1])[it])*((*vecMatrix[1])[it])+((*vecMatrix[2])[it])*((*vecMatrix[2])[it])+((*vecMatrix[3])[it])*((*vecMatrix[3])[it])));
				//cout<<(*vecMatrix[0])[it]<<","<<(*vecMatrix[1])[it]<<","<<(*vecMatrix[2])[it]<<","<<(*vecMatrix[3])[it]<<endl;
		}
		/*for(size_t it=0;it<(*vecMatrix[0]).size();it++)
		{
			cout<<(*vecMatrix[8])[it]<<endl;
		}*/
    }
    else
    {
		cout<<"\n The file is not in good condition and can not be opened";
    }
    //getMeanVec(vecMatrix, 20);
	return vecMatrix;
}

size_t fileHelp::getNumberOfCol(std::string testLine, char delim_)
{
	std::vector<std::string> vecLine;
	std::string str="";
	for(size_t i=0;i<testLine.length();i++)
	{

		if(testLine[i]==delim_ || testLine[i]==10 || i==testLine.length()-1)
		{
			if(i==testLine.length()-1)
			{
				str += testLine[i];
				vecLine.push_back(str);
				cout<<"\n Pushing back: "<<str;
				str="";
			}
			else
			{

				vecLine.push_back(str);
				cout<<"\n Pushing back: "<<str;
				str="";
			}
		}
		else
		{
			str += testLine[i];
		}
	}
	return vecLine.size();
}



int main(int argc, char* argv[])
{
	fileHelp fh;
	std::vector<std::string> fileList=fh.parseCommandLineArguments(argc, argv);
	cout<<fileList.size();
	for(size_t it=2;it<fileList.size();it++)
	{
		cout<<fileList[it];
		fileHelp fh1;
		fh1.fileName=fileList[it];

		std::vector<std::vector<double>*> matrix_ = fh1.loadFileAsMatrix(fileList[it],',');
		std::cout<<"Creater Matrix";
		cout<<"Size of matrix is: "<<matrix_.size();
	//cout<<"\n size is: "<<(*matrix_[0])[0];
	std::vector<double> featureVec = fh1.getMeanVec(matrix_, std::stoi(fileList[1]));

	}

	vector<std::string> *vec=new vector<std::string>;
	vector<std::vector<string>*> mainVec;
	mainVec.push_back(vec);
	vec->push_back("Hi");
	cout<<vec->at(0);
	cout<<(*vec)[0];
	cout<<(*mainVec[0])[0];
}
