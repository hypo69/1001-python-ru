# Qu'est-ce que l'apprentissage automatique — et comment «apprend-il» réellement ?
![1](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/1.png)

*Quatre chats sur lesquels repose l'apprentissage automatique*

En quoi l'apprentissage automatique diffère-t-il de la programmation traditionnelle avec son «ça marche tant que tu n'y touches pas» ? Où s'arrêtent les algorithmes clairs — et où commence la magie de la «boîte noire», comme dans le cas de ChatGPT ?

*Ceci est le premier article d'une série de vulgarisation scientifique où nous analyserons les bases de l'IA — sans mots vides, sans clichés, sans brouillard académique et, idéalement, sans équations (comme Stephen Hawking l'a écrit un jour : chaque formule dans un livre de vulgarisation scientifique réduit ses ventes de moitié).*

Aujourd'hui, nous parlerons des fondements mêmes : quels types d'apprentissage utilisent les modèles d'IA, pourquoi sont-ils nécessaires et comment déterminent-ils ce dont un modèle est capable.

Oui, il y aura des chats. Et un peu de sarcasme. Mais exclusivement à des fins nobles — pour créer des associations fortes et mémorables.

Cet article s'adresse à tous ceux qui commencent à se familiariser avec l'IA : aux lecteurs techniques et non techniques, aux architectes de solutions, aux fondateurs de startups, aux développeurs expérimentés et à tous ceux qui veulent enfin se faire une idée claire de ce qu'est l'apprentissage automatique et de la façon dont tout cela commence.

Dans cette partie, nous aborderons les bases :
Ce qu'est le ML, en quoi il diffère fondamentalement de la programmation traditionnelle, et quatre paradigmes d'apprentissage clés qui sous-tendent l'ensemble du paysage de l'IA moderne.

#### Programmation classique vs. apprentissage automatique

Si vous êtes déjà confiant dans votre compréhension de la différence entre l'apprentissage automatique et la programmation traditionnelle, n'hésitez pas à sauter cette section. Mais si vous voulez clarifier cette distinction, cela pourrait vous aider.

Commençons par une analogie simple.

Une calculatrice effectue une opération arithmétique à la fois — et uniquement sur commande directe. Un ordinateur avec du code traditionnel va un peu plus loin : il exécute des programmes prédéfinis, prend des décisions à l'aide de structures de contrôle, stocke des valeurs intermédiaires et traite plusieurs entrées. Cela fonctionne très bien lorsque les entrées sont prévisibles et que le comportement peut être décrit par une logique rigide et déterministe.

Mais cette approche échoue dans des situations confuses, ambiguës ou incertaines.

Par exemple, essayez d'écrire un ensemble complet de règles `if/else` pour :
*   distinguer la Lune d'un plafonnier rond,
*   déchiffrer une écriture manuscrite désordonnée,
*   ou détecter le sarcasme dans un tweet.

Cela ne s'adapte pas. Vous vous heurtez rapidement à une explosion combinatoire de cas particuliers.

C'est là que la programmation classique atteint son plafond, et que l'apprentissage automatique commence.

On peut considérer le ML comme le niveau d'abstraction suivant : si les calculatrices travaillent avec l'arithmétique et le code avec la logique structurée, le ML gère l'incertitude non structurée. Même la logique floue — avec ses gradients et ses seuils — ne parvient souvent pas à faire face à la complexité du monde réel. Le ML ne repose pas du tout sur des règles pré-écrites ; au lieu de cela, il apprend le comportement à partir des données.

Au lieu de dire à la machine *quoi faire*, vous lui montrez *ce que vous voulez obtenir*, et elle détermine statistiquement *comment* le faire. L'apprentissage ne se fait pas par des instructions codées en dur, mais par des modèles, des probabilités et la généralisation.
![2](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/2.png)

*La reconnaissance de l'écriture manuscrite et des images ne sont que deux exemples de tâches où il est impossible de prédire tous les scénarios.*

Selon son entraînement, un modèle de ML peut voir une lettre qu'il n'a jamais rencontrée auparavant et la reconnaître quand même — en se basant sur des milliers d'échantillons manuscrits similaires. Il peut déterminer qu'un utilisateur a dessiné un dinosaure, même si cette silhouette exacte ne figurait pas dans les données d'entraînement — parce qu'il comprend les formes, les proportions et la texture non pas comme des règles, mais comme des distributions. Au lieu de suivre rigidement un script pré-écrit — il devine.

#### Paradigmes d'apprentissage automatique

Ce qu'un modèle d'IA peut faire dépend fortement de la façon dont il a été entraîné.

Avant tout, les modèles d'IA sont classés selon leurs paradigmes d'apprentissage. Le paradigme détermine les forces et les faiblesses du modèle.

La plupart des méthodes d'apprentissage automatique relèvent de l'un des quatre paradigmes principaux :
*   Apprentissage supervisé
*   Apprentissage non supervisé
*   Apprentissage par renforcement
*   Apprentissage auto-supervisé (parfois aussi appelé «auto-apprentissage»)

#### Apprentissage supervisé (Supervised Learning)
![3](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/3.png)

Comment entraîner un modèle à distinguer les chats des chiens sur des photos ? Vous lui montrez des dizaines de milliers d'images — chacune avec la bonne étiquette : «Ceci est un chat» ou «Ceci est un chien». Le modèle commence à chercher des motifs : «Ah, les chats ont des oreilles triangulaires, et les chiens ont de longs museaux». Il ne sait pas ce qu'est un chat ou un chien, mais il voit que certaines images se ressemblent, et d'autres non. Et à chaque nouvel exemple, il s'améliore dans la reconnaissance de ces motifs. Après des milliers d'itérations, le modèle commence à remarquer quelque chose par lui-même : les chats ont des oreilles triangulaires, un regard suspicieux et une tendance à s'installer fermement sur le clavier. C'est l'apprentissage supervisé — l'entraînement sur des exemples étiquetés où la «bonne» réponse est connue à l'avance.

Essentiellement, vous dites : «Voici l'entrée — et voici la sortie attendue». La tâche du modèle est de trouver des motifs et de les généraliser à de nouvelles données, jamais vues.

![4](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/4.png)

*Après mille photos de chats, le modèle a saisi l'essence : les oreilles triangulaires sont importantes. Maintenant, il utilise cela pour distinguer les chats des chiens.*

**Cas d'utilisation typiques :**
*   **Classification** (par exemple, spam vs. non-spam)
*   **Régression** (par exemple, prévision des prix)
*   **Estimation de probabilité** (par exemple, probabilité de désabonnement des clients)

**Apprentissage supervisé dans le monde réel :**
*   **Analyse des sentiments :** *Entrée :* texte d'avis → *Sortie :* positif / négatif
*   **Filtrage du spam :** *Entrée :* texte d'e-mail → *Sortie :* spam / non-spam
*   **Diagnostic médical :** *Entrée :* résultats d'analyse → *Sortie :* sain / malade
*   **Modération de contenu :** *Entrée :* texte ou image → *Sortie :* autorisé / enfreint les règles
*   **Catégorisation de produits :** *Entrée :* description du produit → *Sortie :* catégorie du catalogue
*   **OCR (Reconnaissance optique de caractères) :** *Entrée :* photo de document → *Sortie :* texte extrait

#### Apprentissage non supervisé (Unsupervised Learning)
![5](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/5.png)

*Parfois, il semble que les dinosaures ne soient que des grenouilles trop confiantes.*

Dans ce paradigme, le modèle apprend à partir de données non étiquetées, ce qui signifie qu'on ne lui dit jamais quelle est la «bonne» réponse. Au lieu de cela, il essaie de découvrir indépendamment la structure cachée, les motifs ou les relations. Pensez-y comme essayer d'organiser le chaos en catégories alors que personne ne vous a jamais dit quelles devraient être ces catégories.

Imaginez que vous montrez au modèle des milliers d'images — chats, chiens, grenouilles et dinosaures (supposons, pour plus de clarté, que nous ayons d'une manière ou d'une autre obtenu des photos claires de reptiles éteints). Mais nous ne disons pas au modèle qui est qui. En fait, le modèle ne sait même pas combien de catégories il y a : trois ? cinq ? cinquante ? Il cherche simplement des motifs visuels. Finalement, il commence à regrouper les créatures à fourrure dans un cluster, et celles à la peau lisse, aux yeux sur les côtés et au regard sinistrement froid — dans un autre.

![6](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/6.png)

Après des milliers d'exemples, le modèle finit par décider : «Mettons toutes les choses à fourrure dans la boîte n°1,
et tout ce qui a la peau brillante et les yeux sur les côtés — dans la boîte n°2.» Les étiquettes elles-mêmes n'ont pas d'importance — ce qui compte, c'est que le contenu de chaque boîte devienne plus homogène.

Les modèles non supervisés n'essaient pas de prédire des étiquettes. Au lieu de cela, ils :
*   **Regroupent des objets similaires (clustering)**
*   **Détectent les valeurs aberrantes ou les anomalies**
*   **Réduisent la dimensionnalité (simplifient les données complexes)**

Ce paradigme est particulièrement utile lorsque :
*   L'étiquetage des données est trop coûteux ou peu pratique
*   Vous ne savez pas encore ce que vous cherchez
*   Vous voulez découvrir des segments ou des modèles de comportement sans catégories prédéfinies

#### Apprentissage par renforcement (Reinforcement Learning)

Dans ce paradigme, le modèle — appelé agent — apprend en interagissant avec l'environnement par essais et erreurs. L'agent essaie différentes actions et observe la réaction de l'environnement. Les actions qui mènent au résultat souhaité apportent des récompenses ; les actions inefficaces ou nuisibles entraînent des pénalités.

Essayons d'entraîner un chat. (Oui, nous savons que c'est presque impossible dans la vie réelle, mais nous avons déjà commencé avec le thème des chats, alors nous y sommes.)
Le chat est l'agent. L'appartement est l'environnement. Le chat essaie différentes actions : A attrapé une mouche → a reçu une friandise (récompense) A fait tomber la télévision → pas de dîner (pénalité)
Grâce à des expériences répétées, le chat commence à se comporter de manière utile — non pas parce qu'il comprend ce que vous voulez, mais parce qu'il a appris une politique : un ensemble d'actions qui mènent le plus souvent à la nourriture. Il n'a pas besoin de règles — il apprend des conséquences.

