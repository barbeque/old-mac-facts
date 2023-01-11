# ICN# Generator
Builds an ICN# resource out of a 32x32 black and white PNG. Guesses the mask.

Pull requests very welcome.

## How to Use
Invoke the following commands:
```
% virtualenv env
% source env/bin/activate
% pip install -r requirements.txt
% python ./icn-generator.py iconfile.png
```

Copy and paste the resulting text/hex data into ResEdit's "as text" view for ICNs.

# Options
 * `-c`: Generate C header file format instead of raw hex bytes
 * `-b`: Fill mask with all black ($FF)
