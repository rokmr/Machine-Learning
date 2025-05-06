# METRICS

## Content
1. [Basics](#basics)
2. [Accuracy](#accuracy)
3. [Precision](#precision)
4. [Recall](#recall)
5. [PR-Curve](#pr-curve)
6. [F1-Score](#f1-score)
7. [ROC](#receiver-operating-characteristic-roc)
8. [Pixel Accuracy](#pixel-accuracy)
9. [IoU](#intersection-over-union-iou)
10. [Dice Coefficient](#dice-coefficient)
11. [NMS](#non-maxium-supression-nms)

## Basics
- True Positives (TP): actual observation is 1 (True) and prediction is 1 (True) 
- True Negative (TN): actual observation is 0 (False) and prediction is 0 (False) 
- False Positive (FP): actual observation is 0 (False) and prediction is 1 (True) 
- False Negative (FN): actual observation is 1 (True) and prediction is 0 (False) 


## Accuracy
`Balanced`

## Precision 
`Balanced, Imbalanced`

Out of all the True `predictions` how many were actually True.

$Precision = \frac{TP}{TP+FP}$


## Recall
`Balanced, Imbalanced`

Out of all the True `observations` how many were actually True.
$Recall = \frac{TP}{TP+FN}$

<div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Precisionrecall.svg/700px-Precisionrecall.svg.png" height="400" >
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/PrecisionrecallDogExample.svg/800px-PrecisionrecallDogExample.svg.png" height="400">
  </div>
</div>

## PR Curve
<div align='center'>
    <img src="https://classeval.wordpress.com/wp-content/uploads/2015/06/precision-recall-balanced-imbalanced.png" height=200 width=450>
</div>

## F1-score 
`Balanced, Imbalanced`

Harmonic Mean of Precision(P) and Recall(R)

$F1-score = \frac{2*PR}{P+R}$

## Receiver Operating Characteristic (ROC)
The ROC is a probability curve and the area under 
the curve can be thought of as the degree of separability between the two classes. 

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Roc_curve.svg/1920px-Roc_curve.svg.png" height=200 >
</div>

## Pixel Accuracy
A metric that calculates the percentage of correctly classified pixels in an image.

$Pixel Accuracy = \frac{Number\ of\ Correctly\ Classified\ Pixels}{Total\ Number\ of\ Pixels}$

**Limitation**: Can be misleading for imbalanced datasets. For example, if an image has only 2 pixels of interest out of 100 pixels, predicting no objects would still result in 98% accuracy.

## Intersection over Union (IoU)
A more robust metric that measures the overlap between predicted and ground truth segments.

$IoU = \frac{Area\ of\ Overlap}{Area\ of\ Union} = \frac{Intersection}{Union}$

Where:
- Intersection = Area shared between prediction and ground truth
- Union = Total area covered by both prediction and ground truth


If two bbox ahve both Intersection and union high then the IoU will be high.
Assume two case :

1. Intersion is large but the bbox are also very large bbox this leads to very high union depicting same same object.
2. Intersion is large but the bbox are small bbox then possibly they are dipicting different object.

<div>
<img src='../assets/IoU.png' height=200 width=450>
</div>

## Dice Coefficient
Similar to IoU but less harsh on misclassifications. It has a monotonic relationship with IoU.

$Dice = \frac{2 \times Area\ of\ Overlap}{Sum\ of\ Areas} = \frac{2 \times Intersection}{Area\ of\ Prediction + Area\ of\ Ground\ Truth}$

**Relationship with IoU**:
$Dice = \frac{2 \times IoU}{1 + IoU}$


## Non-Maxium Supression (NMS)
We  don't need all the object proposals. We only want to keep the best one.

<div>
<img src='https://thepythoncode.com/media/articles/non-maximum-suppression-using-opencv-in-python/non-max-suppression.webp' height=200>
</div>

<div>
<img src='../assets/NMSAlgo.png'height=200>
</div>


### [&lambda;<sub>NMS</sub>](https://arxiv.org/pdf/1511.06437)
Do not allow the bbos if they are overlapping more than $\lambda_{NMS}$ threshold.
<div>
<img src='../assets/NMSIssue.png' height=200>
</div>

Narrrow Threshold (High IoU) : Low Precision (More False Positive)
Wide Threshold (Low IoU): Low Recall (More False Negative)

