
from typing import Tuple, List

def sliceList(listArg: List, start: int = 0, end: int = None ) -> List:
  retList: List = []
  retList = listArg[start:] if end is None else listArg[start:end]
  return retList
