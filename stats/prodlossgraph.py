#!/usr/bin/python
"""prodlossgraph - graph of production & losses

Requires matplotlib, see http://matplotlib.org or search your package
manager (Debian: apt-get install python-matplotlib)
"""

import sys
import hhist, hdata, prodloss
import matplotlib.pyplot as plt
import datetime

def todt(date):
	return datetime.date(date.year, date.month, date.day)

if __name__ == '__main__':
	entries = hhist.import_from_save(sys.stdin)
	data = prodloss.extract_prodloss(entries)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	cols = 'gyrcmgybrgc'
	dates = [todt(key).toordinal() for key in sorted(data)]
	total = [[sum(d[0] for d in data[key]), sum(d[1] for d in data[key])] for key in sorted(data)]
	gt = plt.plot_date(dates, total, fmt='k+-', tz=None, xdate=True, ydate=False, label='total', zorder=2)
	for bi,b in enumerate(hdata.Bombers.data):
		bprod = [data[key][bi][0] for key in sorted(data)]
		bloss = [data[key][bi][1] for key in sorted(data)]
		gp = plt.plot_date(dates, bprod, fmt='o-'+cols[bi], tz=None, xdate=True, ydate=False, label=b['name'])
		gl = plt.plot_date(dates, bloss, fmt='o-'+cols[bi], tz=None, xdate=True, ydate=False, label=None)
	plt.axhline(y=0, xmin=0, xmax=1, c='k', zorder=-1)
	plt.legend()
	plt.show()
