'''
Explore how infections change as a function of population size
'''

#%% Run

import covasim as cv
import pylab as pl
import sciris as sc

sims = sc.objdict()

popsizes = [10e3, 20e3, 30e3, 40e3, 50e3, 75e3, 100e3, 125e3, 150e3, 200e3, 300e3, 400e3, 500e3]

results = []
keys = []
for psize in popsizes:
    print(f'Running {psize}...')
    key = f'p{psize}'
    keys.append(key)
    sims[key] = cv.Sim(pop_size=psize,
                 n_days=60,
                 rand_seed=1,
                 pop_type = 'random',
                 verbose=0,
                 )
    sims[key].run()
    results.append(sims[key].results['cum_infections'].values)


#%% Ploting

pl.figure(dpi=200)
# pl.rcParams['font.size'] = 18

pl.subplot(1,2,1)
colors = sc.vectocolor(pl.log10(popsizes), cmap='parula')
for k,key in enumerate(keys):
    label = f'{int(float(key[1:]))/1000}k: {results[k][-1]:0.0f}'
    pl.plot(results[k], label=label, lw=3, color=colors[k])
    print(label)
pl.legend()
pl.title('Total number of infections')
pl.xlabel('Day')
pl.ylabel('Number of infections')

pl.subplot(1,2,2)
for k,key in enumerate(keys):
    label = f'{int(float(key[1:]))/1000}k: {results[k][-1]/popsizes[k]*100:0.1f}'
    pl.plot(results[k]/popsizes[k]*100, label=label, lw=3, color=colors[k])
    print(label)
pl.legend()
pl.title('Final prevalence')
pl.xlabel('Day')
pl.ylabel('Prevalence (%)')