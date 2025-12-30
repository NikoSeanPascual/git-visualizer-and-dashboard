import os
import shutil
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Niko's File Organizer: EMERALD EDITION")
        self.geometry("600x580")

        self.green_primary = "#2ecc71"
        self.green_hover = "#27ae60"
        self.bg_accent = "#1e272e"

        self.file_map = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
            "Documents": [".pdf", ".docx", ".doc", ".txt", ".csv", ".xlsx", ".pptx", ".md"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv"],
            "Music": [".mp3", ".wav", ".flac", ".m4a"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json"],
            "Executables": [".exe", ".msi", ".dmg", ".sh"],
        }

        self.setup_ui()

    def setup_ui(self):
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=(30, 20))

        self.label = ctk.CTkLabel(
            self.header_frame,
            text="NIKO'S ORGANIZER",
            font=("Fixedsys", 40, "bold"),
            text_color=self.green_primary
        )
        self.label.pack()

        self.sub_label = ctk.CTkLabel(
            self.header_frame,
            text="System File Management Application Thingy",
            font=("Consolas", 12),
            text_color="#808e9b"
        )
        self.sub_label.pack()

        self.select_btn = ctk.CTkButton(
            self,
            text="SELECT YOUR TARGETTED DIRECTORY",
            command=self.start_organizing_thread,
            font=("Consolas", 14, "bold"),
            fg_color=self.green_primary,
            hover_color=self.green_hover,
            text_color="#000000",
            height=45,
            corner_radius=8
        )
        self.select_btn.pack(pady=10, padx=40, fill="x")

        self.progress_bar = ctk.CTkProgressBar(
            self,
            width=500,
            progress_color=self.green_primary,
            fg_color="#2c3e50"
        )
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(20, 10))

        self.status_box = ctk.CTkTextbox(
            self,
            width=520,
            height=250,
            font=("Consolas", 12),
            fg_color="#0d1117",
            border_color=self.green_primary,
            border_width=1,
            text_color=self.green_primary
        )
        self.status_box.pack(pady=10, padx=20)

        self.stats_label = ctk.CTkLabel(
            self,
            text="YOUR SYSTEM IS READY =)",
            font=("Consolas", 11),
            text_color=self.green_primary
        )
        self.stats_label.pack(pady=5)

    def log(self, message):
        self.status_box.insert("end", f" [info] {message}\n")
        self.status_box.see("end")

    def start_organizing_thread(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            threading.Thread(target=self.organize_files, args=(folder_selected,), daemon=True).start()

    def organize_files(self, target_path):
        self.select_btn.configure(state="disabled", text="ORGANIZING...")
        self.status_box.delete("1.0", "end")
        self.log(f"INITIALIZING SCAN: {target_path}")

        try:
            all_items = [f for f in os.listdir(target_path)
                         if os.path.isfile(os.path.join(target_path, f)) and not f.startswith('.')]

            total_files = len(all_items)

            if total_files == 0:
                self.log("NO FILES DETECTED =(.")
                self.select_btn.configure(state="normal", text="SELECT TARGET DIRECTORY")
                return

            for folder in list(self.file_map.keys()) + ["Others"]:
                os.makedirs(os.path.join(target_path, folder), exist_ok=True)

            count = 0
            for item in all_items:
                full_path = os.path.join(target_path, item)
                ext = os.path.splitext(item)[1].lower()

                target_folder = "Others"
                for folder_name, extensions in self.file_map.items():
                    if ext in extensions:
                        target_folder = folder_name
                        break

                dest_path = os.path.join(target_path, target_folder, item)


                if os.path.exists(dest_path):
                    name, extension = os.path.splitext(item)
                    dest_path = os.path.join(target_path, target_folder, f"{name}_dup{extension}")

                shutil.move(full_path, dest_path)
                count += 1

                self.progress_bar.set(count / total_files)
                self.log(f"RELOCATED: {item} >> {target_folder}")
                self.stats_label.configure(text=f"PROCESSED: {count}/{total_files} UNITS")

            self.log(f"\nOPERATION COMPLETE. {count} FILES SORTED =).")
            messagebox.showinfo("Success", "Directory Organization Finished.")

        except Exception as e:
            self.log(f"CRITICAL ERROR: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.select_btn.configure(state="normal", text="SELECT TARGET DIRECTORY")

if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()