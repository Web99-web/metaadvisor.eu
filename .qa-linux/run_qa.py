from pathlib import Path
import runpy
runpy.run_path(str(Path.cwd()/'.qa-linux/activation_qa.py'),run_name='__main__')
