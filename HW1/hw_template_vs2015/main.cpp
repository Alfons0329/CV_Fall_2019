#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

Mat img;
int n;
int m;
int center_i;
int center_j;
void upside_down()
{
	for (int i = 0; i < center_i; i++)
	{
		for (int j = 0; j < m; j++)
		{
			swap(img.at<uchar>(i, j), img.at<uchar>(n - i - 1, j));
		}
	}
}

void rightside_left()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < center_j; j++)
		{
			swap(img.at<uchar>(i, j), img.at<uchar>(i, m - j - 1));
		}
	}
}

void diag_mirrored()
{
	upside_down();
	rightside_left();
}

void save(string& show_name)
{
	imshow(show_name, img);
	imwrite(show_name, img);
	waitKey(0);
}

void (*function_ptr[3])() = { upside_down, rightside_left, diag_mirrored };

int main()
{
	// IO and set global vars 
	img = imread("lena.bmp", CV_8UC1);
	Mat original = img.clone();
	n = img.rows;
	m = img.cols;
	center_i = img.rows / 2;
	center_j = img.cols / 2;
	
	// doing CV
	vector<string> v_name = { "upside_down.bmp", "rightside_left.bmp", "diag_mirrored.bmp" };
	for (int i = 0; i < 3; i++)
	{
		img = original.clone();
		waitKey(0);
		void* fun_ptr;
		function_ptr[i]();
		save(v_name[i]);
	}
	return 0;
}