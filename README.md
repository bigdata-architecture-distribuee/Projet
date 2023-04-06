# Projet - Bigdata
Titre du projet: Analyse en temps réel de la relation entre les données du trafics aériens et des conditions météorologiques en Europe.

Description du projet:
Dans ce projet, nous allons analyser l'impact des vols sur la qualité de l'air et les conditions météorologiques dans l'espace aérien européen en temps réel, effectuer une régression linéaire et trouver une corrélation entre les données météorologiques et le nombre de vols, utiliser les données de vol et les données météorologiques pour identifier les pays européens qui sont les plus touchés par les conditions météorologiques défavorables. 
Nous utiliserons trois API pour collecter les données nécessaires, puis Kafka Connect, Spark Streaming, PySpark et Docker pour traiter et analyser ces données

Sources de données:
OpenSky API : Pour obtenir le nombre de vols présents dans l'espace aérien européen avec le pays d'origine de chaque vol.
Waqi API : Pour obtenir des informations sur la qualité de l'air par pays européen.
OpenWeatherMap API : Pour obtenir des informations sur la météo par pays européen.

Étapes du projet :

1-Configuration de l'environnement : Configuration de notre environnement avec Docker pour déployer Kafka, Spark et PySpark.

2-Collecte de données en temps réel : Utilisation de Jupyter et python pour récupérer les données en temps réel des trois API (API OpenSky, Waqi API et OpenWeatherMap).

3-Enregistrement des données dans une base de données: Utilisation de Jupyter et python pour l'envoie des données dans une base de données MongoDB pour la facilitation de leur exploitation.

3-Traitement des données : Utilisation de Spark ML et PySpark pour traiter et agréger les données récupérées des API. Création des jointures entre les différentes sources de données pour analyser la correlation entre nos différentes variables et identifier les autres anomalies.

4-Analyse des données : Analyses sur les données agrégées pour déterminer les tendances, les corrélations et les anomalies éventuelles. Par exemple, étude de comment le nombre de vols et leur pays d'origine peuvent influencer la qualité de l'air et les conditions météorologiques dans les pays européens.

5-Visualisation des résultats : Création des visualisations interactives et en temps réel à l'aide d'outils de visualisation comme PowerBI ou Plotly pour afficher les résultats de nos analyses.

7-Documentation et rapport : Rédigez un rapport détaillé expliquant la méthodologie, les résultats et les conclusions de votre projet. Documentez également le code et les configurations utilisés dans le projet.
