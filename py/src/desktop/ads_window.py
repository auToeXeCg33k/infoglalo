from .scrollable_window import ScrollableWindow
from ..core.dao.ad_dao import AdDAO

class AdsWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)
        this.reset()
        
    def reset(this) -> None:
        dao = AdDAO()
        data =  dao.find_all()
        for i in range (len(data)):
            this.main_frame.rowconfigure(index=i, weight=1)
