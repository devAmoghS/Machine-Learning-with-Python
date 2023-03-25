import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score
import matplotlib.pyplot as plt
import matplotlib.patches as ptch 

# Appendix A - working with single threshold
pred_scores = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3]
y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative", "positive"]

# To convert the scores into a class label, a threshold is used. 
# When the score is equal to or above the threshold, the sample is classified as one class. 
# Otherwise, it is classified as the other class. 
# Suppose a sample is Positive if its score is above or equal to the threshold. Otherwise, it is Negative. 
# The next block of code converts the scores into class labels with a threshold of 0.5.

threshold = 0.5

y_pred = ["positive" if score >= threshold else "negative" for score in pred_scores]
print(y_pred)

r = np.flip(confusion_matrix(y_true, y_pred))
print("\n# Confusion Matrix (From Left to Right & Top to Bottom: \nTrue Positive, False Negative, \nFalse Positive, True Negative)")
print(r)

# Remember that the higher the precision, the more confident the model is when it classifies a sample as Positive.
# Higher the recall, the more positive samples the model correctly classified as Positive.

precision = precision_score(y_true=y_true, y_pred=y_pred, pos_label="positive")
print("\n# Precision = 4/(4+1)")
print(precision)

recall = recall_score(y_true=y_true, y_pred=y_pred, pos_label="positive")
print("\n# Recall = 4/(4+2)")
print(recall)

# Appendix B - working with multiple thresholds
y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative", "positive", "positive", "positive", "positive", "negative", "negative", "negative"]

pred_scores = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3, 0.7, 0.5, 0.8, 0.2, 0.3, 0.35]

thresholds = np.arange(start=0.2, stop=0.7, step=0.05)

# Due to the importance of both precision and recall, there is a precision-recall curve that shows 
# the tradeoff between the precision and recall values for different thresholds. 
# This curve helps to select the best threshold to maximize both metrics

def precision_recall_curve(y_true, pred_scores, thresholds):
    precisions = []
    recalls = []
    f1_scores = []
    
    for threshold in thresholds:
        y_pred = ["positive" if score >= threshold else "negative" for score in pred_scores]

        precision = precision_score(y_true=y_true, y_pred=y_pred, pos_label="positive")
        recall = recall_score(y_true=y_true, y_pred=y_pred, pos_label="positive")
        f1_score = (2 * precision * recall) / (precision + recall)
        
        precisions.append(precision)
        recalls.append(recall)
        f1_scores.append(f1_score)

    return precisions, recalls, f1_scores

precisions, recalls, f1_scores = precision_recall_curve(y_true=y_true, 
                                             pred_scores=pred_scores,
                                             thresholds=thresholds)

print("\nRecall:: 	Precision 	:: F1-Score",)
for p, r, f in zip(precisions, recalls, f1_scores):
	print(round(r,4),"\t::\t",round(p,4),"\t::\t",round(f,4))

# np.max() returns the max. value in the array
# np.argmax() will return the index of the value found by np.max()

print('Best F1-Score: ', np.max(f1_scores))
idx_best_f1 = np.argmax(f1_scores)
print('\nBest threshold: ', thresholds[idx_best_f1])
print('Index of threshold: ', idx_best_f1)

# Can disable comment to display the plot

# plt.plot(recalls, precisions, linewidth=4, color="red")
# plt.scatter(recalls[idx_best_f1], precisions[idx_best_f1], zorder=1, linewidth=6)
# plt.xlabel("Recall", fontsize=12, fontweight='bold')
# plt.ylabel("Precision", fontsize=12, fontweight='bold')
# plt.title("Precision-Recall Curve", fontsize=15, fontweight="bold")
# plt.show()

# Appendix C - average precision (AP)
precisions, recalls, f1_scores = precision_recall_curve(y_true=y_true, 
                                             pred_scores=pred_scores, 
                                             thresholds=thresholds)

precisions.append(1)
recalls.append(0)

precisions = np.array(precisions)
recalls = np.array(recalls)

print('\nRecall ::',recalls)
print('Precision ::',precisions)

AP = np.sum((recalls[:-1] - recalls[1:]) * precisions[:-1])
print("\nAP --", AP)

# Appendix D - Intersection over Union

# gt_box -- 	ground-truth bounding box
# pred_box --	prediction bounding box 
def intersection_over_union(gt_box, pred_box):

    inter_box_top_left = [max(gt_box[0], pred_box[0]), max(gt_box[1], pred_box[1])]

    print("\ninter_box_top_left:", inter_box_top_left)
    print("gt_box:", gt_box)
    print("pred_box:", pred_box)
    inter_box_bottom_right = [min(gt_box[0]+gt_box[2], pred_box[0]+pred_box[2]), min(gt_box[1]+gt_box[3], pred_box[1]+pred_box[3])]
    print("inter_box_bottom_right:", inter_box_bottom_right)

    inter_box_w = inter_box_bottom_right[0] - inter_box_top_left[0]
    print("inter_box_w:", inter_box_w)
    inter_box_h = inter_box_bottom_right[1] - inter_box_top_left[1]
    print("inter_box_h:", inter_box_h)

    intersection = inter_box_w * inter_box_h
    union = gt_box[2] * gt_box[3] + pred_box[2] * pred_box[3] - intersection
    
    iou = intersection / union

    return iou, intersection, union

gt_box1 = [320, 220, 680, 900]
pred_box1 = [500, 320, 550, 700]

gt_box2 = [645, 130, 310, 320]
pred_box2 = [500, 60, 310, 320]

iou1 = intersection_over_union(gt_box1, pred_box1)
print("\nIOU1 ::", iou1)

iou2 = intersection_over_union(gt_box2, pred_box2)
print("\nIOU2 ::", iou2)