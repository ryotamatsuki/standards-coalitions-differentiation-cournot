"""Audit-only shadow rechecker: never modifies source files or frozen theory."""
import sys,runpy
import sympy
from sympy.printing.pycode import PythonCodePrinter
from mpmath import iv
orig=sympy.lambdify
class IntervalRationalPrinter(PythonCodePrinter):
 def _print_Rational(self,expr): return f'RAT({expr.p}, {expr.q})'
def replacement(*args,**kw):
 if kw.get('modules')=='math':
  kw['printer']=IntervalRationalPrinter({'fully_qualified_modules':False,'allow_unknown_functions':True})
  out=orig(*args,**kw)
  out.__globals__['RAT']=lambda p,q:iv.mpf(p)/q
  return out
 return orig(*args,**kw)
sympy.lambdify=replacement
path=sys.argv[1]
source=open(path).read()
# Keep signed Gershgorin sums inside interval arithmetic until strict sign test.
source=source.replace('row=float(J[i][i].b)','row=J[i][i]')
source=source.replace('row+=max(abs(float(symmetric_offdiag.a)),\n                         abs(float(symmetric_offdiag.b)))','row+=abs(symmetric_offdiag)')
source=source.replace('row_bounds.append(row)','row_bounds.append(row.b)')
# float conversion only for output metric AFTER exact interval inequality.
source=source.replace('largest_upper=max(largest_upper,max(row_bounds))','largest_upper=max(largest_upper,float(max(row_bounds)))')
exec(compile(source,path,'exec'),{'__name__':'__main__','__file__':path})
