# Jak wrzucić projekt na GitHuba - VS Code

## Krok 1: Przygotuj folder projektu
1. Stwórz nowy folder na swoim komputerze (np. `timer-app`)
2. Wrzuć tam wszystkie pobrane pliki:
   - timer_app.py
   - README.md
   - LICENSE
   - .gitignore

## Krok 2: Otwórz projekt w VS Code
1. Uruchom VS Code
2. File → Open Folder (lub Ctrl+K Ctrl+O)
3. Wybierz folder z projektem

## Krok 3: Zainstaluj Git (jeśli nie masz)

### Windows:
Pobierz z https://git-scm.com/download/win i zainstaluj

### macOS/Linux:
Otwórz terminal w VS Code (Ctrl+`) i wpisz:
```bash
git --version
```

Po instalacji **zrestartuj VS Code**.

## Krok 4: Skonfiguruj Git (tylko pierwszy raz)

W terminalu VS Code (Ctrl+` aby otworzyć) wpisz:
```bash
git config --global user.name "Twoje Imię"
git config --global user.email "twoj@email.com"
```

## Krok 5: Utwórz repozytorium na GitHubie
1. Wejdź na https://github.com i zaloguj się
2. Kliknij zielony przycisk **"New"** (lewy górny róg)
3. Nazwa: `timer-stopwatch-app` (lub inna)
4. Opis (opcjonalnie): `Simple timer and stopwatch desktop app`
5. **NIE zaznaczaj** "Add a README file" (już go mamy!)
6. Kliknij **"Create repository"**
7. **SKOPIUJ** adres który się pojawi (np. `https://github.com/username/timer-stopwatch-app.git`)

## Krok 6: Wrzuć kod na GitHuba przez VS Code

### Metoda 1: Graficzny interfejs (najłatwiejsza)

1. **Zainicjuj Git**
   - Kliknij ikonę "Source Control" po lewej (gałązka, trzecia ikona od góry)
   - Kliknij **"Initialize Repository"**

2. **Dodaj pliki**
   - Zobaczysz listę plików z literą "U" (Untracked)
   - Najedź na "Changes" i kliknij **"+"** (Stage All Changes)
   - Wszystkie pliki przejdą do sekcji "Staged Changes"

3. **Commit (zapisz zmiany)**
   - U góry w polu "Message" wpisz: `Initial commit`
   - Kliknij **"Commit"** (lub Ctrl+Enter)

4. **Połącz z GitHubem**
   - Kliknij trzy kropki **"..."** → **"Remote"** → **"Add Remote"**
   - Wklej adres z GitHuba (np. `https://github.com/username/timer-stopwatch-app.git`)
   - Nazwa: `origin` (zostaw domyślną)

5. **Wyślij na GitHuba (Push)**
   - Kliknij trzy kropki **"..."** → **"Push"**
   - VS Code może zapytać o logowanie - zaloguj się do GitHuba
   - Gotowe! 🎉

### Metoda 2: Terminal (dla zaawansowanych)

Otwórz terminal w VS Code (Ctrl+`) i wpisz:

```bash
# Zainicjuj Git
git init

# Dodaj wszystkie pliki
git add .

# Zapisz zmiany
git commit -m "Initial commit"

# Połącz z GitHubem (ZAMIEŃ na swój adres!)
git remote add origin https://github.com/username/timer-stopwatch-app.git

# Wyślij kod
git branch -M main
git push -u origin main
```

## Krok 7: Sprawdź na GitHubie
Odśwież stronę repozytorium na GitHub.com - Twój kod jest już tam! 🚀

## Aktualizowanie projektu w przyszłości

Gdy zmienisz coś w kodzie:

1. **Source Control** (ikona gałązki)
2. **Stage** zmiany (kliknij + przy plikach)
3. Wpisz opis zmian w "Message"
4. Kliknij **"Commit"**
5. Kliknij **"Sync Changes"** (lub trzy kropki → Push)

## Przydatne rozszerzenia VS Code

- **GitLens** - zaawansowane funkcje Git
- **GitHub Pull Requests** - integracja z GitHubem

Zainstaluj przez: Extensions (Ctrl+Shift+X) → wyszukaj nazwę → Install

## Problemy?

### "Git not found"
Zainstaluj Git i zrestartuj VS Code.

### "Authentication failed"
VS Code otworzy okno logowania do GitHuba - zaloguj się tam.

### "Permission denied"
Użyj Personal Access Token zamiast hasła:
1. GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Zaznacz `repo`
4. Użyj tego tokena jako hasła w VS Code

---

**Potrzebujesz pomocy?** Pisz! 😊
