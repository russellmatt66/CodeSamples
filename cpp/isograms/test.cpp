#include <fstream>
#include <vector>
#include <string>

bool is_isogram(std::string str, std::ofstream& errorLog) {
	std::vector<int> freq(256,0);
	for (int is = 0; is < str.size(); is++){
		errorLog << "Ascii value of str[" << is << "] is " << int(str[is]) << std::endl;
		freq[int(str[is])]++;
	}
	for (int iq = 0; iq < freq.size(); iq++){
		if(freq[iq] > 1){
			return false;
		}
	}
	return true;
}

int main(){
	std::ofstream errorLog;
	std::ifstream inputFile;
	std::vector<std::string> testStrings;
	std::string tempString;
	bool tempBool;
	errorLog.open("errorLog.txt");
	inputFile.open("testInput.txt");
	while(std::getline(inputFile,tempString)){
		testStrings.push_back(tempString);
	}
	for (int is = 0; is < testStrings.size(); is++){
		errorLog << "Calling is_isogram() with " << testStrings[is] << std::endl;
		tempBool = is_isogram(testStrings[is], errorLog);
		errorLog << testStrings[is] << " is an isogram? " << tempBool << std::endl;
		errorLog << "~~~~~" << std::endl;
	}
	errorLog.close();
	inputFile.close();	
}

