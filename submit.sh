#! /bin/bash


cd /user/kmulrey/beacon/BEACON_sims/jobs_proton

qsub -t 1-15 10000_coreas_proton.q
qsub -t 1-15 10001_coreas_proton.q
qsub -t 1-15 10002_coreas_proton.q
qsub -t 1-15 10003_coreas_proton.q

qsub -t 1-15 20000_coreas_proton.q
qsub -t 1-15 20001_coreas_proton.q
qsub -t 1-15 20002_coreas_proton.q
qsub -t 1-15 20003_coreas_proton.q

qsub -t 1-15 30000_coreas_proton.q
qsub -t 1-15 30001_coreas_proton.q
qsub -t 1-15 30002_coreas_proton.q
qsub -t 1-15 30003_coreas_proton.q

cd /user/kmulrey/beacon/BEACON_sims/jobs_iron

qsub -t 1-15 10000_coreas_iron.q
qsub -t 1-15 10001_coreas_iron.q
qsub -t 1-15 10002_coreas_iron.q
qsub -t 1-15 10003_coreas_iron.q

qsub -t 1-15 20000_coreas_iron.q
qsub -t 1-15 20001_coreas_iron.q
qsub -t 1-15 20002_coreas_iron.q
qsub -t 1-15 20003_coreas_iron.q

qsub -t 1-15 30000_coreas_iron.q
qsub -t 1-15 30001_coreas_iron.q
qsub -t 1-15 30002_coreas_iron.q
qsub -t 1-15 30003_coreas_iron.q

