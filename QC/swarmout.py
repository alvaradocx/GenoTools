import subprocess

command = 'cat swarm_26880828_0.e; cat swarm_26880577_0.e; cat swarm_26880520_0.e; cat swarm_26837423_0.e; cat swarm_26835217_0.e; cat swarm_26584592_0.e; cat swarm_26834905_0.e; cat swarm_26833118_0.e; cat swarm_26832607_0.e; cat swarm_26832011_0.e; cat swarm_26831746_0.e; cat swarm_26831710_0.e; cat swarm_26831297_0.e; cat swarm_26826645_0.e; cat swarm_26826458_0.e; cat swarm_26825970_0.e; cat swarm_26825458_0.e; cat swarm_26825179_0.e; cat swarm_26824189_0.e; cat swarm_26823275_0.e; cat swarm_26822632_0.e; cat swarm_26821972_0.e; cat swarm_26820935_0.e; cat swarm_26555745_0.e; cat swarm_26500656_0.e; cat swarm_26500639_0.e; cat swarm_26500620_0.e; cat swarm_26500553_0.e; cat swarm_26500357_0.e; cat swarm_26317866_0.e; cat swarm_26317852_0.e; cat swarm_26317517_0.e; cat swarm_26317457_0.e; cat swarm_26317355_0.e; cat swarm_26317255_0.e; cat swarm_26317220_0.e; cat swarm_26261002_0.e'

p = subprocess.run(command, shell=True, stdout=subprocess.PIPE )

#print( 'stdout:', p.stdout.decode() )

with open('swamrout_1117.txt', 'wb') as f:
    f.write(p.stdout)