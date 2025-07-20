from PIL import Image, ImageDraw, ImageFont
import os

# === Auto-detect script's folder ===
base_dir = os.path.dirname(os.path.abspath(__file__))
characters_txt_path = os.path.join(base_dir, "characters.txt")
output_path = os.path.join(base_dir, "character_loop.gif")
font_path = "C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NotoSansCJKtc-Bold.otf"  # Adjust path if needed

font_size = 180
frame_size = (256, 256)
duration_per_frame = 200  # in milliseconds

# === Function to parse characters.txt ===
def expand_characters(filepath):
    characters = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#empty"):  # Now using lowercase
                characters.append("§EMPTY§")  # Internal marker for empty frame
                continue
            if ":" not in line:
                continue
            mode, seq = line.split(":", 1)
            mode = mode.strip().lower()
            seq = list(seq.strip())
            if "pingpongx" in mode:
                count = int(mode.replace("pingpongx", ""))
                pingpong = seq + seq[-2:0:-1]
                characters.extend(pingpong * count)
            elif "loopx" in mode:
                count = int(mode.replace("loopx", ""))
                characters.extend(seq * count)
    return characters

# === Read characters from file ===
characters = expand_characters(characters_txt_path)

# === Generate animation frames ===
frames = []
for char in characters:
    img = Image.new("RGB", frame_size, color="black")
    if char != "§EMPTY§":
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        bbox = font.getbbox(char)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = (
            (frame_size[0] - w) // 2 - bbox[0],
            (frame_size[1] - h) // 2 - bbox[1]
        )
        draw.text(position, char, font=font, fill="white")
    frames.append(img)

# === Save animated GIF ===
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:] + frames,
    duration=duration_per_frame,
    loop=0
)

print(f"✅ Animation saved as: {output_path}")
