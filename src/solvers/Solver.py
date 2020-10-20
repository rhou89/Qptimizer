import platform
import psutil
import pip

class Solver:
    def __init__(self):
        pass

    @staticmethod
    def packageInstall(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

    @staticmethod
    def getBitSize(bytes, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor
    
    @staticmethod
    def getSysInfo():
        try:
            import cpuinfo
        except ImportError:
            Solver.packageInstall('py-cpuinfo')
            print('Please run the program again!')
            exit()

        
        uname = platform.uname()
        svmem = psutil.virtual_memory()
        ci = cpuinfo.get_cpu_info()
        mem = Solver.getBitSize(svmem.total)

        print('='*40, 'Computer Info', '='*40)
        print(f'System: {uname.system} - {uname.node} - {uname.machine}')
        print('CPU model:', ci['brand_raw'])
        print('CPU details - Physical cores:', psutil.cpu_count(logical=False), '; Total cores:', psutil.cpu_count(logical=True))
        print(f"Total Memory: {mem}")

        return uname.system, uname.machine, ci['brand_raw'], mem