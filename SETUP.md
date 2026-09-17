# GitHub Profile README — setup

This folder is your **GitHub profile README** (the special repo that shows on your
profile page). AI/robotic theme, live stats, no trophies, a green **contribution
heatmap**, and a live **contribution snake** animation.

## Files
```
README.md                    ← your profile page
assets/hero.gif              ← starter GIF (replace with your own)
.github/workflows/snake.yml  ← generates the contribution-snake animation
```

## 1. Create the special repo
Create a **new public repo named EXACTLY your username**: `Sumit-Pluto`
(github.com/new → Repository name: `Sumit-Pluto` → Public → Create).
> A repo whose name matches your username is the one GitHub renders on your profile.

## 2. Push these files
```bash
cd github-profile
git init && git add . && git commit -m "profile readme"
git branch -M main
git remote add origin https://github.com/Sumit-Pluto/Sumit-Pluto.git
git push -u origin main
```

## 3. Turn on the snake animation
The snake image is **blank until the Action runs once**:
1. Repo → **Actions** tab → enable workflows if prompted.
2. Open **Generate Snake** → **Run workflow** (runs manually the first time; then it
   auto-refreshes twice a day).
3. It publishes `github-snake-dark.svg` to an **`output`** branch, which the README
   already points at. Give it ~1 minute, then hard-refresh your profile.

> The green **contribution heatmap** (ghchart) shows immediately — it needs no Action.

### Want the actual Pac-Man sprite (with ghosts) instead of the snake?
It's a community action that's finicky (it's why the earlier Pac-Man image was blank).
`snake.yml` has a ready-to-swap Pac-Man job commented at the bottom — paste it in, then
point the README image at `.../output/pacman-contribution-graph.svg`. The snake is the
bulletproof default; use Pac-Man only if you're happy to babysit the Action.

## 4. Make it yours (2 min)
- **Swap the GIF:** drop your own into `assets/hero.gif` (robot / AI / coding loop).
- **Portfolio link:** in README.md, replace `https://your-portfolio.vercel.app` with your
  deployed portfolio URL.
- **CP numbers:** the Codeforces/CodeChef/LeetCode badges are static — bump the numbers in
  README.md as you climb (the GitHub stats + streak + heatmap are live).
- Optional: add Twitter/X, Discord, etc. badges in **Connect** (copy the shields.io pattern).

## What's live vs static
| Live (auto-updates) | Static (edit by hand) |
|---|---|
| Profile views, followers, stars | Codeforces / CodeChef / LeetCode **badge numbers** |
| GitHub stats, top languages, streak | Portfolio URL |
| Contribution heatmap (ghchart) | The `whoami` code block |
| Contribution snake (via Action) | |

## Troubleshooting
- **Snake image blank?** It only exists after the **Generate Snake** Action runs once
  (Actions → Run workflow). Confirm the `output` branch has `github-snake-dark.svg`.
- **Stats card blank sometimes?** The shared `github-readme-stats` instance gets rate-limited
  (HTTP 503) under load — transient, and GitHub caches a good render. To be bulletproof,
  self-host `anuraghazra/github-readme-stats` on your own Vercel and point the URLs at it.
- **A skill icon missing?** `skillicons.dev` just skips unknown keys — no broken image.

Your **portfolio repo** README also shows this same snake (it points at this repo's
`output` branch), so set this repo up first.
