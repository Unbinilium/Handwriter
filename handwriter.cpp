// Handwriter v0.1.3 Written by Unbinilium https ://unbinilium.github.io/Handwriter/

#pragma once
#pragma execution_character_set("utf-8")

#include <ctime>
#include <vector>
#include <string>
#include <locale>
#include <fstream>
#include <codecvt>
#include <cstdlib>
#include <iostream>
using namespace std;

#define USAGE              "Usage: Command Arguments <TEXT PATH> <OUT PUT PATH> <FONT(1) PATH> <FONT(2) PATH> ... <FONT(n) PATH>"
#define NOT_FIND_ERR       "Could not find the file!"
#define READ_FILE_STR      "Reading file: "
#define READ_FILE_CUT      "Reading count: "
#define OUT_FILE_ERR       "Could not create out file!"
#define OUT_FILE_STR	   "Writing file: "
#define OUT_FILE_HEADER    "Writing header: "
#define OUT_FILE_FONT      "Writing font file: "
#define OUT_FILE_STYLE     "Writing font style count: "
#define OUT_FILE_TEXT      "Writing text(s) count: "
#define OUT_FILE_FIN       "Writing to file finished!"

#define HTML_TITLE         "Handwriter"
#define FONT_SIZE_MIN      21
#define FONT_SIZE_MAX      25
#define FONT_SIZE_PRECISON 0.1
#define MARGIN_MIN         5.0
#define MARGIN_MAX         5.5
#define MARGIN_PRECISION   0.01

#define RANDOM_NUM(left, right, precision) ((rand() % (int)((right - left) / precision) + left / precision) * precision)

vector<wchar_t>* InputData_To_Vector_UTF8(const char* argv[])
{
	vector<wchar_t>* p = new vector<wchar_t>;
	wifstream infile(argv[1], ios::in | ios::binary);
	const std::locale empty_locale = std::locale::empty();
	typedef std::codecvt_utf8<wchar_t> converter_type;
	const converter_type* converter = new converter_type;
	const std::locale utf8_locale = std::locale(empty_locale, converter);
	infile.imbue(utf8_locale);
	if (!infile.is_open())
	{
		cout << NOT_FIND_ERR << endl;
		exit(EXIT_FAILURE);
	}
	else
	{
		cout << READ_FILE_STR << argv[1] << endl;
	}
	wchar_t wc = NULL;
	while (!infile.eof())
	{
		infile >> noskipws >> wc;
		if (infile.good())
		{
			if (wc != (wchar_t)'\0')
			{
				p->push_back(wc);
			}
		}
	}
	p->pop_back();
	infile.close();
	cout << READ_FILE_CUT << p->size() << endl;
	return p;
}

void OutputData_From_Vector(vector<wchar_t>* p, int* argc, const char* argv[])
{
	vector<wchar_t>::iterator it;
	wofstream outfile;
	outfile.open(argv[2], ios::out | ios::binary);
	if (!outfile)
	{
		cout << OUT_FILE_ERR << endl;
		exit(EXIT_FAILURE);
	}
	cout << OUT_FILE_STR << argv[2] << endl;
	auto utf8 = locale(locale(""), new codecvt_utf8<wchar_t>);
	outfile.imbue(utf8);
	cout << OUT_FILE_HEADER << HTML_TITLE << endl;
	outfile << "<!DOCTYPE html><html><head><meta charset=\"UTF-8\"/><title>" << HTML_TITLE << "</title><style>*{font-family:Arial;font-size:10pt;}";
	for (int i = 1; i < *argc - 2; i++) 
	{
		cout << OUT_FILE_FONT << argv[i + 2] << endl;
		outfile << "@font-face{font-family:'" << to_wstring(i) << "';src:url(" << argv[i + 2] << ")}";
	}
	cout << OUT_FILE_STYLE << p->size() << endl;
	outfile << "a.NoteRef{text-decoration:none}hr{height:1px;padding:0;margin:1em 0;border:0;border-top:1px solid #CCC}table{border:1px solid black;border-spacing:0px;width:100%}td{border:1px solid black}";
	for (int i = 1; i <= p->size(); i++)
	{
		outfile << ".T" << to_wstring(i) << "{font-family:'" << to_wstring((int)RANDOM_NUM(1, *argc - 2, 1)) << "';font-size:" << to_wstring((float)RANDOM_NUM(FONT_SIZE_MIN, FONT_SIZE_MAX, FONT_SIZE_PRECISON)) << "pt;}";
	}
	outfile << "</style></head><body>";
	outfile << "<p style=\"margin-bottom:" << to_wstring((float)RANDOM_NUM(MARGIN_MIN, MARGIN_MAX, MARGIN_PRECISION)) << "pt;\">";
	cout << OUT_FILE_TEXT << p->size() << endl;
	for (it = p->begin(); it != p->end(); ++it)
	{
		static long int c = 1;
		if (*it == (wchar_t)'\n')
		{
			c++;
			outfile << "</p><p style=\"margin-bottom:" << to_wstring((float)RANDOM_NUM(MARGIN_MIN, MARGIN_MAX, MARGIN_PRECISION)) << "pt;\">";
		}
		else
		{
			outfile << "<span class=\"T" << to_wstring(c++) << "\">" << *it << "</span>";
		}
	}
	outfile << "</p></body></html>";
	outfile.close();
	cout << OUT_FILE_FIN << endl;
}

int main(int argc, const char* argv[])
{
	if (argc < 4)
	{
		cerr << argv[0] << USAGE << endl;
		exit(EXIT_FAILURE);
	}
	srand((unsigned)time(NULL));
	vector<wchar_t>* file_to_vector = InputData_To_Vector_UTF8(argv);
	OutputData_From_Vector(file_to_vector, &argc, argv);
	return 0;
}
