# Data Scraper UC Wages
## Table of Contents
1. [Getting Started](#getting-starteed)
2. [Running Locally](#running-locally)
3. [Model](#model)

<a name = "getting-started"></a>
## Getting Started
### Required Software
1. Install required packages.
```
pip3 install -r requirements.txt
```

<a name = "running-locally"></a>
## Running Locally
1. Install required packages.
```
pip3 install -r requirements.txt
```
2. Navigate to the directory data
3. Create proper input file of desired information as follows
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
4. Navigate to the directory app
5. Run the following command
```
python3 main.py
```
6. Navigate to the directory data. There should be an output file called output.csv.

<a name = "model"></a>
## Model
![](/images/diagram.png)

