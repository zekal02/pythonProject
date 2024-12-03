'''

as 키워드 별명 사용하기 (alias)
'''

import converter as cvt
from converter import kilometer_to_miles as k_to_m
from converter import gram_to_pound as g_to_p
miles = cvt.kilometer_to_miles(150)
print(f'150km = {miles}miles')

miles2 = k_to_m(150)
print(f'150km = {miles}miles')

pound = cvt.gram_to_pound(1000)
print(f'1000g = {pound}pound')

pound2 = g_to_p(1000)
print(f'1000g = {pound}pound')

