# Jak wrzucić projekt na GitHuba - Instrukcja

## Krok 1: Przygotuj pliki
Upewnij się, że masz wszystkie pliki w jednym folderze:
- timer_app.py (główny program)
- README.md (opis projektu)
- LICENSE (licencja)
- .gitignore (ignorowane pliki)

## Krok 2: Zainstaluj Git (jeśli jeszcze nie masz)

### Windows:
1. Pobierz Git z: https://git-scm.com/download/win
2. Zainstaluj z domyślnymi ustawieniami
3. Otwórz "Git Bash" lub Command Prompt

### macOS:
Otwórz Terminal i wpisz:
```bash
git --version
```
Jeśli nie masz Gita, system zapyta czy chcesz go zainstalować.

### Linux:
```bash
sudo apt-get install git
```

## Krok 3: Skonfiguruj Git (tylko pierwszy raz)
Otwórz terminal/cmd i wpisz:
```bash
git config --global user.name "Twoje Imię"
git config --global user.email "twoj@email.com"
```

## Krok 4: Utwórz repozytorium na GitHubie
1. Wejdź na https://github.com
2. Zaloguj się (lub załóż konto jeśli nie masz)
3. Kliknij zielony przycisk "New" (nowe repozytorium)
4. Nazwij projekt np. "timer-stopwatch-app"
5. Możesz dodać opis: "Simple timer and stopwatch desktop app"
6. NIE zaznaczaj "Initialize with README" (już go mamy!)
7. Kliknij "Create repository"

## Krok 5: Wrzuć kod na GitHuba

Otwórz terminal/cmd, przejdź do folderu z projektem i wykonaj:

```bash
# Przejdź do folderu z projektem
cd ścieżka/do/twojego/folderu

# Zainicjuj repozytorium Git
git init

# Dodaj wszystkie pliki
git add .

# Zapisz zmiany (commit)
git commit -m "Initial commit - Timer and Stopwatch app"

# Połącz z GitHubem (ZAMIEŃ "username" i "repo-name" na swoje!)
git remote add origin https://github.com/username/timer-stopwatch-app.git

# Wyślij kod na GitHuba
git branch -M main
git push -u origin main
```

## Krok 6: Gotowe! 🎉

Twój projekt jest teraz na GitHubie!
Odśwież stronę repozytorium na GitHub.com i zobaczysz swoje pliki.

## Przydatne komendy na przyszłość

Gdy będziesz chciał zaktualizować projekt:
```bash
git add .
git commit -m "Opis zmian"
git push
```

## Problemy?

### "Permission denied"
Musisz skonfigurować klucz SSH lub użyć Personal Access Token.
Zobacz: https://docs.github.com/en/authentication

### "Repository not found"
Sprawdź czy adres repozytorium jest poprawny:
```bash
git remote -v
```

Możesz zmienić adres:
```bash
git remote set-url origin https://github.com/POPRAWNY-USERNAME/POPRAWNA-NAZWA.git
```
