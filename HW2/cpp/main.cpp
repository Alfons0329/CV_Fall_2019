#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;
Mat img;
vector<int> mymap;

void dfs(int i, int j, int& label, int& row, int& col)
{
	if (i < 0 || i >= row || j < 0 || j >= row)
	{
		return;
	}
	else if (img.at<uchar>(i, j) != 1) // has been labeld or background 0
	{
		return;
	}
	else
	{
		img.at<uchar>(i, j) = label;
		if (i > 0) dfs(i - 1, j, label, row, col);
		if (i < row - 1) dfs(i + 1, j, label, row, col);
		if (j > 0) dfs(i, j - 1, label, row, col);
		if (j < col - 1) dfs(i, j +1, label, row, col);
	}
}

int main()
{
	// read image 
	img = imread("lena.bmp", CV_8UC1);
	int row = img.rows, col = img.cols;

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			img.at<uchar>(i, j) = (img.at<uchar>(i, j) > 0x7f ? 1 : 0);
		}
	}

	int label = 2;
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			if (img.at<uchar>(i, j) == 1)
			{
				printf("i %d j %d \n", i, j);
				dfs(i, j, label, row, col);
				label += 10;
			}
		}
	}

	mymap.resize(1 << 17);
	fill(mymap.begin(), mymap.end(), 0);
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			mymap[img.at<uchar>(i, j)]++;
		}
	}

	system("pause");
	// show image
	imshow("connected_components", img);

	// write image 
	imwrite("connected_components.jpg", img);

	waitKey(0);

	int idx = 0;
	for (auto x : mymap)
	{
		if (x > 0)
		{
			printf("%d --> %d \n", idx++, x);
		}
	}
	return 0;
}