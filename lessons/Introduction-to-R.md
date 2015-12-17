---
title: Introduction to R
authors:
- Taryn Dewar
date: 2015-09-14
reviewers:
- James Baker
- John Russell
layout: default
---

#Introduction

R is a programming language that can be used to complete simple and complex quantitative analysis on data. This includes running statistical tests and many other functions. R lets researchers analyze data quickly and produces repeatable results.

R is ideal for analyzing larger data sets that would take too much time to compute manually. Once you understand how to write some of the basic functions and how to import your own data files, you can analyze and visualize the data quickly and efficiently.

This tutorial will go through some of the basic functions of R and serves as an introduction to the language. It will take you through the installation process, explain some of the tools that you can use in R, as well as explain how to work with data sets while doing research. R can be a very useful tool because it enables users to reproduce results - re-running the same code will get you the same results. R also lets users go back to old functions to either repeat them or build off of them.

#Installing R

R is run off of a console that can be launched from your computer once it has been installed. To get started with R, download the program from [The Comprehensive R Archive Network](https://cran.r-project.org/). R is compatible with Linux, Mac, and Windows.

When you first open the R console, it will open in a window that looks like this:

{% include figure.html src="../images/Intro-to-R-1.png" caption="R Console" %}  

The console is where you will type in commands. To clear the initial screen, go to “Edit” in the menu bar and select “Clear Console”. You can also change the appearance of the console by clicking on the colour wheel at the top of the console on a Mac, or by going to "Edit", "GUI preferences" on a PC. You can adjust the background screen colour and the font colours for functions. Spend some time looking at the different features of the console, including the `Commands` history and file loading features.

R runs like a command-line system where you enter data into a console row by row. It can also be run from a [command-line](http://programminghistorian.org/lessons/intro-to-bash) if that is easier for you.

It can do basic mathematical operations when you enter functions into the console. There are many different ways to compute different functions using R. This tutorial will give the basic ways to use some of the tools, but as you get more comfortable with the program, you will be able to develop faster ways to make computations.

If at any time you become stuck with a function or cannot fix an error, type `help()` into the console to open the help page. You can also find general help by using the "Help" menu at the top of the console. If you make a mistake or want to change something in the code you have already written, use the arrow keys on your keyboard to scroll up and down in the console.

#Using Data Sets

R can be used to evaluate data and comes loaded with quite a few data sets already. To bring up the list of all of the available data sets, type `data()` into the console and hit "Enter". These are great for practicing while you are learning the language, but in order to use R in your own research you will have to import your data into R. One of the easiest ways to do this is to have your data in a CSV file.

A CSV (comma separated value) file will show the values in rows and columns and separates those values with a comma. You can save any document you create in Excel as a .csv file and then load it into R. To use a CSV file in R, assign a name to the file using the `<-` command and then type `read.csv(file=”file-name.csv”,header=TRUE,sep=”,”)` into the console. `file-name` tells R which file to select, while setting the header to `TRUE` says that the first row are headings and not variables. `sep` means that there is a comma between every number and line. Make sure that the file you are accessing is within the directory you are working from (to check this, you can type `dir()` into the console or `getdir()`. You can change the directory if needed.)

Before uploading your own data, it helps to practice using the built-in datasets. To access the datasets, you will first have to install them. Type `install.packages()` into the console and hit "Enter" to access the datasets. From there, you can search through the built-in data sets by entering `data()` into the console.

Depending on the data set, you may be able to use the `attach()` function to help with your calculations. When you use that function, it lets you access the datasets already in R, or that you add in, and makes the contents of that dataset into a directory that can be searched based on the column headings.

Take a look at the data set `AirPassengers` by entering `data(AirPassengers)` into the console and hit Enter.

```
> data(AirPassengers)
> AirPassengers
     Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
1949 112 118 132 129 121 135 148 148 136 119 104 118
1950 115 126 141 135 125 149 170 170 158 133 114 140
1951 145 150 178 163 172 178 199 199 184 162 146 166
1952 171 180 193 181 183 218 230 242 209 191 172 194
1953 196 196 236 235 229 243 264 272 237 211 180 201
1954 204 188 235 227 234 264 302 293 259 229 203 229
1955 242 233 267 269 270 315 364 347 312 274 237 278
1956 284 277 317 313 318 374 413 405 355 306 271 306
1957 315 301 356 348 355 422 465 467 404 347 305 336
1958 340 318 362 348 363 435 491 505 404 359 310 337
1959 360 342 406 396 420 472 548 559 463 407 362 405
1960 417 391 419 461 472 535 622 606 508 461 390 432
```

This shows the information in the `AirPassengers` dataset. You can now use R to determine a number of different things from this data. 

#Basic Functions

R can be used to calculate a number of values that might be useful to you while doing research on a data set. For example, you can find the mean, median, minimum, and maximum values in a data set. To find the mean and median values in the data set, you can enter `mean(AirPassengers)` and `median(AirPassengers)`, respectively, into the console. What if you wanted to calculate more than just one value at a time, though? To produce a summary of the data, enter `summary(AirPassengers)` into the console. This will give you the minimum and maximum data points, as well as the mean, median and first and third quartile values.

Using the `summary()` function is a good way to get an overview of the entire data set, but what happens if you are interested in just part of the data? You can select different data points and ranges in R to calculate many different values.

To start, try adding the first two values from the `AirPassengers` data in the console and then hit “Enter”. You should see two lines that read:

```
> 112+118
[1] 230
```

R can do more than just simple arithmetic, though. You can create objects, or variables, to represent numbers and expressions. For example, you could assign the January 1949 value a variable such as `x`. Type `x<- 112` into the console and then `x` on the next line. The `<-` notation assigns the value `112` to the variable `x`. You should see:

```
> x <- 112
> x
[1] 112
```

R is case sensitive, so be careful that you use the same notation when you use the variables you have assigned in other actions. To remove a variable from the console, type `rm()` with the variable you want to remove inside the brackets and hit "Enter". To see all of the variables you have assigned, type `ls()` into the console and press enter – this will help to make sure you are not using the same name for multiple variables. This is also important because R stores all of the objects you create in its memory, so even if you cannot see `x` in the console, it may have been created before and you could accidentally overwrite it when assigning another variable.

You can use letters as variables but when you start working with your own data it may be easier to assign names that are more representative of that data. Even with the `AirPassengers` data, assigning variables that correlate with specific months or years would make it easier to know exactly which points you are working with.

##Practice

1. Assign variables for the January 1950 and January 1960 `AirPassengers` data points. Add the two variables together on the next line:

```
> Jan1950<- 115
> Jan1960<- 417
> Jan1950+Jan1960
[1] 532 
```

2. Use the variables you just created to find the difference between air travellers in 1960 versus 1950:

```
> Jan1960-Jan1950
[1] 302
```

Setting variables for individual data points can be tedious, especially if the names you give them are quite long. However, the process is similar for assigning a range of values to one variable such as all of the data points for one year. We do this by creating lists called “vectors” using the `c` command. `c` stands for “combine" or "concatenate" and lets us link numbers together. For example, you could create a vector for the AirPassenger data for 1949. From there, you can select a data point from the vector by using square brackets:

```
> Air49<- c(112,118,132,129,121,135,148,148,136,119,104,118)
> Air49[2]
[1] 118
```

You can select one of the values in the list to work with by typing the variable followed by the number of the term in the list in square brackets. In this case, the value that corresponds to February 1949 was selected - `118`.

Variables do not have to be just lists of numbers, however. You can create a string of consecutive data points using a semicolon. For example:

```
> y<- 1:10
> y
[1] 1 2 3 4 5 6 7 8 9 10
```

This series included the values from one to ten. When it is expanded, it shows all of the terms in that range. To find the length (or the number of terms included) of a sequence or series, use the `length()` function. 

So, to make defining a variable for all of the `AirPassengers` terms from 1949 easier, you could use the following expression to shorten the variable definition:

```
> Air49<- AirPassengers[1:12]
> Air49
 [1] 112 118 132 129 121 135 148 148 136 119 104 118
```

`Air49` selected the first twelve terms in the `AirPassengers` data set. This gives you the same result as above, but takes less time and also reduces the chance that a value will be written incorrectly in a long string.

##Practice

1.	Create a variable for the 1950 `AirPassengers` data.
2.	Select the second term in the 1950 series.
3.	What is the length of the sequence in Question 2? 

##Solutions

1.	
```
Air50<- AirPassengers[13:24]
Air50
[1] 115 126 141 135 125 149 170 170 158 133 114 140
```
2.	
```
Air50[2]
[1] 126
```
3.	
```
length(Air50)
[1] 12
```

Notice how the above example would not scale well for a large data set - counting through all of the data points to find the right ones could be tedious. Think about what would happen if you were looking for the 96th year of data in a a data set with 150 years worth of data. 

You can actually select specific rows or columns of data if the data set is in a certain format. Load the `mtcars` data set into the console:

```
> data(mtcars)
> mtcars
                     mpg cyl  disp  hp drat    wt  qsec vs am gear carb
Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
```

From here, you can select columns by entering the name of the data set followed by square brackets and the number of either the row or column of data you are interested in. To sort out the rows and columns, think of `dataset[x,y]`, where `dataset` is the data you are working with, `x` is the row, and `y` is the column.

If you were interested in the first row of information in the `mtcars` data set, you would enter the following into the console:

```
> mtcars[1,]
          mpg cyl disp  hp drat   wt  qsec vs am gear carb
Mazda RX4  21   6  160 110  3.9 2.62 16.46  0  1    4    4
```

To see a column of the data, you could enter:

```
> mtcars[,2]
 [1] 6 6 4 6 8 6 8 4 4 6 6 8 8 8 8 8 8 4 4 4 4 8 8 8 8 4 4 4 8 6 8 4
 > mtcars[1,2]
 ```
 
 This would show you all of the values under the `cyl` category. You can also select single data points by entering values for both `x` and `y`:
 
 ```
 > mtcars[1,2]
[1] 6
```

This returns the value in the first row, second column. From here, you could run a summary on one row or column of data without having to count the number of terms in the data set. For example, this would give the summary for the miles per gallon the different cars use in the `mtcars` data set:

```
> summary(mtcars[,1])
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  10.40   15.42   19.20   20.09   22.80   33.90 
```

#Matrices

You can use R to construct matrices and then make calculations. The benefit of knowing how to construct matrices is if you only have a few data points to work with, you could simply create a matrix instead of a CSV that you would then have to import. One of the simplest ways to build a matrix is to create at least two variables or vectors and then bind them together. Try setting the following variables `x` and `y`. To create a matrix, use the `cbind()` function. This binds `x` and `y` together in columns, represented by `z` below. 

```
> x<- c(5,8,9,3)
> y<- c(6,4,7,1)
> z<- cbind(x,y)
> z
	 x y
[1,] 5 6
[2,] 8 4
[3,] 9 7
[4,] 3 1
```

You can set a matrix using `rbind()` as well. Look at the difference between `z` and `a`:

```
> a<- rbind(x,y)
> a
  [,1] [,2] [,3] [,4]
x   5    8    9    3
y   6    4    7    1
```

The second matrix could also be created by using the `t(z)` function, which creates the inverse of `z`.

You can also construct a matrix using the `matrix()` function. It lets you turn a string of numbers into a matrix:

```
> matrix(c(1,2,3,4,5,6),nrow=3)
     [,1] [,2]
[1,]   1    4
[2,]   2    5
[3,]   3    6
>matrix(c(1,2,3,4,5,6),ncol=3)
     [,1] [,2] [,3]
[1,]   1    3    5
[2,]   2    4    6
```

The first part of the function is the list of numbers. After that, you can determine how many rows (`nrow=`) or columns (`ncol=`) the matrix will have. 

You can perform operations on matrices such as adding them together or multiplying by a constant. You can also multiply matrices together, but not through conventional matrix multiplication – in R, multiplication is done component-wise instead and can be expressed as `a%*%b`, for example. To check the dimensions of a matrix, you can use `dim()` to find out the number of rows and columns in a particular matrix.

Another way to avoid writing the same function over and over again is to use the `apply()` function. It allows you to perform the same function on every row or column of a matrix. There are three parts to the apply function: first you have to select the matrix you are using, the terms you want to use, and what function you are performing on a matrix:

```
> y<- matrix(c(1,7,4,9,2,6),nrow=2)
> y 
     [,1] [,2] [,3]
[1,]   1    4    2
[2,]   7    9    6
> apply(y,2,mean)
[1] 4.0 6.5 4.0
```

The above example shows the apply function used on matrix `y` to calculate the mean of each column. If you want to find the mean of each row, you would use `1` instead of `2` inside of the function. 

##Practice

1.	Create a matrix with three rows using the following data: `c(4,8,12,5,7,2,9,13,8)`
2.	Use the ‘cbind’ function to join `x<- c(4,9,3,13)` and `y<- c(5,14,8,7)` together.
3.	Multiply the matrix you just created by 2.
4.	Calculate the mean of each row for the above matrix using the apply function.

##Solutions

1.	
```
> matrix(c(4,8,12,5,7,9,13,8),nrow=3)
     [,1] [,2] [,3]
[1,]   4    5    9
[2,]   8    7   13
[3,]  12    2    8
``` 

2.	
```
> x<- c(4,9,3,13)
> y<- c(5,14,8,7)
> z<- cbind(x,y)
> z
       x    y
[1,]   4    5
[2,]   9   14
[3,]   3    8
[4,]  13    7
```

3.	
```
> z*2
       x    y
[1,]   8   10
[2,]  18   28
[3,]   6   16
[4,]  26   14
```

4. 
 ```
> apply(z,1,mean)
[1] 4.5 11.5 5.5 10.0
```

#Summary and Next Steps

This tutorial has explored the basics of using R to help analyze research data. R can be a very useful tool for humanities research because the data analysis is reproducible and allows you to analyze data quickly without having to set up a complicated system. Now that you know a few of the basics of R, you can explore some of the other functions of the program, including statistical computations, producing graphs, and creating your own functions. 

For more information on R, you can also visit the [R Manual](https://cran.r-project.org/doc/manuals/r-release/R-intro.html). 

There are also a number of other R tutorials online including:

* [R: A self-learn tutorial](https://www.nceas.ucsb.edu/files/scicomp/Dloads/RProgramming/BestFirstRTutorial.pdf)
* [R Tutorial: An R Introduction to Statistics](http://www.r-tutor.com/r-introduction)
* [R Tutorial](http://www.cyclismo.org/tutorial/R/index.html)
* [DataCamp Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r)

Finally, a great resource for digital historians is Lincoln Mullen's [Digital History Methods in R](http://lincolnmullen.com/projects/dh-r/).
