---
name: le-unslop
description: Write, rewrite, translate into, or review natural French prose, removing formulaic AI phrasing and applying France typography by default. Preserve requested tone, regional conventions, and technical literals.
---

# le-unslop

Rends un texte français précis et humain. Ce skill vise le français de France.

Respecte la demande avant les préférences de style : ton, registre, variante régionale et format de sortie. Conserve le sens, tous les faits et leurs nuances (« à partir de », « environ », objectif plutôt que résultat). Un texte déjà juste peut rester inchangé.

Les règles typographiques portent sur la prose. Conserve à l'identique le code, les commandes, les URL, les identifiants, les données structurées et les citations à reproduire mot pour mot. Dans un document technique, corrige la prose autour de ces éléments.

## Pourquoi un texte sent l'IA

Un modèle choisit la suite la plus probable. Il écrit donc la phrase moyenne : générale, équilibrée, polie, qui irait dans n'importe quel texte. Les tics sont les symptômes de trois causes. Corrige la cause, pas le mot : remplacer « crucial » par « essentiel » garde le même tic.

1. **Pas de référent.** La phrase ne dit ni qui, ni quoi, ni quand, ni combien. Mets le fait, ou coupe. S'il manque, demande-le ou laisse `[à préciser : …]`. N'invente jamais un chiffre, une source ou une citation.
2. **Symétrie.** Contrastes en série, triplets, trois parties de même longueur, conclusion qui répète l'introduction. Casse le moule et garde le nombre réel d'éléments.
3. **Anglais traduit.** Calques, typographie anglaise, formules d'e-mail traduites. Écris ce qu'un francophone dirait.

Un mot de la liste ne condamne pas un texte : c'est la densité qui trahit. Ces exemples sont des indices à examiner, pas des interdictions. Garde une tournure utile au sens, au genre ou au ton demandé. Le français n'est pas de l'anglais raccourci. Garde la phrase longue qui se tient et les connecteurs qui relient vraiment. Le staccato de réseau social (« Résultat : », une phrase par ligne) est lui aussi un tic.

## Ce qu'il faut couper

| Tic | Exemples | À la place |
|---|---|---|
| Ouverture de décor | Dans un monde en constante évolution, À l'ère du numérique, À l'heure où | un fait daté |
| Cheville | Il est important de noter que, Il convient de souligner, Force est de constater | rien |
| Méta-discours | Dans cet article, nous allons explorer, Plongeons dans, Décryptons | le contenu |
| Emphase | joue un rôle clé, témoigne de, s'inscrit dans une dynamique, pierre angulaire, au cœur de | ce qui s'est passé |
| Verbe d'apparat | permet de, s'avère, constitue, se positionne comme, afin de | est, a, le verbe direct, pour |
| Participe de remorque | …, permettant ainsi de ; …, garantissant ; ce qui témoigne de | une phrase avec un vrai sujet, ou rien |
| Adjectif valise | crucial, incontournable, véritable, robuste, innovant, fluide | rien, ou un fait |
| Jargon de consultant | levier, écosystème, enjeux, accompagner, déployer, solution, au sein de, au niveau de | le mot dit à voix haute |
| Faux contraste | Ce n'est pas X, c'est Y ; Plus qu'un X ; non seulement… mais aussi ; Au-delà de | affirme Y |
| Question de théâtre | Le résultat ? La clé ? Pourquoi est-ce important ? | la réponse |
| Connecteur vide | Par ailleurs, En outre, De plus, Ainsi, en tête de chaque paragraphe | garde ceux qui portent une cause, une opposition, une conséquence |
| Conclusion-résumé | En conclusion, En somme, Au final, L'avenir nous le dira | le dernier point utile |
| Publicité | Découvrez, Sublimez, Libérez le potentiel, Que vous soyez A ou B, niché au cœur de, allie X et Y, expérience unique | le prix, la distance, l'horaire, le verbe de l'action |
| Voix de marque | Nous sommes ravis, notre équipe passionnée, votre partenaire de confiance | ce que l'entreprise fait, pour qui |
| Faux savoir | Selon les experts, De nombreuses études montrent | la source, ou rien |
| Reste de chatbot | Bien sûr !, Excellente question !, N'hésitez pas à, Souhaitez-vous que je… | rien |
| Poncif littéraire | un instant suspendu, comme si le temps s'était figé, un silence vibrant | un détail observé |
| Mise en forme | émojis, gras partout, titres En Casse Anglaise, markdown dans un courriel | des phrases, casse de phrase |

