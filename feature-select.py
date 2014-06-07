# based off of
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#example-ensemble-plot-forest-importances-py
import numpy as np

from sklearn.ensemble import ExtraTreesClassifier

# Loads feature data from features file.
def load_data():
  data = []
  target = []
  with open('files/feats/test.lsvm', 'r') as f:
    for i, line in enumerate(f.readlines()):
      feats = []
      features = line.split(' ')
      for j, feature in enumerate(features):
        # Ignore features > 192
        if (len(feature.split(':')) == 2 and j < 192):
          feats.append(feature.split(':')[1])
      data.append(feats)
      if i <= 10: # BRK
          target.append(1)
      elif i <= 54: # BRM
          target.append(2)
      elif i <= 941: # GRW
          target.append(3)
      elif i <= 1014: # LRM
          target.append(4)
      elif i <= 1060: # LRR
          target.append(5)
      elif i <= 1063: # MCR
          target.append(6)
      elif i <= 1078: # ROR
          target.append(7)
      elif i <= 1105: # RRM
          target.append(8)
      elif i <= 1163: # RUM
          target.append(9)
      elif i <= 1290: # SQK
          target.append(10)
      elif i <= 1303: # SQL
          target.append(11)
      elif i <= 1348: # TMP
          target.append(12)

  return data, target

def main():
  X, y = load_data()
  # Build a forest and compute the feature importances
  forest = ExtraTreesClassifier(n_estimators=250, compute_importances=True,
                                random_state=0)
  
  forest.fit(X, y)
  importances = forest.feature_importances_
  std = np.std([tree.feature_importances_ for tree in forest.estimators_],
               axis=0)
  indices = np.argsort(importances)[::-1]
  # Print the feature ranking
  print("Feature ranking:")
  
  for f in range(len(indices)):
        print("%d. feature %d (%f)" % (f + 1, indices[f],
          importances[indices[f]]))

  # Plot the feature importances of the forest
  import pylab as pl
  pl.figure()
  pl.title("Feature importances")
  pl.bar(range(10), importances[indices],
       color="r", yerr=std[indices], align="center")
  pl.xticks(range(10), indices)
  pl.xlim([-1, 10])
  pl.show()


if  __name__ =='__main__':main()
