#! /bin/bash


cd /user/kmulrey/beacon/BEACON_sims/jobs_proton

qsub -t 1-15 10000_corsika_proton.q
qsub -t 1-15 10001_corsika_proton.q
qsub -t 1-15 10002_corsika_proton.q
qsub -t 1-15 10003_corsika_proton.q

qsub -t 1-15 20000_corsika_proton.q
qsub -t 1-15 20001_corsika_proton.q
qsub -t 1-15 20002_corsika_proton.q
qsub -t 1-15 20003_corsika_proton.q

qsub -t 1-15 30000_corsika_proton.q
qsub -t 1-15 30001_corsika_proton.q
qsub -t 1-15 30002_corsika_proton.q
qsub -t 1-15 30003_corsika_proton.q

cd /user/kmulrey/beacon/BEACON_sims/jobs_iron

qsub -t 1-15 10000_corsika_iron.q
qsub -t 1-15 10001_corsika_iron.q
qsub -t 1-15 10002_corsika_iron.q
qsub -t 1-15 10003_corsika_iron.q

qsub -t 1-15 20000_corsika_iron.q
qsub -t 1-15 20001_corsika_iron.q
qsub -t 1-15 20002_corsika_iron.q
qsub -t 1-15 20003_corsika_iron.q

qsub -t 1-15 30000_corsika_iron.q
qsub -t 1-15 30001_corsika_iron.q
qsub -t 1-15 30002_corsika_iron.q
qsub -t 1-15 30003_corsika_iron.q

