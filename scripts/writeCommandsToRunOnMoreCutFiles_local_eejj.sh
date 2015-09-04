#!/bin/bash

# Please run this script from the rootNtupleAnalyzerV2 directory by:  
# ./scripts/writeCommandsToRunOnMoreCutFiles.sh

# This scripts creates the whole sets of commands needed to run the analysis on multiple cut files.
# The commands will be written in a text file commandsToRunOnMoreCutFiles.txt in the current directory, 
# to be used by doing cut&paste to a terminal.

# Cut Files should first be created by a script ../rootNtupleMacrosV2/config/eejj/make_eejj_cutFiles.py
# This script will then use those cut files to create the commands needed to run on them.

#### INPUTS HERE ####
#------------
files=`ls $LQMACRO/config2012/Analysis/cutTable_lq_eejj.txt`
#files=`ls $LQMACRO/config2012/Analysis/cutTable_lq_eejj_StopChangeOptimization_LQ2cuts.txt`
#files=`ls $LQMACRO/config2012/Analysis/cutTable_lq_eejj_StopChangeOptimization.txt`
#files=`ls $LQMACRO/config2012/Systematics/cutTable_lq_eejj_Systematics_PUup_StopChangeOptimization.txt`
#files=`ls $LQMACRO/config2012/Systematics/cutTable_lq_eejj_Systematics_PUdown.txt`
#files=`ls $LQMACRO/config2012/MakeFlatNtupleSkims/cutTable_lq_eejjPreselection_skim.txt`
#files=`ls $LQMACRO/config2012/Analysis/cutTable_lq_eejj.txt`
#files=`ls $LQMACRO/config2012/Analysis/cutTable_lq_eejj_noEEMassCut.txt`
#files=`ls $LQMACRO/config2012/MakeFlatNtupleSkims/cutTable_lq_eejjPreselection_skim.txt`
#------------
OUTDIRPATH=$LQDATA  # a subdir will be created for each cut file 
#SUBDIR=eejj_analysis_stopEBBQ_newCwrElectronScaleRes/
#SUBDIR=eejj_analysis_stopEBBQ_newCwrElectronScaleRes_EER/
#SUBDIR=eejj_analysis_stopEBBQ_newCwrElectronScaleRes_EESup/
#SUBDIR=eejj_analysis_stopEBBQ_newCwrElectronScaleRes_EESdown/
SUBDIR=eejj_analysis_lqvector_newCwrElectronScaleRes_EESdown/
#SUBDIR=eejj_analysis_lqvector_newCwrElectronScaleRes_EESup/
#SUBDIR=eejj_analysis_lqvector_newCwrElectronScaleRes_EER/
#SUBDIR=eejj_analysis_lqvector_newCwrElectronScaleRes/
#SUBDIR=eejj_analysis_newCwrElectronScaleRes_EER/
#SUBDIR=eejj_analysis_newCwrElectronScaleRes_EESdown/
#SUBDIR=eejj_analysis_newCwrElectronScaleRes_EESup/
#SUBDIR=eejj_analysis_newCwrElectronScaleRes/
#SUBDIR=StopToEBBQ_analysis_LQ2cuts/
#SUBDIR="lq_skim_2014/RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_LegacyNTupleVersion"
#SUBDIR=EGammaMediumID_eejj_analysis/
#SUBDIR=lq_microSkims/DY2JetsToLL_ScaleSysts/
#SUBDIR=lq_microSkims/DY3JetsToLL_ScaleSysts/
#SUBDIR=eejj_analysis/DY2JetsToLL_ScaleSysts/
#SUBDIR=eejj_analysis/DY3JetsToLL_ScaleSysts/
#SUBDIR=eejj_analysis/TTBar_Systs/
#SUBDIR=eejj_analysis/DY4JetsToLL_ScaleMatchingSysts/
#SUBDIR=eejj_analysis/CombinedDY4JetsToLL_MGSysts/
#SUBDIR=eejj_analysis/NoEEMassCut_CombinedDY4JetsToLL_MGSysts/
         # output sub-directory (i.e. output will be in OUTDIRPATH/SUBDIR)
         # it is suggested to specify the luminosity in the name of the directory
