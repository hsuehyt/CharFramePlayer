from PIL import Image, ImageDraw, ImageFont
import os

# === Auto-detect script's folder ===
base_dir = os.path.dirname(os.path.abspath(__file__))
characters_txt_path = os.path.join(base_dir, "characters.txt")
subtitle_path = os.path.join(base_dir, "characters_subtitles.txt")
output_path = os.path.join(base_dir, "character_loop.gif")
font_path = "C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NotoSansCJKtc-Bold.otf"  # Adjust if needed

font_size = 800
frame_size = (1080, 1080)
duration_per_frame = 200  # in milliseconds

# === Function to parse characters.txt ===
def expand_characters(filepath):
    characters = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#empty"):
                characters.append("§EMPTY§")
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

# === Function to parse subtitles ===
def parse_subtitles(filepath):
    subtitles = {}
    with open(filepath, "r", encoding="utf-8") as f:
        in_subtitle_section = False
        for line in f:
            line = line.strip()
            if line.lower().startswith("subtitle"):
                in_subtitle_section = True
                continue
            if in_subtitle_section and ":" in line:
                char, text = line.split(":", 1)
                subtitles[char.strip()] = text.strip()
    return subtitles

# === Load characters and subtitles ===
characters = expand_characters(characters_txt_path)
char_subtitles = parse_subtitles(subtitle_path)

# === Generate frames ===
frames = []
for char in characters:
    img = Image.new("RGB", frame_size, color="black")
    if char != "§EMPTY§":
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)

        # Draw main character
        bbox = font.getbbox(char)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = (
            (frame_size[0] - w) // 2 - bbox[0],
            (frame_size[1] - h) // 2 - bbox[1] - 100  # shift up slightly for subtitle
        )
        draw.text(position, char, font=font, fill="white")

        # Draw subtitle if available
        subtitle = char_subtitles.get(char)
        if subtitle:
            subtitle_font_size = 64
            subtitle_font = ImageFont.truetype(font_path, subtitle_font_size)
            sw, sh = subtitle_font.getsize(subtitle)
            subtitle_position = (
                (frame_size[0] - sw) // 2,
                frame_size[1] - sh - 50  # 50px from bottom
            )
            draw.text(subtitle_position, subtitle, font=subtitle_font, fill="lightgray")

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
