from PIL import Image
from numpy import asarray
import numpy as np
from heapq import nlargest
import sys

np.set_printoptions(suppress=True)

#In local format, e.g 'grid.png'
def getMaxPointsFromFiles(gridPath, partitionPath, patchesPath):

  #open using Pillow's image module

  #.convert('L') used to make monochrome
  
  gridPNG = Image.open(gridPath).convert('L')
  #.getchannel('B') used to isolate blue channel
  partitionPNGR = Image.open(partitionPath).getchannel('R')
  partitionPNGG = Image.open(partitionPath).getchannel('G')
  partitionPNGB = Image.open(partitionPath).getchannel('B')
  
  patchesPNG = Image.open(patchesPath)

  #parse into numpy arrays
  #array goes inner array is row, outer array is column
  grid = asarray(gridPNG)
  
  #using blue + green * 255 to determine patch ID
  partitionR = asarray(partitionPNGR)
  partitionG = asarray(partitionPNGG)
  partitionB = asarray(partitionPNGB)

  #getting partition labels
  partition = np.zeros(shape=(partitionR.shape))
  for i in range(len(partition)):
    for j in range(len(partition[0])):
      partition[i][j] = int((partitionR[i][j] << 16) + (partitionG[i][j] << 8) + partitionB[i][j])

  #list of all patches
  listOfPatches = []
  for x in partition:
    for y in x:
      if y not in listOfPatches:
        listOfPatches.append(y)

  partitionMax = {}

  #maximum point of patches
  for i in range(len(partition)):
    for j in range(len(partition[0])):
      xy = partition[i][j]
      if partitionMax.get(xy) is None:
        partitionMax[xy] = (None,None,0)
      else:
        height = 255-grid[i][j]
        if height > partitionMax[xy][2]:
          partitionMax[xy] = (j,i,height)

  #remove 0 patch
  partitionMax.pop(0)

  return partitionMax


def getTallestTree(maxPoints, N=1):
  maxTree = None
  for x in maxPoints.values():
    
    if maxTree == None:
      maxTree = x
    else:
      if maxTree[2] < x[2]:
        maxTree = x
  return maxTree

def treeData():
  treePartitions = getMaxPointsFromFiles('grid.png', 'partition.png', 'patches.png')
  tallestTree = getTallestTree(treePartitions)
  return tallestTree
#sys.modules[__name__] = tree_data
#maxPointsOfPatches = getMaxPointsFromFiles('grid.png', 'partition.png', 'patches.png')
#print(getTallestTree(maxPointsOfPatches))













