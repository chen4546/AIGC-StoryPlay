from ui.main_window import GameGUI, QApplication


def main():
    app = QApplication([])
    window = GameGUI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
