#!/usr/bin/env python

#---Import
import sys
import string
import math


def GetSamplesToCombineDict(sampleListForMerging):
  dictSamples = {}
  for l,line in enumerate( open( sampleListForMerging ) ):
    # ignore comments
    if line.startswith('#'):
      continue
    line = string.strip(line,"\n")
    # ignore empty lines
    if len(line) <= 0:
      continue

    #print line
    # line looks like: "ZJet_Madgraph_Inc    DYJetsToLL_M-5to50 DYJetsToLL_M-50"
  
    # the rule is that the name of each 'piece' here must match the inputList name and filename 
    for i,piece in enumerate(line.split()):
      #print "i=", i , "  piece= " , piece
      if (i == 0):
        key = piece
        dictSamples[key] = []
      elif piece in dictSamples:
        dictSamples[key].extend(dictSamples[piece])
      else:
        dictSamples[key].append(piece)
  return dictSamples


def ParseXSectionFile(xsectionFile):
  xsectionDict = {}

  for line in open( xsectionFile ):

    # ignore comments
    if line.startswith('#'):
      continue
    line = string.strip(line,"\n")
    # ignore empty lines
    if len(line) <= 0:
      continue

    try:
      (dataset , xsection_val) = string.split(line)
    except ValueError:
      print 'ERROR: could not split line "',line,'"'
      exit(-1)
    #print dataset + " " + xsection_val

    #dataset_mod_1 = dataset[1:].replace('/','__')
    # this logic is copied from the submission script for the ntuples:
    #    https://github.com/CMSLQ/submitJobsWithCrabV2/blob/master/createAndSubmitJobsWithCrab3.py
    outputFileNames = []
    outputFileNames.append(dataset[1:dataset.find('_Tune')])
    outputFileNames.append(dataset[1:dataset.find('_13TeV')])
    outputFileNames.append(dataset.split('/')[1])
    # use the one with the shortest filename
    outputFile = sorted(outputFileNames, key=len)[0]
    if 'ext' in dataset:
       extN = dataset[dataset.find('_ext')+4]
       outputFile = outputFile+'_ext'+extN
    xsectionDict[outputFile] = xsection_val
  
  return xsectionDict


def lookupXSection(datasetNameFromInputList,xsectionDict):
  if len(xsectionDict) <= 0:
    print
    print 'ERROR: xsectionDict is empty. Cannot lookupXSection for',datasetNameFromInputList
    exit(-1)
  if datasetNameFromInputList.endswith('_reduced_skim'):
    datasetNameFromInputList = datasetNameFromInputList[0:datasetNameFromInputList.find('_reduced_skim')]
  try:
    return xsectionDict[datasetNameFromInputList]
  except KeyError:
    print
    for key,val in xsectionDict.iteritems():
      print 'sample=',key,'xsection=',val
    print 'ERROR: xsectionDict does not have an entry for',datasetNameFromInputList
    exit(-1)


#def lookupXSection(datasetFromAnalysis,xsectionFile):
#  dataset_forXsec = datasetFromAnalysis
#  if datasetFromAnalysis.endswith('_reduced_skim'):
#    dataset_forXsec = datasetFromAnalysis[0:datasetFromAnalysis.find('_reduced_skim')]
#
#  xsectionDataset = ''
#  xsectionVal = -999
#  for lin1 in open( xsectionFile ):
#
#    lin1 = string.strip(lin1,"\n")
#
#    (dataset , xsection_val) = string.split(lin1)
#    #print dataset + " " + xsection_val
#
#    dataset_mod_1 = dataset[1:].replace('/','__')
#    #print dataset_mod_1 + " " + xsection_val
#
#    # TODO: fix this hack!
#    if ( dataset_mod_1.startswith(dataset_forXsec+'_Tune') or
#         dataset_mod_1.startswith(dataset_forXsec+'_13TeV') or
#         #('Run20' in dataset_mod_1 and dataset_mod_1.startswith(dataset_forXsec)) or
#         ('Run20' in dataset_mod_1 and dataset[1:].replace('/','_').startswith(dataset_forXsec)) or
#         (dataset_forXsec=='DYJetsToLL_Mbin_M-50' and dataset_mod_1.startswith('DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8')) or
#         (dataset_forXsec=='TTJets_SingleLeptFromTbar_ext1' and dataset_mod_1.startswith('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8__RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2')) or
#         (dataset_forXsec=='TTJets_DiLept_ext1' and dataset_mod_1.startswith('TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8__RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1'))):
#      # TODO: fix this hack
#      # special handling of DYJetsToLL_M-50
#      # for madgraph; Mbin has _Mbin in it
#      if dataset_forXsec=='DYJetsToLL_M-50':
#        if not 'madgraph' in dataset:
#          continue
#      #elif dataset_forXsec=='DYJetsToLL_Mbin_M-50':
#      #  if not 'amcatnloFXFX' in dataset:
#      #    continue
#      #
#      if len(xsectionDataset) <= 0:
#        xsectionDataset = dataset
#        xsectionVal = xsection_val
#      elif xsectionVal != xsection_val:
#        print 'ERROR: Two datasets in xsection file start with',dataset_forXsec
#        print '1)',xsectionDataset,xsectionVal
#        print '2)',dataset,xsection_val
#        print 'Cannot figure out which is correct; exiting'
#        sys.exit()
#
#  xsection_val = xsectionVal
#  dataset = xsectionDataset
#  if xsection_val < -1: # -1 being the value for data
#    print "ERROR: xsection for dataset " + dataset_forXsec + " not found in " + xsectionFile
#    print "Expected a line in xsection file to start with "+dataset_forXsec+"_Tune but couldn't find one."
#    print "exiting..."
#    sys.exit()
#  return dataset,xsection_val
#
#

