from pathlib import Path
import runpy
runpy.run_path(str(Path.cwd()/'.qa-linux/bench/paired_benchmark.py'),run_name='__main__')
