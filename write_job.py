import numpy as np
from random import random
from random import randint


proton_dir='/user/kmulrey/beacon/BEACON_sims/jobs_proton/'
iron_dir='/user/kmulrey/beacon/BEACON_sims/BEACON_sims/jobs_iron/'

base_dir='/user/kmulrey/beacon/BEACON_sims/'

def write_file(event, azimuth, zenith, energy, seed, type):


    
    part_id=''
    if type=='proton':
        part_id='14'
        outfile=open(proton_dir+event+'_corsika_'+type+'.q','w')

    if type=='iron':
        part_id='5626'
        outfile=open(iron_dir+event+'_corsika_'+type+'.q','w')





    outfile.write('#! /bin/bash\n')
    #outfile.write('#SBATCH --time=2-00:00:00\n')
    #outfile.write('#SBATCH --output {0}/run/output/{1}_coreas_{2}-%j\n'.format(base_dir,event,part_id))
    #outfile.write('#SBATCH --error {0}/run/output/{1}_coreas_{2}-ERROR-%j\n'.format(base_dir,event,part_id))

    #outfile.write('umask 002\n')
    #outfile.write('export FLUPRO=/vol/optcoma/cr-simulations/fluka64\n')

    #outfile.write('use geant\n')
    outfile.write('export RUNNR=`printf "%06d" $PBS_ARRAYID`\n')
    outfile.write('cd {0}/events/\n'.format(base_dir))

    outfile.write('mkdir -p {0}/events/{1}/corsika/{2}/steering/\n'.format(base_dir,event,type))
    outfile.write('rm -rf /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('mkdir -p /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('python /user/kmulrey/beacon/BEACON_sims/geninp.py -r $RUNNR -s {0} -u {1} -a {2} -z {3} -t {5} -d /scratch/kmulrey/{4}/{5}/$RUNNR/ > /scratch/kmulrey/{4}/{5}/$RUNNR/RUN$RUNNR.inp\n'.format(seed,energy,azimuth,zenith,event,part_id))

    outfile.write('cd /user/kmulrey/software/corsika-77100/run/\n')
    outfile.write('./corsika77100Linux_QGSII_urqmd_thin_conex < //scratch/kmulrey/{0}/{1}/$RUNNR/RUN$RUNNR.inp\n'.format(event,part_id))
    outfile.write('cd /scratch/kmulrey/{0}/{1}/$RUNNR\n'.format(event,part_id))
    outfile.write('mv RUN$RUNNR.inp {0}/events/{1}/corsika/{2}/steering/RUN$RUNNR.inp\n'.format(base_dir,event,type))
    outfile.write('mv *.long {0}events/{1}/corsika/{2}/\n'.format(base_dir,event,type))
    #outfile.write('export LOFARSOFT=/vol/optcoma/pycrtools\n')
    #outfile.write('G4WORKDIR=$LOFARSOFT/LORA_simulation\n')
    outfile.write('source /software/geant4/geant4.9.6-install/bin/geant4.sh\n')
    outfile.write('/software/geant4/LORA_simulation/DAT2txt DAT$RUNNR DAT$RUNNR.tmp\n')
    outfile.write('/software/geant4/LORA_simulation DAT$RUNNR.tmp DAT$RUNNR.lora\n')
    outfile.write('rm DAT$RUNNR.tmp\n')
    
    outfile.write('cp -r * {0}events/{1}/corsika/{2}/\n'.format(base_dir,event,type))
    outfile.write('rm -rf /scratch/kmulrey/{0}/{1}/$RUNNR/*\n'.format(event,part_id))

    outfile.close()

#1e16.5, 1e17.0, 1e17.5
#60,65,70,75


zenith=[60,65,70,75]
energy=[31622776,100000000,316227766]


seed = randint(0, 10000)
    
write_file('10000',0, zenith[0], energy[0], seed+1,'proton')
write_file('10000',0, zenith[0], energy[0], seed+2,'iron')

write_file('10001',0, zenith[1], energy[0], seed+3,'proton')
write_file('10001',0, zenith[1], energy[0], seed+4,'iron')
    
write_file('10002',0, zenith[2], energy[0], seed+5,'proton')
write_file('10002',0, zenith[2], energy[0], seed+6,'iron')

write_file('10003',0, zenith[3], energy[0], seed+7,'proton')
write_file('10003',0, zenith[3], energy[0], seed+8,'iron')

################################################################

write_file('20000',0, zenith[0], energy[1], seed+9,'proton')
write_file('20000',0, zenith[0], energy[1], seed+10,'iron')

write_file('20001',0, zenith[1], energy[1], seed+11,'proton')
write_file('20001',0, zenith[1], energy[1], seed+12,'iron')
    
write_file('20002',0, zenith[2], energy[1], seed+13,'proton')
write_file('20002',0, zenith[2], energy[1], seed+14,'iron')

write_file('20003',0, zenith[3], energy[1], seed+15,'proton')
write_file('20003',0, zenith[3], energy[1], seed+16,'iron')

################################################################


write_file('30000',0, zenith[0], energy[2], seed+17,'proton')
write_file('30000',0, zenith[0], energy[2], seed+18,'iron')

write_file('30001',0, zenith[1], energy[2], seed+19,'proton')
write_file('30001',0, zenith[1], energy[2], seed+20,'iron')
    
write_file('30002',0, zenith[2], energy[2], seed+21,'proton')
write_file('30002',0, zenith[2], energy[2], seed+22,'iron')

write_file('30003',0, zenith[3], energy[2], seed+23,'proton')
write_file('30003',0, zenith[3], energy[2], seed+24,'iron')

