# message-splitter

## about

This is a small app written in python for splitting larger texts into smaller definable chunks in order to post them on
social media plattforms like Twitter/X or Gettr. The app has a GUI written with (custom)tkinter aswell as a CLI written with
argparse.

## usage

If you like to use the GUI version of the app, just run `app.py` without any arguments but if you would like to use the CLI you can run `app.py` with following arguments:

| argument      | description                                                        | required | example                   |
| ------------- | ------------------------------------------------------------------ | -------- | ------------------------- |
| i / input     | Defines the input file with content to split                       | True     | `-i inputfile.txt`        |
| o / output    | Defines the output file for writing splitted content to            | False    | `--output=outputfile.txt` |
| c / chunksize | character size of chunks in which the given text shall be splitted | True     | `-c 280`                  |

e.g. Windows CLI usage:

```powershell
> python.exe .\app.py -i test.txt --output=outputfile.txt --chunksize=280
```
