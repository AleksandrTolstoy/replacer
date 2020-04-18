# Replacer
CLI program to replace text in files.  

With its help, you can do something similar to this.  
It is useful to use if you need to replace some template text in large files.  

# How to run?
1)clone or download this repository  
2)run from the terminal as ```./replacer.py```  

# Examples of using
```python3 replacer.py -o <old text> -n <new text> --file <file path>```  
```python3 replacer.py -o <starting point> -n <end point> --file <file path> --insertion <insert value>```  

# Аlso you can use
MacOS : ```sed -i '' 's/old-text/new-text/g' test_data1.txt```  
Linux : ```sed -i 's/old-text/new-text/g' test_data1.txt```  
