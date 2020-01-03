#include <iostream>
#include <fstream>
#include <istream>
#include <vector>
#include "missingValues.h"
using namespace std;
bool missingValues::missingValue(std::string fileData)
{
	int state=0;
	std::string one,two,three, four, five, six, seven, eight;
	one=""; two=""; three=""; four="";five=""; six="";seven="", eight="";
	int start=0;
	for(size_t i=0; i<fileData.length();i++)
	{
		if(state==0 || state==1)
		{
		  if(state==0)
		  {
		      if(fileData[i]==44)
		      {
			start=std::stoi(one);
			state=2;
		      }
		      else
			one += fileData[i];
		  }
		  else
		  {
		    if(fileData[i]==44)
		    {
			start=start+1;
			if(start==stoi(one))
			  state=2;
			else
			{

			  cout<<"\n "<<start<<" and "<<stoi(one);
			  return false;
			}
		    }
		    else
		      one += fileData[i];
		  }			
		}
		/*else if(state==1)
		{
		 if(fileData[i]==44)
		 {
		   cout<<one;
		   state=2;
		 }
		   
		 else
		   one += fileData[i];
		}*/
		else if(state==2)
		{
			if(fileData[i]==44)
			{
//				cout<<two;
				state=3;
			}
			else
				two += fileData[i];
		}
		else if(state==3)
		{
			if(fileData[i]==44)
			{
//				cout<<three;
				state=4;
			}
			else
				three += fileData[i];
		}
		else if(state==4)
		{
			if(fileData[i]==44)
			{
//				cout<<four;
				state=5;
			}
			else 
				four += fileData[i];
		}
		else if(state==5)
		{
			if(fileData[i]==44)
			{
//				cout<<five;
				state=6;
			}
			else 
				five += fileData[i];
		}
		else if(state==6)
		{
			if(fileData[i]==44)
				state=7;
			else 
				six += fileData[i];
		}
		else if(state==7)
		{
			if(fileData[i]==44)
				state=8;
			else 
				seven += fileData[i];
		}
		else if(state==8)
		{
			if(fileData[i]==10)
			{
				state=1;
//				cout<<"\nNew Line";
				//cout<<"\n"<<one<<","<<two<<","<<three<<","<<four<<","<<five<<","<<six<<","<<seven<<","<<eight<<endl;
				one="";two="";three="";four="";five="";six="";seven="";eight="";
			}
			else 
				eight += fileData[i];
		}	        

	}
	return true;
}



