# ProDJLink Data Logger

## Project description

This project reads data from the ProDJLink network with [Beat Link Trigger][1], sends it via UDP to a Python script and then saves the data in a SQL database.

> **Disclaimer**: This project is **not** affiliated with Pioneer Corp. or its related companies
in any way and has been written independently! ProDJLink to SQL is licensed under the [MIT license][license-link]. The maintainers of the project are not liable for any damages to your data cause this is an expermintal project.

## Table of contents

1. Introduction
2. Requirements
3. Installation
4. Usage
5. Configuration
6. Database structure
7. Troubleshooting
8. Licence

## Introduction

A brief introduction to the project and its objectives.

## Requirements

- Beat Link Trigger
- Python 3.x
- SQL database (e.g. MySQL, PostgreSQL)
- UDP support

## Installation

Steps to install the required software and libraries:

1. clone this repository: `git clone https://github.com/hfanieng/ProDJLink-to-SQL`
2. install the Python dependencies:  
`pip install mysql.connector`  
`pip install socket`  
`pip install json`

3. configure the SQL database (see configuration)

## Usage

Instructions for using the project:

1. start Beat Link Trigger and configure it to send data over UDP.
2. run the Python script: `python main.py`
3. check the SQL database for the stored data.

## Configuration

Details on the configuration of the project, including the database connection and UDP settings.

## Database structure

A description of the tables and fields in the SQL database.

## Troubleshooting

Common problems and their solutions.

## Licence

Information on licensing the project.

[1]:<https://github.com/Deep-Symmetry/beat-link-trigger>
