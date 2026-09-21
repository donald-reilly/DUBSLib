
import tkinter as tk
from tkinter import ttk, filedialog
import os
import time

class MiniDesktopApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Mini Desktop")
        self.geometry("1000x650")

        self._build_ui()
        self._populate_files(os.getcwd())
        self._tick_clock()

    def __str__(self):
        return f"{self.__class__.__name__}"
    # ---------------- UI ----------------
    def _build_ui(self):
        self.status = tk.StringVar(value="Ready")

        # Top-level layout
        self.paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # LEFT: file browser
        self.left_frame = ttk.Frame(self.paned)
        self.paned.add(self.left_frame, weight=1)

        self.path_label = ttk.Label(self.left_frame, text="Files")
        self.path_label.pack(anchor="w")

        self.file_list = tk.Listbox(self.left_frame)
        self.file_list.pack(fill=tk.BOTH, expand=True)
        self.file_list.bind("<Double-Button-1>", self._on_file_open)

        btn_frame = ttk.Frame(self.left_frame)
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame, text="Open Folder", command=self._open_folder).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="Refresh", command=self._refresh).pack(side=tk.LEFT)

        # RIGHT: tabs
        self.right = ttk.Notebook(self.paned)
        self.paned.add(self.right, weight=3)

        # --- Editor tab ---
        self.editor_tab = ttk.Frame(self.right)
        self.right.add(self.editor_tab, text="Notes")

        self.text = tk.Text(self.editor_tab, wrap="word")
        self.text.pack(fill=tk.BOTH, expand=True)

        editor_btns = ttk.Frame(self.editor_tab)
        editor_btns.pack(fill=tk.X)

        ttk.Button(editor_btns, text="Save", command=self._save_file).pack(side=tk.LEFT)
        ttk.Button(editor_btns, text="Load", command=self._load_file).pack(side=tk.LEFT)
        ttk.Button(editor_btns, text="Clear", command=lambda: self.text.delete("1.0", tk.END)).pack(side=tk.LEFT)

        # --- Canvas tab ---
        self.canvas_tab = ttk.Frame(self.right)
        self.right.add(self.canvas_tab, text="Canvas")

        self.canvas = tk.Canvas(self.canvas_tab, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self._draw)

        ttk.Button(self.canvas_tab, text="Clear Canvas", command=self.canvas.delete).pack()

        # --- Log tab ---
        self.log_tab = ttk.Frame(self.right)
        self.right.add(self.log_tab, text="Log")

        self.log = tk.Text(self.log_tab, bg="#111", fg="#0f0")
        self.log.pack(fill=tk.BOTH, expand=True)

        # STATUS BAR
        self.status_bar = ttk.Frame(self)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        self.status_label = ttk.Label(self.status_bar, textvariable=self.status)
        self.status_label.pack(side=tk.LEFT)

        self.clock = ttk.Label(self.status_bar, text="")
        self.clock.pack(side=tk.RIGHT)

    # ---------------- FILE BROWSER ----------------
    def _populate_files(self, path):
        self.current_path = path
        self.file_list.delete(0, tk.END)

        self.path_label.config(text=f"Files: {path}")

        try:
            for item in os.listdir(path):
                self.file_list.insert(tk.END, item)
        except Exception as e:
            self._log(str(e))

    def _open_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self._populate_files(folder)
            self.status.set(f"Opened {folder}")

    def _refresh(self):
        self._populate_files(self.current_path)
        self.status.set("Refreshed")

    def _on_file_open(self, event):
        selection = self.file_list.curselection()
        if not selection:
            return

        name = self.file_list.get(selection[0])
        full = os.path.join(self.current_path, name)

        if os.path.isfile(full):
            try:
                with open(full, "r", encoding="utf-8") as f:
                    self.text.delete("1.0", tk.END)
                    self.text.insert(tk.END, f.read())
                self.status.set(f"Loaded {name}")
            except Exception as e:
                self._log(f"Error opening file: {e}")

    # ---------------- EDITOR ----------------
    def _save_file(self):
        path = filedialog.asksaveasfilename()
        if not path:
            return

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))
            self.status.set("Saved file")
            self._log(f"Saved {path}")
        except Exception as e:
            self._log(str(e))

    def _load_file(self):
        path = filedialog.askopenfilename()
        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())
            self.status.set("Loaded file")
        except Exception as e:
            self._log(str(e))

    # ---------------- CANVAS ----------------
    def _draw(self, event):
        x, y = event.x, event.y
        r = 2
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")

    # ---------------- LOGGING ----------------
    def _log(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)

    # ---------------- CLOCK ----------------
    def _tick_clock(self):
        self.clock.config(text=time.strftime("%H:%M:%S"))
        self.after(1000, self._tick_clock)
