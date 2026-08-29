from calculates_results_stats import calculates_results_stats

rd1 = {'a.jpg':['maltese','maltese',1,1,1], 'b.jpg':['tabby','tabby',1,0,0]}
print('rd1 ->', calculates_results_stats(rd1))
rd2 = {'a.jpg':['maltese','maltese',1,1,1], 'b.jpg':['golden','golden retriever',0,1,1]}
print('rd2 ->', calculates_results_stats(rd2))
rd3 = {'a.jpg':['cat','cat',1,0,0], 'b.jpg':['tabby','tabby',1,0,0]}
print('rd3 ->', calculates_results_stats(rd3))
