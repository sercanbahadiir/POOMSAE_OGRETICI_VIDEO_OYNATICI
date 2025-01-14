import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
import sys

# Proje kök dizinini al
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Dizin yollarını göreli olarak tanımla
VIDEO_DIR = os.path.join(ROOT_DIR, "videos")
ICONS_DIR = os.path.join(ROOT_DIR, "icons")
NOTES_FILE = os.path.join(ROOT_DIR, "notes.txt")

# Puanlar ve videolar listesi
videos = [
    ("part_1.mp4", 1), ("part_2.mp4", 1), ("part_3.mp4", 2),
    ("part_4.mp4", 1), ("part_5.mp4", 1), ("part_6.mp4", 2),
    ("part_7.mp4", 5), ("part_8.mp4", 1), ("part_9.mp4", 5),
    ("part_10.mp4", 1), ("part_11.mp4", 1), ("part_12.mp4", 2),
    ("part_13.mp4", 1), ("part_14.mp4", 1), ("part_15.mp4", 2),
    ("part_16.mp4", 5), ("part_17.mp4", 1), ("part_18.mp4", 5),
    ("part_19.mp4", 1), ("part_20.mp4", 1), ("part_21.mp4", 2),
    ("part_22.mp4", 1), ("part_23.mp4", 1), ("part_24.mp4", 2),
    ("part_25.mp4", 5), ("part_26.mp4", 1), ("part_27.mp4", 1),
    ("part_28.mp4", 5), ("part_29.mp4", 6), ("part_30.mp4", 6),
    ("part_31.mp4", 10), ("part_32.mp4", 20)
]

class PoomsaeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poomsae Öğretici Video Oynatıcı-1.Poomsae")
        
        # Temel dizinlerin kontrolü ve oluşturulması
        self.check_directories()
        
        # Uygulama değişkenleri
        self.dark_mode = False
        self.current_video_index = 0
        self.total_score = 0
        self.max_score = sum(score for _, score in videos)
        self.video_width = 640
        self.video_height = 360
        
        # Tema değişkenleri
        self.style = ttk.Style()
        self.set_light_mode()
        self.notes_header_bg = "#F0F0F0"
        self.notes_header_fg = "#333333"
        self.notes_border_color = "#D3D3D3"
        self.notes_bg = "#FFFFFF"
        
        # UI oluşturma
        self.create_widgets()
        
        # Pencere olayları
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Escape>", self.exit_fullscreen)

    def check_directories(self):
        """Gerekli dizinlerin varlığını kontrol et ve oluştur"""
        directories = [VIDEO_DIR, ICONS_DIR, os.path.dirname(NOTES_FILE)]
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Oluşturulan dizin: {directory}")

    def set_light_mode(self):
        self.bg_color = "#FFFFFF"
        self.fg_color = "#000000"
        self.text_bg_color = "#F0F0F0"
        self.progress_fg_color = "#4CAF50"
        self.style.theme_use('clam')
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TButton", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TCheckbutton", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TProgressbar", background=self.progress_fg_color)

    def set_dark_mode(self):
        self.bg_color = "#333333"
        self.fg_color = "#FFFFFF"
        self.text_bg_color = "#444444"
        self.progress_fg_color = "#FFFFFF"
        self.style.theme_use('clam')
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TButton", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TCheckbutton", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TProgressbar", background=self.progress_fg_color)

    def create_widgets(self):
        # Ana çerçeve
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Video ve Notlar Çerçevesi
        self.video_notes_frame = ttk.Frame(self.main_frame)
        self.video_notes_frame.pack(fill=tk.BOTH, expand=True)

        # Video oynatıcı
        self.video_label = tk.Label(self.video_notes_frame, width=self.video_width, height=self.video_height, bg="#000000")
        self.video_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Notlar bölümü
        self.notes_frame = ttk.Frame(self.video_notes_frame)
        self.notes_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Notlar başlık çerçevesi
        self.notes_header_frame = ttk.Frame(self.notes_frame)
        self.notes_header_frame.pack(fill=tk.X, pady=(0, 10))

        self.notes_header = tk.Frame(
            self.notes_header_frame,
            bg=self.notes_header_bg,
            bd=1,
            relief="solid"
        )
        self.notes_header.pack(fill=tk.X, pady=(0, 5))

        self.notes_label = tk.Label(
            self.notes_header,
            text="📝 NOTLAR",
            font=("Helvetica", 14, "bold"),
            bg=self.notes_header_bg,
            fg=self.notes_header_fg,
            pady=8
        )
        self.notes_label.pack()

        # Not alanı çerçevesi
        self.notes_content_frame = tk.Frame(
            self.notes_frame,
            bd=1,
            relief="solid",
            bg=self.notes_border_color
        )
        self.notes_content_frame.pack(fill=tk.BOTH, expand=True)

        self.notes_text = tk.Text(
            self.notes_content_frame,
            font=("Helvetica", 12),
            wrap=tk.WORD,
            padx=10,
            pady=10,
            bg=self.notes_bg,
            fg=self.fg_color,
            relief="flat",
            height=20,
            width=30
        )
        self.notes_text.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        self.notes_scrollbar = ttk.Scrollbar(
            self.notes_content_frame,
            orient="vertical",
            command=self.notes_text.yview
        )
        self.notes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.notes_text.configure(yscrollcommand=self.notes_scrollbar.set)

        self.load_notes()

        # İlerleme çubuğu
        self.progress_frame = ttk.Frame(self.main_frame)
        self.progress_frame.pack(fill=tk.X, pady=(10, 0))

        self.progress = ttk.Progressbar(self.progress_frame, length=300, mode='determinate', style="TProgressbar")
        self.progress.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        self.progress_label = ttk.Label(self.progress_frame, text="0%", font=("Roboto Mono", 14))
        self.progress_label.pack(side=tk.LEFT, padx=10)

        self.parts_label = ttk.Label(self.progress_frame, text="0/32 🥋", font=("Roboto Mono", 14))
        self.parts_label.pack(side=tk.LEFT, padx=10)

        # Kontrol Butonları
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # İkonları yükleyin
        self.load_icons()

        # Butonlar
        self.speed_label = ttk.Label(self.button_frame, text="⚙ Oynatma Hızı:", font=("Inter", 14))
        self.speed_label.grid(row=0, column=0, pady=(10, 0))

        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_menu = ttk.Combobox(self.button_frame, textvariable=self.speed_var, values=[0.5, 1.0, 1.5, 2.0], font=("Inter", 14), state="readonly", width=5)
        self.speed_menu.grid(row=0, column=1, pady=(9, 0), padx=8)
        self.speed_menu.bind("<<ComboboxSelected>>", self.change_speed)

        self.reset_button = ttk.Button(self.button_frame, image=self.reset_icon, command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=8)

        self.back_button = ttk.Button(self.button_frame, image=self.back_icon, command=self.prev_video)
        self.back_button.grid(row=0, column=3, padx=8)

        self.pause_button = ttk.Button(self.button_frame, image=self.play_icon, command=self.pause_video)
        self.pause_button.grid(row=0, column=4, padx=8)

        self.next_button = ttk.Button(self.button_frame, image=self.next_icon, command=self.next_video)
        self.next_button.grid(row=0, column=5, padx=8)

        self.fullscreen_button = ttk.Button(self.button_frame, image=self.fullscreen_icon, command=self.toggle_fullscreen)
        self.fullscreen_button.grid(row=0, column=6, padx=8)

        self.dark_mode_button = ttk.Button(self.button_frame, text="☀🌙", command=self.toggle_dark_mode, style="TButton")
        self.dark_mode_button.grid(row=0, column=7, padx=8)

        self.cap = None
        self.paused = False
        self.fullscreen = False
        self.delay = 33  # Default delay for ~30 FPS video playback
        self.update_video()

    def load_icons(self):
        """İkonları yükleyin."""
        try:
            self.reset_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "reset.png"))
            self.back_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "back.png"))
            self.play_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "play.png"))
            self.pause_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "pause.png"))
            self.next_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "next.png"))
            self.fullscreen_icon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "fullscreen.png"))
        except Exception as e:
            messagebox.showerror("Hata", f"İkonlar yüklenirken hata oluştu: {str(e)}")
            sys.exit(1)

    def get_belt_color(self, index):
        if 0 <= index <= 5:
            return "#F3F3F3"
        elif 6 <= index <= 11:
            return "#FCFF3A"
        elif 12 <= index <= 17:
            return "#2cab0c"
        elif 18 <= index <= 23:
            return "#0c4bab"
        elif 24 <= index <= 29:
            return "#ab0c0c"
        else:
            return "#000000"

    def update_progress_bar_color(self):
        belt_color = self.get_belt_color(self.current_video_index)
        style_name = f"{belt_color}.Horizontal.TProgressbar"

        # Yeni bir stil oluşturun ve ilerleme çubuğuna uygulayın
        self.style.configure(style_name, troughcolor=self.bg_color, background=belt_color)
        self.progress.configure(style=style_name)

    def update_video(self):
        if self.cap:
            self.cap.release()  # Önceki videonun bellekteki yerini serbest bırak
        video, score = videos[self.current_video_index]
        video_path = os.path.join(VIDEO_DIR, video)

        if not os.path.exists(video_path):
            messagebox.showerror("Hata", f"Video dosyası bulunamadı: {video_path}")
            return

        self.cap = cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # Video önbellek boyutunu artırma

        if not self.cap.isOpened():
            messagebox.showerror("Hata", f"Video yüklenemedi: {video_path}")
            return

        self.play_video()
        progress_percentage = (self.total_score / self.max_score) * 100
        self.progress['value'] = progress_percentage
        self.progress_label.config(text=f"{progress_percentage:.2f}%")
        self.parts_label.config(text=f"{self.current_video_index + 1}/32 🥋")
        self.update_progress_bar_color()

    def resize_frame(self, frame, target_width, target_height):
        (h, w) = frame.shape[:2]
        if h > target_height or w > target_width:
            if w > h:
                target_height = int(h * (target_width / w))
            else:
                target_width = int(w * (target_height / h))
        return cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_AREA)

    def play_video(self):
        if self.paused:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.resize_frame(frame, self.video_width, self.video_height)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

            self.delay = int(1000 / (30 * self.speed_var.get()))
            self.root.after(self.delay, self.play_video)
        else:
            self.cap.release()
            self.back_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.fullscreen_button.config(state=tk.NORMAL)

    def pause_video(self):
        self.paused = not self.paused
        self.pause_button.config(image=self.play_icon if self.paused else self.pause_icon)
        if not self.paused:
            self.play_video()

    def next_video(self):
        if self.current_video_index < len(videos) - 1:
            self.total_score += videos[self.current_video_index][1]
            self.current_video_index += 1
            self.update_video()
        else:
            messagebox.showinfo("Tebrikler!", "1. Poomsayi Öğrendiniz! Tebrikler!🥋")

    def prev_video(self):
        if self.current_video_index > 0:
            self.total_score -= videos[self.current_video_index - 1][1]
            self.current_video_index -= 1
            self.update_video()

    def reset(self):
        self.current_video_index = 0
        self.total_score = 0
        self.update_video()

    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r", encoding="utf-8") as file:
                notes = file.read()
                self.notes_text.insert(tk.END, notes)

    def save_notes(self):
        with open(NOTES_FILE, "w", encoding="utf-8") as file:
            notes = self.notes_text.get(1.0, tk.END)
            file.write(notes)

    def on_closing(self):
        self.save_notes()
        self.root.destroy()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.video_width = 1280
            self.video_height = 720
            self.root.attributes("-fullscreen", True)
        else:
            self.video_width = 640
            self.video_height = 360
            self.root.attributes("-fullscreen", False)
        self.update_video_label_size()

    def exit_fullscreen(self, event):
        if self.fullscreen:
            self.toggle_fullscreen()

    def update_video_label_size(self):
        self.video_label.config(width=self.video_width, height=self.video_height)

    def change_speed(self, event):
        self.delay = int(1000 / (30 * self.speed_var.get()))
        if not self.paused:
            self.play_video()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.set_dark_mode()
            self.notes_header_bg = "#404040"
            self.notes_header_fg = "#FFFFFF"
            self.notes_border_color = "#555555"
            self.notes_bg = "#333333"
        else:
            self.set_light_mode()
            self.notes_header_bg = "#F0F0F0"
            self.notes_header_fg = "#333333"
            self.notes_border_color = "#D3D3D3"
            self.notes_bg = "#FFFFFF"
            
        self.update_theme()
        self.update_notes_theme()

    def update_theme(self):
        self.root.config(bg=self.bg_color)
        self.main_frame.config(style="TFrame")
        self.video_notes_frame.config(style="TFrame")
        self.notes_frame.config(style="TFrame")
        self.progress_frame.config(style="TFrame")
        self.button_frame.config(style="TFrame")
        self.notes_label.config(style="TLabel")
        self.notes_text.config(bg=self.text_bg_color, fg=self.fg_color)
        self.progress_label.config(style="TLabel")
        self.parts_label.config(style="TLabel")
        self.speed_label.config(style="TLabel")
        self.dark_mode_button.config(style="TButton")

    def update_notes_theme(self):
        self.notes_header.configure(bg=self.notes_header_bg)
        self.notes_label.configure(bg=self.notes_header_bg, fg=self.notes_header_fg)
        self.notes_content_frame.configure(bg=self.notes_border_color)
        self.notes_text.configure(
            bg=self.notes_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PoomsaeApp(root)
    root.mainloop()