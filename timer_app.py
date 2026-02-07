import tkinter as tk
from tkinter import font
import time
from threading import Thread

class TimerStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Minutnik i Stoper")
        self.root.geometry("450x400")
        self.root.configure(bg='#f5f5f5')
        
        # Zmienne dla minutnika
        self.timer_seconds = 0
        self.timer_running = False
        
        # Zmienne dla stopera
        self.stopwatch_seconds = 0
        self.stopwatch_running = False
        
        # Aktywny tryb
        self.current_mode = "timer"
        
        self.create_widgets()
        
    def create_widgets(self):
        # Nagłówek
        header = tk.Frame(self.root, bg='#f5f5f5')
        header.pack(pady=20)
        
        # Przyciski wyboru trybu
        self.btn_timer = tk.Button(
            header,
            text="MINUTNIK",
            command=self.show_timer,
            font=('Arial', 14, 'bold'),
            bg='#2196F3',
            fg='white',
            width=15,
            height=2,
            relief=tk.RAISED,
            bd=3
        )
        self.btn_timer.pack(side=tk.LEFT, padx=10)
        
        self.btn_stopwatch = tk.Button(
            header,
            text="STOPER",
            command=self.show_stopwatch,
            font=('Arial', 14, 'bold'),
            bg='#e0e0e0',
            fg='#333',
            width=15,
            height=2,
            relief=tk.FLAT,
            bd=3
        )
        self.btn_stopwatch.pack(side=tk.LEFT, padx=10)
        
        # ===== SEKCJA MINUTNIKA =====
        self.timer_frame = tk.Frame(self.root, bg='#f5f5f5')
        
        # Ustawienia minutnika
        settings_frame = tk.Frame(self.timer_frame, bg='#f5f5f5')
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Minuty:", font=('Arial', 12), bg='#f5f5f5').grid(row=0, column=0, padx=5)
        self.timer_min_entry = tk.Spinbox(settings_frame, from_=0, to=99, width=5, font=('Arial', 18, 'bold'))
        self.timer_min_entry.delete(0, tk.END)
        self.timer_min_entry.insert(0, "5")
        self.timer_min_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(settings_frame, text="Sekundy:", font=('Arial', 12), bg='#f5f5f5').grid(row=0, column=2, padx=5)
        self.timer_sec_entry = tk.Spinbox(settings_frame, from_=0, to=59, width=5, font=('Arial', 18, 'bold'))
        self.timer_sec_entry.delete(0, tk.END)
        self.timer_sec_entry.insert(0, "0")
        self.timer_sec_entry.grid(row=0, column=3, padx=5)
        
        # Wyświetlacz minutnika
        self.timer_display = tk.Label(
            self.timer_frame,
            text="05:00",
            font=('Courier', 60, 'bold'),
            bg='#f5f5f5',
            fg='#2196F3'
        )
        self.timer_display.pack(pady=30)
        
        # Przyciski minutnika
        timer_buttons = tk.Frame(self.timer_frame, bg='#f5f5f5')
        timer_buttons.pack(pady=20)
        
        self.timer_start_btn = tk.Button(
            timer_buttons,
            text="START",
            command=self.start_pause_timer,
            font=('Arial', 16, 'bold'),
            bg='#4CAF50',
            fg='white',
            width=10,
            height=2
        )
        self.timer_start_btn.grid(row=0, column=0, padx=10)
        
        self.timer_reset_btn = tk.Button(
            timer_buttons,
            text="RESET",
            command=self.reset_timer,
            font=('Arial', 16, 'bold'),
            bg='#f44336',
            fg='white',
            width=10,
            height=2
        )
        self.timer_reset_btn.grid(row=0, column=1, padx=10)
        
        # ===== SEKCJA STOPERA =====
        self.stopwatch_frame = tk.Frame(self.root, bg='#f5f5f5')
        
        # Wyświetlacz stopera
        self.stopwatch_display = tk.Label(
            self.stopwatch_frame,
            text="00:00:00",
            font=('Courier', 60, 'bold'),
            bg='#f5f5f5',
            fg='#2196F3'
        )
        self.stopwatch_display.pack(pady=60)
        
        # Przyciski stopera
        stopwatch_buttons = tk.Frame(self.stopwatch_frame, bg='#f5f5f5')
        stopwatch_buttons.pack(pady=20)
        
        self.stopwatch_start_btn = tk.Button(
            stopwatch_buttons,
            text="START",
            command=self.start_pause_stopwatch,
            font=('Arial', 16, 'bold'),
            bg='#4CAF50',
            fg='white',
            width=10,
            height=2
        )
        self.stopwatch_start_btn.grid(row=0, column=0, padx=10)
        
        self.stopwatch_reset_btn = tk.Button(
            stopwatch_buttons,
            text="RESET",
            command=self.reset_stopwatch,
            font=('Arial', 16, 'bold'),
            bg='#f44336',
            fg='white',
            width=10,
            height=2
        )
        self.stopwatch_reset_btn.grid(row=0, column=1, padx=10)
        
        # Pokaż minutnik domyślnie
        self.timer_frame.pack()
    
    def show_timer(self):
        self.current_mode = "timer"
        self.btn_timer.config(bg='#2196F3', fg='white', relief=tk.RAISED)
        self.btn_stopwatch.config(bg='#e0e0e0', fg='#333', relief=tk.FLAT)
        self.stopwatch_frame.pack_forget()
        self.timer_frame.pack()
    
    def show_stopwatch(self):
        self.current_mode = "stopwatch"
        self.btn_stopwatch.config(bg='#2196F3', fg='white', relief=tk.RAISED)
        self.btn_timer.config(bg='#e0e0e0', fg='#333', relief=tk.FLAT)
        self.timer_frame.pack_forget()
        self.stopwatch_frame.pack()
    
    # ===== FUNKCJE MINUTNIKA =====
    def start_pause_timer(self):
        if not self.timer_running:
            # Pobierz czas z pól lub użyj aktualnego
            if self.timer_seconds == 0:
                minutes = int(self.timer_min_entry.get())
                seconds = int(self.timer_sec_entry.get())
                self.timer_seconds = minutes * 60 + seconds
            
            if self.timer_seconds > 0:
                self.timer_running = True
                self.timer_start_btn.config(text="PAUZA", bg='#FF9800')
                Thread(target=self.run_timer, daemon=True).start()
        else:
            self.timer_running = False
            self.timer_start_btn.config(text="WZNÓW", bg='#4CAF50')
    
    def run_timer(self):
        while self.timer_running and self.timer_seconds > 0:
            mins = self.timer_seconds // 60
            secs = self.timer_seconds % 60
            self.timer_display.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.timer_seconds -= 1
        
        if self.timer_seconds == 0:
            self.timer_display.config(text="00:00")
            self.timer_running = False
            self.timer_start_btn.config(text="START", bg='#4CAF50')
            self.play_beep()
    
    def reset_timer(self):
        self.timer_running = False
        self.timer_seconds = 0
        minutes = int(self.timer_min_entry.get())
        seconds = int(self.timer_sec_entry.get())
        self.timer_display.config(text=f"{minutes:02d}:{seconds:02d}")
        self.timer_start_btn.config(text="START", bg='#4CAF50')
    
    # ===== FUNKCJE STOPERA =====
    def start_pause_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.stopwatch_start_btn.config(text="PAUZA", bg='#FF9800')
            Thread(target=self.run_stopwatch, daemon=True).start()
        else:
            self.stopwatch_running = False
            self.stopwatch_start_btn.config(text="WZNÓW", bg='#4CAF50')
    
    def run_stopwatch(self):
        while self.stopwatch_running:
            hours = self.stopwatch_seconds // 3600
            mins = (self.stopwatch_seconds % 3600) // 60
            secs = self.stopwatch_seconds % 60
            self.stopwatch_display.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.stopwatch_seconds += 1
    
    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_seconds = 0
        self.stopwatch_display.config(text="00:00:00")
        self.stopwatch_start_btn.config(text="START", bg='#4CAF50')
    
    def play_beep(self):
        try:
            import winsound
            winsound.Beep(1000, 1000)
        except:
            print('\a')  # System beep dla innych systemów

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerStopwatch(root)
    root.mainloop()
