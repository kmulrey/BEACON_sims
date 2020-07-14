import numpy as np
from random import random
from random import randint


proton_dir='/vol/astro3/lofar/sim/kmulrey/beacon/BEACON_sims/jobs_proton/'
iron_dir='/vol/astro3/lofar/sim/kmulrey/beacon/BEACON_sims/jobs_iron/'

base_dir='/vol/astro7/lofar/kmulrey/sim/beacon/'

def write_file(event, azimuth, zenith, energy, seed, type):


    
    part_id=''
    if type=='proton':
        part_id='14'
        outfile=open(proton_dir+event+'_coreas_'+type+'.q','w')

    if type=='iron':
        part_id='5626'
        outfile=open(iron_dir+event+'_coreas_'+type+'.q','w')





    outfile.write('#! /bin/bash\n')
    outfile.write('#SBATCH --time=4-00:00:00\n')
    #outfile.write('#SBATCH --output {0}/run/output/{1}_coreas_{2}-%j\n'.format(base_dir,event,part_id))
    #outfile.write('#SBATCH --error {0}/run/output/{1}_coreas_{2}-ERROR-%j\n'.format(base_dir,event,part_id))

    outfile.write('umask 002\n')
    outfile.write('export FLUPRO=/vol/optcoma/cr-simulations/fluka64\n')

    outfile.write('use geant\n')
    outfile.write('export RUNNR=`printf "%06d" $SLURM_ARRAY_TASK_ID`\n')
    outfile.write('cd {0}/events/\n'.format(base_dir))

    outfile.write('mkdir -p {0}/events/{1}/corsika/{2}/steering/\n'.format(base_dir,event,type))
    outfile.write('rm -rf /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('mkdir -p /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('python /vol/astro3/lofar/sim/kmulrey/beacon/BEACON_sims/geninp.py -r $RUNNR -s {0} -u {1} -a {2} -z {3} -t {5} -d /scratch/kmulrey/{4}/{5}/$RUNNR/ > /scratch/kmulrey/{4}/{5}/$RUNNR/RUN$RUNNR.inp\n'.format(seed,energy,azimuth,zenith,event,part_id))

    outfile.write('cd /vol/optcoma/cr-simulations/corsika_production/run/\n')
    outfile.write('./corsika77100Linux_QGSII_fluka_thin_conex < //scratch/kmulrey/{0}/{1}/$RUNNR/RUN$RUNNR.inp\n'.format(event,part_id))
    outfile.write('cd /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('mv RUN$RUNNR.inp {0}/events/{1}/corsika/{2}/steering/RUN$RUNNR.inp\n'.format(base_dir,event,type))
    outfile.write('mv *.long {0}events/{1}/corsika/{2}/\n'.format(base_dir,event,type))
    outfile.write('export LOFARSOFT=/vol/optcoma/pycrtools\n')
    outfile.write('G4WORKDIR=$LOFARSOFT/LORA_simulation\n')
    outfile.write('. /vol/optcoma/geant4_9.6_install/share/Geant4-9.6.4/geant4make/geant4make.sh\n')
    outfile.write('/vol/optcoma/pycrtools/LORA_simulation/DAT2txt DAT$RUNNR DAT$RUNNR.tmp\n')
    outfile.write('/vol/optcoma/pycrtools/LORA_simulation/LORA_simulation DAT$RUNNR.tmp DAT$RUNNR.lora\n')
    outfile.write('rm DAT$RUNNR.tmp\n')
    
    outfile.write('cp -r * {0}events/{1}/corsika/{2}/\n'.format(base_dir,event,type))
    outfile.write('rm -rf /scratch/kmulrey/{0}/{1}/$RUNNR/*\n'.format(event,part_id))

    outfile.close()



event=[]
azimuth=[57.8777037378,5.62278563,24.5338416226,85.323975652,-45.2948503091,-11.61947731,25.876497776,-170.239430922,130.84941074,14.554336601,-32.732258602]
zenith=[28.7984121752,36.3926767814,17.6159726846,28.5091835026,38.2803974379,35.5384552615,14.4052883375,40.6923782667,20.8766959694,39.5359400205,47.2151295936]
energy=[159421449.975,656804646.049,470693726.644,102292495.459,325078049.841,151927036.517,127390466.343,319912958.115,101648514.077,273404353.855,201546777.962]
seed=[43356,6726,53394,72474,38098,15078,60740,25706,51352,37712,91526]


for i in np.arange(100):
    value = randint(0, 10)
    print value
    #write_file(str(int(event[i])),azimuth[i], zenith[i], energy[i], seed[i],'proton')
    #write_file(str(int(event[i])),azimuth[i], zenith[i], energy[i], seed[i],'iron')

