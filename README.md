# Directory tree

## Run
```
python3 main.py
```
Use Ctrl-C to exit.
## Support
- Only A-Z, a-z, 0-9, -, _ is supported in the file / folder name
- All name and command are case-sensitive
- Same name can be used in different folder (e.g. Following directory is valid)
```commandline
Photos
  Jack
  John
Music
  Jack
```
- Do NOT support override in the MOVE
- Do NOT support create child folder if the parent does not exist (Need to create from parent first)
- 