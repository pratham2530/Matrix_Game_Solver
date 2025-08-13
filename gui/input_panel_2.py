"""
This module contains the Input Panel 2 frame class. 
It handles constructing the entry fields for the matrix. 
"""

from tkinter import Tk, Frame, Label, Button, Entry, Canvas, Scrollbar
from typing import List, Union, Dict, TypedDict


class WidgetGroups(TypedDict):
    """
    Type-hinted container for organized GUI widgets.

    Groups widgets by type for structured access:
    - labels: Text display widgets (Dict[str, Label])
    - entries: Input fields (Dict[str, Entry])
    - buttons: Interactive buttons (Dict[str, Button])
    - frames: Container frames (Dict[str, Frame])
    - scroll: Scroll components (Dict[str, Union[Canvas, Scrollbar]])
    """

    labels: Dict[str, Label]
    entries: Dict[str, Entry]
    buttons: Dict[str, Button]
    frames: Dict[str, Frame]
    scroll: Dict[str, Union[Canvas, Scrollbar]]


class Input_Panel_2(Frame):
    """
    The second frame of the application, responsible for matrix value input.
    Handles matrix entry with scrolling capability and validation.
    """

    # Class-level text constants
    MATRIX_INSTRUCTIONS = "Now input the matrix values (integers or decimals)."

    def __init__(self, parent: Union[Tk, Frame]) -> None:
        """
        Initialize the matrix input frame and setup UI components.

        Args:
            parent: The parent container (typically the root Tk window)

        Initializes:
            - app: Reference to parent application
            - rows/cols/maxormin: Matrix parameters
            - entries: List of matrix Entry widgets
            - matrix: The input matrix data
            - widgets: Dictionary organizing all UI components
        """
        super().__init__(parent)
        self.app = parent

        # Matrix parameters
        self.rows = 0
        self.cols = 0
        self.maxormin = ""

        # Data storage
        self.entries: List[Entry] = []
        self.matrix: List[List[float]] = []

        # Widget containers
        self.widgets: WidgetGroups = {
            "labels": {},
            "entries": {},
            "buttons": {},
            "frames": {},
            "scroll": {},
        }

        # UI setup
        self._setup_ui()

    def _setup_ui(self) -> None:
        """
        Initialize all UI components and layout.
        """
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create all widgets
        self._create_frames()
        self._create_labels()
        self._setup_matrix_input()
        self._create_buttons()

        # Setup layout and bindings
        self._setup_layout()

    def _create_frames(self) -> None:
        """Create frame widgets."""
        w = self.widgets
        w["frames"]["input"] = Frame(
            self,
            borderwidth=1,
            padx=59.45,
            pady=19.45,
            highlightbackground="black",
            highlightthickness=1,
        )
        w["frames"]["entries"] = Frame(w["frames"]["input"])

    def _create_labels(self) -> None:
        """Create label widgets."""
        w = self.widgets
        w["labels"] = {
            "instructions": Label(w["frames"]["input"], text=self.MATRIX_INSTRUCTIONS),
            "dimensions": Label(w["frames"]["input"], text=""),
            "error": Label(w["frames"]["input"], text="", fg="red"),
        }

    def _setup_matrix_input(self) -> None:
        """
        Set up the matrix input area with scrollable canvas.
        """
        w = self.widgets
        # Scroll components
        w["scroll"]["canvas"] = Canvas(
            w["frames"]["entries"],
            bg="#FFFFFF",
            scrollregion=(0, 0, 500, 500),
            width=250,
            height=150,
        )
        w["scroll"]["hbar"] = Scrollbar(
            w["frames"]["entries"],
            orient="horizontal",
            command=w["scroll"]["canvas"].xview,
        )
        w["scroll"]["vbar"] = Scrollbar(
            w["frames"]["entries"],
            orient="vertical",
            command=w["scroll"]["canvas"].yview,
        )

        # Inner frame for entries
        w["frames"]["inner"] = Frame(w["scroll"]["canvas"])
        w["scroll"]["canvas"].create_window(
            (0, 0), window=w["frames"]["inner"], anchor="nw"
        )

    def _create_buttons(self) -> None:
        """
        Create button widgets.
        """
        w = self.widgets
        w["buttons"] = {
            "back": Button(
                w["frames"]["input"],
                text="Go Back!",
                command=self.app.first.tkraise,
            ),
            "submit": Button(
                w["frames"]["input"], text="Enter", command=self.validate_inputs
            ),
        }

    def _setup_layout(self) -> None:
        """
        Arrange widgets in grid layout.
        """
        w = self.widgets
        # Main frames
        w["frames"]["input"].grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        w["frames"]["entries"].grid(row=2, column=0, pady=5, sticky="n", columnspan=2)

        # Scroll components
        w["scroll"]["hbar"].grid(row=1, column=0, sticky="ew")
        w["scroll"]["vbar"].grid(row=0, column=1, sticky="ns")
        w["scroll"]["canvas"].config(
            xscrollcommand=w["scroll"]["hbar"].set,
            yscrollcommand=w["scroll"]["vbar"].set,
        )
        w["scroll"]["canvas"].grid(row=0, column=0, sticky="nsew")

        # Configure grid weights
        w["frames"]["entries"].grid_rowconfigure(0, weight=1)
        w["frames"]["entries"].grid_columnconfigure(0, weight=1)

        # Labels and buttons
        w["labels"]["instructions"].grid(row=0, column=0, columnspan=2)
        w["labels"]["dimensions"].grid(row=1, column=0, columnspan=2)
        w["buttons"]["back"].grid(row=3, column=0)
        w["buttons"]["submit"].grid(row=3, column=1)
        w["labels"]["error"].grid(row=4, column=0, columnspan=2)

    def update_rows_cols_maxormin(self, rows: int, cols: int, maxormin: str) -> None:
        """
        Update the matrix dimensions and player type, and create input fields.
        """
        w = self.widgets
        self.rows = int(rows)
        self.cols = int(cols)
        self.maxormin = maxormin

        w["labels"]["dimensions"].config(
            text=f"Inputs - Rows: {self.rows}, Columns: {self.cols}, "
            f"Row player: {self.maxormin}imiser"
        )

        # Clear existing entries
        for widget in w["frames"]["inner"].winfo_children():
            widget.destroy()

        self.entries = []
        self._create_matrix_entries()
        self._update_button_positions()

    def _create_matrix_entries(self) -> None:
        """
        Create entry widgets for matrix input.
        """
        w = self.widgets
        for x in range(self.rows):
            for y in range(self.cols):
                entry = Entry(w["frames"]["inner"])
                entry.grid(row=x, column=y, padx=5, pady=5)
                self.entries.append(entry)

        w["frames"]["inner"].update_idletasks()
        w["scroll"]["canvas"].config(scrollregion=w["scroll"]["canvas"].bbox("all"))

    def _update_button_positions(self) -> None:
        """
        Update button positions based on matrix size.
        """
        w = self.widgets
        w["buttons"]["back"].grid(row=3 + self.rows, column=0)
        w["buttons"]["submit"].grid(row=3 + self.rows, column=1)
        w["labels"]["error"].grid(row=4 + self.rows, column=0, columnspan=2)

    def validate_inputs(self) -> None:
        """
        Validate the matrix inputs and proceed if valid.
        """
        w = self.widgets
        try:
            self.matrix = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    idx = i * self.cols + j
                    value = float(self.entries[idx].get())
                    row.append(value)
                self.matrix.append(row)

            self.app.third.update_inputs(
                self.rows, self.cols, self.maxormin, self.matrix
            )
            self.app.third.tkraise()

        except ValueError:
            w["labels"]["error"].config(
                text="Enter an integer or decimal number in each cell!", fg="red"
            )
            self.app.first.clear_label_after(w["labels"]["error"], 2000)


