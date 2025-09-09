# Accessibility

## Description
Ce projet se concentre sur l'implémentation des meilleures pratiques d'accessibilité web pour garantir que les sites web soient utilisables par tous, y compris les personnes en situation de handicap. Il couvre les techniques essentielles pour améliorer l'accessibilité selon les standards WCAG (Web Content Accessibility Guidelines).

## Objectifs d'apprentissage
À la fin de ce projet, vous serez capable de :

- Comprendre et appliquer les directives WCAG (Web Content Accessibility Guidelines)
- Implémenter une structure HTML sémantique appropriée
- Utiliser correctement les attributs ARIA (Accessible Rich Internet Applications)
- Créer des skip links pour faciliter la navigation au clavier
- Assurer une navigation complète au clavier
- Optimiser le contraste des couleurs et la lisibilité
- Rendre les formulaires et les médias accessibles
- Corriger les problèmes d'accessibilité courants

## Structure du projet

### 📁 Fichiers principaux
- `00-index.html` - Page HTML de base avec structure Techium
- `00-styles.css` - Feuilles de style CSS principales

### 📁 fix-a11y/
Exercices de correction des problèmes d'accessibilité :
- `01-index.html` - Correction de la structure sémantique HTML
- `02-index.html` - Amélioration des attributs alt et ARIA
- `03-index.html` - Optimisation de la navigation au clavier
- `04-index.html` - Correction complète d'accessibilité

### 📁 skip-links/
Implémentation des liens de navigation rapide :
- `01-index.html` - Page avec skip links intégrés
- `01-article.html` - Article avec navigation optimisée
- `01-styles.css` - Styles pour les skip links

### 📁 keyboard/
Navigation au clavier et focus management :
- `01-index.html` - Page avec navigation au clavier améliorée
- `01-styles.css` - Styles pour les états de focus

### 📁 images/
Ressources visuelles du projet incluant logos et images décoratives

## Technologies utilisées
- **HTML5** - Structure sémantique
- **CSS3** - Styles et animations accessibles
- **ARIA** - Attributs d'accessibilité
- **WCAG 2.1** - Standards d'accessibilité

## Fonctionnalités d'accessibilité implémentées

### ✅ Navigation
- Skip links pour accéder rapidement au contenu principal
- Navigation complète au clavier (Tab, Shift+Tab, Enter, Escape)
- Indicateurs de focus visibles et personnalisés
- Menu hamburger accessible

### ✅ Contenu
- Hiérarchie des titres logique (h1-h6)
- Texte alternatif pour toutes les images informatives
- Contraste de couleurs conforme (ratio minimum 4.5:1)
- Tailles de police lisibles et redimensionnables

### ✅ Formulaires
- Labels associés à tous les champs
- Messages d'erreur descriptifs
- Groupement logique des éléments connexes
- Instructions claires pour la saisie

### ✅ ARIA
- Rôles ARIA appropriés
- États et propriétés ARIA dynamiques
- Live regions pour les mises à jour de contenu
- Landmarks pour la structure de page

## Comment tester l'accessibilité

### Outils recommandés
1. **Lecteurs d'écran**
   - NVDA (Windows)
   - JAWS (Windows)
   - VoiceOver (macOS/iOS)
   - TalkBack (Android)

2. **Extensions navigateur**
   - axe DevTools
   - WAVE (WebAIM)
   - Lighthouse (Chrome DevTools)

3. **Tests manuels**
   - Navigation au clavier uniquement
   - Zoom jusqu'à 200%
   - Désactivation des CSS
   - Test de contraste des couleurs

## Installation et utilisation

1. Cloner le repository :
```bash
git clone https://github.com/holbertonschool/holbertonschool-web_front_end.git
cd holbertonschool-web_front_end/accessibility
```

2. Ouvrir les fichiers HTML dans un navigateur :
```bash
open 00-index.html
```

3. Tester l'accessibilité :
   - Utiliser Tab pour naviguer
   - Activer un lecteur d'écran
   - Vérifier avec les outils d'audit

## Bonnes pratiques appliquées

- **Progressive Enhancement** : Fonctionnalité de base accessible sans JavaScript
- **Mobile First** : Design responsive et accessible sur tous les appareils
- **Semantic HTML** : Utilisation des éléments HTML appropriés
- **Color Independence** : Information non véhiculée uniquement par la couleur
- **Keyboard Navigation** : Toutes les fonctionnalités accessibles au clavier
- **Screen Reader Friendly** : Contenu compréhensible avec lecteur d'écran

## Ressources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices-1.1/)
- [WebAIM Resources](https://webaim.org/resources/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)

## Auteur
Projet réalisé dans le cadre du cursus Holberton School

## License
© 2024 Holberton School. Tous droits réservés.