![7](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/7.png)

*Comme le montre le graphique — crier ne vous mènera nulle part.)*

**L'apprentissage par renforcement est utilisé lorsque :**
*   Le comportement doit s'améliorer avec le temps
*   Il n'y a pas de réponses «correctes» prédéfinies
*   Les conséquences sont différées, pas immédiates

#### Apprentissage auto-supervisé (Self-Supervised Learning)

Dans cette approche, le modèle apprend à partir de données non étiquetées, mais la tâche d'apprentissage est extraite des données elles-mêmes — sans intervention humaine dans l'étiquetage. Le modèle apprend à prédire une partie des données d'entrée en fonction d'une autre.

**Exemple**
Phrase originale : *«Le chat a sauté sur le clavier et a commis du code inachevé en production.»*

Nous pouvons transformer cela en une tâche d'apprentissage. Par exemple :
*   **Masquer un mot :** *entrée :* «Le chat a sauté sur le \*\*\* et a déployé du code inachevé...», *cible :* prédire le mot **clavier**.
*   **Interrompre une phrase :** *entrée :* «Le chat a sauté sur...», *cible :* continuer la phrase.

![8](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/8.png)

*Pour un chat tensoriel, écrire à l'envers n'est qu'une question de choix du bon système de coordonnées.*

Ces paires «entrée + cible» sont générées automatiquement, sans étiquetage manuel. La même idée s'applique à différents types de données, tels que les images (prédiction de fragments manquants) ou l'audio.

