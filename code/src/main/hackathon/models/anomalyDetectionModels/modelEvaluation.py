from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_score, silhouette_samples

def plot_clustering(df,labels,title):
  fig = plt.figure(figsize=(8,6))
  ax = fig.add_subplot(111, projection='3d')
  unique_labels = np.unique(labels)
  for label in unique_labels:
    cluster_data = df[labels == label]
    ax.scatter(cluster_data.iloc[:,0],cluster_data.iloc[:,1],cluster_data.iloc[:,2],label=label)
  ax.set_title(title)
  ax.set_xlabel('PC1')
  ax.set_ylabel('PC2')
  ax.set_zlabel('PC3')
  ax.legend()
  plt.show()

def calculate_silhouette_scores(df,labels):
  unique_labels = np.unique(labels)
  avg_silhouette_scores = {}
  if len(unique_labels)>1:
    silhouette_scores = silhouette_samples(df,labels)
    cluster_silhouette_scores={}
    for label in unique_labels:
      cluster_indices = np.where(labels == label)[0]
      cluster_silhouette_scores[label] = silhouette_scores[cluster_indices]
    for label,score in cluster_silhouette_scores.items():
      avg_score = score.mean()
    #   print(f"Cluster {label}: Average Silhouette Score = {avg_score:.2f}")
      avg_silhouette_scores[label] = avg_score
    #   print(score)
    #   print()

    # print("the average silhouette score is",silhouette_score(df,labels))
    return avg_silhouette_scores
  else:
    # print("No clusters found")
    return None