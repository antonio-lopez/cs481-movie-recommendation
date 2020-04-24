# CPSC 481 Movie Recommendation Project

A python based A.I. project that recommends movies based on a recommendation engine using Surprise, is an easy-to-use Python scikit for recommender systems.

## Prerequisites

This project runs on Windows OS and uses Python 3.7+, Anaconda, and Spyder.

* Download and install Python [here](https://www.python.org/downloads/)

* Download and install Anaconda for Python 3.7 [here](https://www.anaconda.com/distribution/)

Create a new environment:

* Open Anaconda and select the `Environments` tab

* `Create` and new environment and name it `ENV`

* Select Python 3.7 or higher

Install the Surprise library

* Open the terminal by selecting the arrow next to your environment name, `ENV`

* Run `conda install -c conda-forge scikit-surprise`

* Hit ‘y’ to proceed if prompted

Installing Spyder

* Select the `Home` tab of Anaconda

* Make sure the channel selected is your `ENV` environment

* Hit the `Install` button under Spyder to install

Download the repository

* Download and save into your preferred directory

## Usage

* Hit `Launch` under Spyder

* Click `Allow access` if prompted

* Open the `MovieRecommendation.py` file from the repository directory

* Click the green play button to run the recommendation project

## File Description

### MovieLoader

Gets movie name, movie ID, and user ratings from the CSV files. Contains functions for converting a movie ID to a movie name and vice versa.

### MovieRecommendation

Gets an arbritary user, which can be changed in `selectedUser = `, from the ratings CSV file and applies the SVD algorithm to recommend movies the user might like based on their movie likes and dislikes. It also displays the Mean Absolute Error (MAE) and Root mean squared error (RMSE) of the algorithm.

### ml-latest-small

Directory that contains 4 CSV files with the dataset obtained from [Grouplens](https://grouplens.org/datasets/movielens/). Only two files were used in this project.

* movies.csv

* ratings.csv


## Team Members

* Antonio Lopez

* Hunter Gerace

* Zhiwei Su