#------------
ILUM=19600 # integrated luminosity in pb-1 to be used for rescaling/merging MC samples
FACTOR=1000 # numbers in final tables (but *not* in plots) will be multiplied by this scale factor (to see well the decimal digits)
#------------
CODENAME=analysisClass_lq_eejj #the actual name of the code used to process the ntuples (without the suffix ".C") 
#------------
INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EESdown/inputListBetaOneYM500only.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EESup/inputListBetaOneYM500only.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EER/inputListBetaOneYM500only.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector/inputListBetaOneYM500only.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_EER/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_EESup/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_EESdown/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EESdown/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EESup/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector_EER/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQVector/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_SignalsAndBackgrounds/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_SignalsAndBackgrounds_EESdown/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_SignalsAndBackgrounds_EESup/inputListAllCurrent.txt
#INPUTLIST=config/ReducedSkimDataSets_RootNtuple-V00-03-18-Summer12MC_SignalsAndBackgrounds_EER/inputListAllCurrent.txt
#INPUTLIST=config/PreselectionSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_LegacyNTupleVersion_eejj_EER/inputListAllCurrent.txt
#INPUTLIST=config/PreselectionSkimDataSets_RootNtuple-V00-03-18-Summer12MC_StopToEBBQ_LegacyNTupleVersion_eejj/inputListAllCurrent.txt
#INPUTLIST=config/PreselectionSkimDataSets_RootNtuple-V00-03-18-EGammaMediumIDLegacyNTupleVersion_eejj/inputListAllCurrent.txt
#INPUTLIST=config/PreselectionSkimDataSets_RootNtuple-V00-03-18-Summer12MC_LQ_Vector_LegacyNTupleVersion_eejj/inputListAllCurrent.txt
#INPUTLIST=config/FlatNtuple_EEJJ_Preselection/inputListAllCurrent.txt
#INPUTLIST=config/MiniSkimDatasets_Summer12MC_DY2JetsToLL_ScaleSysts_MG/inputListAllCurrent.txt
#INPUTLIST=config/MiniSkimDatasets_Summer12MC_DY3JetsToLL_ScaleSysts_MG/inputListAllCurrent.txt
#INPUTLIST=config/MiniSkimDatasets_Summer12MC_TTBar_Systs_MG/inputListAllCurrent.txt
#INPUTLIST=config/MiniSkimDatasets_Summer12MC_DY4JetsToLL_ScaleMatchingSysts_MG/inputListAllCurrent.txt
#INPUTLIST=config/MicroSkimDatasets_Summer12MC_DYJetsToLL_ScaleMatchingSysts_MG/inputListAllCurrent.txt
#------------
XSECTION=config/xsection_8TeV_2012.txt #specify cross section file
#------------
#SAMPLELISTFORMERGING=config/sampleListForMerging_8TeV_eejj.txt
SAMPLELISTFORMERGING=config/sampleListForMerging_8TeV_eejj_LQVector.txt ### CHANGE TO USE VECTOR LQ
#SAMPLELISTFORMERGING=config/sampleListForMerging_8TeV_eejj_rpvStop.txt ### CHANGE TO USE RPV STOP
#------------
NCORES=8 #Number of processor cores to be used to run the job
#NCORES=16 #Number of processor cores to be used to run the job
#------------

#### END OF INPUTS ####

#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwr_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESdown_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEER_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwr_lqvector_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEER_lqvector_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESup_lqvector_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESdown_lqvector_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESdown_stopEBBQ_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESup_stopEBBQ_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEER_stopEBBQ_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwr_stopEBBQ_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwr_lqvector_YM500BetaOneOnly_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEER_lqvector_YM500BetaOneOnly_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
#COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESup_lqvector_YM500BetaOneOnly_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
COMMANDFILE=commandsToRunOnMoreCutFiles_newCwrEESdown_lqvector_YM500BetaOneOnly_eejj_local_`hostname -s |perl -pi -e 's|lxplus[0-9]*|lxplus|'`.txt
echo "" > $COMMANDFILE

for file in $files
do
suffix=`basename $file`
suffix=${suffix%\.*}
cat >> $COMMANDFILE <<EOF

####################################################
#### launch, check and combine cmds for $suffix ####

time python scripts/launchAnalysis.py \
    -i $INPUTLIST \
    -n rootTupleTree/tree \
    -c $file \
    -o $OUTDIRPATH/$SUBDIR/output_$suffix  \
    -p $NCORES \
    >& launch_${suffix}.log

mv launch_${suffix}.log $OUTDIRPATH/$SUBDIR/output_$suffix/

time  ./scripts/combineTablesTemplate.py \
    -i $INPUTLIST \
    -c $CODENAME \
    -d $OUTDIRPATH/$SUBDIR/output_$suffix \
    -l  `echo "$ILUM*$FACTOR" | bc` \
    -x $XSECTION  \
    -o $OUTDIRPATH/$SUBDIR/output_$suffix \
    -s $SAMPLELISTFORMERGING \
    | tee $OUTDIRPATH/$SUBDIR/output_$suffix/combineTables_${suffix}.log

time  ./scripts/combinePlotsTemplate.py \
    -i $INPUTLIST \
    -c $CODENAME \
    -d $OUTDIRPATH/$SUBDIR/output_$suffix \
    -l ${ILUM} \
    -x $XSECTION  \
    -o $OUTDIRPATH/$SUBDIR/output_$suffix \
    -s $SAMPLELISTFORMERGING \
    | tee $OUTDIRPATH/$SUBDIR/output_$suffix/combinePlots_${suffix}.log

EOF
done


echo "The set of commands to run on the cut files:" 
for file in $files
do
echo "  " $file
done 
echo "has been written to $COMMANDFILE"
