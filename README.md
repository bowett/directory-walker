# directory-walker
A colleage at work asked me if I could output a list of all directories and files in a particular path to act as a checklist. The purpose of this utility is to solve that problem.

It takes a given path, walks through it and produces an output in csv. Future versions will allow outputting into json.

## Usage

The utlity takes two arguments:

####--path 
This is the path to the folder you'd like to output

####--output 
The path of the file to create

####--withhidden
A flag - if included the output will include hidden files and directories

####Running the utility
```
$ python directory-walker.py --path /some/path/on/the/computer --output /some/output/file.csv
```

####Windows exe version
As Windows does not come pre-installed with Python I've uploaded a Windows executable version to the dist folder. To use, download and unzip the archive. From the command prompt from within that dir you can then run...

```
> directory-walker.exe --path C:\Some\Path\On\The\Computer --output C:\some\output\file.csv
```

