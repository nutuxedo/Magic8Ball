#!/usr/bin/env python3
import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, 
    QVBoxLayout, QHBoxLayout, QWidget, QDialog,
    QMessageBox
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont


class EightBall:
    """Logic for the Magic 8 Ball answers, kept identical to Tkinter version."""
    def __init__(self):
        # Answers from https://en.wikipedia.org/wiki/Magic_8_Ball
        self.answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]
    
    def shake(self):
        """Return an answer immediately (non-blocking)."""
        return random.choice(self.answers)


class AboutDialog(QDialog):
    """About dialog showing app info."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(200, 100)
        
        layout = QVBoxLayout()
        
        title_label = QLabel("8 ball funsies")
        title_label.setFont(QFont("Arial", 12, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        
        version_label = QLabel("by nutuxedo - v0.1alpha-qttest")
        version_label.setFont(QFont("Arial", 8))
        version_label.setAlignment(Qt.AlignCenter)
        
        close_button = QPushButton("Exit")
        close_button.clicked.connect(self.accept)
        close_button.setStyleSheet("background-color: skyblue;")
        
        layout.addWidget(title_label)
        layout.addWidget(version_label)
        layout.addWidget(close_button)
        
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("8 Ball funsies")
        self.setFixedSize(250, 180)
        
        # Create the eight ball instance
        self.eightball = EightBall()
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create widgets
        header_label = QLabel("The 8-ball")
        header_label.setFont(QFont("Arial", 12, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("padding: 5px;")
        
        self.shake_button = QPushButton("Shake!")
        self.shake_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.shake_button.setStyleSheet("background-color: darkblue;")
        self.shake_button.clicked.connect(self.on_shake)
        
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("padding: 5px;")
        self.result_label.setMinimumHeight(50)
        
        # Bottom buttons in horizontal layout
        button_layout = QHBoxLayout()
        
        about_button = QPushButton("About")
        about_button.setStyleSheet("background-color: darkblue;")
        about_button.clicked.connect(self.show_about)
        
        exit_button = QPushButton("Exit")
        exit_button.setStyleSheet("background-color: darkblue;")
        exit_button.clicked.connect(self.confirm_exit)
        
        button_layout.addWidget(about_button)
        button_layout.addWidget(exit_button)
        
        # Add widgets to main layout
        layout.addWidget(header_label)
        layout.addWidget(self.shake_button)
        layout.addWidget(self.result_label)
        layout.addLayout(button_layout)
        
    def on_shake(self):
        """Handle shake button click."""
        self.result_label.setText("Shaking...")
        self.shake_button.setEnabled(False)
        
        # Use QTimer for the delay (equivalent to Tkinter's after)
        QTimer.singleShot(2000, self.show_answer)
    
    def show_answer(self):
        """Show the 8-ball's answer after delay."""
        answer = self.eightball.shake()
        self.result_label.setText(answer)
        self.shake_button.setEnabled(True)
    
    def show_about(self):
        """Show the about dialog."""
        about = AboutDialog(self)
        about.exec()
    
    def confirm_exit(self):
        """Show exit confirmation dialog."""
        reply = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            print("Program exited")  # Keep same console output as Tkinter version
            self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()