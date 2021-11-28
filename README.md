# COMP 551 (Winter 2021)

**Instructor:** Reihaneh Rabbany

**Group:** Emily Tam, Alvin Chen, Ziqi Li

This course covers a selected set of topics in machine learning and data mining, with an emphasis on good methods and practices for deployment of real systems. The majority of sections are related to commonly used supervised learning techniques, and to a lesser degree unsupervised methods. This includes fundamentals of algorithms on linear and logistic regression, decision trees, support vector machines, clustering, neural networks, as well as key techniques for feature selection and dimensionality reduction, error estimation and empirical validation.

## Mini Project 1: Getting started with machine learning

**Abstract:**

  In this project, we investigated the performance of the K-nearest neighbour (KNN) and decision tree models on these two benchmark datasets from the UC Irvine Machine Learning Repository: the Wisconsin breast cancer dataset and the hepatitis dataset. For the KNN model we tested the accuracy using different values of K and distance functions, and for the Decision Tree model we tried different maximum tree depths and cost functions. We found that the KNN model had an accuracy of 98% using a Euclidean distance function and k = 20 for the Wisconsin breast cancer dataset, and the decision tree model had an accuracy of 95% for the hepatitis dataset using an entropy cost function with maximum depth of 5. In our analysis, we found that increasing K in the KNN model resulted in clear underfitting, and increasing depth for the decision trees resulted in overfitting. We also investigated selecting only important features to simplify the dataset, and used PCA to visualize the model predictions.

## Mini Project 2: Classification of textual data

**Abstract:**

  In this project, we investigated the performance of two linear classification models, multinomial naive Bayes and logistic regression, on two benchmark datasets: the 20 news group dataset and the IMDB dataset. We used 5-fold cross validation for the hyperparameter tuning of our models and found that the logistic regression model achieved better accuracy than the naive Bayes model but was significantly slower to train compared to the naive Bayes model. Our results also showed that the accuracy of the two models increased as the training dataset size increased. For the creativity section, we experimented with using bag-of-words text embedding for data pre-processing but the accuracy performance was found to be worse than using tf-idf text embedding. We also investigated the effect of various n-grams on the accuracy of the two datasets, and found that n-grams can increase and decrease accuracy, depending on the situation.

## Mini Project 3: Classification of image data

**Abstract:**

  In this project, we implemented a multilayer perceptron (MLP) model and trained it using mini-batch stochastic gradient descent (SGD) methods. We explored the accuracy performance of this model when classifying image data from the MNIST dataset. In order to have a better understanding on MLP model, we conducted experiments to analyze the impact of number of hidden layers, types of activation function, regularization, and adaptive gradient descent methods on the testing accuracy. We found that increasing depth and width on an MLP model increases accuracy up until the convergence bound, and obtained surprising results when comparing normalized vs. unnormalized training data performance. Finally, we investigated and demonstrated how adaptive gradient descent methods can speed up convergence significantly.

## Mini Project 4: Reproducibility in ML

**Abstract:**

  The main claim of the paper "Visualizing Data using t-SNE" by Laurens van der Maaten and and Geoffrey Hinton is that t-SNE, a new technique for visualizing high-dimensional data, produces significantly better maps compared to other non-parametric visualization techniques. In this project, we reproduced the visualizations of the MNIST dataset from the paper by Maaten and Hinton using t-SNE, Sammon mapping, isomap, and locally linear embedding (LLE). We found that it was possible to reproduce the results from the original paper. We then extended the results of the original paper by exploring different parameter choices and using the 2D representation of data to train KNN and decision tree models.
