# Guida alle variabili di WP-PageNavi per WordPress.

La navigazione tra le pagine è una parte importante di qualsiasi blog o sito di notizie su WordPress. Uno degli strumenti più popolari per una navigazione paginata comoda è il plugin **WP-PageNavi**. Permette di sostituire i link standard "Precedente / Successivo" con una paginazione più flessibile e accattivante.

Una delle funzionalità chiave è la personalizzazione del testo dei link tramite **variabili**, che sostituiscono automaticamente il numero di pagina corrente, il numero totale di pagine e altre informazioni.

In questo articolo esamineremo **tutte le variabili disponibili**, esempi del loro utilizzo e mostreremo con screenshot dove inserirle.

---

## Dove si trovano le impostazioni di WP-PageNavi

Dopo aver installato il plugin, vai nell'amministrazione di WordPress:

**Impostazioni → PageNavi**

Lì vedrai un menu per configurare il testo dei link (esempio nello screenshot qui sotto):

![Impostazioni PageNavi in WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 In ogni campo è possibile utilizzare variabili per visualizzare dinamicamente la pagina corrente, il numero totale di pagine e altri elementi di navigazione.

---

## Variabili disponibili in WP-PageNavi

Il plugin fornisce un set di segnaposto (variabili modello) che possono essere utilizzati nelle impostazioni:

### 🔹 %CURRENT_PAGE%
Visualizza il **numero della pagina corrente**.

Esempio:
```

Sei sulla pagina %CURRENT\_PAGE%

```
👉 Se ti trovi sulla pagina 3, il risultato sarà:
```

Sei sulla pagina 3

```

---

### 🔹 %TOTAL_PAGES%
Mostra il **numero totale di pagine**.

Esempio:
```

Pagine totali: %TOTAL\_PAGES%

```
👉 Se ci sono 10 pagine in totale, l'output sarà:
```

Pagine totali: 10

```

---

### 🔹 %PAGE_NUMBER%
Utilizzato per visualizzare il **numero di ogni pagina** nell'elenco.

Esempio:
```

Pagina %PAGE\_NUMBER%

```
👉 Nella navigazione appariranno i link:
```

Pagina 1 | Pagina 2 | Pagina 3 | ...

```

---

## Tabella delle variabili di WP-PageNavi

| Variabile        | Descrizione                           | Esempio di impostazione                   | Risultato (se 3a pagina su 10)       |
|-------------------|---------------------------------------|-------------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Numero della pagina corrente          | `Ora sei sulla pagina %CURRENT_PAGE%`     | `Ora sei sulla pagina 3`             |
| **%TOTAL_PAGES%**  | Numero totale di pagine               | `Pagine totali: %TOTAL_PAGES%`            | `Pagine totali: 10`                  |
| **%PAGE_NUMBER%**  | Numero di ogni pagina nell'elenco     | `Pagina %PAGE_NUMBER%`                    | `Pagina 1 | Pagina 2 | Pagina 3 …` |
| **1 (statico)**   | Prima pagina (nessuna variabile)      | `Prima` o `Pagina 1`                      | `Prima`                              |
| **%TOTAL_PAGES%**  | Ultima pagina                         | `Pagina %TOTAL_PAGES%`                    | `Pagina 10`                          |
| **← / → / …**      | Simboli per frecce e abbreviazioni    | `← Indietro`, `Avanti →`, `…`             | `← Indietro | 1 | 2 | 3 | … | 10 | Avanti →` |

---

## Esempio di configurazione completa

Nello screenshot sopra, i campi possono essere compilati come segue:

- **Text For Number Of Pages**:
  `Pagina %CURRENT_PAGE% di %TOTAL_PAGES%`

- **Text For Current Page**:
  `%PAGE_NUMBER%`

- **Text For Page**:
  `%PAGE_NUMBER%`

- **Text For First Page**:
  `Prima`

- **Text For Last Page**:
  `Pagina %TOTAL_PAGES%`

- **Text For Previous Page**:
  `← Indietro`

- **Text For Next Page**:
  `Avanti →`

- **Text For Previous …**:
  `…`

- **Text For Next …**:
  `…`

👉 Di conseguenza, i visitatori vedranno una navigazione simile a questa:
```

← Indietro | Prima | 1 | 2 | 3 | … | Pagina 10 | Avanti →

```

---

## Riepilogo

Le variabili in WP-PageNavi sono semplici, ma offrono flessibilità nella configurazione della navigazione:

- `%CURRENT_PAGE%` — pagina corrente
- `%TOTAL_PAGES%` — pagine totali
- `%PAGE_NUMBER%` — numero di una pagina specifica

Per la prima pagina usa `1`, e per l'ultima `%TOTAL_PAGES%`.

Grazie a queste impostazioni, è possibile rendere la navigazione del sito più chiara e comoda per i visitatori.
