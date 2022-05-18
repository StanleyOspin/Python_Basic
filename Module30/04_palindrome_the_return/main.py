from collections import Counter

if __name__ == '__main__':
   def can_be_poly(string: str) -> bool:
        return len(list(filter(lambda x: x % 2 != 0, Counter(string).values()))) < 2

   print(can_be_poly('abcba'))
   print(can_be_poly('abbbc'))
