'''
Matthew Younatan
copyright MIT License

graph.py

Purpose: generate a clean looking graph
'''

from matplotlib import pyplot

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
x_ticks = ['10.png','20.png','30.png','40.png','50.png','60.png','70.png','80.png','90.png','100.png','110.png','120.png','130.png','140.png','150.png','160.png','170.png','180.png','190.png','200.png'];
y_initial=[1170,4592,10242,18419,28704,41473,56859,74162,94009,116311,140737,167571,196217,227998,261542,297745,336476,377143,420137,465380];
y_min=[563,2074,4362,7703,11787,16738,22646,29246,36685,44764,53531,62856,72996,84825,96657,109119,123172,137043,150987,166612];
y_time=[0.031914234,0.150597095,0.307177544,0.737029076,1.154910564,1.923849821,3.258280754,4.034207344,4.612653494,5.419495583,6.673145056,9.631232023,11.28978586,13.16078019,16.51081991,17.26978588,21.86349154,23.59785557,25.00907779,30.63602543];


fig, ax1 = pyplot.subplots()

pyplot.xticks(x, x_ticks,rotation='vertical')
pyplot.title('Toffolis Before / After Minimization')

# initial count y axis
line1,=ax1.plot(x, y_initial, '-', color='k', label='initial count', linewidth=2)
line2,=ax1.plot(x, y_min, '--', color='k', label='minimized count', linewidth=2)
ax1.set_ylabel('Toffoli Gate Count')

ax2 = ax1.twinx()
ax2.set_ylabel('TT-LITE Execution Time (s)')
line3,=ax2.plot(x, y_time, ':', color='k', label='time (s)', linewidth=1)

pyplot.legend(loc='upper left', handles=[line1,line2,line3])
fig.savefig("rgb_graph.png", bbox_inches='tight')