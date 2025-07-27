# 🟫 Simple Minecraft

**Simple Minecraft** is a terminal-based Python mini-game inspired by Minecraft, where players can place blocks, navigate a grid, and break obstacles using a simplified mechanics system.

---

## 🧱 Features

* Place blocks: Grass, Stone, and Iron
* Durability system:

  * Grass: 1 hit
  * Stone: 2 hits
  * Iron: 5 hits
  * Bedrock: Unbreakable (used internally)
* Prevent movement through solid blocks
* Map wraps around (moving off one edge brings you to the opposite side)
* ASCII-styled map with block symbols and player avatar

---

## 🕹️ Controls

* `w` – Move up
* `a` – Move left
* `s` – Move down
* `d` – Move right
* `b` – Break a block in a chosen direction
* Input `n` when finished placing blocks

---

## 🧰 Technologies

* Python 3 (no external dependencies)

---

## 🚀 How to Run

1. Clone or download the repo:

   ```bash
   git clone https://github.com/your-username/simple-minecraft.git
   cd simple-minecraft
   ```

2. Run the game:

   ```bash
   python simple_minecraft.py
   ```

---

## 📸 Sample Gameplay

```
Please choose the block you want to place in map:
1. Grass
2. Stone
3. Iron
> 2

please enter row and column you want to place:
> 2 2

Do you want to continue to place block? (y/n)
> n

please enter player position:
> 1 1

Please input direction (w/a/s/d/b):
> s
Move down

Please input direction (w/a/s/d/b):
> b
Please input break direction (w/a/s/d):
> s
```

---

## 👤 Author

GitHub: [@Justin-113](https://github.com/Justin-113)

---

## 📄 License

MIT License