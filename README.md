# PermissionDeniedTest

Repro repo for https://forum.sublimetext.com/t/bug-sublime-holds-lock-on-file-even-after-file-is-saved-and-closed/41392/23?u=herr.kaste

- Clone into Packages folder
- Open the folder in Sublime
- Open the `core/diff.py` file
- From the Sublime console start the program

```
import PermissionDeniedTest
PermissionDeniedTest.plugin.program()
```

On my computer, reliably throws with current Sublime vanilla install **if** you have `diff.py` open. Otherwise, if not, 
Sublime never reloads the view and the program will just run and finish. 

