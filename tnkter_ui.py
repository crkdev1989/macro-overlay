
import tkinter as tk
from build_service import (
    list_races,
    list_matchups,
    list_build_files,
    load_build_from_file,
)


class BuildRunner:
    def __init__(self, steps):
        self.steps = steps
        self.index = 0

    @property
    def current_text(self):
        if not self.steps:
            return "No steps loaded."
        if self.index < 0 or self.index >= len(self.steps):
            return "Build complete!"
        step = self.steps[self.index]
        return f"{step['supply']} – {step['action']}"

    def next_step(self):
        if self.index < len(self.steps) - 1:
            self.index += 1
        else:
            self.index = len(self.steps)

    def prev_step(self):
        if self.index > 0:
            self.index -= 1

    def reset(self):
        self.index = 0


class MacroOverlayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Macro Overlay")
        self.attributes("-topmost", True)

        self.races = list_races()
        self.matchups = []
        self.build_files = []

        self.selected_race = tk.StringVar(value=self.races[0] if self.races else "")
        self.selected_matchup = tk.StringVar(value="")
        self.selected_build_index = tk.IntVar(value=0)

        self.runner = BuildRunner([])

        self._build_selection_ui()
        self._build_overlay_ui()
        self._wire_events()

        self._refresh_matchups()
        self._refresh_build_list()
        self._refresh_overlay_label()

    # --- UI SECTIONS ---

    def _build_selection_ui(self):
        frame = tk.LabelFrame(self, text="Select Build")
        frame.pack(padx=10, pady=10, fill="x")

        # Race dropdown
        tk.Label(frame, text="Race:").grid(row=0, column=0, sticky="w")
        self.race_menu = tk.OptionMenu(frame, self.selected_race, *self.races)
        self.race_menu.grid(row=0, column=1, sticky="w", padx=5, pady=2)

        # Matchup dropdown
        tk.Label(frame, text="Matchup:").grid(row=1, column=0, sticky="w")
        self.matchup_menu = tk.OptionMenu(frame, self.selected_matchup, "")
        self.matchup_menu.grid(row=1, column=1, sticky="w", padx=5, pady=2)

        # Build list
        tk.Label(frame, text="Builds:").grid(row=2, column=0, sticky="nw")
        self.build_listbox = tk.Listbox(frame, height=6, width=40)
        self.build_listbox.grid(row=2, column=1, sticky="w", padx=5, pady=2)

        self.load_button = tk.Button(frame, text="Load Build", command=self.load_selected_build)
        self.load_button.grid(row=3, column=0, columnspan=2, pady=5)

    def _build_overlay_ui(self):
        frame = tk.LabelFrame(self, text="Overlay")
        frame.pack(padx=10, pady=10, fill="x")

        self.step_label = tk.Label(
            frame,
            text="No build loaded.",
            font=("Arial", 16),
            wraplength=400,
            justify="left",
            padx=10,
            pady=10,
        )
        self.step_label.pack()

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=5)

        self.prev_button = tk.Button(btn_frame, text="← Prev", command=self.prev_step)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(btn_frame, text="Next →", command=self.next_step)
        self.next_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(btn_frame, text="Reset", command=self.reset_build)
        self.reset_button.grid(row=0, column=2, padx=5)

    # --- EVENT WIRING ---

    def _wire_events(self):
        self.selected_race.trace_add("write", lambda *args: self._on_race_changed())
        self.selected_matchup.trace_add("write", lambda *args: self._on_matchup_changed())
        self.build_listbox.bind("<<ListboxSelect>>", self._on_build_selected)

    # --- REFRESH HELPERS ---

    def _refresh_matchups(self):
        race = self.selected_race.get()
        self.matchups = list_matchups(race) if race else []
        if self.matchups:
            self.selected_matchup.set(self.matchups[0])
        else:
            self.selected_matchup.set("")

        # rebuild OptionMenu
        menu = self.matchup_menu["menu"]
        menu.delete(0, "end")
        for m in self.matchups:
            menu.add_command(label=m, command=lambda value=m: self.selected_matchup.set(value))

    def _refresh_build_list(self):
        race = self.selected_race.get()
        matchup = self.selected_matchup.get()
        self.build_files = list_build_files(race, matchup) if race and matchup else []

        self.build_listbox.delete(0, "end")
        for path in self.build_files:
            self.build_listbox.insert("end", path.name)

    def _refresh_overlay_label(self):
        self.step_label.config(text=self.runner.current_text)

    # --- CALLBACKS ---

    def _on_race_changed(self):
        self._refresh_matchups()
        self._refresh_build_list()

    def _on_matchup_changed(self):
        self._refresh_build_list()

    def _on_build_selected(self, event):
        sel = self.build_listbox.curselection()
        if not sel:
            return
        self.selected_build_index.set(sel[0])

    def load_selected_build(self):
        if not self.build_files:
            return
        idx = self.selected_build_index.get()
        if idx < 0 or idx >= len(self.build_files):
            idx = 0
        path = self.build_files[idx]
        steps = load_build_from_file(path)
        self.runner = BuildRunner(steps)
        self.runner.reset()
        self._refresh_overlay_label()

    # overlay controls
    def next_step(self):
        self.runner.next_step()
        self._refresh_overlay_label()

    def prev_step(self):
        self.runner.prev_step()
        self._refresh_overlay_label()

    def reset_build(self):
        self.runner.reset()
        self._refresh_overlay_label()


def run_overlay():
    app = MacroOverlayApp()
    app.mainloop()


if __name__ == "__main__":
    run_overlay()