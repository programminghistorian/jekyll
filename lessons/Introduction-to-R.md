---
title: Introduction to R
authors:
- Taryn Dewar
date: 2015-09-14
reviewers:
-
layout: default
---

#Introduction

R is a programming language that can be used to complete simple and complex qualitative analysis on data. This includes doing statistical computing and creating graphics to represent data sets. R can also be used for linear and non-linear modelling, to run statistical tests, and many other functions.

R is ideal for analyzing larger data sets that would take too much time to compute manually. Once you understand how to write some of the basic functions and how to import your own data files, you can generate information about the data quickly and efficiently.

This tutorial will go through some of the basic functions of R and serves as an introduction to the language. It will take you through the installation process, explain some of the tools that you can use in R, as well as how to work with data sets while doing research.

#Installing R

R is run off of a console that can be launched from your computer once it has been installed. To get started with R, download the program from [The Comprehensive R Archive Network](http://cran.cnr.berkeley.edu/). R is compatible with Linux, Mac, and Windows.

When you first open the R console, it will open in a window that looks like this:

{% include figure.html src="../images/Intro-to-R-1.png" caption="R Console" %}  

The console is where you will enter commands to create objects, vectors, variables, and matrices, as well as use functions to analyze data. To clear the initial screen, go to “Edit” in the menu bar and select “Clear Console”. You can also change the appearance of the console by clicking on the colour wheel at the top of the console. You can adjust the background screen colour and the font colours for functions. Spend some time looking at the different features of the console, including the `Commands` history and file loading features.

If at any time you become stuck with a function or cannot fix an error, type `help()` into the console to bring up the built-in help system. Use the arrow keys on your keyboard to scroll up and down in the console if you need to make any changes to previous lines.

#Basic Functions

R runs like a command-line system where you enter data into a console row by row.

It can do basic mathematical operations when you enter functions into the console. There are many different ways to compute different functions using R. This tutorial will give the basic ways to use some of the tools, but as you get more comfortable with the program, you will be able to develop faster ways to make computations.

Try entering `1+3` into the console and then hit “Enter”. The line that appears should read `[1] 4`.

R can do more than just simple arithmetic, though. You can create objects, or variables, to represent numbers and expressions. For example, try typing `x<- 3` into the console and then `x` on the next line. The `<-` notation assigns the value `3` to the variable `x`. You should see:

```
> x <- 3
> x
[1] 3
```

R is case sensitive, so be careful that you use the same notation when you use the variables you have assigned in other actions. To remove a variable from the console, type `rm()` with the variable you want to remove inside the brackets and hit "Enter". To see all of the variables you have assigned, type `ls()` into the console and press enter – this will help to make sure you are not reassigning variables. This is also important because R stores all of the objects you create in its memory, so even if you cannot see `x` in the console, it may have been saved before and not removed.

For now, we will use letters as variables but when you start working with your own data it may be easier to assign names that are more representative of that data.

##Practice

Assign variable `x` with a value of `4` and `y` with a value of `2`. Add `x` and `y` together on the next line. It will look like this:

```
> x<- 4
> y<- 2
> x+y
[1] 6 
```

Remove variables `x` and `y`. Re-enter `x=5` and `y=7` to complete the following exercises:

1.	`x-y`
2.	`x*y`
3.	`2*x+3*y`

##Solutions

1.	`-2`
2.	`35`
3.	`31`

You can also use variables to create lists called “vectors”. To do this, we use the `c` command. `c` stands for “combine" and lets us link numbers together. An example of a list would be:

```
> x<- c(3,7,2,9)
> x[1]
[1] 3
```

You can select one of the values in the list to work with by typing the variable followed by the number of the term in the list. In this case, the first value was selected, which was `3`.

You can also create sequences of numbers that follow a pattern instead of a list with random terms. There are a number of ways to do this. The easiest way is to use a semicolon:

```
> y<- 1:10
> y
[1] 1 2 3 4 5 6 7 8 9 10
```

When the series is expanded, it shows all of the terms. To find the length of a sequence or series, or the number of terms included, use the `length()` function. You can also use that command to specify how long a series should repeat for.

```
> seq(1,20,by=4)
[1] 1 5 9 13 17
```

##Practice

1.	What would `a<- 2:15` return?
2.	Define: `seq(4,25,by=2)`
3.	What is the length of the sequence in Question 2? (Hint – first assign the sequence a variable name and then find the answer or include the entire formula in the length function.)
4.	What would you enter to return `7 10 13 16 19 22 25 28`

##Solutions

1.	`2 3 4 5 6 7 8 9 10 11 12 13 14 15`
2.	`4 6 8 10 12 14 16 18 20 22 24`
3.	`11`
4.	`seq(7,30,by=3)`

#Matrices

You can use R to construct matrices and then make calculations. One of the simplest ways to do this is to create at least two variables or vectors and then bind them together. Try setting the following variables `x` and `y`. To create a matrix, use the `cbind()` function. This binds `x` and `y` together in columns, represented by `z` below. 

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

#Using Data Sets

R is loaded with quite a few data sets already. To bring up the list of all of the data sets, type `data()` into the console and hit "Enter". These are great for practicing while you are learning the language, but in order to use R in your own research you will have to import your data into R. One of the easiest ways to do this is to have your data in a CSV file.

A CSV (comma separated value) file will show the values in rows and columns and separates those values with a comma. You can save any document you create in Excel as a .csv file and then load it into R. To use a CSV file in R, assign a name to the file using the `<-` command and then type `read.csv(file=”file-name.csv”,header=TRUE,sep=”,”)` into the console. `file-name` tells R which file to select, while setting the header to `TRUE` says that the first row are headings and not variables. `sep` means that there is a comma between every number and line. Make sure that the file you are accessing is within the directory you are working from (to check this, you can type `dir()` into the console or `getdir()`. You can change the directory if needed.)

Before uploading your own data, practice using the built-in datasets. To access the datasets, you will first have to install them. Type `install.packages()` into the console and hit "Enter" to access the datasets. From there, you can search through the built-in data sets by entering `data()` into the console.

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

This shows the information in the `AirPassengers` dataset. You can now use R to determine a number of different things from this data. To find the mean and median values in the data set, you can enter `mean(AirPassengers)` and `median(AirPassengers)`, respectively, into the console. However, this can be tedious if there are a number of different values that you want to calculate. To produce a summary of the data, enter `summary(AirPassengers)` into the console. This will give you the minimum and maximum data points, as well as the mean, median and first and third quartile values.

Using the `summary()` function is a better way to get an overview of the entire data set, but what happens if you are interested in just part of the data? For example, if you wanted to create a summary for 1955 instead of the entire twelve-year period, you can run a summary on just the data you are interested in studying. There are two ways to go about doing this – you can either select the terms you want or create a variable to represent those terms:

```
> y1955<- AirPassengers[73:84]
> y1955
[1] 242 233 267 269 270 315 364 347 312 274 237 278
> summary(1955)
 Min.  1st Qu.  Median  Mean  3rd Qu.  Max
 233.0  260.8   272.0   284.0  312.8   364.0
 > summary(AirPassengers[73:84]
  Min.  1st Qu.  Median  Mean  3rd Qu.  Max
 233.0  260.8   272.0   284.0  312.8   364.0
```

If you only needed to use the data once, it would probably be easier to use the second option, but if you were doing a number of different calculations, creating a variable for each year would make more sense.

##Practice

1.	Load the dataset UKgas into the console.
2.	Compute a summary of the data.
3.	Find the mean gas usage for 1970.

##Solutions

1.	
```
> data(UKgas)
> UKgas
       Qtr1   Qtr2   Qtr3   Qtr4
1960  160.1  129.7   84.8  120.1
1961  160.1  124.9   84.8  116.9
1962  169.7  140.9   89.7  123.3
1963  187.3  144.1   92.9  120.1
1964  176.1  147.3   89.7  123.3
1965  185.7  155.3   99.3  131.3
1966  200.1  161.7  102.5  136.1
1967  204.9  176.1  112.1  140.9
1968  227.3  195.3  115.3  142.5
1969  244.9  214.5  118.5  153.7
1970  244.9  216.1  188.9  142.5
1971  301.0  196.9  136.1  267.3
1972  317.0  230.5  152.1  336.2
1973  371.4  240.1  158.5  355.4
1974  449.9  286.6  179.3  403.4
1975  491.5  321.8  177.7  409.8
1976  593.9  329.8  176.1  483.5
1977  584.3  395.4  187.3  485.1
1978  669.2  421.0  216.1  509.1
1979  827.7  467.5  209.7  542.7
1980  840.5  414.6  217.7  670.8
1981  848.5  437.0  209.7  701.2
1982  925.3  443.4  214.5  683.6
1983  917.3  515.5  224.1  694.8
1984  989.4  477.1  233.7  730.0
1985 1087.0  534.7  281.8  787.6
1986 1163.9  613.1  347.4  782.8
```

2.  
```
> summary(UKgas)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   84.8   153.3   220.9   337.6   469.9  1164.0 
```

3. 
 ```
> mean(UKgas[41:44])
[1] 198.1
```
 
Depending on the data set, you may also be able to use the `attach()` function to help with your calculations. When you use that function, it lets you access the datasets already in R, or that you add in, and makes the contents of that dataset into a directory that can be searched based on the column headings.

#Next Steps

Now that you know a few of the basics of R, you can explore some of the other functions of the program, including statistical computations, producing graphs, and creating your own functions.

For more information on R, you can also visit the [R manual](https://cran.r-project.org/doc/manuals/r-release/R-intro.html). 

There are also a number of other R tutorials online including:
- [R: A self-learn tutorial](https://www.nceas.ucsb.edu/files/scicomp/Dloads/RProgramming/BestFirstRTutorial.pdf)
- [R Tutorial: An R Introduction to Statistics](http://www.r-tutor.com/r-introduction)
- [R Tutorial](http://www.cyclismo.org/tutorial/R/index.html)
- [DataCamp Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r)
