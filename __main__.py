# coding: utf-8

from kwl import text_to_kwl, kwl_to_text
import sys

if __name__ == '__main__':
   args_len = len(sys.argv)
   if args_len == 3:
     print kwl_to_text(sys.argv[1], sys.argv[2])
   elif args_len == 2:
     print text_to_kwl(sys.argv[1])
   else:
     print """Usage:
     python kwl.py <kwl2text> <language>
     python kwl.py <text2kwl>
     """
