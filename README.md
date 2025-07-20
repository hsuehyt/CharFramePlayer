# CharFramePlayer

**CharFramePlayer** is a Python tool that generates animated GIFs from sequences of characters — such as Chinese Hanzi, Japanese Kana, Arabic, emojis, or any other Unicode text — with support for frame looping, ping-pong animation, and user-defined empty frames between sections.

Ideal for:
- Experimental typography
- Language visualization
- Motion graphics
- Character animation studies

---

## ✨ Features

- ✅ Reads character sequences from a text file (`characters.txt`)
- 🔁 Supports `loopxN:` and `pingpongxN:` playback modes
- 🕳️ Add empty (blank) frames with `#empty` markers
- 🌐 Unicode-friendly: works with multiple languages and symbols
- 🖋️ Custom font support via `NotoSans` or any `.ttf/.otf` file

---

## 📁 File Structure

```bash
CharFramePlayer/
│
├── CharFramePlayer.py      # Main animation script
├── characters.txt          # Defines the character sequences and modes
├── output.gif              # Generated animated GIF (output)
└── /fonts/                 # Optional: font files like NotoSansCJK, NotoSansArabic, etc.
````

---

## 📄 `characters.txt` Format

Use `loopxN:` or `pingpongxN:` followed by characters to animate. Use `#empty` to insert a blank frame.

```txt
loopx3: ABC
pingpongx2: 甲乙丙
#empty
loopx2: 😀😂😎
```

---

## ▶️ How to Use

1. Install [Pillow](https://pillow.readthedocs.io/en/stable/):

   ```bash
   pip install pillow
   ```

2. Place your characters in `characters.txt`.

3. Run the script:

   ```bash
   python CharFramePlayer.py
   ```

4. The output will be saved as `character_loop.gif`.

---

## 🎨 Font Support

Edit the `font_path` in the script to use a font that supports your characters:

```python
font_path = "NotoSans-Regular.ttf"
```

You can download multilingual fonts from the [Noto Fonts Project](https://www.google.com/get/noto/).

---

## 🪪 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

## ❤️ Credits

Created by \Yuting Hsueh.
