from typing import List
from functools import reduce

sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic", "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic", "or had been"]

total = reduce(lambda a,b: a + b.count('was'), sentences, 0)
print(total)