## Calques de l'anglais

- adresser un problème : traiter. Impacter : affecter. Réaliser que : se rendre compte que. Opportunité : occasion. Supporter : soutenir, prendre en charge. Éventuellement (*eventually*) : finalement. Délivrer : livrer, fournir. Initier : lancer. À travers (*through*) : par, grâce à. Sur une base régulière : régulièrement. Faire du sens : avoir du sens.
- Évite la virgule systématique avant le « et » final d'une énumération. Garde-la si elle clarifie la phrase.
- Préfère l'actif quand l'acteur compte. Garde le passif si l'acteur est inconnu ou secondaire.
- « Il haussa les épaules », pas « ses épaules ».

## Typographie

- Guillemets « » avec une espace insécable à l'intérieur. Jamais de guillemets droits.
- Espace insécable (U+00A0, ou fine U+202F) avant `:` `;` `!` `?`. Ni espace ordinaire, ni absence d'espace.
- Pas de tiret cadratin ni demi-cadratin pour une incise, sauf dans un dialogue de fiction. Virgule, deux-points ou point.
- `1 000`, `3,5`, `10 %`, `20 €`, `14 h 30`, `1er`, `1re`, `2e` (jamais « 2ème »).
- Titres en casse de phrase. Accents sur les capitales (À, É). Jours, mois et langues en minuscule. `M.` et `Mme`, jamais « Mr ».
- « cœur », « œuvre », jamais « coeur ». « etc. » sans points de suspension. `…` en un seul signe.
- Écriture inclusive : suis le texte d'origine, n'en ajoute pas et n'en retire pas.

Dans la prose d'un message de commit, une espace ordinaire suffit. Le code reste intact. Pour le détail des nombres, dates, majuscules et apostrophes, consulte [typographie](references/typographie.md).

## Courrier

Le courrier français est formulaire. Garde la formule attendue, une fois, et coupe l'empilement. Ne retire pas la politesse attendue : un courrier trop sec passe pour impoli.

- Ouvre sur l'objet quand il n'y a pas de raison personnelle de commencer autrement. « Je vous écris au sujet de… » est poli. Garde une salutation chaleureuse ou une formule de relance si elle convient à la relation ou si l'utilisateur la demande.
- La formule finale reprend l'appel : « Madame la Directrice, » appelle « Je vous prie d'agréer, Madame la Directrice, l'expression de ma considération distinguée. »
- Une seule formule de politesse, pas « Restant à votre disposition… Dans l'attente de votre retour… Veuillez agréer… ».
- « Espérant une réponse rapide, je vous prie d'agréer… » : le sujet du participe est « je ». « Espérant…, veuillez agréer » est fautif.
- Dans un courriel, « Cordialement, » est neutre et « Bien cordialement, » plus chaleureux. Réserve la formule longue aux échanges dont le registre la justifie.
- Dans une lettre de motivation, utilise les faits fournis sur l'employeur et les réalisations du candidat. Chiffre une réalisation seulement si le chiffre est connu. Une réalisation concrète sans chiffre suffit ; ne réclame pas de données inutiles pour remplir un modèle.

## Exemple

Avant :

> Niché au cœur de la vallée, notre hôtel allie élégance et authenticité pour vous offrir une expérience unique. Que vous soyez en quête de détente ou d'aventure, notre équipe passionnée vous accompagne pour faire de votre séjour un moment magique.

Après (faits fournis par le client) :

> L'hôtel compte quatorze chambres, toutes tournées vers le lac. Le petit-déjeuner se prend sur la terrasse dès 7 h 30, et le sentier du tour du lac part à cent mètres de la porte.

## Avant de rendre

Relis à voix haute. Cherche ce qui sent encore la machine, et vérifie que tu n'as pas échangé un tic contre un autre.

Vérifie les espaces avant `:` `;` `!` `?` et à l'intérieur des guillemets. Si Python 3 est disponible, `python3 <chemin-du-skill>/scripts/check_spacing.py extrait.txt` signale les espaces ordinaires ou absentes. Utilise-le sur un extrait de prose seule en français de France, sans code, URL, citation verbatim ni heure numérique comme `13:52`. Ce contrôle ne remplace pas la relecture du document.

Pour une demande de rédaction, de traduction ou de réécriture, rends le texte seul, sauf commentaire demandé ou fait manquant à signaler. Pour une revue ou une explication, rends l'analyse demandée ; ne réécris pas le texte sans demande.
