from flask import Flask, request, render_template, url_for, redirect
import os
from PIL import Image
import io

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['STATIC_FOLDER'] = 'static/'

# Ensure upload and static directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['STATIC_FOLDER'], exist_ok=True)

# Split the frame into tiles
def split_frame(frame_image, n_rows, n_cols):
    width, height = frame_image.size
    tile_width = width // n_cols
    tile_height = height // n_rows
    tiles = []

    for row in range(n_rows):
        for col in range(n_cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height
            box = (left, upper, right, lower)
            tile = frame_image.crop(box)
            tiles.append(tile)

    return tiles

# Process the GIF file
def process_gif(file_path, n_rows, n_cols):
    gif = Image.open(file_path)
    frames = []
    durations = []
    try:
        while True:
            frame = gif.copy()
            frames.append(frame)
            durations.append(gif.info.get('duration', 100))
            gif.seek(len(frames))
    except EOFError:
        pass

    duration = durations[0] if durations else 100

    grid_frames = [[] for _ in range(n_rows * n_cols)]
    for frame in frames:
        tiles = split_frame(frame, n_rows, n_cols)
        for idx, tile in enumerate(tiles):
            grid_frames[idx].append(tile)

    output_files = []
    for idx, frame_list in enumerate(grid_frames):
        output_filename = f'output_{idx}.gif'
        output_path = os.path.join(app.config['STATIC_FOLDER'], output_filename)
        frame_list[0].save(output_path, save_all=True, append_images=frame_list[1:], duration=duration, loop=0)
        output_files.append(output_filename)

    return output_files, gif.size

# Upload the GIF file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        n_rows = int(request.form['rows'])
        n_cols = int(request.form['cols'])
        file = request.files['gif']
        if file and file.filename.endswith('.gif'):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            output_files, original_size = process_gif(file_path, n_rows, n_cols)
            
            return render_template(
                'display.html',
                files=output_files,
                n_cols=n_cols,
                original_width=original_size[0],
                original_height=original_size[1]
            )
        else:
            return "Please upload a valid GIF file."
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)