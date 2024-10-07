## SQLite Lab

![4 17-etl-sqlite-RAW](https://github.com/nogibjj/sqlite-lab/assets/58792/b39b21b4-ccb4-4cc4-b262-7db34492c16d)


# US Birth Data Pipeline

This project provides a simple ETL (Extract, Transform, Load) pipeline for processing and analyzing the US Birth dataset. The pipeline includes three main components:
1. **Extract**: Downloads the dataset from a URL and saves it locally.
2. **Transform & Load**: Transforms the data and loads it into a local SQLite3 database.
3. **Query**: Performs SQL operations such as SELECT, INSERT, UPDATE, and DELETE on the dataset.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
  - [Extract Data](#extract-data)
  - [Transform and Load Data](#transform-and-load-data)
  - [Query Data](#query-data)
- [Dependencies](#dependencies)
- [License](#license)

## Project Structure


- **mylib/extract.py**: Downloads the dataset from the specified URL.
- **mylib/transform_load.py**: Transforms and loads the dataset into a local SQLite3 database.
- **mylib/query.py**: Executes SQL queries to interact with the dataset in the SQLite3 database.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IDS_DE_SQL_T.git
   cd IDS_DE_SQL_T
pip install -r requirements.txt
python mylib/extract.py
python mylib/transform_load.py
python mylib/query.py
pip install -r requirements.txt