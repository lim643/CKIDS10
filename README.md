# Data Scraper UC Wages
## Table of Contents
1. [Points of Contact](#points-of-contact)
2. [Getting Started](#getting-starteed)
    - [Required Software](#required-software)
    - [Running Locally](#running-locally)
    - [Model](#model)

<a name = "points-of-contact)"></a>
## Points of Contact
- Matthew Lim (lim643@usc.edu)
- Minh Nguyen (minhhn@usc.edu)
- Kevin Tran (ktran774@usc.edu)
- Sindhu Ravi (sindhu@usc.edu)
- Vihang Sunil Mangalvedhekar (mangalve@usc.edu)

<a name = "getting-started"></a>
## Getting Started
<a name = "required-software"></a>
### Required Software
1. Install required packages.
```
pip3 install -r requirements.txt
```

<a name = "running-locally"></a>
### Running Locally
1 Navigate to the directory data.
2 Create proper input file of desired information as follows and name it input.csv.
```
First Name, Middle Initial (if provided), Last Name, Institution
Jane,,Doe,Los Angeles
John,,Smith,Davis


Possible Institutions:
ASUCLA
Berkeley
Davis
Hastings
Irvine
Los Angeles
Merced
Riverside
San Diego
San Francisco
Santa Barbara
Santa Cruz
UCOP
```
3 Navigate to the directory app.
4 Run the following command:
```
python3 main.py
```
5 Navigate to the directory data. There should be an output file called output.csv.

<a name = "model"></a>
### Model
![](/images/diagram.png)

