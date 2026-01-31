class ScannerError(Exception):
    pass

class InvalidIPError(ScannerError):
    pass
class InvalidPortError(ScannerError):
    pass
class ScanConfigurationError(ScannerError):
    pass