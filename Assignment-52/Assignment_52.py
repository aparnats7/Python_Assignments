import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    Border = "-"*40

    #----------------------------------------------------
    # Step 1 :- Load and Explore Dataset
    #----------------------------------------------------

    print(Border)
    print("Step 1 :- Load and Explore Dataset")
    print(Border)

    df = pd.read_csv("student-mat.csv", sep=';')

    print("Shape:", df.shape)
    print("First 5 rows:\n", df.head())

    print("Columns:\n", df.columns)

    print("Missing values:\n", df.isnull().sum())

    #----------------------------------------------------
    # Step 2 :- Select Features
    #----------------------------------------------------

    print(Border)
    print("Step 2 :- Feature Selection")
    print(Border)

    # Selected features from assignment
    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']

    data = df[features]

    print("Selected Data:\n", data.head())

    #----------------------------------------------------
    # Step 3 :- Scaling
    #----------------------------------------------------

    print(Border)
    print("Step 3 :- Scaling")
    print(Border)

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    #----------------------------------------------------
    # Step 4 :- K-Means Clustering
    #----------------------------------------------------

    print(Border)
    print("Step 4 :- K-Means Clustering")
    print(Border)

    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    df['Cluster'] = clusters

    print("Cluster Assigned:\n", df[['G3', 'Cluster']].head())

    #----------------------------------------------------
    # Step 5 :- Visualization
    #----------------------------------------------------

    print(Border)
    print("Step 5 :- Visualization")
    print(Border)

    plt.scatter(df['G3'], df['absences'], c=df['Cluster'])
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Absences")
    plt.title("Student Clusters")
    plt.show()

    #----------------------------------------------------
    # Step 6 :- Cluster Analysis
    #----------------------------------------------------

    print(Border)
    print("Step 6 :- Cluster Analysis")
    print(Border)

    print(df.groupby('Cluster')[features].mean())

    print("\nCluster Meaning:")
    print("Cluster 0 → Top Performers")
    print("Cluster 1 → Average Students")
    print("Cluster 2 → Struggling Students")


if __name__ == "__main__":
    main()