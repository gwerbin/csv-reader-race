## The Great CSV Reader Race

May the fastest parser win; may the most useful attain glory.

Rules:
1. The parsed result must be correct. Correctness is judget by the output from R's `read.csv` which is nothing if not battle tested. If the output is different, the entry is invalidated.
2. I am the umpire and my computer is the official test machine. It must 
3. All entries must include instructions to run them, and instructions for installing dependencies. They don't necessarily need to be cross-platform, but they do need to run on El Capitan. See Rule #2.

Contributions are welcome! Just make a pull request.

Todos:
- ☐ Adhere to my own rules and add installation/execution instructions for the scripts I have here.
- ☐ Add a correctness-checking script.
- ☐ Add a versioning/naming system for entries.
- ☐ Add a script to generate the data.
- ☐ Add more/better data sets to test against.
- ☐ Add a fair system for doing multiple runs.


### Method

Each function lives in a separate file. Each is timed using its language's native timing features.


### Data

The test data set is the famous "iris" data set, repeated 13001 times. This produces a data set that is 1950150 rows and 5 columns, and about 59 megabytes in size.


### Setup

- Early 2015 MacBook Pro
    - 2.7 GHz Intel Core i5 processor
    - 16 GB 1867 MHz DDR3 RAM
    - Mac OS version 10.11.6

- R version 3.3.1
    - data.table version 1.9.6

- Python version 3.5.2
    - Pandas version 0.18.1


### Results
- R `data.table::fread()`: 0.978 seconds
- Python `csv.reader()`: 3.754 seconds
- Python `pandas.read_csv()`: 1.445 seconds
