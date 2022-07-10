from notifications import (NewsPaperNotifications,
                           TvNotifications)
from places import Kostroma, Tokio, Titan
from heroes import ChuckNorris, SuperMan
from save_place import SavePlace


if __name__ == '__main__':
    SavePlace(ChuckNorris(), Tokio(), TvNotifications())
    print("-" * 20)
    SavePlace(SuperMan(), Kostroma(), NewsPaperNotifications())
    print("-" * 20)
    SavePlace(SuperMan(), Titan(), NewsPaperNotifications())