#def AddHisto(inputHistoName, outputHisto, inputRootFileName, currentWeight,
#             rebin=int(1), currentColor=int(1), currentFillStyle=int(1001), currentMarker=int(1)):

def UpdateTable(inputTable, outputTable):
    if not outputTable:
        for j,line in enumerate( inputTable ):
            outputTable[int(j)]={'variableName': inputTable[j]['variableName'],
                                 'min1': inputTable[j]['min1'],
                                 'max1': inputTable[j]['max1'],
                                 'min2': inputTable[j]['min2'],
                                 'max2': inputTable[j]['max2'],
                                 'N':       float(inputTable[j]['N']),
                                 'errN':    pow( float(inputTable[j]['errN']), 2 ),
                                 'Npass':       float(inputTable[j]['Npass']),
                                 'errNpass':    pow( float(inputTable[j]['errNpass']), 2 ),
                                 'EffRel':      float(0),
                                 'errEffRel':   float(0),
                                 'EffAbs':      float(0),
                                 'errEffAbs':   float(0),
                                 }
    else:
        for j,line in enumerate( inputTable ):
            outputTable[int(j)]={'variableName': inputTable[j]['variableName'],
                                 'min1': inputTable[j]['min1'],
                                 'max1': inputTable[j]['max1'],
                                 'min2': inputTable[j]['min2'],
                                 'max2': inputTable[j]['max2'],
                                 'N':       float(outputTable[int(j)]['N']) + float(inputTable[j]['N']),
                                 'errN':    float(outputTable[int(j)]['errN']) + pow( float(inputTable[j]['errN']), 2 ),
                                 'Npass':       float(outputTable[int(j)]['Npass']) + float(inputTable[j]['Npass']),
                                 'errNpass':    float(outputTable[int(j)]['errNpass']) + pow( float(inputTable[j]['errNpass']), 2 ),
                                 'EffRel':      float(0),
                                 'errEffRel':   float(0),
                                 'EffAbs':      float(0),
                                 'errEffAbs':   float(0),
                                 }
    return
            

def CalculateEfficiency(table):
    for j,line in enumerate( table ):
        if( j == 0):
            table[int(j)] = {'variableName':       table[int(j)]['variableName'],
                             'min1':        table[int(j)]['min1'],
                             'max1':        table[int(j)]['max1'],
                             'min2':        table[int(j)]['min2'],
                             'max2':        table[int(j)]['max2'],
                             'N':          float(table[j]['N']) ,
                             'errN':       int(0), 
                             'Npass':      float(table[j]['Npass']) ,
                             'errNpass':   int(0), 
                             'EffRel':     int(1),
                             'errEffRel':  int(0),
                             'EffAbs':     int(1),
                             'errEffAbs':  int(0),
                             }
        else:
            N = float(table[j]['N']) 
            errN = math.sqrt(float(table[j]["errN"]))
            if( float(N) > 0 ):
                errRelN = errN / N 
            else:
                errRelN = float(0)

            Npass = float(table[j]['Npass']) 
            errNpass = math.sqrt(float(table[j]["errNpass"]))
            if( float(Npass) > 0 ):
                errRelNpass = errNpass / Npass
            else:
                errRelNpass = float(0)

            if(Npass > 0  and N >0 ):
                EffRel = Npass / N
                errRelEffRel = math.sqrt( errRelNpass*errRelNpass + errRelN*errRelN )
                errEffRel = errRelEffRel * EffRel
            
                EffAbs = Npass / float(table[0]['N'])
                errEffAbs = errNpass / float(table[0]['N'])
            else:
                EffRel = 0
                errEffRel = 0
                EffAbs = 0
                errEffAbs = 0 
            
            table[int(j)]={'variableName': table[int(j)]['variableName'],
                           'min1': table[int(j)]['min1'],
                           'max1': table[int(j)]['max1'],
                           'min2': table[int(j)]['min2'],
                           'max2': table[int(j)]['max2'],
                           'N':       N,
                           'errN':    errN, 
                           'Npass':       Npass,
                           'errNpass':    errNpass, 
                           'EffRel':      EffRel,
                           'errEffRel':   errEffRel,
                           'EffAbs':      EffAbs,
                           'errEffAbs':   errEffAbs,
                           }
            #print table[j]
    return


