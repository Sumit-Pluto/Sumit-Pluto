# GitHub Profile README — setup

This folder is your **GitHub profile README** (the special repo that shows on your
profile page). AI/robotic theme, modern stat cards, and a live **Pac-Man contribution
graph**.

## Files
```
README.md                     ← your profile page
assets/hero.gif               ← your GIF (already cropped + compressed)
.github/workflows/pacman.yml  ← generates the Pac-Man contribution graph
```

## 1. Create / use the special repo
Your repo is `github.com/Sumit-Pluto/Sumit-Pluto` (a repo whose name == your username is
the one GitHub renders on your profile). If it already exists, skip to step 2.

## 2. Push these files
```bash
cd github-profile
git add -A
git commit -m "profile refresh"
git push
```
(First time only: `git init && git branch -M main && git remote add origin
https://github.com/Sumit-Pluto/Sumit-Pluto.git && git push -u origin main --force`.)

## 3. Turn on the Pac-Man graph
The Pac-Man image is **blank until the Action runs once**:
1. Repo → **Actions** tab → enable workflows if prompted.
2. Open **Generate Pac-Man** → **Run workflow** (runs manually the first time; then it
   auto-refreshes twice a day).
3. It publishes `pacman-contribution-graph.svg` to an **`output`** branch, which the README
   already points at. Give it ~1 minute, then hard-refresh your profile.

> If it 404s: open the `output` branch and check the exact SVG filename, then match it in the
> README `src`. `abozanona/pacman-contribution-graph` is a community action — if it ever
> misbehaves, the bullet-proof fallback is the snake: swap the workflow to `Platane/snk` and
> point the image at `github-snake-dark.svg` (ask me and I'll switch it in one step).

## 4. Make it yours
- **GIF:** replace `assets/hero.gif` anytime (keep it < ~5 MB so GitHub autoplays it — if you
  drop in a big one, tell me and I'll crop/compress it like I did this one).
- **Portfolio link:** in README.md, replace `https://your-portfolio.vercel.app` with your URL.
- **CP numbers:** the `Wins` line in the `whoami` block is plain text — bump Codeforces/CodeChef
  as you climb.

## What's live vs static
| Live (auto-updates) | Static (edit by hand) |
|---|---|
| Profile views, followers, stars | Codeforces / CodeChef numbers (the `Wins` line) |
| GitHub summary cards + language cards | Portfolio URL |
| Streak card | The `whoami` code block |
| Pac-Man graph (via Action) | |

## Notes
- **Stats cards** now use `github-profile-summary-cards` (reliable) instead of the frequently
  rate-limited `github-readme-stats`.
- **A skill icon missing?** `skillicons.dev` just skips unknown keys — no broken image.

Your **portfolio repo** README also shows this same Pac-Man graph (it points at this repo's
`output` branch), so set this repo up first.
