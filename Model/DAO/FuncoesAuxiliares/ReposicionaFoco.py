from PyQt5.QtWidgets import QLineEdit


def reposiciona_foco(widget):
    line_edits = widget.findChildren(QLineEdit)
    if line_edits:
        primeiro_line_edit = sorted(line_edits, key=lambda x: x.objectName())[0]
        primeiro_line_edit.setFocus()
