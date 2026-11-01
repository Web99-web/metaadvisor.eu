from pathlib import Path
import runpy
runpy.run_path(str(Path.cwd()/'.qa-linux/bench/benchmark_adapter.py'),run_name='__main__')
