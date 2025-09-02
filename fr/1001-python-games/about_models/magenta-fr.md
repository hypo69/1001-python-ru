Comment connecter et utiliser le modèle Magenta Melody RNN, basé sur Python et TensorFlow.

Version Python 3.7

**1. Installation de Magenta :**

Tout d'abord, vous devez installer la bibliothèque Magenta. La méthode d'installation recommandée est via pip.

*   **Créer un environnement virtuel (recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\\Scripts\\activate  # Windows
    ```
*   **Installer Magenta :**
    ```bash
    pip install magenta
    ```
    *   **Remarque :** Magenta peut nécessiter TensorFlow. Si vous ne l'avez pas, pip l'installera automatiquement.
    *   **Pour l'accélération GPU :** Si vous avez un GPU NVIDIA et CUDA, vous pouvez installer la version de TensorFlow avec prise en charge GPU (voir la documentation TensorFlow).

**2. Importation des modules nécessaires :**

Après l'installation de Magenta, importez les modules nécessaires dans votre script Python :
```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.common import sequence_example_lib
```

**3. Chargement d'un modèle entraîné :**

Les modèles Melody RNN sont entraînés sur de grands ensembles de données et sont disponibles en téléchargement. Vous pouvez choisir l'un des modèles pré-entraînés (par exemple, `attention_rnn` ou `basic_rnn`).

*   **Initialisation du modèle :**
    ```python
    model_name = 'attention_rnn'  # Ou 'basic_rnn'
    melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
        model_name=model_name
    )
    ```
    *   Lors de l'initialisation, le modèle chargera automatiquement les poids nécessaires.

**4. Génération d'une mélodie :**

Vous pouvez maintenant générer une mélodie. Pour ce faire, utilisez la méthode `generate()` :
```python
# Paramètres de génération
temperature = 1.0  # Contrôle le caractère aléatoire, 1.0 - valeur normale
num_steps = 128   # Nombre d'étapes (longueur) de la mélodie
primer_sequence = None # Vous pouvez spécifier une mélodie d'amorce, en laissant None, le modèle commencera à partir de zéro.
# Création d'une mélodie
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)
```
*   `temperature` : Plus la valeur est élevée, plus la génération sera aléatoire et "créative", mais elle peut aussi devenir moins cohérente.
*   `steps` : Spécifie le nombre d'étapes dans la mélodie générée.
*  `primer_sequence` : Spécifie la mélodie à partir de laquelle le modèle commence à générer. Si `None`, le modèle commencera à partir de zéro.

**5. Travailler avec MIDI :**

La mélodie générée est représentée sous la forme d'un objet `Sequence`, qui peut être enregistré dans un fichier MIDI ou utilisé pour un traitement ultérieur :
```python
# Enregistrement en MIDI
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)
midi_file = os.path.join(output_dir, 'generated_melody.mid')
mm.sequence_proto_to_midi_file(melody_sequence, midi_file)

print(f"Melody saved to: {midi_file}")
```

**6. Ajout d'accords et de percussions (comme dans l'exemple) :**

Vous pouvez combiner la mélodie générée avec des progressions d'accords et des parties de percussions, comme indiqué dans votre exemple de code :
```python
# Accords
chords = ["C", "G", "Am", "F"] * (num_steps // 4) # Création d'une séquence d'accords, par répétition
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# Percussions
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps//4,
    steps_per_quarter=4,
)

music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120  # Réglage du tempo

# Enregistrement de la piste complète en MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

**Exemple complet :**

```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator

# 1. Définition des paramètres
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)

model_name = 'attention_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model_name=model_name
)

temperature = 1.0
num_steps = 128
primer_sequence = None
# 2. Génération d'une mélodie
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)

# 3. Ajout d'accords
chords = ["C", "G", "Am", "F"] * (num_steps // 4)
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)


# 4. Ajout de percussions
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps // 4,
    steps_per_quarter=4,
)
music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120


# 5. Enregistrement en MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")

```

**Conseils supplémentaires :**

*   **Expérimentez avec les paramètres :** Essayez différentes valeurs de `temperature` et `num_steps`.
*   **Chargez vos propres MIDI :** Vous pouvez utiliser vos propres mélodies comme amorce (`primer_sequence`).
*   **Entraînez le modèle sur vos propres données :** Si vous souhaitez un style spécifique, essayez d'entraîner le modèle sur votre propre ensemble de données.
*   **Explorez la documentation Magenta :** Magenta fournit une bonne documentation et des exemples.
*  **Remarque :** `primer_sequence` doit être sous la forme de `mm.NoteSequence()`.
