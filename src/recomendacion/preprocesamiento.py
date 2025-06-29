import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans


# Cargar los archivos
df_dest = pd.read_csv("Expanded_Destinations.csv")
df_users = pd.read_csv("Final_Updated_Expanded_Users.csv")
df_history = pd.read_csv("Final_Updated_Expanded_UserHistory.csv")
df_reviews = pd.read_csv("Final_Updated_Expanded_Reviews.csv")

# Mostrar formas de los datasets
print(">> Formas:")
print(f"Destinos: {df_dest.shape}")
print(f"Usuarios: {df_users.shape}")
print(f"Historial: {df_history.shape}")
print(f"Reseñas: {df_reviews.shape}\n")

# Revisar valores únicos
print(">> Registros únicos:")
print(f"Usuarios únicos (Users): {df_users['UserID'].nunique()}")
print(f"Usuarios únicos (History): {df_history['UserID'].nunique()}")
print(f"Usuarios únicos (Reviews): {df_reviews['UserID'].nunique()}")

print(f"Destinos únicos (Destinations): {df_dest['DestinationID'].nunique()}")
print(f"Destinos únicos (History): {df_history['DestinationID'].nunique()}")
print(f"Destinos únicos (Reviews): {df_reviews['DestinationID'].nunique()}\n")

# Revisar valores nulos
print(">> Valores nulos:")
print("Users:", df_users.isnull().sum().to_dict())
print("History:", df_history.isnull().sum().to_dict())
print("Reviews:", df_reviews.isnull().sum().to_dict())
print("Destinations:", df_dest.isnull().sum().to_dict(), "\n")

# Revisar duplicados
print(">> Duplicados:")
print(f"Users: {df_users.duplicated().sum()}")
print(f"History: {df_history.duplicated().sum()}")
print(f"Reviews: {df_reviews.duplicated().sum()}")
print(f"Destinations: {df_dest.duplicated().sum()}")

# Crear matriz usuario × destino
matriz_ratings = df_history.pivot_table(index='UserID', columns='DestinationID', values='ExperienceRating')

# Mostrar un resumen
print("Matriz de ratings creada:")
print(matriz_ratings.head())

# Opcional: mostrar cuántos destinos promedio ha calificado cada usuario
calificaciones_por_usuario = matriz_ratings.notnull().sum(axis=1).mean()
print(f"Promedio de destinos calificados por usuario: {calificaciones_por_usuario:.2f}")
print("Forma real de la matriz:", matriz_ratings.shape)

# Paso 1: rellenar los NaN con 0
matriz_ratings_llena = matriz_ratings.fillna(0)

print("Matriz lista para calcular similitudes:")
print(matriz_ratings_llena.head())

# Paso 2: calcular similitud coseno entre destinos
matriz_transpuesta = matriz_ratings_llena.T  # destinos como filas
matriz_similitud = cosine_similarity(matriz_transpuesta)

# Convertimos a DataFrame para mejor manejo
df_similitud_destinos = pd.DataFrame(
    matriz_similitud,
    index=matriz_transpuesta.index,
    columns=matriz_transpuesta.index
)

# Mostrar parte de la matriz de similitud
print("Similitud entre destinos (primeras filas):")
print(df_similitud_destinos.iloc[:5, :5])

# Paso 1: Cargar destinos si no lo has hecho ya
# df_dest = pd.read_csv("Expanded_Destinations.csv")  # si no está cargado

# Paso 2: Codificar columnas categóricas
categoricas = ['Type', 'State', 'BestTimeToVisit']
encoder = OneHotEncoder(sparse_output=False) 
encoded = encoder.fit_transform(df_dest[categoricas])

# Crear DataFrame con columnas codificadas
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categoricas))

# Añadir columna de Popularidad (numérica)
features_destinos = pd.concat([encoded_df, df_dest[['Popularity']].reset_index(drop=True)], axis=1)

# Mostrar las primeras filas del vector de características
print("Vector de características para clustering:")
print(features_destinos.head())

# Paso 2: Agrupar destinos en clusters
k = 6  # Puedes probar con otros valores
modelo_kmeans = KMeans(n_clusters=k, random_state=42)
clusters = modelo_kmeans.fit_predict(features_destinos)

# Añadir la columna de cluster al DataFrame original
df_dest['Cluster'] = clusters

# Mostrar algunos ejemplos por cluster
print("Ejemplos de destinos por clúster:")
print(df_dest[['DestinationID', 'Name', 'Type', 'State', 'Cluster']].groupby('Cluster').head(3))