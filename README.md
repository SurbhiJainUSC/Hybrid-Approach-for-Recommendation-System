# Hybrid-Approach-for-Recommendation-System

This Hybrid Approach for Recommendation System is based on User Collaborative Filtering, Item-Based Collaborative Filtering 
and Adaptive Association Rule Mining (ARM) to improve the performance of existing Recommender systems. This recommendation 
system has the following major purposes associated with it:
- Avoid the problem of recommending only similar products
- Overcome the problem of false nearest neighbors
- Overcome the inefficiency of ARM algorithms to process large data
- Adaptivity in support levels required in ARM algorithms
- More personalized recommendations and specific to the user needs
- Computationally faster system than the traditional recommendation system algorithms.

## Dataset
A well-known MovieLens dataset has been used to test this hybrid approach. The dataset contains 100000 ratings (1-5)
given by 943 users to 1682 movies. Each user has rated at least 20 movies.

## Algorithm
The hybrid algorithm works in 4 phases:
* The first phase is based on user collaborative filtering. It involves computation of nearest neighbors of the target user 
using K-Nearest Neighbor (KNN) algorithm. The similarity between each user is measured by applying Pearson’s correlation
coefficient on the item ratings given by the user. All the items rated by a user are considered as transactions corresponding 
to that user. Next, the transactions of all the nearest neighbors are combined with the transaction of the target user to 
form the transaction database for the target user. Thus, the transaction database contains the transactions of only the 
relevant users.
* Next step is to compute the similarity of each item with every other item in the transaction database formed in the 
previous phase using Jaccard index and store these values in a form of the similarity matrix.
* Next phase is to generate the required association rules via FP-growth approach. The input to the FP-growth algorithm 
includes the transaction database of the target user, minimum support count, and minimum confidence. Since it is tough to
choose a proper minimum support count before the mining process, adaptivity in the support levels has been introduced. 
The algorithm adjusts the support threshold such that an adequate number of rules are generated.
* Once the strong association rules are generated, they are sorted in the descending order of their confidence values. 
To provide recommendations, consequents of those association rules are added to recommendation list whose antecedent 
completely match with the input item list. Finally, if the number of recommendations obtained from association rules is 
less than the required recommendations, the remaining places are filled on the basis of similarity values computed in 
second phase. To provide recommendations, similarity values of items in the input list are added corresponding to every item
in the database. Consequently, items with more similarity values are appended to the recommendation list generated through 
association rules.

## Web Interface
The website has been built using Django 1.8, a MVC web framework for python. When a user opens up the website, he has to 
first authenticate his identity using his credentials (username and password). The usernames for all 943 users has been set
as 1-943 and their password is same as their username. After successful log in, the home screen displays a list of all the 
movies in the database. There is a navigation bar on the top which consists of buttons such as 'Home' to redirect a 
user to home screen; a drop down menu containing list of all the genres to which all the movies belongs; search box using 
which a user can search for any movie in the database. 'Add to cart' adds a particular product chosen by a user into his cart 
for recommendation process and 'Cart' allows user to access his cart. User can also delete movie from his cart by clicking on
'Remove' button. Also, there is a 'History' button which displays the list of all the movies rated by that user previously. 
Finally, the user can use the 'Logout' button to log off his session.

<b> For more information, visit the link: https://bit.ly/32RlCnQ