**Applications réelles de l'apprentissage auto-supervisé :**
*   **Modèles linguistiques** (GPT, LLaMA, Claude)
*   **Vision par ordinateur** (CLIP, DINO)
*   **Audio et parole** (Wav2Vec 2.0)
*   **Modèles multimodaux** (Gemini, CLIP)
*   **Pré-entraînement (modèles fondamentaux)**

**Idée principale**
Le modèle apprend à partir de tâches générées automatiquement, où la «bonne réponse» est extraite directement des données elles-mêmes. Cela nous confère une évolutivité, une capacité de généralisation et la base de la plupart des systèmes génératifs et linguistiques modernes.

#### Résumé des paradigmes d'apprentissage

| Paradigme                 | Comment le modèle apprend                                    |
|---------------------------|--------------------------------------------------------------|
| Apprentissage supervisé   | Sur des données étiquetées (entrée → bonne réponse)          |
| Apprentissage non supervisé | Sur des données non étiquetées (le modèle trouve la structure lui-même) |
| Apprentissage par renforcement | Par interaction avec l'environnement via des récompenses et des pénalités |
| Apprentissage auto-supervisé | Sur des données non étiquetées, où les tâches sont générées à partir d'elles-mêmes |

#### Qu'est-ce qui existe d'autre ?

Outre ces quatre, il existe d'autres approches (semi-supervisé, actif, apprentissage en ligne, etc.). Elles sont rarement considérées comme des paradigmes indépendants car elles sont généralement des hybrides ou des variations des stratégies principales que nous avons déjà examinées. Pour comprendre l'essence de l'apprentissage automatique, il suffit de maîtriser ces quatre.

Dans la partie suivante, nous plongerons dans ce qu'est réellement un réseau neuronal : neurones, poids, connexions. Comment «apprend-il» ? Pourquoi a-t-il besoin de couches ? Et quel est le rapport entre un tas de nombres et la compréhension du langage, des images ou... de la réalité ?

Nous allons éplucher couche par couche — et essayer de répondre à la seule question qui compte :

**Alors, y a-t-il de la magie ici... ou est-ce juste des mathématiques déguisées ?**

https://medium.com/@paul.ilvez/how-ai-learns-no-formulas-but-plenty-of-cats-fc43471add24
