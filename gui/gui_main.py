"""
This module contains the Main Frame class.
It is responsible for the initial user input and validation of matrix dimensions.
"""

from tkinter import END, Button, Entry, Event, Frame, Label
from typing import Any, Dict, TypedDict


class WidgetGroups(TypedDict):
    """
    Type-hinted container for organized GUI widgets.

    Groups widgets by type for structured access:
    - labels: Text display widgets (Dict[str, Label])
    - entries: Input fields (Dict[str, Entry])
    - buttons: Interactive buttons (Dict[str, Button])
    """

    labels: Dict[str, Label]
    entries: Dict[str, Entry]
    buttons: Dict[str, Button]


class Main(Frame):
    """
    The main frame of the application, responsible for initial user input.
    Handles gathering matrix dimensions and player role (maximizer/minimizer).
    """

    # Class-level text constants
    WELCOME_MESSAGE = "Enter the pay-off matrix dimensions below."
    ROLE_QUESTION = "Is the row player the maximiser or minimiser?"

    PLACEHOLDERS = {
        "rows": "Enter the number of rows of the matrix",
        "cols": "Enter the number of columns of the matrix",
        "role": "Enter 'max' or 'min'",
    }

    def __init__(self, parent: Any) -> None:
        """
        Initialize the main application frame and setup UI components.

        Args:
            parent: The parent container

        Initializes:
            - app: Reference to parent application
            - entry_map: Dictionary mapping entries to their placeholders
            - All UI widgets through _setup_ui()
        """
        super().__init__(parent)
        self.app = parent
        self.entry_map = {}
        self._setup_ui()

    def _setup_ui(self) -> None:
        """
        Initialize all UI components and layout.
        """
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main container
        self.input_frame = Frame(
            self,
            borderwidth=1,
            padx=5,
            pady=5,
            highlightbackground="black",
            highlightthickness=1,
        )
        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(9):
            self.input_frame.grid_rowconfigure(i, weight=1)

        self.input_frame.grid_columnconfigure(0, weight=1)

        # Widget organization
        self.widgets = {
            "labels": self._create_labels(),
            "entries": self._create_entries(),
            "buttons": self._create_buttons(),
        }

        self._setup_bindings()
        self._setup_layout()

    def _create_labels(self) -> Dict[str, Label]:
        """
        Create and return label widgets.
        """
        return {
            "main": Label(
                self.input_frame, text=self.WELCOME_MESSAGE, font=self.master.font
            ),
            "question": Label(
                self.input_frame,
                text=self.ROLE_QUESTION,
                font=self.master.font,
                anchor="w",
            ),
            "error_rows": Label(
                self.input_frame, text="", font=self.master.error_font, fg="red"
            ),
            "error_cols": Label(
                self.input_frame, text="", font=self.master.error_font, fg="red"
            ),
            "error_role": Label(
                self.input_frame, text="", font=self.master.error_font, fg="red"
            ),
            "confirm": Label(
                self.input_frame, text="", font=self.master.font, fg="green"
            ),
        }

    def _create_entries(self) -> Dict[str, Entry]:
        """
        Create and return entry widgets.
        """
        return {
            "rows": Entry(self.input_frame, width=40, font=self.master.font, fg="gray"),
            "cols": Entry(self.input_frame, width=40, font=self.master.font, fg="gray"),
            "role": Entry(self.input_frame, width=40, font=self.master.font, fg="gray"),
        }

    def _create_buttons(self) -> Dict[str, Button]:
        """
        Create and return button widgets.
        """
        return {
            "submit": Button(
                self.input_frame,
                text="Enter",
                font=self.master.font,
                command=self.validate_inputs,
            )
        }

    def _setup_bindings(self) -> None:
        """
        Configure widget event bindings.
        """
        for i in ["rows", "cols", "role"]:
            self.entry_map[self.widgets["entries"][i]] = self.PLACEHOLDERS[i]

        for entry, placeholder in self.entry_map.items():
            entry.insert(0, placeholder)
            entry.bind("<Button-1>", self.click)
            entry.bind("<Leave>", self.leave)

    def _setup_layout(self) -> None:
        """
        Arrange widgets in grid layout.
        """
        w = self.widgets
        w["labels"]["main"].grid(row=0, column=0, sticky="", pady=5, columnspan=2)
        w["entries"]["rows"].grid(row=1, column=0, sticky="", pady=0, columnspan=2)
        w["labels"]["error_rows"].grid(row=2, column=0, sticky="", pady=0, columnspan=2)
        w["entries"]["cols"].grid(row=3, column=0, sticky="", pady=(5, 0), columnspan=2)
        w["labels"]["error_cols"].grid(row=4, column=0, sticky="", pady=0, columnspan=2)
        w["labels"]["question"].grid(row=5, column=0, sticky="", pady=5, columnspan=2)
        w["entries"]["role"].grid(row=6, column=0, sticky="", pady=0, columnspan=2)
        w["labels"]["error_role"].grid(row=7, column=0, sticky="", pady=0, columnspan=2)
        w["buttons"]["submit"].grid(
            row=8, column=0, sticky="", pady=(10, 0), columnspan=2
        )
        w["labels"]["confirm"].grid(row=9, column=0, sticky="", pady=0, columnspan=2)

    def click(self, event: Event) -> None:
        """
        Handles click events for entry widgets.
        """
        widget = event.widget
        if isinstance(widget, Entry) and widget.get() in self.entry_map.values():
            widget.delete(0, END)
            widget.config(fg="black")

    def leave(self, event: Event) -> None:
        """
        Handles leave events for entry widgets.
        """
        widget = event.widget
        if isinstance(widget, Entry) and not widget.get():
            placeholder = self.entry_map.get(widget)
            if placeholder:
                widget.insert(0, placeholder)
                widget.config(fg="gray")
        self.master.focus()

    def clear_label_after(self, label: Label, delay: int = 2000) -> None:
        """
        Clears label text after specified delay.
        """
        label.after(delay, lambda: label.config(text=""))

    def validate_input_entry(self, entry_key: str, error_key: str) -> bool:
        """
        Generic validation method for entry fields.

        Args:
            entry_key: Key for the entry widget ('rows', 'cols', or 'role')
            error_key: Key for the error label ('error_rows', 'error_cols', 'error_role')

        Returns:
            bool: True if validation passes
        """
        entry = self.widgets["entries"][entry_key]
        error_label = self.widgets["labels"][error_key]
        value = entry.get()

        error_label.config(text="")

        if entry_key == "role":
            if value.lower() not in {"max", "min"}:
                error_label.config(text="Enter 'max' or 'min'!")
                self.clear_label_after(error_label)
                return False
            return True

        try:
            num = int(value)
            if num <= 0:
                raise ValueError
            return True
        except ValueError:
            error_label.config(
                text="Enter a positive integer - use numerals like 1, 2, 3, ... !"
            )
            self.clear_label_after(error_label)
            return False

    def validate_inputs(self) -> None:
        """
        Validates all input fields and proceeds if valid.
        """
        validations = [
            self.validate_input_entry("rows", "error_rows"),
            self.validate_input_entry("cols", "error_cols"),
            self.validate_input_entry("role", "error_role"),
        ]

        if all(validations):
            confirm = self.widgets["labels"]["confirm"]
            confirm.config(text="All input fields are valid!")
            self.clear_label_after(confirm)

            # Update application state
            self.app.second.update_rows_cols_maxormin(
                self.widgets["entries"]["rows"].get(),
                self.widgets["entries"]["cols"].get(),
                self.widgets["entries"]["role"].get().lower(),
            )
            self.app.second.tkraise()

    def clear_entries(self) -> None:
        """
        Clears all entry widgets.
        """
        for entry in self.widgets["entries"].values():
            entry.delete(0, END)
