from aqt import mw
from aqt.utils import openLink
from aqt.qt import QMenu, QAction

from .config import conf

def setupMenu() -> None:
    menu = mw.form.menuTools
    menuAction = QAction("ReColour", menu)
    menuAction.triggered.connect(conf.open_config)
    menu.addSeparator()
    menu.addAction(menuAction)

setupMenu()