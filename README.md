# Bulk USR Generator

Takes as input a tsv file containing sentence IDs in the first column, and Hindi sentence in the second column. An example can be seen [here.](https://docs.google.com/spreadsheets/d/1UZ5__0C4m1JqbXxNfqahKlzQvZnH6ZDI6kp0TZ3gphA/edit?usp=sharing)

## Usage
1. Clone the repository into a folder.
2. In the folder, run

`python3 combined.py [filename]`

where [filename] is the .tsv file containing the sentence IDs and sentences in previously mentioned format. The program might take time to run, and its progress can be tracked in the terminal.

For each file, three folders will be created, for example, if the file is called `hindi11.tsv`, the following folders will be created:
1. `hindi11`: this folder contains the sentences from the spreadsheet in individual txt files.
2. `hindi11_output`: this folder contains the generated USRs, in txt format.
3. `hindi11_output_excel`: this folder contains the generated USRs in excel format.

**Note**: If execution is stopped mid-way, delete all the generated folders, and start again.