#--- TODO: FIX TABLE FORMAT (NUMBER OF DECIMAL PLATES AFTER THE 0)

def WriteTable(table, name, file):
    print >>file, name
    print >>file, "variableName".rjust(25),
    print >>file, "min1".rjust(15),
    print >>file, "max1".rjust(15),
    print >>file, "min2".rjust(15),
    print >>file, "max2".rjust(15),
    print >>file, "Npass".rjust(17),
    print >>file, "errNpass".rjust(17),
    print >>file, "EffRel".rjust(15),
    print >>file, "errEffRel".rjust(15),
    print >>file, "EffAbs".rjust(15),
    print >>file, "errEffAbs".rjust(15)

    for j, line in enumerate(table):
        print >>file, table[j]['variableName'].rjust(25),
        print >>file, table[j]['min1'].rjust(15),
        print >>file, table[j]['max1'].rjust(15),
        print >>file, table[j]['min2'].rjust(15),
        print >>file, table[j]['max2'].rjust(15),
        ###
        if( table[j]['Npass'] >= 0.1 ):
            print >>file, ("%.04f" % table[j]['Npass']).rjust(17),
        else:
            print >>file, ("%.04e" % table[j]['Npass']).rjust(17),
        ### 
        if( table[j]['errNpass'] >= 0.1):    
            print >>file, ("%.04f" % table[j]['errNpass']).rjust(17),
        else:
            print >>file, ("%.04e" % table[j]['errNpass']).rjust(17),
        ### 
        if( table[j]['EffRel'] >= 0.1 ):
            print >>file, ("%.04f" % table[j]['EffRel']).rjust(15),
        else:
            print >>file, ("%.04e" % table[j]['EffRel']).rjust(15),
        ### 
        if( table[j]['errEffRel'] >= 0.1 ):
            print >>file, ("%.04f" % table[j]['errEffRel']).rjust(15),    
        else:
            print >>file, ("%.04e" % table[j]['errEffRel']).rjust(15),
        ### 
        if( table[j]['EffAbs'] >= 0.1 ):
            print >>file, ("%.04f" % table[j]['EffAbs']).rjust(15),
        else:
            print >>file, ("%.04e" % table[j]['EffAbs']).rjust(15),
        ### 
        if( table[j]['errEffAbs'] >= 0.1 ):
            print >>file, ("%.04f" % table[j]['errEffAbs']).rjust(15)
        else:
            print >>file, ("%.04e" % table[j]['errEffAbs']).rjust(15)         
        ###
            
    print >>file, "\n"

    #--- print to screen
    
    print "\n"
    print name
    print "variableName".rjust(25),
    print "min1".rjust(15),
    print "max1".rjust(15),
    print "min2".rjust(15),
    print "max2".rjust(15),
    print "Npass".rjust(17),
    print "errNpass".rjust(17),
    print "EffRel".rjust(15),
    print "errEffRel".rjust(15),
    print "EffAbs".rjust(15),
    print "errEffAbs".rjust(15)

    for j, line in enumerate(table):
        print table[j]['variableName'].rjust(25),
        print table[j]['min1'].rjust(15),
        print table[j]['max1'].rjust(15),
        print table[j]['min2'].rjust(15),
        print table[j]['max2'].rjust(15),
        ###
        if( table[j]['Npass'] >= 0.1 ):
            print ("%.04f" % table[j]['Npass']).rjust(17),
        else:
            print ("%.04e" % table[j]['Npass']).rjust(17),
        ### 
        if( table[j]['errNpass'] >= 0.1):    
            print ("%.04f" % table[j]['errNpass']).rjust(17),
        else:
            print ("%.04e" % table[j]['errNpass']).rjust(17),
        ### 
        if( table[j]['EffRel'] >= 0.1 ):
            print ("%.04f" % table[j]['EffRel']).rjust(15),
        else:
            print ("%.04e" % table[j]['EffRel']).rjust(15),
        ### 
        if( table[j]['errEffRel'] >= 0.1 ):
            print ("%.04f" % table[j]['errEffRel']).rjust(15),    
        else:
            print ("%.04e" % table[j]['errEffRel']).rjust(15),
        ### 
        if( table[j]['EffAbs'] >= 0.1 ):
            print ("%.04f" % table[j]['EffAbs']).rjust(15),
        else:
            print ("%.04e" % table[j]['EffAbs']).rjust(15),
        ### 
        if( table[j]['errEffAbs'] >= 0.1 ):
            print ("%.04f" % table[j]['errEffAbs']).rjust(15)
        else:
            print ("%.04e" % table[j]['errEffAbs']).rjust(15)         
        ###

    return


